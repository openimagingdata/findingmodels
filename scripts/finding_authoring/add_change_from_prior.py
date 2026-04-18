#!/usr/bin/env python3
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "findingmodel",
# ]
# ///
"""Add a `change from prior` attribute to an existing finding model.

Use this when review finds an older model that only has a `presence` attribute.
Preserves the model's oifm_id and all existing attribute oifma_ids / value_codes;
only allocates a new oifma_id for the added attribute.

DO NOT use `findingmodel.tools.add_ids_to_model` for this case: when a model is
loaded via FindingModelBase.model_validate, existing IDs may be stripped and
regenerated. This helper uses Index.generate_attribute_id() surgically so the
only new ID is the one for the new attribute.

Usage:
    uv run --env-file .env scripts/finding_authoring/add_change_from_prior.py \\
        defs/<file>.fm.json \\
        --pairs larger-smaller,worsened-improved

Direction pairs to include (comma-separated):
    larger-smaller       for findings with measurable size (masses, effusions)
    increased-decreased  for quantities / density / extent
    worsened-improved    for conditions / disease processes

Omit --pairs to include only the minimum set (unchanged, stable, new, resolved).

Source is inferred from the model's existing oifm_id.
"""

import argparse
import json
import re
import sys
from pathlib import Path

from findingmodel.index import Index


# Standard change-from-prior value metadata.
# None = value gets no index_codes (matches existing repo pattern for resolved).
_STD_CODES = {
    "unchanged": ("RID39268", "unchanged", "260388006", "No status change (qualifier value)"),
    "stable": ("RID5734", "stable", "58158008", "Stable (qualifier value)"),
    "new": ("RID5720", "new", "7147002", "New (qualifier value)"),
    "resolved": None,
    "larger": ("RID5791", "enlarged", "263768009", "Greater (qualifier value)"),
    "smaller": ("RID38669", "diminished", "263796003", "Lesser (qualifier value)"),
    "increased": ("RID36043", "increased", "35105006", "Increased (qualifier value)"),
    "decreased": ("RID36044", "decreased", "1250004", "Decreased (qualifier value)"),
    "worsened": None,
    "improved": None,
}

_VALID_PAIRS = {
    "larger-smaller": ("larger", "smaller"),
    "increased-decreased": ("increased", "decreased"),
    "worsened-improved": ("worsened", "improved"),
}


def _description_for(value_name: str, finding_cap: str) -> str:
    if value_name == "resolved":
        return f"{finding_cap} seen on a prior exam has resolved"
    if value_name in ("unchanged", "stable", "new", "larger", "smaller"):
        verb = "is"
        return f"{finding_cap} {verb} {value_name}"
    if value_name in ("increased", "decreased", "worsened", "improved"):
        return f"{finding_cap} has {value_name}"
    return ""


def _build_value(name: str, idx_in_list: int, oifma_id: str, finding_cap: str) -> dict:
    entry: dict = {
        "value_code": f"{oifma_id}.{idx_in_list}",
        "name": name,
        "description": _description_for(name, finding_cap),
    }
    codes = _STD_CODES[name]
    if codes is not None:
        radlex_code, radlex_display, snomed_code, snomed_display = codes
        entry["index_codes"] = [
            {"system": "RADLEX", "code": radlex_code, "display": radlex_display},
            {"system": "SNOMED", "code": snomed_code, "display": snomed_display},
        ]
    return entry


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Add 'change from prior' attribute to an existing finding model."
    )
    parser.add_argument("filepath", help="Path to .fm.json file")
    parser.add_argument(
        "--pairs",
        default="",
        help="Comma-separated direction pairs to include: "
             "larger-smaller, increased-decreased, worsened-improved",
    )
    args = parser.parse_args()

    path = Path(args.filepath)
    if not path.exists():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        sys.exit(1)

    data = json.loads(path.read_text())

    existing_oifm = data.get("oifm_id")
    if not existing_oifm:
        print("ERROR: model has no oifm_id; use create_model.py for new models.",
              file=sys.stderr)
        sys.exit(1)

    m = re.match(r"^OIFM_([A-Z0-9]+)_\d+$", existing_oifm)
    if not m:
        print(f"ERROR: cannot parse source from oifm_id: {existing_oifm}",
              file=sys.stderr)
        sys.exit(1)
    source = m.group(1)

    for attr in data.get("attributes", []):
        if attr.get("name") == "change from prior":
            print("ERROR: model already has a 'change from prior' attribute",
                  file=sys.stderr)
            sys.exit(1)

    requested_pairs = [p.strip() for p in args.pairs.split(",") if p.strip()]
    for p in requested_pairs:
        if p not in _VALID_PAIRS:
            print(
                f"ERROR: unknown pair '{p}'. Valid: {', '.join(_VALID_PAIRS)}",
                file=sys.stderr,
            )
            sys.exit(1)

    value_names: list[str] = ["unchanged", "stable", "new", "resolved"]
    for pair_key in requested_pairs:
        value_names.extend(_VALID_PAIRS[pair_key])

    finding_name = data.get("name", "<finding>")
    finding_cap = finding_name[0].upper() + finding_name[1:] if finding_name else "<finding>"

    new_oifma = Index().generate_attribute_id(model_oifm_id=existing_oifm, source=source)

    values = [_build_value(n, i, new_oifma, finding_cap) for i, n in enumerate(value_names)]

    change_attr = {
        "oifma_id": new_oifma,
        "name": "change from prior",
        "description": f"Whether and how {finding_name} has changed over time",
        "type": "choice",
        "values": values,
        "required": False,
        "max_selected": 1,
        "index_codes": [
            {"system": "RADLEX", "code": "RID49896", "display": "change"},
            {"system": "SNOMED", "code": "263703002",
             "display": "Changed status (qualifier value)"},
        ],
    }

    data.setdefault("attributes", [])
    if data["attributes"] and data["attributes"][0].get("name") != "presence":
        print(
            "WARNING: first attribute is not 'presence'; inserting 'change from prior' "
            "at position 1 regardless",
            file=sys.stderr,
        )
    data["attributes"].insert(1, change_attr)

    path.write_text(json.dumps(data, indent=2) + "\n")
    print(f"{path}|{finding_name}|{new_oifma}")


if __name__ == "__main__":
    main()
