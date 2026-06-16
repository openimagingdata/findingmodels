"""Standard finding model conventions (presence, change from prior, naming, ordering)."""

from __future__ import annotations

import re
from typing import Any

PRESENCE_ATTRIBUTE_NAME = "presence"
CHANGE_ATTRIBUTE_NAME = "change from prior"

PRESENCE_VALUE_NAMES = ("absent", "present", "indeterminate", "unknown")

CHANGE_VALUE_NAMES = (
    "unchanged",
    "stable",
    "new",
    "resolved",
    "increased",
    "decreased",
    "larger",
    "smaller",
)


def _sentence_subject(finding_name: str) -> str:
    """Use finding name as description subject (lowercase, no leading article)."""
    return finding_name.strip().lower()


def _presence_description(value_name: str, finding_name: str) -> str:
    subject = _sentence_subject(finding_name)
    descriptions = {
        "absent": f"{subject.capitalize()} is absent",
        "present": f"{subject.capitalize()} is present",
        "indeterminate": f"Presence of {subject} cannot be determined",
        "unknown": f"Presence of {subject} is unknown",
    }
    return descriptions[value_name]


def _change_description(value_name: str, finding_name: str) -> str:
    subject = _sentence_subject(finding_name)
    descriptions = {
        "unchanged": f"{subject.capitalize()} is unchanged",
        "stable": f"{subject.capitalize()} is stable",
        "new": f"{subject.capitalize()} is new",
        "resolved": f"{subject.capitalize()} seen on a prior exam has resolved",
        "increased": f"{subject.capitalize()} has increased",
        "decreased": f"{subject.capitalize()} has decreased",
        "larger": f"{subject.capitalize()} is larger",
        "smaller": f"{subject.capitalize()} is smaller",
    }
    return descriptions[value_name]


def _is_presence_attribute(attr: dict[str, Any]) -> bool:
    name = (attr.get("name") or "").strip().lower()
    if name == PRESENCE_ATTRIBUTE_NAME:
        return True
    return name.endswith(" presence") or name == "finding presence"


def _is_change_attribute(attr: dict[str, Any]) -> bool:
    name = (attr.get("name") or "").strip().lower()
    return name == CHANGE_ATTRIBUTE_NAME or name.replace("_", " ") == CHANGE_ATTRIBUTE_NAME


def create_presence_attribute(finding_name: str) -> dict[str, Any]:
    """Build a standard presence choice attribute."""
    subject = _sentence_subject(finding_name)
    return {
        "name": PRESENCE_ATTRIBUTE_NAME,
        "description": f"Presence or absence of {subject}",
        "type": "choice",
        "required": False,
        "max_selected": 1,
        "values": [
            {
                "name": value_name,
                "description": _presence_description(value_name, finding_name),
            }
            for value_name in PRESENCE_VALUE_NAMES
        ],
    }


def create_change_from_prior_attribute(finding_name: str) -> dict[str, Any]:
    """Build a standard change-from-prior choice attribute."""
    subject = _sentence_subject(finding_name)
    return {
        "name": CHANGE_ATTRIBUTE_NAME,
        "description": f"Whether and how a {subject} has changed over time",
        "type": "choice",
        "required": False,
        "max_selected": 1,
        "values": [
            {
                "name": value_name,
                "description": _change_description(value_name, finding_name),
            }
            for value_name in CHANGE_VALUE_NAMES
        ],
    }


def _choice_value_names(attr: dict[str, Any]) -> set[str]:
    names: set[str] = set()
    for value in attr.get("values") or []:
        if isinstance(value, dict):
            name = value.get("name", "")
        else:
            name = getattr(value, "name", "")
        if name:
            names.add(str(name).lower())
    return names


def _merge_choice_values(
    attr: dict[str, Any],
    required_names: tuple[str, ...],
    finding_name: str,
    description_fn,
    *,
    preserve_extras: bool = True,
) -> dict[str, Any]:
    """Ensure a choice attribute includes required value names."""
    existing_values = list(attr.get("values") or [])
    existing_by_name = {}
    for value in existing_values:
        if isinstance(value, dict):
            val_name = (value.get("name") or "").lower()
            existing_by_name[val_name] = value
        else:
            val_name = (getattr(value, "name", "") or "").lower()
            existing_by_name[val_name] = value

    yes_no_map = {"yes": "present", "no": "absent"}
    for alias, canonical in yes_no_map.items():
        if alias in existing_by_name and canonical not in existing_by_name:
            existing_by_name[canonical] = existing_by_name[alias]

    merged_values = []
    seen: set[str] = set()
    for required in required_names:
        if required in existing_by_name:
            value = dict(existing_by_name[required])
            value["name"] = required
            merged_values.append(value)
            seen.add(required)
        else:
            merged_values.append(
                {"name": required, "description": description_fn(required, finding_name)}
            )
            seen.add(required)

    if preserve_extras:
        for val_name, value in existing_by_name.items():
            if val_name in seen or val_name in yes_no_map:
                continue
            merged_values.append(value if isinstance(value, dict) else dict(value))

    attr = dict(attr)
    attr["name"] = PRESENCE_ATTRIBUTE_NAME if description_fn is _presence_description else CHANGE_ATTRIBUTE_NAME
    attr["values"] = merged_values
    return attr


def ensure_presence_attribute(
    attributes: list[dict[str, Any]],
    finding_name: str,
) -> tuple[list[dict[str, Any]], dict[str, Any] | None]:
    """Ensure a standard presence attribute exists; return updated list and the presence attr."""
    presence_attr: dict[str, Any] | None = None
    others: list[dict[str, Any]] = []

    for attr in attributes:
        if _is_presence_attribute(attr):
            if presence_attr is None:
                normalized = dict(attr)
                normalized["name"] = PRESENCE_ATTRIBUTE_NAME
                presence_attr = _merge_choice_values(
                    normalized,
                    PRESENCE_VALUE_NAMES,
                    finding_name,
                    _presence_description,
                )
            continue
        others.append(attr)

    if presence_attr is None:
        presence_attr = create_presence_attribute(finding_name)

    return others, presence_attr


def ensure_change_from_prior_attribute(
    attributes: list[dict[str, Any]],
    finding_name: str,
) -> tuple[list[dict[str, Any]], dict[str, Any] | None]:
    """Ensure a standard change-from-prior attribute exists."""
    change_attr: dict[str, Any] | None = None
    others: list[dict[str, Any]] = []

    for attr in attributes:
        if _is_change_attribute(attr):
            if change_attr is None:
                normalized = dict(attr)
                normalized["name"] = CHANGE_ATTRIBUTE_NAME
                change_attr = _merge_choice_values(
                    normalized,
                    CHANGE_VALUE_NAMES,
                    finding_name,
                    _change_description,
                    preserve_extras=False,
                )
            continue
        others.append(attr)

    if change_attr is None:
        change_attr = create_change_from_prior_attribute(finding_name)

    return others, change_attr


def ensure_standard_attributes(
    attributes: list[dict[str, Any]],
    finding_name: str,
) -> list[dict[str, Any]]:
    """Insert or upgrade presence and change-from-prior; order handled separately."""
    attrs = list(attributes)
    attrs, presence = ensure_presence_attribute(attrs, finding_name)
    attrs, change = ensure_change_from_prior_attribute(attrs, finding_name)
    return [presence, change] + attrs


def reorder_attributes(attributes: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Place presence first and change from prior second."""
    presence: dict[str, Any] | None = None
    change: dict[str, Any] | None = None
    others: list[dict[str, Any]] = []

    for attr in attributes:
        if _is_presence_attribute(attr) and presence is None:
            item = dict(attr)
            item["name"] = PRESENCE_ATTRIBUTE_NAME
            presence = item
        elif _is_change_attribute(attr) and change is None:
            item = dict(attr)
            item["name"] = CHANGE_ATTRIBUTE_NAME
            change = item
        else:
            others.append(attr)

    ordered: list[dict[str, Any]] = []
    if presence is not None:
        ordered.append(presence)
    if change is not None:
        ordered.append(change)
    ordered.extend(others)
    return ordered


def lowercase_name(value: str) -> str:
    """Lowercase a model/attribute/value name; preserve internal spacing."""
    cleaned = value.replace("_", " ").strip()
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned.lower()


def lowercase_model_dict(model: dict[str, Any]) -> dict[str, Any]:
    """Lowercase finding name, attribute names, and choice value names."""
    result = dict(model)
    if result.get("name"):
        result["name"] = lowercase_name(str(result["name"]))

    normalized_attrs = []
    for attr in result.get("attributes") or []:
        attr = dict(attr)
        if attr.get("name"):
            name = str(attr["name"])
            if name.lower().endswith(" finding"):
                name = name[: -len(" finding")].strip()
            attr["name"] = lowercase_name(name)

        if attr.get("type") == "choice":
            values = []
            for value in attr.get("values") or []:
                value = dict(value) if isinstance(value, dict) else dict(value)
                if value.get("name"):
                    value["name"] = lowercase_name(str(value["name"]))
                values.append(value)
            attr["values"] = values
        normalized_attrs.append(attr)

    result["attributes"] = normalized_attrs
    return result
