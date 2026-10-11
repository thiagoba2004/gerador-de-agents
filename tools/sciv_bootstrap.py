"""Compose a documentary SCIV adapter offline. No network, effects or grants."""
from __future__ import annotations

import re
from pathlib import Path
from string import Template

BEGIN = "<!-- SCIV_BOOTSTRAP_BEGIN v1 -->"
END = "<!-- SCIV_BOOTSTRAP_END -->"
ANCHOR = "**Bootstrap obrigatório:**"
TEMPLATE = Path(__file__).resolve().parents[1] / "templates/SCIV_BOOTSTRAP.example.md"


class BootstrapError(ValueError):
    pass


def reference(value):
    if (not isinstance(value, str) or len(value) > 200 or
            not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._/-]*", value) or
            ".." in value or "//" in value or value.endswith(("/", ".", ".lock")) or
            any(part.startswith(".") for part in value.split("/"))):
        raise BootstrapError("INVALID_OPERATIONAL_REF")
    return value


def path(value):
    if (not isinstance(value, str) or not re.fullmatch(r"comunicados/[a-z0-9_/-]+", value) or
            "//" in value or value.endswith("/") or
            any(p in value.split("/") for p in ("governanca-para-projetos", "projetos-para-governanca"))):
        raise BootstrapError("INVALID_LOCAL_MAILBOX_PATH")
    return value


def render(profile: dict, state: dict) -> str | None:
    """Input evidence is declared trusted configuration, not authentication."""
    if not isinstance(profile, dict) or not isinstance(state, dict):
        raise BootstrapError("CONFIGURATION_MUST_BE_OBJECT")
    config = profile.get("sciv_bootstrap")
    if config is None:
        return None
    if not isinstance(config, dict):
        raise BootstrapError("CONFIGURATION_MUST_BE_OBJECT")
    if config.get("enabled") is False:
        return None
    if config.get("enabled") is not True:
        raise BootstrapError("INVALID_ENABLE_FLAG")
    for key in ("binding_evidence", "github_read_evidence", "provisioning_evidence"):
        if not isinstance(config.get(key), str) or not config[key].strip():
            raise BootstrapError("BOOTSTRAP_DEPENDENCY_MISSING:" + key)
    project, repo = profile.get("project_code"), profile.get("project_ref")
    if (not isinstance(project, str) or not re.fullmatch(r"PRJ-[0-9]{6}", project) or
            not isinstance(repo, str) or not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo) or
            repo == "thiagoba2004/governanca-geral-modelos-ia"):
        raise BootstrapError("INVALID_PROJECT_REPOSITORY")
    if state.get("project_code") != project or state.get("repository") != repo:
        raise BootstrapError("STATE_PROJECT_REPOSITORY_MISMATCH")
    inbox, outbox = path(state.get("inbox")), path(state.get("outbox"))
    if inbox == outbox or inbox.startswith(outbox + "/") or outbox.startswith(inbox + "/"):
        raise BootstrapError("MAILBOX_COLLISION")
    ref = reference(state.get("operational_ref"))
    # Ref comes from current local state, never a permanent pilot default.
    return Template(TEMPLATE.read_text(encoding="utf-8")).substitute(
        project=project, repository=repo, state_path="comunicados/SCIV_STATE.json",
        inbox=inbox, outbox=outbox, ref=ref).rstrip("\n") + "\n\n"


def integrate(existing: str, profile: dict, state: dict) -> str:
    block = render(profile, state)
    if block is None:
        # Disabling propagation is not permission to erase an installed block.
        return existing
    if existing.count(BEGIN) != existing.count(END) or existing.count(BEGIN) > 1:
        raise BootstrapError("MANAGED_BLOCK_CORRUPT")
    if existing.count("<!-- SCIV_BOOTSTRAP_BEGIN") != existing.count(BEGIN):
        raise BootstrapError("MANAGED_BLOCK_VERSION_REVIEW_REQUIRED")
    if BEGIN in existing:
        start, end = existing.index(BEGIN), existing.index(END) + len(END)
        if end < start:
            raise BootstrapError("MANAGED_BLOCK_CORRUPT")
        if existing[end:end + 2] != "\n\n":
            raise BootstrapError("MANAGED_BLOCK_BOUNDARY_CORRUPT")
        return existing[:start] + block + existing[end + 2:]
    if existing.count(ANCHOR) != 1:
        raise BootstrapError("BOOTSTRAP_ANCHOR_REVIEW_REQUIRED")
    at = existing.index(ANCHOR)
    return existing[:at] + block + existing[at:]
