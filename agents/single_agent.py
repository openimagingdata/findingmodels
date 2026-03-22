"""
Single Agent (Option B: Single agent with tools).

Processes incoming Markdown or JSON finding definitions, searches for similar models,
merges when appropriate, and produces final FindingModelFull output.
Uses GPT-5.4 with pydantic-ai tools.
"""

import json
import logging
from dataclasses import dataclass
from typing import Any, Dict

import logfire
import findingmodels.compat  # noqa: F401 - patch findingmodel.index for findingmodel-ai
from dotenv import load_dotenv
from findingmodel import FindingModelFull, FindingModelBase, Index
from findingmodel.tools import add_ids_to_model, add_standard_codes_to_model
from findingmodel_ai.authoring import create_info_from_name, create_model_from_markdown
from findingmodel_ai.search import find_anatomic_locations
from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIChatModel

from findingmodels.hood.hood_json_adapter import HoodJsonAdapter

from agents.prompts import load_single_agent_instructions

load_dotenv()

logfire.configure(send_to_logfire='if-token-present')
logfire.instrument_pydantic_ai()

logger = logging.getLogger(__name__)

# GPT-5.4 model (aligned with merge/create/review agents)
MODEL = OpenAIChatModel("gpt-5.4")


@dataclass
class AgentContext:
    """Dependencies passed to the agent at runtime."""

    index: Index
    source_code: str = "MGB"


class ProcessingResult(BaseModel):
    """Structured output from the single agent."""

    final_model: Dict[str, Any] = Field(
        description="The final FindingModelFull as a JSON-serializable dict, ready to save"
    )
    match_used: str | None = Field(
        default=None,
        description="OIFM ID of the existing model merged with, or None if new model created",
    )
    merge_summary: str = Field(
        default="",
        description="Brief summary of merge decisions if a match was used",
    )
    findings_to_create: list[str] = Field(
        default_factory=list,
        description="Names of findings that need their own models — associated findings, components, or compound finding splits",
    )


# --- Agent (created first so tools can be registered via decorator) ---

single_agent = Agent(
    model=MODEL,
    deps_type=AgentContext,
    output_type=ProcessingResult,
    system_prompt=load_single_agent_instructions(),
)


# --- Tools ---


@single_agent.tool
async def search_finding_models(
    ctx: RunContext[AgentContext], query: str, limit: int = 10
) -> str:
    """
    Search for existing finding models in the index.

    Args:
        query: Search terms (finding names, anatomical terms, etc.)
        limit: Maximum number of results (default 10)

    Returns:
        JSON string of search results with oifm_id, name, description, synonyms
    """
    try:
        results = await ctx.deps.index.search(query, limit=limit)
        if not results:
            return json.dumps({"query": query, "count": 0, "results": []})
        formatted = [
            {
                "oifm_id": r.oifm_id,
                "name": r.name,
                "description": getattr(r, "description", None) or None,
                "synonyms": getattr(r, "synonyms", None) or None,
            }
            for r in results
        ]
        return json.dumps({"query": query, "count": len(results), "results": formatted})
    except Exception as e:
        return json.dumps({"error": str(e)})


@single_agent.tool
async def get_full_model(ctx: RunContext[AgentContext], oifm_id: str) -> str:
    """
    Retrieve a full finding model by OIFM ID.

    Args:
        oifm_id: The OIFM ID (e.g. OIFM_RADLEX_000001)

    Returns:
        JSON string of the full FindingModelFull
    """
    try:
        model = await ctx.deps.index.get_full(oifm_id)
        return model.model_dump_json(indent=2, exclude_none=False)
    except Exception as e:
        return json.dumps({"error": str(e)})


@single_agent.tool
async def create_from_markdown(
    ctx: RunContext[AgentContext],
    finding_name: str,
    markdown_content: str,
) -> str:
    """
    Create a finding model from Markdown content.

    Args:
        finding_name: Name of the finding (from filename or content)
        markdown_content: The markdown definition content

    Returns:
        JSON string of the generated FindingModelBase (without IDs yet)
    """
    try:
        info = await create_info_from_name(finding_name)
        model = await create_model_from_markdown(
            info,
            markdown_text=markdown_content,
        )
        return model.model_dump_json(indent=2, exclude_none=False)
    except Exception as e:
        return json.dumps({"error": str(e)})


@single_agent.tool
async def adapt_hood_json(
    ctx: RunContext[AgentContext],
    json_content: str,
    filename: str,
) -> str:
    """
    Convert Hood JSON definition to FindingModelFull.

    Args:
        json_content: Raw JSON string of the Hood definition
        filename: Original filename (e.g. pulmonary_nodule.json)

    Returns:
        JSON string of the adapted FindingModelFull
    """
    try:
        hood_data = json.loads(json_content)
        model = await HoodJsonAdapter.adapt_hood_json(hood_data, filename)
        return model.model_dump_json(indent=2, exclude_none=False)
    except Exception as e:
        return json.dumps({"error": str(e)})


@single_agent.tool
async def add_ids_to_finding_model(
    ctx: RunContext[AgentContext],
    model_json: str,
    source: str | None = None,
) -> str:
    """
    Add OIFM and OIFMA IDs to a finding model.

    Args:
        model_json: JSON string of the finding model (FindingModelBase or FindingModelFull)
        source: 3-4 letter source code (defaults to deps.source_code, e.g. MGB)

    Returns:
        JSON string of the model with IDs added
    """
    try:
        data = json.loads(model_json)
        base = FindingModelBase(**data)
        src = source or ctx.deps.source_code
        full = add_ids_to_model(base, source=src)
        return full.model_dump_json(indent=2, exclude_none=False)
    except Exception as e:
        return json.dumps({"error": str(e)})


@single_agent.tool
async def add_standard_codes(ctx: RunContext[AgentContext], model_json: str) -> str:
    """
    Add standard RadLex/SNOMED index codes to a finding model.

    Args:
        model_json: JSON string of the FindingModelFull

    Returns:
        JSON string of the model with standard codes added
    """
    try:
        model = FindingModelFull.model_validate_json(model_json)
        add_standard_codes_to_model(model)
        return model.model_dump_json(indent=2, exclude_none=False)
    except Exception as e:
        return json.dumps({"error": str(e)})


@single_agent.tool
async def find_anatomic_locations_tool(
    ctx: RunContext[AgentContext],
    finding_name: str,
    description: str | None = None,
) -> str:
    """
    Find anatomic locations for a finding using ontology search.
    Returns JSON with anatomic_locations in IndexCode format (system, code, display).
    Call this to populate anatomic_locations before returning the final model.
    """
    try:
        result = await find_anatomic_locations(
            finding_name=finding_name,
            description=description,
        )
        locations = []
        for loc in [result.primary_location] + result.alternate_locations:
            if loc.concept_id != "NO_RESULTS":
                index_code = loc.as_index_code().model_dump()
                locations.append(index_code)
        return json.dumps(
            {"anatomic_locations": locations if locations else None, "reasoning": result.reasoning}
        )
    except Exception as e:
        return json.dumps({"anatomic_locations": None, "reasoning": str(e), "error": str(e)})


def create_single_agent() -> Agent[AgentContext, ProcessingResult]:
    """Return the single definition processor agent (tools registered via decorators)."""
    return single_agent
