# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Compare a metadata assignment run against the regression-floor expectations."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_FLOOR = REPO_ROOT / "evals" / "regression_floor" / "regression-floor-v1.json"
DEFAULT_RUN_DIR = REPO_ROOT / ".metadata-runs" / "phase6-targeted-v1" / "run"
DEFAULT_OUTPUT_DIR = REPO_ROOT / ".metadata-runs" / "phase6-targeted-v1" / "comparison"
DEFAULT_MARKDOWN = REPO_ROOT / "docs" / "plans" / "metadata-enrichment-regression-floor-results-2026-05-05.md"


def display_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def comparable(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: comparable(value[key]) for key in sorted(value)}
    if isinstance(value, list):
        normalized = [comparable(item) for item in value]
        return sorted(normalized, key=lambda item: json.dumps(item, sort_keys=True))
    return value


def audit_flags(run_dir: Path, item: str) -> list[dict[str, Any]]:
    audit_path = run_dir / "audits" / f"{item}.audit.json"
    if not audit_path.exists():
        return []
    payload = load_json(audit_path)
    flags = payload.get("flags")
    return flags if isinstance(flags, list) else []


def status_rows(run_dir: Path) -> list[dict[str, Any]]:
    status_path = run_dir / "status.jsonl"
    if not status_path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line in status_path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def compare(floor_path: Path, run_dir: Path) -> dict[str, Any]:
    floor = load_json(floor_path)
    records = floor.get("records", [])
    mismatches: list[dict[str, Any]] = []
    missing_outputs: list[str] = []
    compared_fields = 0
    flags_by_item: dict[str, list[dict[str, Any]]] = {}

    for record in records:
        item = record["item"]
        output_path = run_dir / "before-after" / f"{item}.after.json"
        if not output_path.exists():
            missing_outputs.append(item)
            continue
        actual = load_json(output_path)
        expected = record.get("expected", {})
        flags = audit_flags(run_dir, item)
        if flags:
            flags_by_item[item] = flags

        for field, expected_value in expected.items():
            compared_fields += 1
            actual_value = actual.get(field)
            if comparable(expected_value) != comparable(actual_value):
                mismatches.append(
                    {
                        "item": item,
                        "field": field,
                        "guards": record.get("guards"),
                        "expected": expected_value,
                        "actual": actual_value,
                    }
                )

    statuses = status_rows(run_dir)
    status_counts = Counter(str(row.get("status")) for row in statuses)
    audit_flag_counts = {item: len(flags) for item, flags in flags_by_item.items()}

    return {
        "floor": display_path(floor_path),
        "run_dir": display_path(run_dir),
        "records_expected": len(records),
        "records_with_outputs": len(records) - len(missing_outputs),
        "fields_compared": compared_fields,
        "status_counts": dict(sorted(status_counts.items())),
        "missing_outputs": missing_outputs,
        "mismatch_count": len(mismatches),
        "mismatch_counts_by_field": dict(sorted(Counter(row["field"] for row in mismatches).items())),
        "mismatches": mismatches,
        "audit_flag_count": sum(audit_flag_counts.values()),
        "audit_flag_counts_by_item": audit_flag_counts,
        "audit_flags_by_item": flags_by_item,
        "passed": not missing_outputs and not mismatches and not flags_by_item,
    }


def markdown_summary(summary: dict[str, Any]) -> str:
    lines = [
        "# Metadata Regression-Floor Results",
        "",
        "Date: 2026-05-05",
        "",
        "## Summary",
        "",
        f"- Floor: `{summary['floor']}`",
        f"- Run directory: `{summary['run_dir']}`",
        f"- Records expected: {summary['records_expected']}",
        f"- Records with outputs: {summary['records_with_outputs']}",
        f"- Fields compared: {summary['fields_compared']}",
        f"- Strict mismatches: {summary['mismatch_count']}",
        f"- Deterministic audit flags on floor records: {summary['audit_flag_count']}",
        f"- Result: {'pass' if summary['passed'] else 'needs follow-up'}",
        "",
        "## Batch Status",
        "",
    ]
    for status, count in summary["status_counts"].items():
        lines.append(f"- `{status}`: {count}")
    if not summary["status_counts"]:
        lines.append("- No `status.jsonl` rows found.")

    lines.extend(["", "## Strict Mismatches", ""])
    if summary["mismatches"]:
        lines.extend(["| Item | Field | Guards | Expected | Actual |", "| --- | --- | --- | --- | --- |"])
        for row in summary["mismatches"]:
            expected = json.dumps(row["expected"], sort_keys=True).replace("|", "\\|")
            actual = json.dumps(row["actual"], sort_keys=True).replace("|", "\\|")
            lines.append(
                f"| `{row['item']}` | `{row['field']}` | {row.get('guards') or ''} | "
                f"`{expected}` | `{actual}` |"
            )
    else:
        lines.append("No strict mismatches.")

    lines.extend(["", "## Audit Flags", ""])
    if summary["audit_flags_by_item"]:
        lines.extend(["| Item | Field | Severity | Message |", "| --- | --- | --- | --- |"])
        for item, flags in summary["audit_flags_by_item"].items():
            for flag in flags:
                message = str(flag.get("message", "")).replace("|", "\\|")
                lines.append(
                    f"| `{item}` | `{flag.get('field', '')}` | `{flag.get('severity', '')}` | {message} |"
                )
    else:
        lines.append("No deterministic audit flags on floor records.")

    if summary["missing_outputs"]:
        lines.extend(["", "## Missing Outputs", ""])
        for item in summary["missing_outputs"]:
            lines.append(f"- `{item}`")

    lines.append("")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--floor", type=Path, default=DEFAULT_FLOOR)
    parser.add_argument("--run-dir", type=Path, default=DEFAULT_RUN_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--markdown", type=Path, default=DEFAULT_MARKDOWN)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    summary = compare(args.floor, args.run_dir)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.output_dir / "metadata-regression-floor-comparison.json"
    json_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    args.markdown.parent.mkdir(parents=True, exist_ok=True)
    args.markdown.write_text(markdown_summary(summary), encoding="utf-8")
    print(f"Wrote {display_path(json_path)}")
    print(f"Wrote {display_path(args.markdown)}")
    print(
        f"Compared {summary['records_with_outputs']} records; "
        f"mismatches={summary['mismatch_count']}; audit_flags={summary['audit_flag_count']}"
    )


if __name__ == "__main__":
    main()
