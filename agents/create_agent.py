"""
Create agent for producing FindingModelBase from raw Markdown or Hood JSON.
"""

from pathlib import Path
from typing import Any, Dict

from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel, OpenAIChatModelSettings

MODEL = OpenAIChatModel("gpt-5.4")

PROMPTS_DIR = Path(__file__).resolve().parent.parent / "prompts"


class CreateResult(BaseModel):
    """Structured output from the create agent."""

    model: Dict[str, Any]
    sub_findings: list[str]
    naming_decisions: list[str]


create_agent = Agent(
    model=MODEL,
    output_type=CreateResult,
    instructions=(PROMPTS_DIR / "create_agent.md").read_text(encoding="utf-8"),
    model_settings=OpenAIChatModelSettings(openai_reasoning_effort="low"),
    retries=3,
)
