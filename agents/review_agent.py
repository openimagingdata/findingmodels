"""
Review agent for quality-checking and correcting finding model definitions.
"""

from pathlib import Path
from typing import Any, Dict

from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel

MODEL = OpenAIChatModel("gpt-5.4")

PROMPTS_DIR = Path(__file__).resolve().parent.parent / "prompts"


class ReviewResult(BaseModel):
    """Structured output from the review agent."""

    reviewed_model: Dict[str, Any]
    changes_made: list[str]
    quality_warnings: list[str]
    sub_findings: list[str]


review_agent = Agent(
    model=MODEL,
    output_type=ReviewResult,
    instructions=(PROMPTS_DIR / "review_agent.md").read_text(encoding="utf-8"),
    retries=3,
)
