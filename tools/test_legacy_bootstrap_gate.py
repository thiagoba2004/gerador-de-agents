"""Historical Git fixtures are synthetic; never fabricate production matrices."""
import json
import os
from pathlib import Path
import subprocess
import unittest

from project_creation_gate import inspect
import test_project_creation_gate as fixtures


class LegacyGateTests(unittest.TestCase):
    # Reuse fixture helpers without inheriting/rerunning the existing test suite.
    setUp = fixtures.CreationGateTests.setUp
    write = fixtures.CreationGateTests.write
    setup_sciv = fixtures.CreationGateTests.setup_sciv
    setup_site = fixtures.CreationGateTests.setup_site
    save_site = fixtures.CreationGateTests.save_site
    setup_receipt = fixtures.CreationGateTests.setup_receipt

    def git(self, *args, stamp="2026-10-10T12:00:00-03:00"):
        env = dict(os.environ, GIT_AUTHOR_DATE=stamp, GIT_COMMITTER_DATE=stamp)
        result = subprocess.run(["git", "-c", f"safe.directory={self.root.as_posix()}",
                                 "-C", str(self.root), *args], env=env,
                                capture_output=True, encoding="utf-8")
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout.strip()

    def legacy(self, stamp="2026-10-10T12:00:00-03:00"):
        path = self.root / "STRATEGY_LOG.jsonl"
        first = json.loads(path.read_text().splitlines()[0])
        first.update(date="2026-10-10", phase_total=2, trigger_request_ids=["REQ-1"])
        terminal = dict(strategy_code=first["strategy_code"], event_type="CONCLUDED",
                        date="2026-10-10", status="CONCLUIDO", phase_total=2,
                        phase_number=2, terminal_gate="TECHNICAL_BOOTSTRAP_VERIFIED")
        self.write("STRATEGY_LOG.jsonl", json.dumps(first) + "\n" + json.dumps(terminal) + "\n")
        (self.root / "estrategias/EA-000123-000001-actions.json").unlink()
        self.git("init")
        self.git("add", ".")
        self.git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.test",
                 "commit", "-m", "Synthetic historical bootstrap", stamp=stamp)

    def change_event(self, index, **updates):
        records = [json.loads(s) for s in (self.root / "STRATEGY_LOG.jsonl").read_text().splitlines()]
        records[index].update(updates)
        self.write("STRATEGY_LOG.jsonl", "\n".join(json.dumps(e) for e in records) + "\n")

    def test_legacy_sciv_proof_and_idempotence(self):
        self.legacy(); self.setup_sciv()
        before = self.git("status", "--porcelain")
        result = inspect(self.root, gate="sciv")
        self.assertEqual(result["status"], "PASS", result)
        self.assertEqual(result["evidence"]["action_plan_result"], "NOT_BACKFILLED")
        proof = result["evidence"]["legacy_bootstrap"]
        self.assertEqual(proof["status"], "LEGACY_FIRST_EA_MATRIX_NOT_BACKFILLED")
        self.assertEqual(proof["commit"], self.git("rev-parse", "HEAD"))
        self.assertEqual(result, inspect(self.root, gate="sciv"))
        self.assertEqual(before, self.git("status", "--porcelain"))
        self.assertFalse((self.root / "estrategias/EA-000123-000001-actions.json").exists())

    def test_legacy_bootstrap_still_requires_matrix(self):
        self.legacy()
        self.assertIn("FIRST_EA_ACTION_PLAN_UNVERIFIED", inspect(self.root)["errors"])

    def test_legacy_site_and_post_native(self):
        self.legacy(); self.setup_site(); self.setup_sciv(); self.setup_receipt()
        for route in ("A", "B"):
            receipt_path = self.root / "governanca/recebimentos/RECEIPT_EVIDENCE.json"
            receipt = json.loads(receipt_path.read_text())
            receipt["receipt_test"]["gate"] = "A6" if route == "A" else "B8"
            self.write("governanca/recebimentos/RECEIPT_EVIDENCE.json", json.dumps(receipt))
            for gate in ("site", "sciv", "post_native"):
                result = inspect(self.root, route=route, gate=gate)
                self.assertEqual(result["status"], "PASS", result)
                self.assertEqual(result["evidence"]["action_plan_result"], "NOT_BACKFILLED")

    def test_new_rollout_matrices_and_plans_remain_strict(self):
        self.legacy(); self.setup_site(); self.setup_sciv()
        for relative, gate in (("estrategias/EA-000123-000002-actions.json", "site"),
                               ("estrategias/EA-000123-000003.md", "sciv")):
            path = self.root / relative
            original = path.read_bytes()
            path.write_bytes(b"{}")
            self.assertEqual(inspect(self.root, gate=gate)["status"], "FAIL")
            path.write_bytes(original)

    def test_new_unproven_initial_ea_is_strict_on_both_routes(self):
        self.setup_sciv()
        (self.root / "estrategias/EA-000123-000001-actions.json").unlink()
        for route in ("A", "B"):
            for gate in ("sciv", "post_native", "site"):
                self.assertIn("FIRST_EA_ACTION_PLAN_UNVERIFIED", inspect(self.root, route=route, gate=gate)["errors"])

    def test_new_commit_cannot_backdate_documentary_claim(self):
        self.legacy(stamp="2026-10-11T00:00:00-03:00"); self.setup_sciv()
        self.assertIn("FIRST_EA_ACTION_PLAN_UNVERIFIED", inspect(self.root, gate="sciv")["errors"])

    def test_conclusion_added_only_after_policy_is_not_historical_proof(self):
        self.legacy()
        log = (self.root / "STRATEGY_LOG.jsonl").read_text()
        self.write("STRATEGY_LOG.jsonl", log.splitlines()[0] + "\n")
        self.git("add", ".")
        self.git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.test",
                 "commit", "--amend", "--no-edit")
        self.write("STRATEGY_LOG.jsonl", log)
        self.setup_sciv()
        self.assertIn("FIRST_EA_ACTION_PLAN_UNVERIFIED", inspect(self.root, gate="sciv")["errors"])

    def test_terminal_phase_total_must_match_plan(self):
        self.legacy(); self.setup_sciv()
        self.change_event(0, phase_total=3)
        self.change_event(1, phase_total=3, phase_number=3)
        self.assertIn("FIRST_EA_ACTION_PLAN_UNVERIFIED", inspect(self.root, gate="sciv")["errors"])

    def test_author_date_alone_cannot_grant_legacy(self):
        self.legacy()
        self.git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.test",
                 "commit", "--amend", "--no-edit", "--date=2026-10-11T12:00:00-03:00")
        self.setup_sciv()
        self.assertIn("FIRST_EA_ACTION_PLAN_UNVERIFIED", inspect(self.root, gate="sciv")["errors"])

    def test_unversioned_or_parent_repository_is_not_proof(self):
        (self.root / "estrategias/EA-000123-000001-actions.json").unlink()
        self.setup_sciv()
        self.assertIn("FIRST_EA_ACTION_PLAN_UNVERIFIED", inspect(self.root, gate="sciv")["errors"])

    def test_forged_dates_terminal_request_and_plan_fail(self):
        for target in ("created_date", "concluded_date", "terminal", "request", "plan", "phase", "resumed"):
            with self.subTest(target=target):
                self.setUp(); self.legacy(); self.setup_sciv()
                if target == "created_date": self.change_event(0, date="2026-10-11")
                if target == "concluded_date": self.change_event(1, date="invalid")
                if target == "terminal": self.change_event(1, event_type="UPDATED")
                if target == "request": self.write("REQUEST_LOG.jsonl", '{"request_id":"OTHER"}\n')
                if target == "plan":
                    with (self.root / "estrategias/EA-000123-000001.md").open("a") as f: f.write("\nForged")
                if target == "phase": self.change_event(1, phase_number=1)
                if target == "resumed":
                    with (self.root / "STRATEGY_LOG.jsonl").open("a") as f:
                        f.write(json.dumps({"strategy_code":"EA-000123-000001", "event_type":"RESUMED"}) + "\n")
                self.assertEqual(inspect(self.root, gate="sciv")["status"], "FAIL")

    def test_existing_bad_matrix_never_exempted(self):
        self.legacy(); self.setup_sciv()
        self.write("estrategias/EA-000123-000001-actions.json", "{}")
        self.assertIn("FIRST_EA_ACTION_PLAN_UNVERIFIED", inspect(self.root, gate="sciv")["errors"])

    def test_current_sciv_contract_not_exempted(self):
        self.legacy(); self.setup_sciv()
        path = self.root / "estrategias/EA-000123-000003-actions.json"
        for raw in (None, "{}", "not-json"):
            if raw is None: path.unlink()
            else: path.write_text(raw)
            self.assertIn("SCIV_ACTION_PLAN_UNVERIFIED", inspect(self.root, gate="sciv")["errors"])

    def test_current_sciv_cannot_reuse_bootstrap_or_omit_identity(self):
        self.legacy(); self.setup_sciv()
        path = self.root / "comunicados/SCIV_STATE.json"
        data = json.loads(path.read_text())
        for value in (None, [], "EA-000123-000001", "EA-000124-000003"):
            data["strategy_code"] = value
            self.write("comunicados/SCIV_STATE.json", json.dumps(data))
            self.assertIn("SCIV_SEPARATE_STRATEGY_REQUIRED", inspect(self.root, gate="sciv")["errors"])

    def test_legacy_invariants_and_native_guards_preserved(self):
        for relative in ("REQUEST_LOG.jsonl", "AGENTS.md", "ROADMAP.md",
                         "estrategias/EA-000123-000001.md",
                         "governanca/recebimentos/RECEIPT_EVIDENCE.json"):
            with self.subTest(relative=relative):
                self.setUp(); self.legacy(); self.setup_sciv(); self.setup_receipt()
                (self.root / relative).write_text("")
                self.assertEqual(inspect(self.root, gate="post_native")["status"], "FAIL")


if __name__ == "__main__":
    unittest.main()
