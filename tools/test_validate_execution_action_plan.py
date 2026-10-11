"""Contract tests for action-level plans; no remote side effects."""
import copy
import json
import tempfile
import unittest
from pathlib import Path

from validate_execution_action_plan import validate


def action(n: int, phase: int, executor: str = "CHAT") -> dict:
    return {
        "action_key": f"ACT-000123-000001-{n:03d}",
        "phase_code": f"F-000123-000001-{phase:03d}",
        "description": "Read and save a scoped document",
        "result_ref": "results/readback.md",
        "accountable_owner": "PRJ-000123 owner",
        "executor": executor,
        "executor_scope": "approved session",
        "tool": "GitHub connector" if executor != "HUMAN" else "ChatGPT Project Settings UI",
        "environment": "Global Chat" if executor != "HUMAN" else "Native ChatGPT Project",
        "context_mode": "B0" if executor != "HUMAN" else "B1+C3 if confirmed",
        "source_refs": ["AGENTS.md"],
        "destination_ref": "P2 git repository" if executor != "HUMAN" else "native UI",
        "routing_action_id": "GITHUB_DOC_WRITE" if executor != "HUMAN" else "HUMAN_INTERVENTION",
        "authorization_ref": "NOT_GRANTED",
        "preconditions": ["mandate must be checked"],
        "verification": "readback or human attestation",
        "completion_gate": "GATE_TO_VERIFY",
        "fallback": "BLOCKED unless separately authorized",
        "on_block": "record owner, cause, next step",
        "cost_class": "UNKNOWN",
        "spend_limit": 0,
        "status": "PLANNED"
    }


class ActionPlanTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.plan = "estrategias/EA-000123-000001.md"
        self.matrix = "estrategias/EA-000123-000001-actions.json"
        self.write(self.plan, "# EA-000123-000001\nF-000123-000001-001\nF-000123-000001-002")
        self.data = {"strategy_code": "EA-000123-000001", "plan_ref": self.plan,
                     "actions": [action(1, 1), action(2, 2)]}
        self.save()
    def write(self, name, content):
        file = self.root / name
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(content, encoding="utf-8")
    def save(self):
        self.write(self.matrix, json.dumps(self.data))
    def check(self):
        return validate(self.root, "EA-000123-000001")
    def test_complete_plan_passes(self):
        self.assertEqual(self.check()["status"], "PASS")
    def test_missing_matrix_fails(self):
        (self.root / self.matrix).unlink()
        self.assertEqual(self.check()["status"], "FAIL")
    def test_phase_without_action_fails(self):
        self.data["actions"].pop()
        self.save()
        self.assertTrue(any("PHASES_WITHOUT_ACTIONS" in e for e in self.check()["errors"]))
    def test_missing_executor_fails(self):
        del self.data["actions"][0]["executor"]
        self.save()
        self.assertEqual(self.check()["status"], "FAIL")
    def test_missing_tool_fails(self):
        self.data["actions"][0]["tool"] = "TBD"
        self.save()
        self.assertEqual(self.check()["status"], "FAIL")
    def test_missing_environment_fails(self):
        self.data["actions"][0]["environment"] = ""
        self.save()
        self.assertEqual(self.check()["status"], "FAIL")
    def test_duplicate_key_fails(self):
        self.data["actions"][1]["action_key"] = self.data["actions"][0]["action_key"]
        self.save()
        self.assertEqual(self.check()["status"], "FAIL")
    def test_wrong_phase_fails(self):
        self.data["actions"][0]["phase_code"] = "F-000123-000002-001"
        self.save()
        self.assertEqual(self.check()["status"], "FAIL")
    def test_human_action_requires_human_route(self):
        self.data["actions"][0] = action(1, 1, "HUMAN")
        self.save()
        self.assertEqual(self.check()["status"], "PASS")
        self.data["actions"][0]["routing_action_id"] = "GITHUB_DOC_WRITE"
        self.save()
        self.assertEqual(self.check()["status"], "FAIL")
    def test_ready_without_grant_fails(self):
        self.data["actions"][0]["status"] = "READY"
        self.save()
        self.assertIn("ACTION_1_READY_WITH_UNMET_PREREQUISITES", self.check()["errors"])
    def test_wrong_strategy_fails(self):
        self.assertEqual(validate(self.root, "EA-000123-000002")["status"], "FAIL")
    def test_missing_verification_fails(self):
        self.data["actions"][1]["verification"] = ""
        self.save()
        self.assertEqual(self.check()["status"], "FAIL")


if __name__ == "__main__":
    unittest.main()
