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
COLOR_RE = re.compile(r"^#[a-fA-F0-9]{6}$")
TOKENS = ("background", "surface", "text", "primary", "secondary", "accent", "border", "focus")


def contrast(foreground: str, background: str) -> float:
    """WCAG relative luminance for opaque sRGB tokens; no browser inference."""
    def luminance(color: str) -> float:
        channels = [int(color[i:i + 2], 16) / 255 for i in (1, 3, 5)]
        linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
                  for c in channels]
        return sum(c * w for c, w in zip(linear, (0.2126, 0.7152, 0.0722)))
    low, high = sorted((luminance(foreground), luminance(background)))
    return (high + 0.05) / (low + 0.05)


def inspect(root: Path, route: str = "A", gate: str = "bootstrap") -> dict:
    """Check versioned prerequisites only. PASS is not handoff acceptance."""
    root = root.resolve()
    errors: list[str] = []
    evidence: dict[str, object] = {}

    def fail(code: str) -> None:
        if code not in errors:
            errors.append(code)

    if route not in ("A", "B") or gate not in ("bootstrap", "sciv", "post_native", "site"):
        fail("INVALID_ROUTE_OR_GATE")

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
            if route == "A" or gate != "bootstrap":
                from validate_execution_action_plan import validate
                contract = validate(root, strategy, plan_ref=ref)
                evidence["action_plan_result"] = contract["status"]
                if contract["status"] != "PASS":
                    evidence["action_plan_errors"] = contract["errors"]
                    # Only absence is eligible; a malformed/unsafe existing
                    # matrix is never excused, and bootstrap always stays strict.
                    matrix = root / f"estrategias/{strategy}-actions.json"
                    proof = None
                    if gate != "bootstrap" and not matrix.exists() and not matrix.is_symlink() and not errors:
                        from legacy_bootstrap_evidence import legacy_proof
                        proof = legacy_proof(root, first, history, requests, plan)
                    if proof:
                        evidence["action_plan_result"] = "NOT_BACKFILLED"
                        evidence["legacy_bootstrap"] = proof
                    else:
                        fail("FIRST_EA_ACTION_PLAN_UNVERIFIED")

    # Module decisions live in PROJECT_STATE; the separate publication state can
    # also trigger the requirement. Existing projects without Site remain valid.
    modules = state.get("modules", [])
    active_site = ((isinstance(modules, dict) and modules.get("web-site") == "ATIVADO") or
                   (isinstance(modules, list) and any(
                       isinstance(item, dict) and item.get("module_id") == "web-site" and
                       item.get("status") == "ATIVADO" for item in modules)))
    site_ref = "governanca/SITE_PUBLICATION_STATE.json"
    has_site_state = (root / site_ref).exists()
    site = obj(site_ref) if gate == "site" or active_site or has_site_state else {}
    approved_site = site.get("mandate_status") == "APPROVED"
    if gate == "site" or active_site or approved_site:
        if site.get("project_code") != code:
            fail("SITE_PROJECT_MISMATCH")
        if not approved_site:
            fail("SITE_MANDATE_NOT_APPROVED")
        authorization = site.get("authorization_ref")
        if not isinstance(authorization, str) or not authorization.strip() or not any(
                entry.get("request_id") == authorization for entry in requests):
            fail("SITE_AUTHORIZATION_REQUEST_MISSING")
        strategy = site.get("site_strategy_code")
        sm = STRATEGY_RE.fullmatch(strategy) if isinstance(strategy, str) else None
        if not sm or sm.group(1) != number:
            fail("SITE_STRATEGY_ID_INVALID")
        else:
            matches = [entry for entry in created if entry["strategy_code"] == strategy]
            if len(matches) != 1:
                fail("SITE_EA_CREATED_NOT_UNIQUE")
            else:
                ref = matches[0].get("plan_ref")
                if not isinstance(ref, str) or not ref.startswith("estrategias/"):
                    fail("SITE_PLAN_REF_MISSING")
                else:
                    plan = document(ref)
                    ids = sorted({int(c) for a, b, c in PHASE_RE.findall(plan)
                                  if strategy == f"EA-{a}-{b}"})
                    if strategy not in plan or len(ids) < 2 or ids != list(range(1, max(ids, default=0) + 1)):
                        fail("SITE_PHASE_PLAN_INCOMPLETE")
                    if strategy == evidence.get("initial_strategy"):
                        fail("SITE_SEPARATE_EA_REQUIRED")
                    if strategy not in roadmap:
                        fail("SITE_ROADMAP_REFERENCE_MISSING")
                    # New Rota A Site EAs require the matrix even at bootstrap.
                    # Historical B EAs are preserved; remaining preflight actions
                    # must have an explicit contract before technical readiness.
                    if route == "A" or gate == "site":
                        from validate_execution_action_plan import validate
                        contract = validate(root, strategy, plan_ref=ref)
                        if contract["status"] != "PASS":
                            fail("SITE_ACTION_PLAN_UNVERIFIED")
                            evidence["site_action_plan_errors"] = contract["errors"]
                    evidence["site_strategy"] = strategy
                    evidence["site_plan"] = ref
        evidence["site_mandate"] = site.get("mandate_status")
    elif has_site_state:
        if site.get("mandate_status") not in ("NOT_APPLICABLE", "PENDING_EVIDENCE"):
            fail("SITE_MANDATE_STATUS_INVALID")
        # A pending/absent mandate cannot quietly include a published Site.
        if site.get("publication_status") not in (None, "NOT_DEPLOYED"):
            fail("SITE_PUBLICATION_WITHOUT_MANDATE")
        evidence["site_mandate"] = site.get("mandate_status")

    if gate == "site":
        architecture = document("SITE_ARCHITECTURE.md")
        style = document("SITE_STYLE_GUIDE.md")
        if not architecture.strip() or not style.strip():
            fail("SITE_DESIGN_DOCUMENTS_EMPTY")
        tokens = site.get("design_tokens")
        if not isinstance(tokens, dict):
            tokens = {}
        valid_colors = True
        for token in TOKENS:
            value = tokens.get(token)
            if not isinstance(value, str) or not COLOR_RE.fullmatch(value):
                fail("SITE_TOKEN_INVALID:" + token)
                valid_colors = False
            elif value.lower() not in style.lower():
                fail("SITE_STYLE_TOKEN_UNDOCUMENTED:" + token)
        if valid_colors:
            ratios = {surface: contrast(tokens["text"], tokens[surface])
                      for surface in ("background", "surface")}
            evidence["site_text_contrast"] = ratios
            for surface, ratio in ratios.items():
                if ratio < 4.5:
                    fail("SITE_TEXT_CONTRAST_LOW:" + surface)
        if site.get("palette_portfolio_review") != "VERIFIED":
            fail("SITE_PALETTE_REVIEW_UNVERIFIED")
        review = site.get("palette_review_evidence_ref")
        if not isinstance(review, str) or not review.strip():
            fail("SITE_PALETTE_REVIEW_EVIDENCE_MISSING")
        elif not document(review).strip():
            fail("SITE_PALETTE_REVIEW_EVIDENCE_EMPTY")
        folder = site.get("source_folder")
        # Reuse the same containment/path checks for the public entry point.
        if not isinstance(folder, str) or not folder.strip():
            fail("SITE_SOURCE_FOLDER_MISSING")
        else:
            document(folder + "/index.html")
        publication = site.get("publication_status")
        if publication not in ("NOT_DEPLOYED", "SITE_SOURCE_STAGED", "WAITING_HUMAN_PAGES_CONFIG",
                               "PAGES_CONFIGURED", "PUBLIC_SITE_VERIFIED"):
            fail("SITE_PUBLICATION_STATUS_INVALID")
        if publication == "PUBLIC_SITE_VERIFIED":
            for key in ("source_commit", "deploy_commit"):
                if not HEX_SHA.fullmatch(str(site.get(key, ""))):
                    fail("SITE_PUBLICATION_SHA_MISSING:" + key)
            url = site.get("public_url")
            if not isinstance(url, str) or not re.fullmatch(r"https://[^\s/]+(?:/[^\s]*)?", url):
                fail("SITE_PUBLIC_URL_MISSING")
            http = site.get("http_evidence_ref")
            if not isinstance(http, str) or not http.strip():
                fail("SITE_HTTP_EVIDENCE_MISSING")
            elif not document(http).strip():
                fail("SITE_HTTP_EVIDENCE_EMPTY")
        evidence["site_publication_status"] = publication
        evidence["public_site_verified_by_this_check"] = False

    if gate in ("sciv", "post_native"):
        sciv = obj("comunicados/SCIV_STATE.json")
        # The historical bootstrap exemption never covers the current rollout.
        rollout = sciv.get("strategy_code")
        sm = STRATEGY_RE.fullmatch(rollout) if isinstance(rollout, str) else None
        if not sm or sm.group(1) != number or rollout == evidence.get("initial_strategy"):
            fail("SCIV_SEPARATE_STRATEGY_REQUIRED")
        else:
            matches = [e for e in created if e["strategy_code"] == rollout]
            if len(matches) != 1:
                fail("SCIV_EA_CREATED_NOT_UNIQUE")
            else:
                from validate_execution_action_plan import validate
                ref = matches[0].get("plan_ref")
                if not isinstance(ref, str) or not ref.startswith("estrategias/"):
                    fail("SCIV_PLAN_REF_MISSING")
                else:
                    plan = document(ref)
                    ids = sorted({int(c) for a, b, c in PHASE_RE.findall(plan)
                                  if rollout == f"EA-{a}-{b}"})
                    if rollout not in plan or len(ids) < 2 or ids != list(range(1, max(ids, default=0) + 1)):
                        fail("SCIV_PHASE_PLAN_INCOMPLETE")
                    contract = validate(root, rollout, plan_ref=ref)
                    evidence["sciv_action_plan_result"] = contract["status"]
                    if contract["status"] != "PASS":
                        fail("SCIV_ACTION_PLAN_UNVERIFIED")
                        evidence["sciv_action_plan_errors"] = contract["errors"]
                    if rollout not in roadmap:
                        fail("SCIV_ROADMAP_REFERENCE_MISSING")
                    evidence["sciv_strategy"] = rollout
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
            "limitation": "Documentary consistency only; never native UI attestation, A6/B8 acceptance or live PEP authorization. Site checks do not verify live deploy/HTTP, visual portfolio distinction, browser navigation or full accessibility."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", required=True, type=Path)
    parser.add_argument("--route", choices=("A", "B"), default="A")
    parser.add_argument("--gate", choices=("bootstrap", "sciv", "post_native", "site"), default="bootstrap")
    args = parser.parse_args()
    outcome = inspect(args.project_root, route=args.route, gate=args.gate)
    print(json.dumps(outcome, ensure_ascii=False, indent=2))
    return 0 if outcome["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
