"""
Merge agent for combining incoming finding definitions with existing database models.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict

from findingmodel import Index
from pydantic import BaseModel
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIChatModel, OpenAIChatModelSettings
from pydantic_ai.exceptions import ModelRetry

MODEL = OpenAIChatModel("gpt-5.2")

PROMPTS_DIR = Path(__file__).resolve().parent.parent / "prompts"


class MergeResult(BaseModel):
    """Structured output from the merge agent."""

    merged_model: Dict[str, Any]
    target_oifm_id: str
    changes_made: list[str]
    sub_findings: list[str]


@dataclass
class MergeContext:
    """Dependencies for the merge agent."""

    index: Index


merge_agent = Agent(
    model=MODEL,
    deps_type=MergeContext,
    output_type=MergeResult,
    instructions=(PROMPTS_DIR / "merge_agent.md").read_text(encoding="utf-8"),
    model_settings=OpenAIChatModelSettings(openai_reasoning_effort="high"),
    retries=3,
)


@merge_agent.tool
async def get_full_model(ctx: RunContext[MergeContext], oifm_id: str) -> dict[str, Any]:
    """Retrieve a full finding model by OIFM ID to inspect before merging."""
    try:
        model = await ctx.deps.index.get_full(oifm_id)
        return model.model_dump(exclude_none=False)
    except Exception as e:
        raise ModelRetry(f"Failed to retrieve model {oifm_id}: {e}")
