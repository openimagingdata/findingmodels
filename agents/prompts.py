"""Prompt loading utilities for agents."""

import re
from pathlib import Path

PROMPTS_DIR = Path(__file__).resolve().parent.parent / "prompts"

_FRONTMATTER_RE = re.compile(r"\A---\s*\n.*?\n---\s*\n", re.DOTALL)
_OUTPUT_SECTION_RE = re.compile(r"\n## Output\s*\n.*?(?=\n## |\Z)", re.DOTALL)

MGB_CONTRIBUTORS = '{"name": "Massachusetts General Brigham", "code": "MGB"}'


def _strip_frontmatter(text: str) -> str:
    """Remove YAML frontmatter from markdown."""
    return _FRONTMATTER_RE.sub("", text).strip()


def _strip_output_section(text: str) -> str:
    """Remove the ## Output section (agent-specific return format)."""
    return _OUTPUT_SECTION_RE.sub("", text).strip()


def load_single_agent_instructions() -> str:
    """Load composed instructions for the single agent.

    Combines: single_agent workflow + create rules + merge rules + review rules + naming_rules.
    """
    parts = []

    # 1. Workflow (single_agent.md)
    workflow = _strip_frontmatter((PROMPTS_DIR / "single_agent.md").read_text(encoding="utf-8"))
    parts.append(workflow)

    # 2. Create rules (when parsing)
    create_raw = (PROMPTS_DIR / "create_agent.md").read_text(encoding="utf-8")
    create_body = _strip_frontmatter(_strip_output_section(create_raw))
    parts.append(f"---\n\n## When Parsing (create_from_markdown / adapt_hood_json)\n\n{create_body}")

    # 3. Merge rules (when merging)
    merge_raw = (PROMPTS_DIR / "merge_agent.md").read_text(encoding="utf-8")
    merge_body = _strip_frontmatter(_strip_output_section(merge_raw))
    merge_body = merge_body.replace("{contributors}", MGB_CONTRIBUTORS.strip())
    parts.append(f"---\n\n## When Merging with Existing Model\n\n{merge_body}")

    # 4. Review rules (quality checklist)
    review_raw = (PROMPTS_DIR / "review_agent.md").read_text(encoding="utf-8")
    review_body = _strip_frontmatter(_strip_output_section(review_raw))
    parts.append(f"---\n\n## Quality Checklist (ensure final model meets these criteria)\n\n{review_body}")

    # 5. Naming rules
    naming = (PROMPTS_DIR / "naming_rules.md").read_text(encoding="utf-8")
    parts.append(f"---\n\n{naming.strip()}")

    return "\n\n".join(parts)


def load_instructions(agent_name: str) -> str:
    """Load agent instructions with shared naming rules appended.

    Reads ``prompts/{agent_name}.md``, strips any YAML frontmatter,
    and appends ``prompts/naming_rules.md``.
    """
    raw = (PROMPTS_DIR / f"{agent_name}.md").read_text(encoding="utf-8")
    body = _FRONTMATTER_RE.sub("", raw)
    shared = (PROMPTS_DIR / "naming_rules.md").read_text(encoding="utf-8")
    return f"{body.strip()}\n\n---\n\n{shared.strip()}\n"
