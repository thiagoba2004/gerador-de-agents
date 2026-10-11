#!/usr/bin/env python3
"""Validate action-level execution contracts. Structural check, never authorization."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

EA = re.compile(r"^EA-(\d{6})-(\d{6})$")
ACTION = re.compile(r"^ACT-(\d{6})-(\d{6})-(\d{3})$")
PHASE = re.compile(r"F-(\d{6})-(\d{6})-(\d{3})")
EXECUTORS = {"CHAT", "WORK", "CODEX", "SCRIPT_DETERMINISTICO", "HUMAN", "CI_RUNNER"}
STATUS = {"PLANNED", "READY", "IN_PROGRESS", "BLOCKED", "WAITING_HUMAN_ACTION", "VERIFIED"}
NEEDED = ("description", "result_ref", "accountable_owner", "tool", "environment",
          "context_mode", "destination_ref", "authorization_ref", "verification",
          "completion_gate", "fallback", "on_block", "cost_class", "spend_limit")


def validate(root: Path, strategy_code: str,
             matrix_ref: str | None = None, plan_ref: str | None = None) -> dict:
    """Validate declared action coverage; no tool, catalog or user attestation checks."""
    root = root.resolve()
    errors: list[str] = []
    match = EA.fullmatch(strategy_code)
    if not match:
        return {"status": "FAIL", "errors": ["INVALID_STRATEGY_CODE"]}
    namespace, sequence = match.groups()
    matrix_ref = matrix_ref or f"estrategias/{strategy_code}-actions.json"

    def read(rel: str) -> str:
        if not isinstance(rel, str) or not rel or rel.startswith(("/", "\\")) or (
                "\\" in rel or any(part in (".", "..", "") for part in rel.split("/"))):
            errors.append("INVALID_PATH:" + str(rel))
            return ""
        resolved = (root / rel).resolve()
        if not resolved.is_relative_to(root) or not resolved.is_file():
            errors.append("FILE_MISSING:" + rel)
            return ""
        try:
            return resolved.read_text(encoding="utf-8")
        except (UnicodeError, OSError):
            errors.append("FILE_UNREADABLE:" + rel)
            return ""

    raw = read(matrix_ref)
    try:
        matrix = json.loads(raw)
        if not isinstance(matrix, dict):
            raise ValueError
    except ValueError:
        matrix = {}
        errors.append("ACTION_MATRIX_INVALID_JSON")
    if matrix.get("strategy_code") != strategy_code:
        errors.append("ACTION_MATRIX_STRATEGY_MISMATCH")
    plan = plan_ref or matrix.get("plan_ref")
    if not isinstance(plan, str) or not plan.endswith(".md"):
        errors.append("PHASE_PLAN_REF_MISSING")
        plan_text = ""
    else:
        plan_text = read(plan)
    phases = {f"F-{a}-{b}-{c}" for a, b, c in PHASE.findall(plan_text)
              if a == namespace and b == sequence}
    if strategy_code not in plan_text or not phases:
        errors.append("PHASE_PLAN_INVALID_OR_EMPTY")
    actions = matrix.get("actions")
    if not isinstance(actions, list) or not actions:
        actions = []
        errors.append("NO_ACTIONS_DEFINED")
    seen_keys: set[str] = set()
    covered: set[str] = set()
    for index, item in enumerate(actions, 1):
        prefix = f"ACTION_{index}"
        if not isinstance(item, dict):
            errors.append(prefix + "_NOT_OBJECT")
            continue
        action_key = item.get("action_key")
        m = ACTION.fullmatch(action_key) if isinstance(action_key, str) else None
        if not m or (m.group(1), m.group(2)) != (namespace, sequence):
            errors.append(prefix + "_KEY_INVALID")
        elif action_key in seen_keys:
            errors.append(prefix + "_KEY_DUPLICATE")
        else:
            seen_keys.add(action_key)
        phase = item.get("phase_code")
        if phase not in phases:
            errors.append(prefix + "_UNKNOWN_PHASE")
        else:
            covered.add(phase)
        for key in NEEDED:
            val = item.get(key)
            if val is None or (isinstance(val, str) and
                               (not val.strip() or val.strip().upper() in ("TBD", "TODO", "UNKNOWN"))):
                errors.append(prefix + "_MISSING_" + key.upper())
        for key in ("source_refs", "preconditions"):
            value = item.get(key)
            if not isinstance(value, list) or not value or not all(isinstance(s, str) and s.strip() for s in value):
                errors.append(prefix + "_MISSING_" + key.upper())
        executor = item.get("executor")
        if executor not in EXECUTORS:
            errors.append(prefix + "_EXECUTOR_INVALID")
        routing = item.get("routing_action_id")
        if executor == "HUMAN":
            if routing != "HUMAN_INTERVENTION":
                errors.append(prefix + "_HUMAN_ROUTING_MISMATCH")
        elif not isinstance(routing, str) or not re.fullmatch(r"[A-Z][A-Z0-9_]+", routing) or routing == "HUMAN_INTERVENTION":
            errors.append(prefix + "_ROUTING_ACTION_ID_INVALID")
        if item.get("status") not in STATUS:
            errors.append(prefix + "_STATUS_INVALID")
        if item.get("status") == "READY" and (
            item.get("authorization_ref") in ("NOT_GRANTED", "PENDING_HUMAN_DECISION") or
            item.get("environment") in ("NOT_AVAILABLE", "PENDING_ACCESS")):
            errors.append(prefix + "_READY_WITH_UNMET_PREREQUISITES")
    missing = sorted(phases - covered)
    if missing:
        errors.append("PHASES_WITHOUT_ACTIONS:" + ",".join(missing))
    return {
        "status": "PASS" if not errors else "FAIL",
        "strategy_code": strategy_code,
        "matrix_ref": matrix_ref,
        "declared_actions": len(actions),
        "phases_covered": len(covered),
        "phase_total": len(phases),
        "errors": errors,
        "limitation": "Structural contract only; action_id catalog routing, capability, PEP authorization and effects require independent runtime checks."
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--project-root", type=Path, required=True)
    ap.add_argument("--strategy-code", required=True)
    ap.add_argument("--matrix-ref")
    ap.add_argument("--plan-ref")
    args = ap.parse_args()
    result = validate(args.project_root, args.strategy_code, args.matrix_ref, args.plan_ref)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
