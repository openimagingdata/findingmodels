#!/usr/bin/env python3
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "findingmodel",
# ]
# ///
"""Create finding model stubs directly, bypassing AI name normalization.

This script calls the findingmodel library functions directly to create
stub models with unique IDs and standard codes, without the AI-based
name normalization step that `make-stub-model` uses (which can rename
findings unexpectedly).

Usage (single model):
    uv run scripts/finding_authoring/create_model.py \
        --name "pneumothorax" \
        --description "Air in the pleural space." \
        --synonyms "air leak" "collapsed lung" \
        --tags chest XR finding \
        --source OIDM \
        --contributor hoodcm \
        --cfp-pairs larger-smaller \
        --output defs/pneumothorax.fm.json

Change-from-prior defaults to the minimum set (unchanged, stable, new, resolved).
Opt in to direction pairs via --cfp-pairs (comma-separated). Valid pair keys:
  larger-smaller, increased-decreased, worsened-improved

Usage (batch via JSON on stdin):
    uv run scripts/finding_authoring/create_model.py --batch << 'EOF'
    {
        "source": "OIDM",
        "contributor": "hoodcm",
        "tags": ["chest", "XR", "finding"],
        "cfp_pairs": "larger-smaller",
        "models": [
            {
                "name": "pneumothorax",
                "description": "Air in the pleural space.",
                "synonyms": ["air leak", "collapsed lung"]
            },
            {
                "name": "atelectasis",
                "description": "Partial or complete collapse of lung parenchyma.",
                "synonyms": ["lung collapse", "pulmonary collapse"],
                "cfp_pairs": "larger-smaller,worsened-improved"
            }
        ]
    }
    EOF

Top-level "cfp_pairs" sets a batch default; per-model "cfp_pairs" overrides.
Omit both for the minimum set.

Output: prints "filename|name|oifm_id" per model created.
"""

import argparse
import json
import sys
from pathlib import Path

from findingmodel import FindingInfo
from findingmodel.common import model_file_name
from findingmodel.create_stub import create_model_stub_from_info
from findingmodel.tools import add_ids_to_model, add_standard_codes_to_model

# Known contributors — same as fix_stub.py
CONTRIBUTORS = {
    "hoodcm": {
        "github_username": "hoodcm",
        "email": "chood@mgh.harvard.edu",
        "name": "C. Michael Hood, MD",
        "organization_code": "MGB",
    },
    "HeatherChase": {
        "github_username": "HeatherChase",
        "name": "Heather Chase",
        "organization_code": "MSFT",
    },
    "radngandhi": {
        "github_username": "radngandhi",
        "name": "Namita Gandhi, MD",
        "organization_code": "RSNA",
    },
    "talkasab": {
        "github_username": "talkasab",
        "email": "talkasab@partners.org",
        "name": "Tarik Alkasab, MD, PhD",
        "organization_code": "MGB",
    },
    "OIDM": {"name": "Open Imaging Data Model", "code": "OIDM"},
    "GMTS": {
        "name": "Radiology Gamuts Ontology",
        "code": "GMTS",
        "url": "https://gamuts.net/",
    },
    "CDE": {"name": "ACR/RSNA Common Data Elements Project", "code": "CDE"},
    "MGB": {"name": "Mass General Brigham", "code": "MGB"},
    "MSFT": {"name": "Microsoft", "code": "MSFT"},
    "RSNA": {"name": "Radiological Society of North America", "code": "RSNA"},
}

# Valid change-from-prior direction pairs for --cfp-pairs. Keys are the pair names;
# values are the two value-names to keep from the upstream library's default set.
_CFP_VALID_PAIRS = {
    "larger-smaller": ("larger", "smaller"),
    "increased-decreased": ("increased", "decreased"),
    "worsened-improved": ("worsened", "improved"),
}
_CFP_CORE = {"unchanged", "stable", "new", "resolved"}


def _parse_cfp_pairs(raw: str | None) -> list[str]:
    """Parse a comma-separated cfp_pairs string. Empty/None → no pairs."""
    if not raw:
        return []
    keys = [p.strip() for p in raw.split(",") if p.strip()]
    for key in keys:
        if key not in _CFP_VALID_PAIRS:
            raise ValueError(
                f"Unknown cfp_pairs value {key!r}. "
                f"Valid: {', '.join(_CFP_VALID_PAIRS)}"
            )
    return keys


def _winnow_change_from_prior(model_dict: dict, cfp_pairs: list[str], finding_name: str) -> None:
    """Reshape the `change from prior` attribute to core + requested direction pairs.

    - Filters values down to core (unchanged/stable/new/resolved) plus the values
      named by the requested pairs. Preserves existing value_code + index_codes.
    - Appends `worsened`/`improved` value entries if that pair is requested
      (upstream create_model_stub_from_info doesn't generate those).
    - Drops the leading article from the attribute description
      ("Whether and how a X has changed" → "Whether and how X has changed").

    Mutates model_dict in place.
    """
    requested_value_names: list[str] = []
    for key in cfp_pairs:
        requested_value_names.extend(_CFP_VALID_PAIRS[key])
    kept_names = _CFP_CORE | set(requested_value_names)
    finding_cap = finding_name[0].upper() + finding_name[1:] if finding_name else ""

    for attr in model_dict.get("attributes", []):
        if attr.get("name") != "change from prior":
            continue

        # Keep core + any upstream-generated direction values that are in kept_names
        existing_names = {v["name"] for v in attr.get("values", [])}
        attr["values"] = [v for v in attr.get("values", []) if v.get("name") in kept_names]

        # Append any requested values that upstream didn't generate (worsened/improved)
        oifma = attr.get("oifma_id", "")
        next_idx = max(
            (int(v["value_code"].rsplit(".", 1)[1])
             for v in attr["values"] if "value_code" in v),
            default=-1,
        ) + 1
        for name in requested_value_names:
            if name in existing_names:
                continue  # already kept from upstream output
            # Build a minimal value entry — no index_codes for worsened/improved,
            # matching the repo pattern for values without standard codes.
            attr["values"].append({
                "value_code": f"{oifma}.{next_idx}",
                "name": name,
                "description": f"{finding_cap} has {name}",
            })
            next_idx += 1

        desc = attr.get("description", "")
        if desc.startswith("Whether and how a "):
            attr["description"] = "Whether and how " + desc[len("Whether and how a "):]
        break


def create_finding_model(
    name: str,
    description: str,
    synonyms: list[str] | None = None,
    tags: list[str] | None = None,
    source: str = "OIDM",
    contributor_keys: list[str] | None = None,
    output_path: str | None = None,
    cfp_pairs: list[str] | None = None,
) -> str:
    """Create a complete finding model stub with IDs and codes.

    Returns "filename|name|oifm_id" on success.
    """
    tags = tags or ["chest", "XR", "finding"]
    contributor_keys = contributor_keys or ["hoodcm", "OIDM"]
    cfp_pairs = cfp_pairs or []

    # 1. Build FindingInfo directly (no AI normalization)
    # FindingModelBase requires at least 1 synonym if synonyms list is provided
    info = FindingInfo(
        name=name,
        description=description,
        synonyms=synonyms if synonyms else None,
    )

    # 2. Create stub with standard attributes (presence + change from prior)
    stub = create_model_stub_from_info(info, tags=tags)

    # 3. Add unique IDs (checks DuckDB index for collision avoidance)
    full_model = add_ids_to_model(stub, source=source)

    # 4. Add standard SNOMED/RadLex codes to attributes/values
    add_standard_codes_to_model(full_model)

    # 5. Serialize and add contributors
    model_dict = json.loads(full_model.model_dump_json(exclude_none=True))
    contributors = []
    for key in contributor_keys:
        if key in CONTRIBUTORS:
            contributors.append(CONTRIBUTORS[key])
        else:
            print(f"WARNING: Unknown contributor '{key}', skipping", file=sys.stderr)
    if contributors:
        model_dict["contributors"] = contributors

    # 5a. Winnow change-from-prior to core + requested direction pairs.
    # Default (no pairs) keeps the minimum set only — reviewers add pairs
    # at create time via --cfp-pairs rather than having review trim after.
    _winnow_change_from_prior(model_dict, cfp_pairs, name)

    # 6. Determine output path
    if not output_path:
        filename = model_file_name(name)
        output_path = f"defs/{filename}"

    # 7. Write canonical JSON
    p = Path(output_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(model_dict, indent=2) + "\n")

    oifm_id = model_dict["oifm_id"]
    return f"{output_path}|{name}|{oifm_id}"


def main():
    parser = argparse.ArgumentParser(
        description="Create finding model stubs (no AI normalization)"
    )
    parser.add_argument("--name", help="Finding name")
    parser.add_argument("--description", help="Finding description")
    parser.add_argument("--synonyms", nargs="*", help="Synonym list")
    parser.add_argument(
        "--tags", nargs="*", default=["chest", "XR", "finding"], help="Tags"
    )
    parser.add_argument("--source", default="OIDM", help="Source code (default: OIDM)")
    parser.add_argument(
        "--contributor",
        nargs="*",
        default=["hoodcm", "OIDM"],
        help="Contributor key(s) (default: hoodcm OIDM)",
    )
    parser.add_argument("--output", "-o", help="Output file path")
    parser.add_argument(
        "--cfp-pairs",
        default="",
        help=(
            "Comma-separated change-from-prior direction pairs to include. "
            f"Valid: {', '.join(_CFP_VALID_PAIRS)}. "
            "Omit for the minimum set (unchanged, stable, new, resolved)."
        ),
    )
    parser.add_argument(
        "--batch", action="store_true", help="Read batch config from stdin (JSON)"
    )

    args = parser.parse_args()

    if args.batch:
        config = json.load(sys.stdin)
        source = config.get("source", "OIDM")
        # Support both "contributor" (single) and "contributors" (list)
        raw_contrib = config.get("contributors", config.get("contributor"))
        if isinstance(raw_contrib, str):
            contributors = [raw_contrib]
        elif isinstance(raw_contrib, list):
            contributors = raw_contrib
        else:
            contributors = ["hoodcm", "OIDM"]
        default_tags = config.get("tags", ["chest", "XR", "finding"])
        default_cfp_pairs = _parse_cfp_pairs(config.get("cfp_pairs"))

        for model_spec in config.get("models", []):
            name = model_spec["name"]
            description = model_spec.get("description", "")
            synonyms = model_spec.get("synonyms", [])
            tags = model_spec.get("tags", default_tags)
            output = model_spec.get("output")
            # Per-model cfp_pairs overrides batch default; missing key → use default.
            if "cfp_pairs" in model_spec:
                cfp_pairs = _parse_cfp_pairs(model_spec.get("cfp_pairs"))
            else:
                cfp_pairs = default_cfp_pairs

            try:
                result = create_finding_model(
                    name=name,
                    description=description,
                    synonyms=synonyms,
                    tags=tags,
                    source=source,
                    contributor_keys=contributors,
                    output_path=output,
                    cfp_pairs=cfp_pairs,
                )
                print(result)
            except Exception as e:
                print(f"ERROR creating '{name}': {e}", file=sys.stderr)

    elif args.name:
        if not args.description:
            print("ERROR: --description is required", file=sys.stderr)
            sys.exit(1)
        try:
            cfp_pairs = _parse_cfp_pairs(args.cfp_pairs)
        except ValueError as e:
            print(f"ERROR: {e}", file=sys.stderr)
            sys.exit(1)
        result = create_finding_model(
            name=args.name,
            description=args.description,
            synonyms=args.synonyms,
            tags=args.tags,
            source=args.source,
            contributor_keys=args.contributor,
            output_path=args.output,
            cfp_pairs=cfp_pairs,
        )
        print(result)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
