# /// script
# requires-python = ">=3.11"
# ///
"""Build the metadata enrichment review page from completed run outputs."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_RUN_DIR = ROOT / ".metadata-runs" / "enrichment"
DEFAULT_OUTPUT_DIR = ROOT / ".metadata-runs" / "review-current"
TEMPLATE = Path(__file__).with_name("metadata_review_template.html")
FIELDS = (
    "name",
    "description",
    "entity_type",
    "sex_specificity",
    "age_profile",
    "expected_time_course",
)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def successful_paths(run_dir: Path) -> list[Path]:
    status = run_dir / "status.jsonl"
    if not status.exists():
        return []
    rows = [json.loads(line) for line in status.read_text(encoding="utf-8").splitlines() if line.strip()]
    latest_successes: dict[str, Path] = {}
    for row in rows:
        if row.get("status") in {"success", "dry_run_success"}:
            path = Path(row["path"])
            latest_successes[str(path)] = path
    return sorted(latest_successes.values(), key=str)


def repo_path(path: Path) -> Path:
    return path if path.is_absolute() else (ROOT / path).resolve()


def default_data_dir(output_dir: Path) -> Path:
    return output_dir.parent / f"{output_dir.name}-data"


def summarize_attributes(attributes: list[dict[str, Any]] | None) -> list[str]:
    summaries = []
    for attr in attributes or []:
        name = attr.get("name") or "attribute"
        if attr.get("type") == "choice":
            values = ", ".join(v["name"] for v in attr.get("values", []) if v.get("name"))
            summaries.append(f"{name} (choice: {values})" if values else f"{name} (choice)")
        elif attr.get("type") == "numeric":
            low = attr.get("min_value", "?")
            high = attr.get("max_value", "?")
            unit = f" {attr['unit']}" if attr.get("unit") else ""
            summaries.append(f"{name} (numeric {low}-{high}{unit})")
        else:
            summaries.append(f"{name} ({attr.get('type') or 'value'})")
    return summaries


def code_summary(code: dict[str, Any]) -> dict[str, str]:
    return {
        "system": str(code.get("system") or ""),
        "code": str(code.get("code") or ""),
        "label": str(code.get("display") or ""),
    }


def review_id(items: list[dict[str, Any]], run_dir: Path) -> str:
    stable_items = sorted((item["id"], item["file_name"], item["path"]) for item in items)
    payload = {"run_dir": rel(run_dir), "items": stable_items}
    return hashlib.sha1(json.dumps(payload, sort_keys=True).encode()).hexdigest()[:12]


def review_item(source_path: Path, run_dir: Path) -> dict[str, Any]:
    item_id = source_path.name.removesuffix(".fm.json")
    enriched_path = run_dir / "before-after" / f"{item_id}.after.json"
    review_path = run_dir / "reviews" / f"{item_id}.metadata-review.json"
    audit_path = run_dir / "audits" / f"{item_id}.audit.json"
    if not enriched_path.exists() or not review_path.exists():
        raise FileNotFoundError(f"Missing completed enrichment outputs for {rel(source_path)} in {rel(run_dir)}")

    model = read_json(enriched_path)
    review = read_json(review_path)
    audit = read_json(audit_path) if audit_path.exists() else {}
    warnings = [str(w) for w in review.get("warnings", [])]
    warnings += [f"Audit {flag.get('severity', 'flag')}: {flag.get('message', flag)}" for flag in audit.get("flags", [])]
    field_confidence = review.get("field_confidence", {})
    non_high_confidence = {
        field: confidence
        for field, confidence in field_confidence.items()
        if str(confidence).lower() != "high"
    }
    sections = []
    if warnings:
        sections.append({"title": "Run warnings", "kind": "list", "value": warnings})
    if non_high_confidence:
        sections.append({
            "title": "Non-high field confidence",
            "kind": "json",
            "value": non_high_confidence,
            "collapsed": True,
        })
    sections.append({
        "title": "Run details",
        "kind": "json",
        "collapsed": True,
        "value": {k: review[k] for k in ("assignment_timestamp", "model_used", "assignment_mode", "logfire_trace_id", "timings") if k in review},
    })
    return {
        "id": item_id,
        "file_name": source_path.name,
        "path": rel(source_path),
        "title": model.get("name") or item_id.replace("_", " "),
        "field_confidence": field_confidence,
        **{field: model.get(field) for field in FIELDS},
        "synonyms": model.get("synonyms") or [],
        "body_regions": model.get("body_regions") or [],
        "subspecialties": model.get("subspecialties") or [],
        "applicable_modalities": model.get("applicable_modalities") or [],
        "etiologies": model.get("etiologies") or [],
        "index_codes": [code_summary(c) for c in model.get("index_codes") or []],
        "anatomic_locations": [code_summary(c) for c in model.get("anatomic_locations") or []],
        "attributes": summarize_attributes(model.get("attributes")),
        "extra_sections": sections,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, default=DEFAULT_RUN_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument(
        "--embed-data",
        action=argparse.BooleanOptionalAction,
        default=True,
        help=(
            "Embed review data directly in index.html so it can be shared as a single file. "
            "Use --no-embed-data to load review-data.json from the same directory instead."
        ),
    )
    parser.add_argument(
        "--data-dir",
        type=Path,
        help=(
            "Directory for the preserved review-data.json when using embedded mode. "
            "Defaults to a sibling of --output-dir, e.g. review-current-data."
        ),
    )
    parser.add_argument("paths", nargs="*", type=Path)
    args = parser.parse_args()
    args.run_dir = repo_path(args.run_dir)
    args.output_dir = repo_path(args.output_dir)

    paths = args.paths or successful_paths(args.run_dir)
    if not paths:
        raise SystemExit(f"No completed enrichment results found in {rel(args.run_dir)}")

    items = [review_item((ROOT / path).resolve(), args.run_dir) for path in paths]
    data = {
        "id": review_id(items, args.run_dir),
        "title": "Metadata Enrichment Review",
        "intro": ["Review each enriched finding model.", "Approve items with no changes needed. Leave feedback when corrections are needed."],
        "items": items,
    }

    args.output_dir.mkdir(parents=True, exist_ok=True)
    data_dir = repo_path(args.data_dir) if args.data_dir else default_data_dir(args.output_dir)
    data_path = data_dir / "review-data.json"
    if args.embed_data:
        (args.output_dir / "review-data.json").unlink(missing_ok=True)
        data_dir.mkdir(parents=True, exist_ok=True)
        data_path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    else:
        data_path = args.output_dir / "review-data.json"
        data_path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    bootstrap_json = json.dumps(data) if args.embed_data else "null"
    html = (
        TEMPLATE.read_text(encoding="utf-8")
        .replace("__DATASET_BOOTSTRAP__", bootstrap_json)
        .replace("__PAGE_TITLE__", data["title"])
    )
    html_path = args.output_dir / "index.html"
    html_path.write_text(html, encoding="utf-8")
    mode = "embedded single-file" if args.embed_data else "external review-data.json"
    print(f"Open review app: {html_path.resolve()} ({mode})")
    print(f"Review data JSON: {data_path.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
