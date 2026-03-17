"""
Python-orchestrated pipeline for processing Hood finding definitions.
Uses 3 focused agents (merge, create, review) and library functions for search/enrichment.
"""

import findingmodels.compat  # noqa: F401 - patch for findingmodel-ai

import asyncio
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import logfire
from findingmodel import FindingModelBase, FindingModelFull, Index
from findingmodel.common import model_file_name
from findingmodel.contributor import Organization
from oidm_common.models import IndexCode
from findingmodel.tools import add_ids_to_model, add_standard_codes_to_model
from findingmodel_ai.authoring import create_info_from_name
from findingmodel_ai.search import find_anatomic_locations, find_similar_models
from pydantic import BaseModel

from agents.create_agent import create_agent
from agents.merge_agent import MergeContext, merge_agent
from agents.review_agent import review_agent
from findingmodels.hood import load_definition
from findingmodels.hood.normalize_output import normalize_for_validation, strip_sub_finding_attributes


@dataclass
class FindingInput:
    """Parsed input from a definition file."""

    name: str
    description: str
    synonyms: list[str] | None
    content: str
    file_type: str
    filename: str


class ProcessingResult(BaseModel):
    """Complete result from processing one finding."""

    final_model: dict[str, Any]
    match_used: str | None
    merge_summary: str
    sub_findings: list[str]
    changes_made: list[str]
    quality_warnings: list[str]


async def parse_input(file_path: Path) -> FindingInput:
    """Parse a definition file into FindingInput."""
    data, markdown_content, file_type = await load_definition(file_path)

    if file_type == "json":
        raw_name = data.get("finding_name") or data.get("name", "") or ""
        content = json.dumps(data, indent=2, ensure_ascii=False)
    else:
        raw_name = file_path.stem.replace("-", " ").replace("_", " ")
        content = markdown_content or ""

    if not raw_name or not raw_name.strip():
        raw_name = file_path.stem.replace("-", " ").replace("_", " ")

    info = await create_info_from_name(raw_name)

    return FindingInput(
        name=info.name,
        description=info.description or "",
        synonyms=info.synonyms,
        content=content,
        file_type=file_type,
        filename=file_path.name,
    )


def _sim_to_dict(sim: Any) -> dict[str, Any]:
    """Convert similar model result to dict for prompt."""
    if isinstance(sim, dict):
        return sim
    if hasattr(sim, "model_dump"):
        return sim.model_dump()
    return {
        "oifm_id": getattr(sim, "oifm_id", ""),
        "name": getattr(sim, "name", ""),
        "description": getattr(sim, "description", ""),
        "synonyms": getattr(sim, "synonyms", []),
    }


def format_merge_prompt(finding: FindingInput, similar_models: list[Any]) -> str:
    """Format user message for merge agent."""
    similar_summaries = []
    for sim in similar_models:
        d = _sim_to_dict(sim)
        similar_summaries.append(
            f"- {d.get('oifm_id', '')}: {d.get('name', '')} — {str(d.get('description', ''))[:150]}..."
        )
    similar_block = "\n".join(similar_summaries) if similar_summaries else "(none)"

    return f"""## Finding to merge

**Name:** {finding.name}
**Description:** {finding.description}
**Synonyms:** {finding.synonyms or []}

## Similar existing models (pick one to merge into, or reject all)

{similar_block}

## Incoming content ({finding.file_type})

{finding.content}

Merge the incoming content into the best-matching existing model. Use get_full_model to retrieve the full model first. If you reject all candidates, set target_oifm_id to empty string and return the incoming content as a new model."""


def format_create_prompt(finding: FindingInput) -> str:
    """Format user message for create agent."""
    return f"""## Finding to create

**Name:** {finding.name}
**Description:** {finding.description}
**Synonyms:** {finding.synonyms or []}

## Raw content ({finding.file_type})

{finding.content}

Produce a complete FindingModelBase dict. Ensure presence and change_from_prior are the first two attributes with standard values."""


def format_review_prompt(model_dict: dict[str, Any], locations: list[dict] | None) -> str:
    """Format user message for review agent."""
    locations_block = (
        json.dumps(locations, indent=2) if locations else "None (will be set in post-processing)"
    )
    return f"""## Model to review

{json.dumps(model_dict, indent=2, ensure_ascii=False)}

## Anatomic locations (for reference)

{locations_block}

Review and fix quality issues per the checklist. Return the corrected model in reviewed_model."""


def finalize_model(
    model_dict: dict[str, Any],
    locations: list[dict] | None,
    source: str = "MGB",
) -> FindingModelFull:
    """Add IDs, standard codes, locations, normalize, validate."""
    model_dict = dict(model_dict)
    model_dict = normalize_for_validation(model_dict)

    if "oifm_id" not in model_dict or not model_dict.get("oifm_id"):
        base = FindingModelBase.model_validate(model_dict)
        full = add_ids_to_model(base, source=source)
    else:
        full = FindingModelFull.model_validate(model_dict)

    # FindingModelBase strips anatomic_locations/contributors; add them after we have FindingModelFull
    mgb_org = Organization(name="Massachusetts General Brigham", code="MGB")
    updates: dict[str, Any] = {}
    if full.anatomic_locations is None:
        updates["anatomic_locations"] = (
            [IndexCode.model_validate(loc) for loc in locations] if locations else None
        )
    if not full.contributors:
        updates["contributors"] = [mgb_org]
    if updates:
        full = full.model_copy(update=updates)

    add_standard_codes_to_model(full)
    return full


async def process_finding(
    file_path: Path,
    index: Index,
    output_dir: Path,
) -> ProcessingResult:
    """Process a single finding definition through the pipeline."""
    with logfire.span("process_finding", file=file_path.name):
        with logfire.span("parse_input"):
            finding = await parse_input(file_path)

        with logfire.span("search_parallel"):
            similar, location_result = await asyncio.gather(
                find_similar_models(
                    finding.name,
                    finding.description,
                    finding.synonyms,
                    index=index,
                ),
                find_anatomic_locations(finding.name, finding.description),
            )

        locations = []
        for loc in [location_result.primary_location] + location_result.alternate_locations:
            if loc.concept_id != "NO_RESULTS":
                locations.append(loc.as_index_code().model_dump())
        locations = locations or None

        with logfire.span("agent_run", branch=similar.recommendation):
            if similar.recommendation == "edit_existing" and similar.confidence >= 0.7:
                result = await merge_agent.run(
                    format_merge_prompt(finding, similar.similar_models),
                    deps=MergeContext(index=index),
                )
                model_dict = result.output.merged_model
                match_used = result.output.target_oifm_id or None
                sub_findings = list(result.output.sub_findings)
                changes = list(result.output.changes_made)
            else:
                result = await create_agent.run(format_create_prompt(finding))
                model_dict = result.output.model
                match_used = None
                sub_findings = list(result.output.sub_findings)
                changes = list(result.output.naming_decisions)

        with logfire.span("review"):
            review = await review_agent.run(format_review_prompt(model_dict, locations))
            model_dict = review.output.reviewed_model
            sub_findings.extend(review.output.sub_findings)
            changes.extend(review.output.changes_made)

        if sub_findings:
            model_dict = strip_sub_finding_attributes(model_dict, sub_findings)

        with logfire.span("finalize"):
            final = finalize_model(model_dict, locations, source="MGB")

        output_file = output_dir / model_file_name(final.name)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(
            final.model_dump_json(indent=2, exclude_none=True),
            encoding="utf-8",
        )

        return ProcessingResult(
            final_model=final.model_dump(exclude_none=True),
            match_used=match_used or None,
            merge_summary="; ".join(changes),
            sub_findings=sub_findings,
            changes_made=changes,
            quality_warnings=review.output.quality_warnings,
        )
