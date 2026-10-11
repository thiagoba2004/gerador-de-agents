"""Offline contract tests: documentary composition is not ChatGPT homologation."""
import copy
import hashlib
import json
import unittest
from pathlib import Path

from sciv_bootstrap import BEGIN, END, BootstrapError, integrate, render

ROOT = Path(__file__).resolve().parents[1]


class SCIVBootstrapContractTests(unittest.TestCase):
    def setUp(self):
        self.profile = {"project_code": "PRJ-000021", "project_ref": "thiagoba2004/cursos-universitarios",
                        "sciv_bootstrap": {"enabled": True, "binding_evidence": "user-session-report",
                                           "github_read_evidence": "tool-read-report",
                                           "provisioning_evidence": "independent-commit-readback"}}
        self.state = {"project_code": "PRJ-000021", "repository": self.profile["project_ref"],
                      "inbox": "comunicados/governanca-geral/mensagens",
                      "outbox": "comunicados/ia-especializada/mensagens",
                      "operational_ref": "feat/sciv-essencial-piloto-20261011"}
        self.original = "Missão aprovada, C3 e segurança.\n\n**Bootstrap obrigatório:** estado e planos.\n\nOutras regras.\n"

    def test_preserves_all_original_instruction_bytes(self):
        result = integrate(self.original, self.profile, self.state)
        start, end = result.index(BEGIN), result.index(END) + len(END) + 2
        self.assertEqual(result[:start] + result[end:], self.original)

    def test_concrete_own_repository_three_sources_before_task_bootstrap(self):
        result = integrate(self.original, self.profile, self.state)
        self.assertLess(result.index(BEGIN), result.index("**Bootstrap obrigatório:**"))
        for value in (self.profile["project_ref"], self.state["operational_ref"],
                      "comunicados/SCIV_STATE.json", self.state["inbox"], self.state["outbox"]):
            self.assertIn(value, result)
        self.assertNotIn("$repository", result)

    def test_reapplication_is_byte_identical(self):
        once = integrate(self.original, self.profile, self.state)
        self.assertEqual(integrate(once, self.profile, self.state), once)
        self.assertEqual(once.count(BEGIN), 1)

    def test_authorized_integration_ref_update_removes_old_pilot(self):
        once = integrate(self.original, self.profile, self.state)
        self.state["operational_ref"] = "main"
        updated = integrate(once, self.profile, self.state)
        self.assertNotIn("feat/sciv-essencial-piloto-20261011", updated)
        self.assertIn("referência deste pacote é `main`", updated)

    def test_unenabled_project_is_unchanged(self):
        self.profile.pop("sciv_bootstrap")
        self.assertEqual(integrate(self.original, self.profile, {}), self.original)

    def test_disabled_profile_does_not_erase_existing_block(self):
        once = integrate(self.original, self.profile, self.state)
        self.profile["sciv_bootstrap"]["enabled"] = False
        self.assertEqual(integrate(once, self.profile, {}), once)

    def test_no_binding_evidence_cannot_propagate(self):
        self.profile["sciv_bootstrap"].pop("binding_evidence")
        with self.assertRaisesRegex(BootstrapError, "DEPENDENCY_MISSING"):
            integrate(self.original, self.profile, self.state)

    def test_no_read_capability_evidence_cannot_propagate(self):
        self.profile["sciv_bootstrap"]["github_read_evidence"] = ""
        with self.assertRaisesRegex(BootstrapError, "DEPENDENCY_MISSING"):
            integrate(self.original, self.profile, self.state)

    def test_no_provisioning_evidence_cannot_propagate(self):
        self.profile["sciv_bootstrap"].pop("provisioning_evidence")
        with self.assertRaisesRegex(BootstrapError, "DEPENDENCY_MISSING"):
            render(self.profile, self.state)

    def test_wrong_project_state_is_rejected(self):
        self.state["project_code"] = "PRJ-000022"
        with self.assertRaisesRegex(BootstrapError, "MISMATCH"):
            render(self.profile, self.state)

    def test_wrong_repository_state_is_rejected(self):
        self.state["repository"] = "thiagoba2004/instituicoes-bancarias"
        with self.assertRaisesRegex(BootstrapError, "MISMATCH"):
            render(self.profile, self.state)

    def test_central_repository_not_destination(self):
        self.profile["project_ref"] = self.state["repository"] = "thiagoba2004/governanca-geral-modelos-ia"
        with self.assertRaisesRegex(BootstrapError, "INVALID_PROJECT_REPOSITORY"):
            render(self.profile, self.state)

    def test_central_mailbox_paths_not_destination(self):
        self.state["inbox"] = "comunicados/governanca-para-projetos/PRJ-000021"
        with self.assertRaisesRegex(BootstrapError, "INVALID_LOCAL_MAILBOX_PATH"):
            render(self.profile, self.state)

    def test_mailbox_collision_is_rejected(self):
        self.state["outbox"] = self.state["inbox"]
        with self.assertRaisesRegex(BootstrapError, "MAILBOX_COLLISION"):
            render(self.profile, self.state)

    def test_injection_in_reference_is_rejected(self):
        self.state["operational_ref"] = "main;$(id)"
        with self.assertRaisesRegex(BootstrapError, "INVALID_OPERATIONAL_REF"):
            render(self.profile, self.state)

    def test_missing_ref_never_defaults_silently_to_main(self):
        self.state.pop("operational_ref")
        with self.assertRaisesRegex(BootstrapError, "INVALID_OPERATIONAL_REF"):
            render(self.profile, self.state)

    def test_malformed_or_duplicate_managed_block_needs_review(self):
        for text in (BEGIN + self.original, END + self.original,
                     BEGIN + END + BEGIN + END + self.original):
            with self.subTest(text=text), self.assertRaises(BootstrapError):
                integrate(text, self.profile, self.state)

    def test_unknown_managed_version_needs_review(self):
        text = "<!-- SCIV_BOOTSTRAP_BEGIN v2 -->\n" + self.original
        with self.assertRaisesRegex(BootstrapError, "VERSION_REVIEW"):
            integrate(text, self.profile, self.state)

    def test_ambiguous_existing_bootstrap_cannot_be_overwritten(self):
        with self.assertRaisesRegex(BootstrapError, "ANCHOR_REVIEW"):
            integrate(self.original * 2, self.profile, self.state)

    def test_composition_does_not_mutate_profile_or_state(self):
        before = copy.deepcopy((self.profile, self.state))
        integrate(self.original, self.profile, self.state)
        self.assertEqual((self.profile, self.state), before)

    def test_access_failure_not_empty_and_independent_work_preserved(self):
        text = render(self.profile, self.state)
        for item in ("INBOX_UNAVAILABLE", "presumir caixa vazia", "tarefas independentes autorizadas",
                     "snapshot coerente", "commit observado"):
            self.assertIn(item, text)

    def test_outbox_version_grounding_no_privileged_execution(self):
        text = render(self.profile, self.state)
        for item in ("in_reply_to", "mesma versão", "hash dos bytes originais", "não replique",
                     "nunca executar", "GVC", "PEP", "WRITE_BLOCKED"):
            self.assertIn(item, text)

    def test_native_and_real_conversation_gates_not_inferred(self):
        text = render(self.profile, self.state)
        for item in ("não instala", "conversa efetivamente processada", "Abrir a interface não dispara",
                     "deduplicação real intersessões", "Não fazer polling", "S2+"):
            self.assertIn(item, text)

    def test_real_pilot_handoff_preserves_original_and_matches_profile(self):
        text = (ROOT / "handoffs/chatgpt/PRJ-000021-INSTRUCOES.md").read_text()
        start, end = text.index(BEGIN), text.index(END) + len(END) + 2
        preserved = text[:start] + text[end:]
        expected = json.loads((ROOT / "audits/sciv-bootstrap-2026-10-11/contrato.json").read_text())
        self.assertEqual(hashlib.sha256(preserved.encode()).hexdigest(), expected["original_adapter_sha256"])
        profile = json.loads((ROOT / "profiles/cursos-universitarios.json").read_text())
        self.assertEqual(profile["project_code"], "PRJ-000021")
        self.assertTrue(profile["sciv_bootstrap"]["enabled"])
        self.assertLessEqual(len(text), 8000)  # Engineering budget, not UI installation proof.


if __name__ == "__main__":
    unittest.main()
