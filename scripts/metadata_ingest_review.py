# /// script
# requires-python = ">=3.11"
# ///
"""Ingest structured human review JSON from the metadata review tool."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
DONE_STATUSES = {"approved", "feedback"}


def display_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def normalize_review_tool_export(data: dict[str, Any]) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for response in data.get("responses") or []:
        status = str(response.get("status") or "missing")
        normalized_status = "accepted" if status == "approved" else ("feedback" if status == "feedback" else "unfinished")
        items.append(
            {
                "item_id": response.get("item_id"),
                "path": response.get("path") or response.get("file_name"),
                "title": response.get("title"),
                "raw_status": status,
                "normalized_status": normalized_status,
                "comment": str(response.get("comment") or ""),
                "first_reviewed_at": response.get("first_reviewed_at"),
                "updated_at": response.get("updated_at"),
            }
        )
    return items


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("review_json", type=Path)
    parser.add_argument("--output", type=Path, default=REPO_ROOT / ".metadata-runs" / "review-fix-list.json")
    args = parser.parse_args()

    data: dict[str, Any] = json.loads(args.review_json.read_text(encoding="utf-8"))
    if "responses" not in data:
        raise SystemExit(
            "Review JSON must be a review-tool export with top-level 'responses'. "
            "Generate it from the standalone HTML review app's Download JSON action."
        )
    items = normalize_review_tool_export(data)
    raw_counts = Counter(item["raw_status"] for item in items)
    normalized_counts = Counter(item["normalized_status"] for item in items)

    unfinished = [item for item in items if item["raw_status"] not in DONE_STATUSES]
    actionable_feedback = [
        item
        for item in items
        if item["normalized_status"] == "feedback" or item["comment"].strip()
    ]

    output = {
        "source_review": str(args.review_json),
        "dataset": data.get("dataset") or {},
        "reviewer": data.get("reviewer") or {},
        "status_counts": {
            "raw": dict(sorted(raw_counts.items())),
            "normalized": dict(sorted(normalized_counts.items())),
        },
        "all_items_reviewed": not unfinished,
        "blocks_progression": bool(unfinished),
        "requires_follow_up": bool(actionable_feedback),
        "unfinished_items": unfinished,
        "actionable_feedback": actionable_feedback,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote review ingestion summary to {display_path(args.output)}")
    return 1 if output["blocks_progression"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
