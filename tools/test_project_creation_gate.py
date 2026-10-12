"""Negative and positive regression tests for the generator creation gate."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from project_creation_gate import contrast, inspect


class CreationGateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.write("AGENTS.md", "Projeto PRJ-000123")
        self.write("ROADMAP.md", "EA-000123-000001")
        self.write("REQUEST_LOG.jsonl", '{"request_id":"REQ-1"}\n')
        self.write("STRATEGY_LOG.jsonl", json.dumps({
            "strategy_code": "EA-000123-000001", "event_type": "CREATED",
            "plan_ref": "estrategias/EA-000123-000001.md"}) + "\n")
        self.write("PROJECT_STATE.json", json.dumps({
            "project_code": "PRJ-000123",
            "last_concluded_strategy_code": "EA-000123-000001"}))
        self.write("estrategias/EA-000123-000001.md",
                   "EA-000123-000001\nF-000123-000001-001\nF-000123-000001-002")
        from test_validate_execution_action_plan import action
        self.write("estrategias/EA-000123-000001-actions.json", json.dumps({
            "strategy_code": "EA-000123-000001",
            "plan_ref": "estrategias/EA-000123-000001.md",
            "actions": [action(1, 1), action(2, 2)]}))
    def write(self, name, value):
        dest = self.root / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(value, encoding="utf-8")
    def setup_sciv(self):
        strategy = "EA-000123-000003"
        ref = f"estrategias/{strategy}.md"
        log = (self.root / "STRATEGY_LOG.jsonl").read_text(encoding="utf-8")
        self.write("STRATEGY_LOG.jsonl", log + json.dumps({
            "event_type": "CREATED", "strategy_code": strategy, "plan_ref": ref}) + "\n")
        roadmap = (self.root / "ROADMAP.md").read_text(encoding="utf-8")
        self.write("ROADMAP.md", roadmap + "\n" + strategy)
        self.write(ref, strategy + "\nF-000123-000003-001\nF-000123-000003-002")
        from test_validate_execution_action_plan import action
        actions = [action(1, 1), action(2, 2)]
        for item in actions:
            for key in ("action_key", "phase_code"):
                item[key] = item[key].replace("000123-000001", "000123-000003")
        self.write(f"estrategias/{strategy}-actions.json", json.dumps({
            "strategy_code": strategy, "plan_ref": ref, "actions": actions}))
        self.write("comunicados/SCIV_STATE.json", json.dumps({
            "project_code": "PRJ-000123", "strategy_code": strategy, "mode": "ON_DEMAND",
            "operational_ref": "main",
            "inbox": "comunicados/governanca-geral/mensagens",
            "outbox": "comunicados/ia-especializada/mensagens"}))
        for where in ("governanca-geral", "ia-especializada"):
            for folder in ("mensagens", "historico"):
                self.write(f"comunicados/{where}/{folder}/README.md", "Queue")
        self.write("adaptadores/chatgpt/INSTRUCOES.md",
                   "<!-- SCIV_BOOTSTRAP_BEGIN v1 -->\nSCIV Sob Demanda\n"
                   "<!-- SCIV_BOOTSTRAP_END -->\nOther instructions")
    def setup_receipt(self):
        self.write("governanca/recebimentos/2026-10-11-prj-000123-gate-a6.md", "Current test")
        self.write("governanca/recebimentos/RECEIPT_EVIDENCE.json", json.dumps({
            "native_installation": {"classification": "HUMAN_ATTESTED",
                                    "evidence_ref": "human confirmation in a project conversation",
                                    "adapter_commit": "a" * 40},
            "receipt_test": {"gate": "A6", "classification": "NOT_VERIFIED",
                             "report_path": "governanca/recebimentos/2026-10-11-prj-000123-gate-a6.md",
                             "transport": "SCIV_ON_DEMAND", "message_id": "MSG-1", "correlation_id": "COR-1"},
            "sciv_test": {"classification": "NOT_VERIFIED"}}))
    def test_good_initial_strategy(self):
        self.assertEqual(inspect(self.root)["status"], "PASS")
    def test_missing_action_matrix_blocks_new_creation(self):
        (self.root / "estrategias/EA-000123-000001-actions.json").unlink()
        self.assertIn("FIRST_EA_ACTION_PLAN_UNVERIFIED",
                      inspect(self.root, route="A")["errors"])

    def test_missing_action_tool_blocks_new_creation(self):
        name = "estrategias/EA-000123-000001-actions.json"
        data = json.loads((self.root / name).read_text())
        data["actions"][0]["tool"] = ""
        self.write(name, json.dumps(data))
        self.assertIn("FIRST_EA_ACTION_PLAN_UNVERIFIED",
                      inspect(self.root, route="A")["errors"])

    def test_missing_first_ea(self):
        self.write("STRATEGY_LOG.jsonl", "")
        self.assertIn("FIRST_EA_CREATED_EVENT_MISSING", inspect(self.root)["errors"])
    def test_missing_plan(self):
        (self.root / "estrategias/EA-000123-000001.md").unlink()
        self.assertEqual(inspect(self.root)["status"], "FAIL")
    def test_incomplete_phase_plan(self):
        self.write("estrategias/EA-000123-000001.md", "EA-000123-000001\nF-000123-000001-002")
        self.assertIn("FIRST_EA_PHASE_PLAN_INCOMPLETE", inspect(self.root)["errors"])
    def test_bad_namespace(self):
        self.write("PROJECT_STATE.json", json.dumps({"project_code": "PRJ-000124"}))
        self.assertEqual(inspect(self.root)["status"], "FAIL")
    def test_sciv_opt_in_full_contract(self):
        self.setup_sciv()
        self.assertEqual(inspect(self.root, gate="sciv")["status"], "PASS")
    def test_sciv_requires_explicit_on_demand(self):
        self.setup_sciv()
        path = self.root / "comunicados/SCIV_STATE.json"
        j = json.loads(path.read_text()); j["mode"] = "AUTO"
        self.write("comunicados/SCIV_STATE.json", json.dumps(j))
        self.assertIn("SCIV_ON_DEMAND_REQUIRED", inspect(self.root, gate="sciv")["errors"])
    def test_no_sciv_block_unavailable(self):
        self.assertEqual(inspect(self.root, gate="sciv")["status"], "FAIL")
    def test_post_native_distinguishes_test_from_acceptance(self):
        self.setup_sciv(); self.setup_receipt()
        r = inspect(self.root, gate="post_native")
        self.assertEqual(r["status"], "PASS")
        self.assertIn("never native UI", r["limitation"])
        self.assertEqual(r["evidence"]["receipt_classification"], "NOT_VERIFIED")
    def test_post_native_requires_installation_attestation(self):
        self.setup_sciv(); self.setup_receipt()
        path = self.root / "governanca/recebimentos/RECEIPT_EVIDENCE.json"
        j = json.loads(path.read_text()); j["native_installation"] = {}
        self.write("governanca/recebimentos/RECEIPT_EVIDENCE.json", json.dumps(j))
        self.assertIn("NATIVE_INSTALLATION_HUMAN_ATTESTATION_MISSING", inspect(self.root, gate="post_native")["errors"])
    def test_route_b_accepts_existing_strategy_without_rewriting(self):
        self.write("STRATEGY_LOG.jsonl", json.dumps({
            "strategy_code": "EA-000123-000003", "event_type": "CREATED",
            "plan_ref": "estrategias/EA-000123-000003.md"}) + "\n")
        self.write("PROJECT_STATE.json", json.dumps({
            "project_code": "PRJ-000123", "current_strategy_code": "EA-000123-000003"}))
        self.write("ROADMAP.md", "EA-000123-000003")
        self.write("estrategias/EA-000123-000003.md",
                   "EA-000123-000003\nF-000123-000003-001\nF-000123-000003-002")
        self.assertEqual(inspect(self.root, route="B")["status"], "PASS")
        self.assertEqual(inspect(self.root, route="A")["status"], "FAIL")
    def test_invalid_jsonl_fails_closed(self):
        self.write("REQUEST_LOG.jsonl", "NOT_JSON")
        self.assertEqual(inspect(self.root)["status"], "FAIL")

    def setup_site(self):
        strategy = "EA-000123-000002"
        plan_ref = f"estrategias/{strategy}.md"
        path = self.root / "STRATEGY_LOG.jsonl"
        self.write("STRATEGY_LOG.jsonl", path.read_text(encoding="utf-8") + json.dumps({
            "event_type": "CREATED", "strategy_code": strategy, "plan_ref": plan_ref}) + "\n")
        self.write("ROADMAP.md", "EA-000123-000001\n" + strategy)
        self.write(plan_ref, strategy + "\n" + "\n".join(
            f"F-000123-000002-{n:03d}" for n in range(1, 7)))
        from test_validate_execution_action_plan import action
        actions = [action(n, n) for n in range(1, 7)]
        for item in actions:
            item["action_key"] = item["action_key"].replace("000123-000001", "000123-000002")
            item["phase_code"] = item["phase_code"].replace("000123-000001", "000123-000002")
        self.write(f"estrategias/{strategy}-actions.json", json.dumps({
            "strategy_code": strategy, "plan_ref": plan_ref, "actions": actions}))
        self.site = {
            "project_code": "PRJ-000123", "site_strategy_code": strategy,
            "authorization_ref": "REQ-1", "mandate_status": "APPROVED",
            "publication_status": "WAITING_HUMAN_PAGES_CONFIG", "source_folder": "docs",
            "design_tokens": {"background": "#FFFFFF", "surface": "#FAFAFA",
                              "text": "#111111", "primary": "#164B79", "secondary": "#365F42",
                              "accent": "#A45813", "border": "#777777", "focus": "#0044CC"},
            "palette_portfolio_review": "VERIFIED",
            "palette_review_evidence_ref": "governanca/palette-review.md"}
        self.save_site()
        self.write("SITE_ARCHITECTURE.md", "Home, menu global, Mapa do Site; revisão própria pendente.")
        self.write("SITE_STYLE_GUIDE.md", json.dumps(self.site["design_tokens"]))
        self.write("governanca/palette-review.md", "Fixture: comparação documental de paletas.")
        self.write("docs/index.html", "<!doctype html><title>Fixture Site</title>")

    def save_site(self):
        self.write("governanca/SITE_PUBLICATION_STATE.json", json.dumps(self.site))

    def test_site_preflight_does_not_accept_publication_or_change_blocked_phase(self):
        self.setup_site()
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        first = inspect(self.root, route="B", gate="site")
        self.assertEqual(first["status"], "PASS", first)
        self.assertFalse(first["evidence"]["public_site_verified_by_this_check"])
        self.assertEqual(first["evidence"]["site_publication_status"], "WAITING_HUMAN_PAGES_CONFIG")
        self.assertEqual(first, inspect(self.root, route="B", gate="site"))
        self.assertEqual(before, {p.relative_to(self.root): p.read_bytes()
                                  for p in self.root.rglob("*") if p.is_file()})

    def test_active_module_without_site_state_blocks_bootstrap(self):
        state = json.loads((self.root / "PROJECT_STATE.json").read_text())
        for modules in ({"web-site": "ATIVADO"}, [{"module_id": "web-site", "status": "ATIVADO"}]):
            state["modules"] = modules
            self.write("PROJECT_STATE.json", json.dumps(state))
            self.assertIn("SITE_MANDATE_NOT_APPROVED", inspect(self.root)["errors"])

    def test_site_no_mandate_has_no_default_activation(self):
        self.assertEqual(inspect(self.root)["status"], "PASS")
        self.assertFalse((self.root / "governanca/SITE_PUBLICATION_STATE.json").exists())
        self.assertIn("SITE_MANDATE_NOT_APPROVED", inspect(self.root, gate="site")["errors"])

    def test_pending_or_not_applicable_does_not_require_ea(self):
        for mandate in ("PENDING_EVIDENCE", "NOT_APPLICABLE"):
            self.site = {"mandate_status": mandate, "publication_status": "NOT_DEPLOYED"}
            self.save_site()
            self.assertEqual(inspect(self.root)["status"], "PASS")
            self.assertEqual(inspect(self.root, gate="site")["status"], "FAIL")
        self.site["publication_status"] = "PUBLIC_SITE_VERIFIED"
        self.save_site()
        self.assertIn("SITE_PUBLICATION_WITHOUT_MANDATE", inspect(self.root)["errors"])

    def test_approved_mandate_requires_site_ea_even_at_bootstrap(self):
        self.setup_site()
        self.write("STRATEGY_LOG.jsonl", (self.root / "STRATEGY_LOG.jsonl").read_text().splitlines()[0] + "\n")
        for gate in ("bootstrap", "site"):
            self.assertIn("SITE_EA_CREATED_NOT_UNIQUE", inspect(self.root, gate=gate)["errors"])

    def test_site_rejects_wrong_namespace_and_project(self):
        self.setup_site()
        self.site.update(project_code="PRJ-000124", site_strategy_code="EA-000124-000002")
        self.save_site()
        result = inspect(self.root, gate="site")
        self.assertIn("SITE_PROJECT_MISMATCH", result["errors"])
        self.assertIn("SITE_STRATEGY_ID_INVALID", result["errors"])

    def test_site_cannot_reuse_constitution_ea(self):
        self.setup_site()
        self.site["site_strategy_code"] = "EA-000123-000001"
        self.save_site()
        self.assertIn("SITE_SEPARATE_EA_REQUIRED", inspect(self.root, gate="site")["errors"])

    def test_site_request_plan_roadmap_and_matrix_are_required(self):
        self.setup_site()
        for relative in ("REQUEST_LOG.jsonl", "estrategias/EA-000123-000002.md", "ROADMAP.md",
                         "estrategias/EA-000123-000002-actions.json"):
            with self.subTest(relative=relative):
                file = self.root / relative
                original = file.read_bytes()
                file.write_bytes(b"")
                self.assertEqual(inspect(self.root, gate="site")["status"], "FAIL")
                file.write_bytes(original)

    def test_site_partial_plan_or_duplicate_created_fails(self):
        self.setup_site()
        self.write("estrategias/EA-000123-000002.md", "EA-000123-000002\nF-000123-000002-001\nF-000123-000002-003")
        self.assertIn("SITE_PHASE_PLAN_INCOMPLETE", inspect(self.root, gate="site")["errors"])
        log = (self.root / "STRATEGY_LOG.jsonl").read_text()
        self.write("STRATEGY_LOG.jsonl", log + log.splitlines()[-1] + "\n")
        self.assertIn("SITE_EA_CREATED_NOT_UNIQUE", inspect(self.root, gate="site")["errors"])

    def test_site_preserves_distinct_palettes_without_universal_colors(self):
        self.setup_site()
        for primary in ("#164B79", "#793516", "#493579"):
            self.site["design_tokens"]["primary"] = primary
            self.save_site()
            self.write("SITE_STYLE_GUIDE.md", json.dumps(self.site["design_tokens"]))
            self.assertEqual(inspect(self.root, gate="site")["status"], "PASS")
            self.assertEqual(json.loads((self.root / "governanca/SITE_PUBLICATION_STATE.json").read_text())
                             ["design_tokens"]["primary"], primary)

    def test_site_token_shape_and_contrast_fail_closed(self):
        self.setup_site()
        for value in (None, "#FFF", "red", 123, "#GGGGGG"):
            self.site["design_tokens"]["primary"] = value
            self.save_site()
            self.assertIn("SITE_TOKEN_INVALID:primary", inspect(self.root, gate="site")["errors"])
        self.site["design_tokens"]["primary"] = "#164B79"
        self.site["design_tokens"]["text"] = "#FFFFFF"
        self.save_site()
        result = inspect(self.root, gate="site")
        for surface in ("background", "surface"):
            self.assertIn("SITE_TEXT_CONTRAST_LOW:" + surface, result["errors"])
        self.assertAlmostEqual(contrast("#000000", "#FFFFFF"), 21)
        self.assertAlmostEqual(contrast("#FFFFFF", "#FFFFFF"), 1)
        self.assertGreaterEqual(contrast("#767676", "#FFFFFF"), 4.5)
        self.assertLess(contrast("#777777", "#FFFFFF"), 4.5)

    def test_site_requires_documented_tokens_and_palette_evidence(self):
        self.setup_site()
        self.write("SITE_STYLE_GUIDE.md", "Undocumented tokens")
        self.site["palette_portfolio_review"] = "NOT_VERIFIED"
        self.site["palette_review_evidence_ref"] = "../outside.md"
        self.save_site()
        result = inspect(self.root, gate="site")
        self.assertIn("SITE_STYLE_TOKEN_UNDOCUMENTED:primary", result["errors"])
        self.assertIn("SITE_PALETTE_REVIEW_UNVERIFIED", result["errors"])
        self.assertIn("INVALID_PATH:../outside.md", result["errors"])

    def test_site_public_source_cannot_escape_root(self):
        self.setup_site()
        self.site["source_folder"] = "../outside"
        self.save_site()
        self.assertIn("INVALID_PATH:../outside/index.html", inspect(self.root, gate="site")["errors"])

    def test_site_publication_claim_without_proof_rejected(self):
        self.setup_site()
        self.site["publication_status"] = "PUBLIC_SITE_VERIFIED"
        self.save_site()
        result = inspect(self.root, gate="site")
        self.assertIn("SITE_HTTP_EVIDENCE_MISSING", result["errors"])
        self.assertIn("SITE_PUBLICATION_SHA_MISSING:deploy_commit", result["errors"])
        self.site.update(source_commit="a" * 40, deploy_commit="b" * 40,
                         public_url="https://example.test/", http_evidence_ref="governanca/http.md")
        self.save_site()
        self.write("governanca/http.md", "Synthetic fixture only, not live HTTP evidence.")
        result = inspect(self.root, gate="site")
        self.assertEqual(result["status"], "PASS")
        self.assertFalse(result["evidence"]["public_site_verified_by_this_check"])

    def test_site_and_sciv_remain_independent(self):
        self.setup_site()
        self.assertEqual(inspect(self.root, gate="site")["status"], "PASS")
        self.assertEqual(inspect(self.root, gate="sciv")["status"], "FAIL")
        self.setup_sciv()
        self.assertEqual(inspect(self.root, gate="sciv")["status"], "PASS")
        self.site["design_tokens"]["text"] = "#FFFFFF"
        self.save_site()
        self.assertEqual(inspect(self.root, gate="sciv")["status"], "PASS")
        self.assertEqual(inspect(self.root, gate="site")["status"], "FAIL")

    def test_unknown_gate_cannot_bypass_checks(self):
        self.assertEqual(inspect(self.root, gate="unknown")["status"], "FAIL")

    def test_site_cli_pass_and_fail_exit_codes(self):
        self.setup_site()
        cmd = [sys.executable, str(Path(__file__).with_name("project_creation_gate.py")),
               "--project-root", str(self.root), "--gate", "site", "--route", "A"]
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["status"], "PASS")
        self.site["mandate_status"] = "PENDING_EVIDENCE"
        self.save_site()
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(json.loads(result.stdout)["status"], "FAIL")

    def test_site_legacy_b_plan_not_renumbered_or_forced_to_new_matrix_at_bootstrap(self):
        self.setup_site()
        (self.root / "estrategias/EA-000123-000002-actions.json").unlink()
        self.assertEqual(inspect(self.root, route="B")["status"], "PASS")
        self.assertIn("SITE_ACTION_PLAN_UNVERIFIED", inspect(self.root, route="A")["errors"])
        self.assertIn("SITE_ACTION_PLAN_UNVERIFIED", inspect(self.root, route="B", gate="site")["errors"])

    def test_site_malformed_state_fails_without_exception(self):
        for raw in ("[]", "null", "{", '{"site_strategy_code": []}'):
            self.write("governanca/SITE_PUBLICATION_STATE.json", raw)
            self.assertEqual(inspect(self.root, gate="site")["status"], "FAIL")


if __name__ == "__main__":
    unittest.main()
