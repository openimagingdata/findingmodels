#!/usr/bin/env python3
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "findingmodel",
# ]
# ///
"""Rename an existing finding model, updating all embedded references.

Use when review decides the canonical name should change (e.g., scope-anchor
correction like `parenchymal hypoattenuation` → `brain parenchymal hypoattenuation`,
or generic → specific like `cavernous malformation` → `cerebral cavernous malformation`).

Performs:
1. Update `name` field.
2. Update every attribute `description` string that embeds the old finding name.
3. Update every value `description` string that embeds the capitalized old name.
4. Rename the file on disk (via Python os.rename, not git mv). If the file is
   git-tracked, follow up with `git add` of both old and new paths so git records
   the rename.

Preserves: oifm_id, all oifma_ids, all value_codes, synonyms, tags, contributors.

Usage:
    uv run --env-file .env scripts/finding_authoring/rename_model.py \\
        defs/parenchymal_hypoattenuation.fm.json \\
        --new-name "brain parenchymal hypoattenuation"

Output: `new_path|old_path|oifm_id`
"""

import argparse
import json
import os
import sys
from pathlib import Path

from findingmodel.common import model_file_name


def main() -> None:
    parser = argparse.ArgumentParser(description="Rename a finding model.")
    parser.add_argument("filepath", help="Path to the existing .fm.json file")
    parser.add_argument("--new-name", required=True,
                        help="New canonical finding name (lowercase, spaces)")
    parser.add_argument("--keep-filename", action="store_true",
                        help="Update `name` field only; do not rename the file on disk")
    args = parser.parse_args()

    old_path = Path(args.filepath)
    if not old_path.exists():
        print(f"ERROR: file not found: {old_path}", file=sys.stderr)
        sys.exit(1)

    data = json.loads(old_path.read_text())
    old_name = data.get("name")
    if not old_name:
        print(f"ERROR: file has no 'name' field: {old_path}", file=sys.stderr)
        sys.exit(1)

    new_name = args.new_name
    if old_name == new_name:
        print(f"ERROR: new name equals current name: {new_name}", file=sys.stderr)
        sys.exit(1)

    data["name"] = new_name

    # Replacements in description text:
    # - exact old_name → new_name
    # - capitalized variant → capitalized new
    old_cap = old_name[0].upper() + old_name[1:]
    new_cap = new_name[0].upper() + new_name[1:]

    def replace_in_string(s: str) -> str:
        return s.replace(old_name, new_name).replace(old_cap, new_cap)

    # Model-level description: leave alone — the description is clinical prose,
    # not a mechanical name reference. Human can rewrite via another edit if needed.

    for attr in data.get("attributes", []):
        if attr.get("description"):
            attr["description"] = replace_in_string(attr["description"])
        for v in attr.get("values", []):
            if v.get("description"):
                v["description"] = replace_in_string(v["description"])

    # Derive new filename from the new name unless told not to
    if args.keep_filename:
        new_path = old_path
    else:
        # model_file_name() returns the full "<stem>.fm.json" filename, not just the stem
        new_filename = model_file_name(new_name)
        new_path = old_path.parent / new_filename
        if new_path.exists() and new_path != old_path:
            print(f"ERROR: target file already exists: {new_path}", file=sys.stderr)
            sys.exit(1)

    # Write new file; if renaming, write new then remove old
    new_path.write_text(json.dumps(data, indent=2) + "\n")
    if new_path != old_path:
        os.remove(old_path)

    oifm_id = data.get("oifm_id", "UNKNOWN")
    print(f"{new_path}|{old_path}|{oifm_id}")


if __name__ == "__main__":
    main()
