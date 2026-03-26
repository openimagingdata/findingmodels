"""
Create agent for producing FindingModelBase from raw Markdown or JSON.
"""

from typing import Any, Dict

from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIResponsesModel, OpenAIResponsesModelSettings

from agents.prompts import load_instructions

MODEL = OpenAIResponsesModel("gpt-5.4")


class CreateResult(BaseModel):
    """Structured output from the create agent."""

    model: Dict[str, Any]
    findings_to_create: list[str]
    naming_decisions: list[str]


create_agent = Agent(
    model=MODEL,
    output_type=CreateResult,
    instructions=load_instructions("create_agent"),
    model_settings=OpenAIResponsesModelSettings(openai_reasoning_effort="low"),
    retries=3,
)
