"""Post-processing for CDEStaging CT chest converted finding models."""

from __future__ import annotations

import logging
from typing import Any

from findingmodel import FindingModelBase, FindingModelFull
from findingmodel.tools import add_ids_to_model

from findingmodels.contributors import default_hood_contributors_as_dicts
from findingmodels.conventions import (
    ensure_standard_attributes,
    lowercase_model_dict,
    reorder_attributes,
)
from findingmodels.metadata_enrichment import (
    DEFAULT_CHEST_TAGS,
    enrich_anatomic_locations,
    enrich_metadata_from_info,
)

logger = logging.getLogger(__name__)


def _attribute_id_map(attributes: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """Map attribute name -> {oifma_id, values: {value_name_lower: value_code}}."""
    result: dict[str, dict[str, Any]] = {}
    for attr in attributes:
        name = (attr.get("name") or "").lower()
        if not name:
            continue
        value_codes: dict[str, str] = {}
        for value in attr.get("values") or []:
            if not isinstance(value, dict):
                continue
            val_name = (value.get("name") or "").lower()
            val_code = value.get("value_code")
            if val_name and val_code:
                value_codes[val_name] = val_code
        result[name] = {
            "oifma_id": attr.get("oifma_id"),
            "values": value_codes,
        }
    return result


def _restore_attribute_ids(
    attributes: list[dict[str, Any]],
    id_map: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    """Restore oifma_id and value_code from a prior model when names match."""
    restored: list[dict[str, Any]] = []
    for attr in attributes:
        item = dict(attr)
        name = (item.get("name") or "").lower()
        prior = id_map.get(name)
        if prior and prior.get("oifma_id"):
            item["oifma_id"] = prior["oifma_id"]
        if item.get("type") == "choice" and prior:
            values = []
            for value in item.get("values") or []:
                val = dict(value) if isinstance(value, dict) else dict(value)
                val_name = (val.get("name") or "").lower()
                code = prior.get("values", {}).get(val_name)
                if code:
                    val["value_code"] = code
                values.append(val)
            item["values"] = values
        restored.append(item)
    return restored


def _apply_conventions(model: FindingModelFull, *, source: str = "MGB") -> FindingModelFull:
    """Apply casing, standard attributes, ordering, and contributors."""
    original = model.model_dump(exclude_none=False)
    original_oifm_id = original.get("oifm_id")
    id_map = _attribute_id_map(original.get("attributes") or [])

    data = lowercase_model_dict(original)
    finding_name = data.get("name") or "finding"
    attributes = ensure_standard_attributes(data.get("attributes") or [], finding_name)
    attributes = reorder_attributes(attributes)
    attributes = _restore_attribute_ids(attributes, id_map)
    data["attributes"] = attributes
    data["contributors"] = default_hood_contributors_as_dicts()

    base_fields = {
        key: data[key]
        for key in FindingModelBase.model_fields
        if key in data
    }
    base = FindingModelBase.model_validate(base_fields)
    with_ids = add_ids_to_model(base, source=source)

    full_dict = with_ids.model_dump(exclude_none=False)
    if original_oifm_id:
        full_dict["oifm_id"] = original_oifm_id
    full_dict["contributors"] = data["contributors"]

    for optional_key in ("synonyms", "tags", "anatomic_locations", "index_codes"):
        if optional_key in data and data[optional_key] is not None:
            full_dict[optional_key] = data[optional_key]

    return FindingModelFull.model_validate(full_dict)


async def enrich_model(
    model: FindingModelFull,
    *,
    source_type: str,
    raw_name: str,
    source: str = "MGB",
    enrich_metadata: bool = False,
    enrich_locations: bool = False,
) -> FindingModelFull:
    """Apply metadata enrichment then project conventions."""
    data = model.model_dump(exclude_none=False)

    if enrich_metadata and source_type == "json":
        data = await enrich_metadata_from_info(data, raw_name)
    elif not data.get("tags"):
        data = dict(data)
        data["tags"] = list(DEFAULT_CHEST_TAGS)

    if enrich_locations:
        data = await enrich_anatomic_locations(data)

    interim = FindingModelFull.model_validate(data)
    result = _apply_conventions(interim, source=source)

    logger.debug(
        "Enriched model '%s' (%d attributes)",
        result.name,
        len(result.attributes or []),
    )
    return result
