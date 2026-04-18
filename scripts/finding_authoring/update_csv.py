#!/usr/bin/env python3
"""Update a CSV file with OIFM IDs for processed findings.

Reads a mapping of row IDs to OIFM IDs (from stdin or --mapping arg) and
updates the specified column in the CSV. Uses Python's csv module to properly
handle quoted fields containing commas.

Usage (mapping as argument):
    uv run scripts/finding_authoring/update_csv.py \
        lists/cxr_findings.csv \
        --id-column 0 \
        --oifm-column 6 \
        --mapping 'FID0010=OIFM_OIDM_207240,FID0011=OIFM_OIDM_449436'

Usage (mapping from fix_stub.py output, with a name-to-id lookup):
    uv run scripts/finding_authoring/update_csv.py \
        lists/cxr_findings.csv \
        --id-column 0 \
        --oifm-column 6 \
        --mapping-json '{"FID0010": "OIFM_OIDM_207240"}'

Usage (mapping JSON from stdin):
    echo '{"FID0010": "OIFM_OIDM_207240"}' | \
    uv run scripts/finding_authoring/update_csv.py \
        lists/cxr_findings.csv \
        --id-column 0 \
        --oifm-column 6 \
        --mapping-stdin
"""

import argparse
import csv
import io
import json
import sys
from pathlib import Path


def update_csv(
    csv_path: str,
    id_column: int,
    oifm_column: int,
    mapping: dict[str, str],
) -> int:
    """Update CSV with OIFM IDs. Returns count of rows updated."""
    p = Path(csv_path)
    content = p.read_text()
    lines = content.split("\n")

    updated = 0
    new_lines = []

    for line in lines:
        if not line.strip():
            new_lines.append(line)
            continue

        # Use csv module to properly parse (handles quoted fields with commas)
        reader = csv.reader(io.StringIO(line))
        try:
            row = next(reader)
        except StopIteration:
            new_lines.append(line)
            continue

        row_id = row[id_column] if len(row) > id_column else ""

        if row_id in mapping:
            # Check if OIFM column already has a value
            current_oifm = row[oifm_column] if len(row) > oifm_column else ""
            if not current_oifm.startswith("OIFM"):
                # Extend row if needed
                while len(row) <= oifm_column:
                    row.append("")
                row[oifm_column] = mapping[row_id]

                # Re-serialize with csv module
                writer_buf = io.StringIO()
                csv.writer(writer_buf).writerow(row)
                line = writer_buf.getvalue().rstrip("\r\n")
                updated += 1

        new_lines.append(line)

    p.write_text("\n".join(new_lines))
    return updated


def main():
    parser = argparse.ArgumentParser(description="Update CSV with OIFM IDs")
    parser.add_argument("csv_file", help="Path to CSV file")
    parser.add_argument(
        "--id-column",
        type=int,
        default=0,
        help="Column index for row IDs (default: 0)",
    )
    parser.add_argument(
        "--oifm-column",
        type=int,
        default=6,
        help="Column index for OIFM IDs (default: 6)",
    )
    parser.add_argument(
        "--mapping",
        help="Comma-separated key=value pairs (e.g., FID0010=OIFM_OIDM_207240)",
    )
    parser.add_argument("--mapping-json", help="JSON string of {id: oifm_id}")
    parser.add_argument(
        "--mapping-stdin",
        action="store_true",
        help="Read JSON mapping from stdin",
    )

    args = parser.parse_args()

    # Build mapping from whichever source
    mapping = {}
    if args.mapping:
        for pair in args.mapping.split(","):
            key, val = pair.strip().split("=", 1)
            mapping[key.strip()] = val.strip()
    elif args.mapping_json:
        mapping = json.loads(args.mapping_json)
    elif args.mapping_stdin:
        mapping = json.load(sys.stdin)
    else:
        print("ERROR: Provide --mapping, --mapping-json, or --mapping-stdin",
              file=sys.stderr)
        sys.exit(1)

    updated = update_csv(args.csv_file, args.id_column, args.oifm_column, mapping)
    print(f"Updated {updated} rows in {args.csv_file}")


if __name__ == "__main__":
    main()
