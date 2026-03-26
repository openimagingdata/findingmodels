"""
Review agent for quality-checking and correcting finding model definitions.
"""

from typing import Any, Dict

from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIResponsesModel

from agents.prompts import load_instructions

MODEL = OpenAIResponsesModel("gpt-5.4")


class ReviewResult(BaseModel):
    """Structured output from the review agent."""

    reviewed_model: Dict[str, Any]
    changes_made: list[str]
    quality_warnings: list[str]
    findings_to_create: list[str]


review_agent = Agent(
    model=MODEL,
    output_type=ReviewResult,
    instructions=load_instructions("review_agent"),
    retries=3,
)
