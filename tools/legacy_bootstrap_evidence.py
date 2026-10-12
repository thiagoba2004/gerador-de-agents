"""Read-only Git evidence for bootstraps predating the action-matrix mandate."""
from datetime import date, datetime
import json
import re
from pathlib import Path
import subprocess

EFFECTIVE_DATE = date(2026, 10, 11)
CUTOFF = datetime.fromisoformat("2026-10-11T00:00:00-03:00")


def legacy_proof(root: Path, first: dict, history: list[dict],
                 requests: list[dict], plan: str) -> dict | None:
    """Require matching CREATED/CONCLUDED, request and plan in an older Git tree.

    Git timestamps/history are documentary evidence, not signed authentication or
    live authorization. No writes, fetch, hooks, or caller-supplied exemption.
    Missing/shallow history fails closed until the operator supplies full history.
    """
    strategy = first["strategy_code"]
    ref = first["plan_ref"]
    concluded = [e for e in history if e.get("strategy_code") == strategy
                 and e.get("event_type") == "CONCLUDED"]
    if len(concluded) != 1:
        return None
    terminal = concluded[0]
    strategy_events = [e for e in history if e.get("strategy_code") == strategy]
    phases = first.get("phase_total")
    plan_phases = {int(n) for n in re.findall(
        rf"F-{re.escape(strategy[3:])}-(\d{{3}})", plan)}
    if (strategy_events[-1] != terminal or terminal.get("status") not in ("CONCLUIDO", "CONCLUDED", "COMPLETED")
            or not terminal.get("terminal_gate") or not isinstance(phases, int) or phases < 2
            or terminal.get("phase_total") != phases or terminal.get("phase_number") != phases
            or plan_phases != set(range(1, phases + 1))):
        return None
    try:
        start, end = (date.fromisoformat(e.get("date", "")) for e in (first, terminal))
        if not start <= end < EFFECTIVE_DATE:
            return None
    except (TypeError, ValueError):
        return None
    triggers = first.get("trigger_request_ids")
    if not isinstance(triggers, list) or not triggers or not all(isinstance(t, str) for t in triggers):
        return None
    linked = [e for e in requests if e.get("request_id") in triggers]
    if {e.get("request_id") for e in linked} != set(triggers):
        return None

    def git(*args: str) -> str:
        # Exact, per-command ownership exception; never changes Git configuration.
        result = subprocess.run(["git", "-c", f"safe.directory={root.as_posix()}",
                                 "-C", str(root), *args], capture_output=True,
                                encoding="utf-8", errors="strict", timeout=15)
        if result.returncode:
            raise ValueError("Git evidence unavailable")
        return result.stdout

    try:
        if Path(git("rev-parse", "--show-toplevel").strip()).resolve() != root:
            return None
        # Require an ancestor of HEAD with both author and committer before policy.
        for line in git("log", "--format=%H %aI %cI", "HEAD").splitlines():
            sha, author, committer = line.split()
            if not (datetime.fromisoformat(author) < CUTOFF and
                    datetime.fromisoformat(committer) < CUTOFF):
                continue
            old_history = [json.loads(s) for s in git("show", f"{sha}:STRATEGY_LOG.jsonl").splitlines() if s.strip()]
            old_requests = [json.loads(s) for s in git("show", f"{sha}:REQUEST_LOG.jsonl").splitlines() if s.strip()]
            if first not in old_history or terminal not in old_history:
                continue
            if not all(e in old_requests for e in linked) or git("show", f"{sha}:{ref}") != plan:
                continue
            project = "PRJ-" + strategy.split("-")[1]
            if (project not in git("show", f"{sha}:AGENTS.md") or
                    strategy not in git("show", f"{sha}:ROADMAP.md")):
                continue
            old_state = json.loads(git("show", f"{sha}:PROJECT_STATE.json"))
            if not isinstance(old_state, dict) or old_state.get("project_code") != project or strategy not in json.dumps(old_state):
                continue
            return {"status": "LEGACY_FIRST_EA_MATRIX_NOT_BACKFILLED",
                    "commit": sha, "author_date": author, "committer_date": committer,
                    "effective_date": EFFECTIVE_DATE.isoformat(),
                    "refs": ["STRATEGY_LOG.jsonl", "REQUEST_LOG.jsonl", ref],
                    "created_event": first.get("event_id"),
                    "concluded_event": terminal.get("event_id")}
    except (OSError, ValueError, UnicodeError, subprocess.SubprocessError):
        return None
    return None
