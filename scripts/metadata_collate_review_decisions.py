# /// script
# requires-python = ">=3.11"
# ///
"""Collate subagent metadata-review triage JSON into one decision file."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
TRIAGE_CATEGORIES = {
    "proposed_accept",
    "proposed_skip",
    "needs_attention",
    "suspected_tool_problem",
}
HUMAN_ACTIONS = {"approve", "skip", "provide_feedback"}


def rel(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_stem(row: dict[str, Any]) -> str:
    stem = str(row.get("id") or row.get("stem") or "").strip()
    if stem:
        return stem
    path = str(row.get("path") or "").strip()
    if not path:
        raise ValueError(f"Decision record is missing id/path: {row}")
    return Path(path).name.removesuffix(".fm.json")


def normalize_decision(row: dict[str, Any], *, source_file: Path) -> dict[str, Any]:
    stem = normalize_stem(row)
    category = str(row.get("triage_category") or "").strip()
    if category not in TRIAGE_CATEGORIES:
        raise ValueError(f"{source_file}: {stem} has invalid triage_category {category!r}")

    action = str(row.get("recommended_human_action") or "").strip()
    if action and action not in HUMAN_ACTIONS:
        raise ValueError(f"{source_file}: {stem} has invalid recommended_human_action {action!r}")
    if not action:
        action = {
            "proposed_accept": "approve",
            "proposed_skip": "skip",
            "needs_attention": "provide_feedback",
            "suspected_tool_problem": "provide_feedback",
        }[category]

    return {
        "id": stem,
        "path": row.get("path") or f"defs/{stem}.fm.json",
        "triage_category": category,
        "recommended_human_action": action,
        "field_flags": [str(item) for item in row.get("field_flags") or []],
        "reason": str(row.get("reason") or "").strip(),
        "evidence": [str(item) for item in row.get("evidence") or []],
        "reviewer_notes": str(row.get("reviewer_notes") or "").strip(),
        "source_decision_file": rel(source_file),
    }


def load_decisions(path: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    payload = read_json(path)
    records = payload.get("records") if isinstance(payload, dict) else payload
    if not isinstance(records, list):
        raise ValueError(f"{path}: expected records[] or a list of decision records")
    patterns = payload.get("patterns") if isinstance(payload, dict) else []
    return [normalize_decision(row, source_file=path) for row in records], list(patterns or [])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("decision_files", nargs="+", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--run-dir", type=Path)
    args = parser.parse_args()

    by_id: dict[str, dict[str, Any]] = {}
    duplicate_ids: list[str] = []
    patterns: list[dict[str, Any]] = []
    for path in args.decision_files:
        records, file_patterns = load_decisions(path)
        patterns.extend(file_patterns)
        for record in records:
            if record["id"] in by_id:
                duplicate_ids.append(record["id"])
            by_id[record["id"]] = record

    if duplicate_ids:
        raise SystemExit(f"Duplicate review decisions: {', '.join(sorted(set(duplicate_ids)))}")

    records = [by_id[key] for key in sorted(by_id)]
    counts = Counter(record["triage_category"] for record in records)
    output = {
        "created_at": datetime.now(tz=UTC).isoformat(),
        "run_dir": rel(args.run_dir) if args.run_dir else None,
        "counts": dict(sorted(counts.items())),
        "records": records,
        "patterns": patterns,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"records": len(records), "counts": output["counts"], "output": rel(args.output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
