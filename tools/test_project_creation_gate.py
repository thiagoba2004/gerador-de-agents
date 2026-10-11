"""Negative and positive regression tests for the generator creation gate."""
import json
import tempfile
import unittest
from pathlib import Path

from project_creation_gate import inspect


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
        self.write("comunicados/SCIV_STATE.json", json.dumps({
            "project_code": "PRJ-000123", "mode": "ON_DEMAND",
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


if __name__ == "__main__":
    unittest.main()
