"""Prompt loading utilities for agents."""

import re
from pathlib import Path

PROMPTS_DIR = Path(__file__).resolve().parent.parent / "prompts"

_FRONTMATTER_RE = re.compile(r"\A---\s*\n.*?\n---\s*\n", re.DOTALL)


def load_instructions(agent_name: str) -> str:
    """Load agent instructions with shared naming rules appended.

    Reads ``prompts/{agent_name}.md``, strips any YAML frontmatter,
    and appends ``prompts/naming_rules.md``.
    """
    raw = (PROMPTS_DIR / f"{agent_name}.md").read_text(encoding="utf-8")
    body = _FRONTMATTER_RE.sub("", raw)
    shared = (PROMPTS_DIR / "naming_rules.md").read_text(encoding="utf-8")
    return f"{body.strip()}\n\n---\n\n{shared.strip()}\n"
