#!/usr/bin/env python3
"""Create finding model stubs directly, bypassing AI name normalization.

This script calls the findingmodel library functions directly to create
stub models with unique IDs and standard codes, without the AI-based
name normalization step that `make-stub-model` uses (which can rename
findings unexpectedly).

Usage (single model):
    uv run .claude/skills/new-finding/scripts/create_model.py \
        --name "pneumothorax" \
        --description "Air in the pleural space." \
        --synonyms "air leak" "collapsed lung" \
        --tags chest XR finding \
        --source OIDM \
        --contributor hoodcm \
        --output defs/pneumothorax.fm.json

Usage (batch via JSON on stdin):
    uv run .claude/skills/new-finding/scripts/create_model.py --batch << 'EOF'
    {
        "source": "OIDM",
        "contributor": "hoodcm",
        "tags": ["chest", "XR", "finding"],
        "models": [
            {
                "name": "pneumothorax",
                "description": "Air in the pleural space.",
                "synonyms": ["air leak", "collapsed lung"]
            },
            {
                "name": "atelectasis",
                "description": "Partial or complete collapse of lung parenchyma.",
                "synonyms": ["lung collapse", "pulmonary collapse"]
            }
        ]
    }
    EOF

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
}


def create_finding_model(
    name: str,
    description: str,
    synonyms: list[str] | None = None,
    tags: list[str] | None = None,
    source: str = "OIDM",
    contributor_keys: list[str] | None = None,
    output_path: str | None = None,
) -> str:
    """Create a complete finding model stub with IDs and codes.

    Returns "filename|name|oifm_id" on success.
    """
    tags = tags or ["chest", "XR", "finding"]
    contributor_keys = contributor_keys or ["hoodcm", "OIDM"]

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

        for model_spec in config.get("models", []):
            name = model_spec["name"]
            description = model_spec.get("description", "")
            synonyms = model_spec.get("synonyms", [])
            tags = model_spec.get("tags", default_tags)
            output = model_spec.get("output")

            try:
                result = create_finding_model(
                    name=name,
                    description=description,
                    synonyms=synonyms,
                    tags=tags,
                    source=source,
                    contributor_keys=contributors,
                    output_path=output,
                )
                print(result)
            except Exception as e:
                print(f"ERROR creating '{name}': {e}", file=sys.stderr)

    elif args.name:
        if not args.description:
            print("ERROR: --description is required", file=sys.stderr)
            sys.exit(1)
        result = create_finding_model(
            name=args.name,
            description=args.description,
            synonyms=args.synonyms,
            tags=args.tags,
            source=args.source,
            contributor_keys=args.contributor,
            output_path=args.output,
        )
        print(result)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
