"""Metadata enrichment for finding models (synonyms, tags, anatomic locations)."""

from __future__ import annotations

import logging
from typing import Any

from findingmodels.conventions import lowercase_name

logger = logging.getLogger(__name__)

DEFAULT_CHEST_TAGS = ("chest", "CT", "finding")


def merge_string_lists(
    existing: list[str] | None,
    *additional: list[str] | None,
    exclude: str | None = None,
) -> list[str] | None:
    """Merge string lists, dedupe case-insensitively, preserve first-seen casing."""
    seen: set[str] = set()
    merged: list[str] = []
    exclude_lower = exclude.lower().strip() if exclude else None

    for source in (existing, *additional):
        if not source:
            continue
        for item in source:
            if not item or not str(item).strip():
                continue
            text = str(item).strip()
            key = text.lower()
            if exclude_lower and key == exclude_lower:
                continue
            if key in seen:
                continue
            seen.add(key)
            merged.append(text)

    return merged or None


async def _fetch_finding_info(raw_name: str):
    """Load FindingInfo from findingmodel_ai (patchable in tests)."""
    import findingmodels.compat  # noqa: F401 - patch findingmodel.index for findingmodel-ai
    from findingmodel_ai.authoring import create_info_from_name

    return await create_info_from_name(raw_name)


def _create_stub_from_info(info):
    """Create a model stub from FindingInfo (patchable in tests)."""
    from findingmodel import create_model_stub_from_info

    return create_model_stub_from_info(info)


async def _search_anatomic_locations(finding_name: str, description: str | None):
    """Search anatomic locations via findingmodel_ai (patchable in tests)."""
    import findingmodels.compat  # noqa: F401 - patch findingmodel.index for findingmodel-ai
    from findingmodel_ai.search import find_anatomic_locations

    return await find_anatomic_locations(finding_name, description, model_tier="full")


async def enrich_metadata_from_info(
    model_dict: dict[str, Any],
    raw_name: str,
) -> dict[str, Any]:
    """Enrich JSON-derived models with name, description, synonyms, and tags from FindingInfo."""
    result = dict(model_dict)
    info = await _fetch_finding_info(raw_name)
    stub = _create_stub_from_info(info)

    canonical_name = lowercase_name(info.name or result.get("name") or raw_name)
    result["name"] = canonical_name

    hood_description = (result.get("description") or "").strip()
    if len(hood_description) < 5 and info.description:
        result["description"] = info.description.strip()
    elif hood_description:
        result["description"] = hood_description

    stub_tags = list(stub.tags) if stub.tags else None
    default_tags = list(DEFAULT_CHEST_TAGS) if not result.get("tags") and not stub_tags else None
    result["synonyms"] = merge_string_lists(
        result.get("synonyms"),
        info.synonyms,
        exclude=canonical_name,
    )
    result["tags"] = merge_string_lists(result.get("tags"), stub_tags, default_tags)

    logger.debug(
        "Metadata enrichment for '%s': %d synonyms, %d tags",
        canonical_name,
        len(result.get("synonyms") or []),
        len(result.get("tags") or []),
    )
    return result


async def enrich_anatomic_locations(model_dict: dict[str, Any]) -> dict[str, Any]:
    """Populate anatomic_locations from ontology search when not already set."""
    if model_dict.get("anatomic_locations") is not None:
        return model_dict

    finding_name = model_dict.get("name") or ""
    description = model_dict.get("description")
    if not finding_name:
        return model_dict

    result = await _search_anatomic_locations(finding_name, description)
    locations = []
    for loc in [result.primary_location] + result.alternate_locations:
        if loc.concept_id != "NO_RESULTS":
            locations.append(loc.as_index_code().model_dump())

    model_dict = dict(model_dict)
    model_dict["anatomic_locations"] = locations or None
    logger.debug(
        "Anatomic locations for '%s': %d result(s)",
        finding_name,
        len(locations),
    )
    return model_dict
