#!/usr/bin/env python3
"""Fail-closed documentary creation gate. Never authenticates ChatGPT UI or executes effects."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

PROJECT_RE = re.compile(r"^PRJ-(\d{6})$")
STRATEGY_RE = re.compile(r"^EA-(\d{6})-(\d{6})$")
PHASE_RE = re.compile(r"F-(\d{6})-(\d{6})-(\d{3})")
HEX_SHA = re.compile(r"^[a-f0-9]{40}$")


def inspect(root: Path, route: str = "A", gate: str = "bootstrap") -> dict:
    """Check versioned prerequisites only. PASS is not handoff acceptance."""
    root = root.resolve()
    errors: list[str] = []
    evidence: dict[str, object] = {}

    def fail(code: str) -> None:
        if code not in errors:
            errors.append(code)

    def required(relative: str) -> Path | None:
        if (not isinstance(relative, str) or not relative or
                relative.startswith(("/", "\\")) or "\\" in relative or
                any(part in (".", "..", "") for part in relative.split("/"))):
            fail("INVALID_PATH:" + str(relative))
            return None
        path = (root / relative).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            fail("MISSING_OR_UNSAFE_PATH:" + relative)
            return None
        return path

    def document(relative: str) -> str:
        path = required(relative)
        if path is None:
            return ""
        try:
            return path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            fail("UNREADABLE:" + relative)
            return ""

    def obj(relative: str) -> dict:
        raw = document(relative)
        try:
            value = json.loads(raw)
            if not isinstance(value, dict):
                raise ValueError("not-object")
            return value
        except (ValueError, TypeError):
            fail("INVALID_JSON:" + relative)
            return {}

    def events(relative: str) -> list[dict]:
        raw = document(relative)
        out = []
        for index, line in enumerate(raw.splitlines(), 1):
            if not line.strip():
                continue
            try:
                value = json.loads(line)
                if not isinstance(value, dict):
                    raise ValueError("not-object")
                out.append(value)
            except ValueError:
                fail(f"INVALID_JSONL:{relative}:{index}")
        return out

    state = obj("PROJECT_STATE.json")
    code = state.get("project_code")
    match = PROJECT_RE.fullmatch(code or "") if isinstance(code, str) else None
    if not match:
        fail("PROJECT_CODE_INVALID")
        number = None
    else:
        number = match.group(1)
    agents = document("AGENTS.md")
    roadmap = document("ROADMAP.md")
    requests = events("REQUEST_LOG.jsonl")
    history = events("STRATEGY_LOG.jsonl")
    if code and code not in agents:
        fail("AGENTS_IDENTITY_MISMATCH")
    if not requests:
        fail("NO_REQUEST_EVENT")
    created = [entry for entry in history if
               entry.get("event_type") == "CREATED" and
               isinstance(entry.get("strategy_code"), str) and
               STRATEGY_RE.fullmatch(entry["strategy_code"]) and
               number and entry["strategy_code"].split("-")[1] == number]
    if not created:
        fail("FIRST_EA_CREATED_EVENT_MISSING")
    if route == "A" and number:
        initial = [entry for entry in created if entry["strategy_code"] == f"EA-{number}-000001"]
        if len(initial) != 1:
            fail("FIRST_EA_000001_NOT_UNIQUE")
    else:
        initial = created[:1]
    if initial:
        first = initial[0]
        strategy = first["strategy_code"]
        evidence["initial_strategy"] = strategy
        if strategy not in roadmap:
            fail("ROADMAP_STRATEGY_REFERENCE_MISSING")
        status_source = json.dumps(state, ensure_ascii=False)
        if strategy not in status_source:
            fail("STATE_STRATEGY_REFERENCE_MISSING")
        ref = first.get("plan_ref")
        if not isinstance(ref, str) or not ref.startswith("estrategias/"):
            fail("FIRST_EA_PLAN_REF_MISSING")
        else:
            plan = document(ref)
            if strategy not in plan:
                fail("FIRST_EA_PLAN_ID_MISMATCH")
            phases = [(a, b, int(c)) for a, b, c in PHASE_RE.findall(plan)
                      if strategy == f"EA-{a}-{b}"]
            ids = sorted(set(c for _, _, c in phases))
            if not ids or ids != list(range(1, max(ids) + 1)) or len(ids) < 2:
                fail("FIRST_EA_PHASE_PLAN_INCOMPLETE")
            evidence["initial_plan"] = ref
            evidence["phases"] = ids
            if route == "A":
                from validate_execution_action_plan import validate
                contract = validate(root, strategy, plan_ref=ref)
                evidence["action_plan_result"] = contract["status"]
                if contract["status"] != "PASS":
                    fail("FIRST_EA_ACTION_PLAN_UNVERIFIED")
                    evidence["action_plan_errors"] = contract["errors"]

    if gate in ("sciv", "post_native"):
        sciv = obj("comunicados/SCIV_STATE.json")
        if sciv.get("project_code") != code:
            fail("SCIV_PROJECT_MISMATCH")
        if sciv.get("mode", (sciv.get("bootstrap") or {}).get("mode")) != "ON_DEMAND":
            fail("SCIV_ON_DEMAND_REQUIRED")
        if sciv.get("operational_ref") != "main":
            fail("SCIV_MAIN_REF_REQUIRED")
        for key, expected in (
            ("inbox", "comunicados/governanca-geral/mensagens"),
            ("outbox", "comunicados/ia-especializada/mensagens"),
        ):
            if sciv.get(key) != expected:
                fail("SCIV_" + key.upper() + "_MISMATCH")
            required(expected + "/README.md")
        for historical in ("comunicados/governanca-geral/historico/README.md",
                           "comunicados/ia-especializada/historico/README.md"):
            required(historical)
        adapter = document("adaptadores/chatgpt/INSTRUCOES.md")
        if (adapter.count("<!-- SCIV_BOOTSTRAP_BEGIN v1 -->") != 1 or
                adapter.count("<!-- SCIV_BOOTSTRAP_END -->") != 1 or
                "SCIV Sob Demanda" not in adapter):
            fail("SCIV_ADAPTER_BLOCK_MISSING_OR_DUPLICATE")
        evidence["sciv_mode"] = sciv.get("mode")

    if gate == "post_native":
        receipt = obj("governanca/recebimentos/RECEIPT_EVIDENCE.json")
        install = receipt.get("native_installation") or {}
        test = receipt.get("receipt_test") or {}
        sciv_test = receipt.get("sciv_test") or {}
        if not isinstance(install, dict) or install.get("classification") != "HUMAN_ATTESTED" or not install.get("evidence_ref"):
            fail("NATIVE_INSTALLATION_HUMAN_ATTESTATION_MISSING")
        if not isinstance(install, dict) or not HEX_SHA.fullmatch(str(install.get("adapter_commit", ""))):
            fail("NATIVE_ADAPTER_COMMIT_MISSING")
        proper = "A6" if route == "A" else "B8"
        if not isinstance(test, dict) or test.get("gate") != proper:
            fail("RECEIPT_GATE_MISMATCH")
        if not isinstance(test, dict) or test.get("classification") not in ("VERIFIED", "HUMAN_ATTESTED", "NOT_VERIFIED", "BLOCKED"):
            fail("RECEIPT_CLASSIFICATION_UNSPECIFIED")
        report = test.get("report_path") if isinstance(test, dict) else None
        if not isinstance(report, str) or not report.startswith("governanca/recebimentos/") or not report.endswith(".md"):
            fail("POST_NATIVE_REPORT_PATH_MISSING")
        else:
            document(report)
            evidence["receipt_report"] = report
        if not isinstance(test, dict) or test.get("transport") != "SCIV_ON_DEMAND" or not test.get("message_id") or not test.get("correlation_id"):
            fail("POST_NATIVE_SCIV_TRANSPORT_NOT_EVIDENCED")
        if not isinstance(sciv_test, dict) or sciv_test.get("classification") not in ("VERIFIED", "HUMAN_ATTESTED", "NOT_VERIFIED", "BLOCKED"):
            fail("SEPARATE_SCIV_TEST_CLASSIFICATION_MISSING")
        evidence["receipt_classification"] = test.get("classification") if isinstance(test, dict) else None
        evidence["sciv_test_classification"] = sciv_test.get("classification") if isinstance(sciv_test, dict) else None

    return {"status": "PASS" if not errors else "FAIL", "gate": gate, "route": route,
            "evidence": evidence, "errors": errors,
            "limitation": "Documentary consistency only; never native UI attestation, A6/B8 acceptance or live PEP authorization."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", required=True, type=Path)
    parser.add_argument("--route", choices=("A", "B"), default="A")
    parser.add_argument("--gate", choices=("bootstrap", "sciv", "post_native"), default="bootstrap")
    args = parser.parse_args()
    outcome = inspect(args.project_root, route=args.route, gate=args.gate)
    print(json.dumps(outcome, ensure_ascii=False, indent=2))
    return 0 if outcome["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
