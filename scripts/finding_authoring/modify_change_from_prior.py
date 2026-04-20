#!/usr/bin/env python3
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "findingmodel",
# ]
# ///
"""Add or remove direction-of-change values on an existing `change from prior` attribute.

Complements `add_change_from_prior.py` (which adds the WHOLE attribute when missing).
Use this when the attribute already exists and quality review decides to winnow
inappropriate direction pairs (most common) or add missing ones.

Core values (`unchanged`, `stable`, `new`, `resolved`) cannot be removed — they are
the required minimum set per `prompts/fragments/presence_and_change.md`.

Preserves: oifm_id, all existing value_codes on values that remain. New values get
fresh value_codes with indices beyond the highest currently used (non-contiguous but
stable — existing external references to value_codes survive).

Usage:
    # Winnow: remove pairs that don't fit this finding
    uv run --env-file .env scripts/finding_authoring/modify_change_from_prior.py \\
        defs/meningioma.fm.json --remove increased,decreased

    # Add: include pairs for a condition/process
    uv run --env-file .env scripts/finding_authoring/modify_change_from_prior.py \\
        defs/nasal_septal_deviation.fm.json --add increased,decreased

    # Both in one call
    uv run --env-file .env scripts/finding_authoring/modify_change_from_prior.py \\
        defs/foo.fm.json --remove larger,smaller --add worsened,improved

Output: `filepath|name|<summary of changes>`
"""

import argparse
import json
import sys
from pathlib import Path


# Standard direction-of-change value metadata (RADLEX, SNOMED codes).
# None = no index_codes (repo pattern for resolved, worsened, improved).
_STD_CODES = {
    "larger": ("RID5791", "enlarged", "263768009", "Greater (qualifier value)"),
    "smaller": ("RID38669", "diminished", "263796003", "Lesser (qualifier value)"),
    "increased": ("RID36043", "increased", "35105006", "Increased (qualifier value)"),
    "decreased": ("RID36044", "decreased", "1250004", "Decreased (qualifier value)"),
    "worsened": None,
    "improved": None,
}

_CORE = {"unchanged", "stable", "new", "resolved"}
_ADDABLE = set(_STD_CODES)


def _description_for(value_name: str, finding_cap: str) -> str:
    if value_name in ("larger", "smaller"):
        return f"{finding_cap} is {value_name}"
    return f"{finding_cap} has {value_name}"


def _build_value(name: str, value_code: str, finding_cap: str) -> dict:
    entry: dict = {
        "value_code": value_code,
        "name": name,
        "description": _description_for(name, finding_cap),
    }
    codes = _STD_CODES[name]
    if codes is not None:
        rad_code, rad_disp, sn_code, sn_disp = codes
        entry["index_codes"] = [
            {"system": "RADLEX", "code": rad_code, "display": rad_disp},
            {"system": "SNOMED", "code": sn_code, "display": sn_disp},
        ]
    return entry


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Add or remove direction-of-change values on an existing change-from-prior attribute.",
    )
    parser.add_argument("filepath", help="Path to .fm.json file")
    parser.add_argument("--add", default="",
                        help=f"Comma-separated values to add. Valid: {', '.join(sorted(_ADDABLE))}")
    parser.add_argument("--remove", default="",
                        help=f"Comma-separated values to remove. Valid: {', '.join(sorted(_ADDABLE))}")
    args = parser.parse_args()

    to_add = [v.strip() for v in args.add.split(",") if v.strip()]
    to_remove = [v.strip() for v in args.remove.split(",") if v.strip()]

    if not to_add and not to_remove:
        print("ERROR: specify at least one of --add or --remove", file=sys.stderr)
        sys.exit(1)

    for v in to_add + to_remove:
        if v not in _ADDABLE:
            print(f"ERROR: {v!r} not a valid direction-of-change value. "
                  f"Valid: {', '.join(sorted(_ADDABLE))}", file=sys.stderr)
            sys.exit(1)

    # Guard against removing core values
    for v in to_remove:
        if v in _CORE:
            print(f"ERROR: cannot remove core value {v!r} (required minimum set)", file=sys.stderr)
            sys.exit(1)

    path = Path(args.filepath)
    if not path.exists():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        sys.exit(1)

    data = json.loads(path.read_text())
    finding_name = data.get("name", "<finding>")
    finding_cap = finding_name[0].upper() + finding_name[1:] if finding_name else "<finding>"

    # Find change_from_prior attribute
    cfp = None
    for attr in data.get("attributes", []):
        if attr.get("name") == "change from prior":
            cfp = attr
            break
    if cfp is None:
        print(f"ERROR: model has no 'change from prior' attribute. "
              f"Use add_change_from_prior.py to add it first.", file=sys.stderr)
        sys.exit(1)

    oifma = cfp["oifma_id"]
    current_values = cfp.get("values", [])

    # Remove first
    removed = []
    if to_remove:
        kept = []
        for v in current_values:
            if v["name"] in to_remove:
                removed.append(v["name"])
            else:
                kept.append(v)
        current_values = kept

    # Add next — allocate value_codes beyond highest currently used
    added = []
    if to_add:
        present = {v["name"] for v in current_values}
        max_idx = -1
        for v in current_values:
            try:
                idx = int(v["value_code"].rsplit(".", 1)[1])
                if idx > max_idx:
                    max_idx = idx
            except (KeyError, ValueError, IndexError):
                pass
        for name in to_add:
            if name in present:
                continue  # idempotent — skip if already present
            max_idx += 1
            current_values.append(_build_value(name, f"{oifma}.{max_idx}", finding_cap))
            added.append(name)

    cfp["values"] = current_values

    path.write_text(json.dumps(data, indent=2) + "\n")

    summary_parts = []
    if removed:
        summary_parts.append(f"removed={removed}")
    if added:
        summary_parts.append(f"added={added}")
    summary = "; ".join(summary_parts) if summary_parts else "no-op"
    print(f"{path}|{finding_name}|{summary}")


if __name__ == "__main__":
    main()
