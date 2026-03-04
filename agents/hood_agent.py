"""
Hood Definition Processor Agent (Option B: Single agent with tools).

Processes incoming Markdown or JSON finding definitions, searches for similar models,
merges when appropriate, and produces final FindingModelFull output.
Uses GPT-5.2 with pydantic-ai tools.
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

load_dotenv()

logfire.configure(send_to_logfire='if-token-present')
logfire.instrument_pydantic_ai()

logger = logging.getLogger(__name__)

# GPT-5.2 model
MODEL = OpenAIChatModel("gpt-5.2")


@dataclass
class AgentContext:
    """Dependencies passed to the agent at runtime."""

    index: Index
    source_code: str = "MGB"


class ProcessingResult(BaseModel):
    """Structured output from the Hood agent."""

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


# --- Tools ---


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


# --- System prompt (Part 4 + Part 7 rules) ---

SYSTEM_PROMPT = """You are a medical imaging expert processing finding model definitions for radiology reports.

Your task: Given an incoming definition (Markdown or Hood JSON), produce a final FindingModelFull ready to save.

## Workflow

1. **Parse the input** using the appropriate approach:
   - If content is already a complete FindingModelFull JSON (has oifm_id or name, attributes, etc.): use it directly as the incoming model. Do NOT call create_from_markdown or adapt_hood_json.
   - For Markdown: use create_from_markdown(finding_name, markdown_content)
   - For Hood JSON (has finding_name, attributes in Hood format): use adapt_hood_json(json_content, filename)

2. **Search for similar models** using search_finding_models(query, limit). Use the finding name and key terms.

3. **Decide match vs create new:**
   - If a search result is an exact or near-exact match AND not too general: use get_full_model(oifm_id), then merge incoming with existing per the merge strategy below.
   - If the existing term is too general (e.g. "detectable hardware" when incoming is "tunneled catheter"): reject the match, create new.
   - If no suitable match: use the model from step 1 as the base.

4. **Ensure presence and change_from_prior** exist and are first in the attribute list. Standard presence values: [absent, present, indeterminate, unknown]. Standard change values: [unchanged, stable, increased, decreased, new, resolved, no prior]. If incoming has [yes, no] and existing has standard values, keep existing.

5. **Apply add_ids_to_finding_model** and **add_standard_codes** to the final model.

6. **Call find_anatomic_locations**(finding_name, description) to get anatomic locations in IndexCode format. Set anatomic_locations from the result. If the result is empty or NO_RESULTS, set anatomic_locations to null. Never use {"name": "..."} for anatomic_locations; use {"system", "code", "display"} from the tool.

7. **Apply naming rules:** lowercase for names, attribute names, and values; expand acronyms (add compact forms as synonyms); minimize eponyms (prefer descriptive terms, keep eponym as synonym).

8. **Return ProcessingResult** with final_model (the complete dict), match_used (oifm_id or null), and merge_summary.

## Merge Strategy (Part 7)

- Hood = incoming. Existing DB = reference.
- Attribute order: presence and change_from_prior must be first.
- Hood contributor (MGB) must be in contributors. For MGB organization, use exactly: {"name": "Massachusetts General Brigham", "code": "MGB"}. Never use "mgb" as name.
- Attribute relationships:
  - **enhanced** (incoming has all existing + more): merge, add new values
  - **identical**: no merge
  - **subset** (existing has all incoming + more): no merge
  - **needs_review**: auto-merge for now
  - **no_similarities**: add as new attribute, unless both are presence/change_from_prior

## Naming & Formatting (Part 4)

- Lowercase: model name, attribute names, values. Descriptions may use normal casing.
- Eponyms: minimize; prefer descriptive terms; keep eponym as synonym.
- Acronyms: spell out in names; add compact forms as synonyms.
- Location: use anatomic nodes in model-level locations; do NOT add separate Location attribute.
- Associated findings: do NOT add; use separate findings instead.
"""


# --- Agent ---

def create_hood_agent() -> Agent[AgentContext, ProcessingResult]:
    """Create the Hood definition processor agent with tools."""
    return Agent(
        model=MODEL,
        deps_type=AgentContext,
        output_type=ProcessingResult,
        tools=[
            search_finding_models,
            get_full_model,
            create_from_markdown,
            adapt_hood_json,
            add_ids_to_finding_model,
            add_standard_codes,
            find_anatomic_locations_tool,
        ],
        system_prompt=SYSTEM_PROMPT,
    )
