# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Compare clean-input metadata rerun outputs against reviewed source corrections."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MANIFEST = REPO_ROOT / ".metadata-runs" / "phase5-clean-input-rerun-v1" / "manifest.json"
DEFAULT_RUN_DIR = REPO_ROOT / ".metadata-runs" / "phase5-clean-input-rerun-v2" / "run"
DEFAULT_SOURCE_DEFS = REPO_ROOT / "defs"
DEFAULT_COVERAGE = REPO_ROOT / "docs" / "plans" / "metadata-enrichment-feedback-tooling-coverage-2026-05-05.md"
DEFAULT_OUTPUT_DIR = REPO_ROOT / ".metadata-runs" / "phase5-clean-input-rerun-v2" / "comparison"
DEFAULT_MARKDOWN = (
    REPO_ROOT / "docs" / "plans" / "metadata-enrichment-clean-input-rerun-graded-comparison-2026-05-05.md"
)

FIELD_BY_THEME = {
    "age": ["age_profile"],
    "anatomy": ["anatomic_locations", "body_regions"],
    "entity type/scope": ["entity_type"],
    "etiology": ["etiologies"],
    "modality": ["applicable_modalities"],
    "ontology/index code": ["index_codes"],
    "sex": ["sex_specificity"],
    "subspecialty": ["subspecialties"],
    "time course": ["expected_time_course"],
}

MOSTLY_EXACT_FIELDS = {"age_profile", "body_regions", "entity_type", "sex_specificity", "subspecialties"}
TIME_ORDER = ["weeks", "months", "years", "permanent"]


@dataclass(frozen=True)
class CoverageRow:
    item: str
    themes: list[str]
    concern: str


@dataclass(frozen=True)
class ComparedField:
    item: str
    field: str
    themes: list[str]
    grade: str
    confidence: str | None
    reviewed: Any
    rerun: Any
    concern: str


def display_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def normalize_cell(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace("<br>", " ")).strip()


def markdown_escape(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def slug_from_path(path: str | Path) -> str:
    return Path(path).name.removesuffix(".fm.json")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_coverage(path: Path) -> dict[str, CoverageRow]:
    rows: dict[str, CoverageRow] = {}
    in_table = False
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line.startswith("| Item | Themes | Tooling area |"):
            in_table = True
            continue
        if not in_table:
            continue
        if line.startswith("| ---"):
            continue
        if not line.startswith("| "):
            if rows:
                break
            continue
        cells = [normalize_cell(cell) for cell in line.strip("|").split("|")]
        if len(cells) < 7:
            continue
        item = cells[0]
        themes = [theme.strip() for theme in cells[1].split(",") if theme.strip()]
        rows[item] = CoverageRow(item=item, themes=themes, concern=cells[6])
    return rows


def fields_for_themes(themes: list[str]) -> list[str]:
    fields: list[str] = []
    for theme in themes:
        fields.extend(FIELD_BY_THEME.get(theme, []))
    return sorted(dict.fromkeys(fields))


def comparable(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: comparable(value[key]) for key in sorted(value)}
    if isinstance(value, list):
        normalized = [comparable(item) for item in value]
        return sorted(normalized, key=lambda item: json.dumps(item, sort_keys=True))
    return value


def exact_equal(reviewed: Any, rerun: Any) -> bool:
    return comparable(reviewed) == comparable(rerun)


def code_key(item: dict[str, Any]) -> str:
    system = str(item.get("system") or "").upper()
    code = str(item.get("code") or "")
    return f"{system}:{code}"


def code_display(item: dict[str, Any]) -> str:
    return str(item.get("display") or item.get("code") or "").strip().lower()


def code_set(value: Any) -> set[str]:
    if not isinstance(value, list):
        return set()
    return {code_key(item) for item in value if isinstance(item, dict)}


def display_set(value: Any) -> set[str]:
    if not isinstance(value, list):
        return set()
    return {code_display(item) for item in value if isinstance(item, dict)}


def value_set(value: Any) -> set[str]:
    if value is None:
        return set()
    if isinstance(value, list):
        return {json.dumps(comparable(item), sort_keys=True) if isinstance(item, dict) else str(item) for item in value}
    return {json.dumps(comparable(value), sort_keys=True) if isinstance(value, dict) else str(value)}


def duration(value: Any) -> str | None:
    if not isinstance(value, dict):
        return None
    raw = value.get("duration")
    return str(raw) if raw else None


def modifiers(value: Any) -> set[str]:
    if not isinstance(value, dict):
        return set()
    raw = value.get("modifiers")
    if not isinstance(raw, list):
        return set()
    return {str(item) for item in raw}


def grade_time_course(reviewed: Any, rerun: Any) -> str:
    if exact_equal(reviewed, rerun):
        return "exact"
    reviewed_duration = duration(reviewed)
    rerun_duration = duration(rerun)
    if reviewed_duration and not rerun_duration:
        return "missing-expected"
    if rerun_duration and not reviewed_duration:
        return "extra-unexpected"
    if reviewed_duration == rerun_duration and modifiers(reviewed) != modifiers(rerun):
        return "modifier-difference"
    if reviewed_duration in TIME_ORDER and rerun_duration in TIME_ORDER:
        reviewed_index = TIME_ORDER.index(reviewed_duration)
        rerun_index = TIME_ORDER.index(rerun_duration)
        distance = rerun_index - reviewed_index
        if distance == -1:
            return "adjacent-shorter"
        if distance == 1:
            return "adjacent-longer"
        return "distant"
    return "needs-review"


def tokenize_display(value: str) -> set[str]:
    stopwords = {"and", "of", "the", "system", "column", "joint"}
    return {token for token in re.findall(r"[a-z0-9]+", value.lower()) if token not in stopwords}


def related_display_grade(reviewed_displays: set[str], rerun_displays: set[str]) -> str | None:
    if not reviewed_displays or not rerun_displays:
        return None
    reviewed_tokens = set().union(*(tokenize_display(value) for value in reviewed_displays))
    rerun_tokens = set().union(*(tokenize_display(value) for value in rerun_displays))
    if reviewed_tokens and rerun_tokens and reviewed_tokens & rerun_tokens:
        return "sibling/nearby"
    reviewed_joined = " ".join(reviewed_displays)
    rerun_joined = " ".join(rerun_displays)
    if reviewed_joined in rerun_joined:
        return "child"
    if rerun_joined in reviewed_joined:
        return "parent"
    return None


def grade_anatomic_locations(reviewed: Any, rerun: Any) -> str:
    if exact_equal(reviewed, rerun):
        return "exact"
    reviewed_codes = code_set(reviewed)
    rerun_codes = code_set(rerun)
    missing = reviewed_codes - rerun_codes
    extra = rerun_codes - reviewed_codes
    if missing and not extra:
        return "missing-reviewed"
    if extra and not missing:
        displays = display_set(rerun)
        reviewed_displays = display_set(reviewed)
        relation = related_display_grade(reviewed_displays, displays)
        if relation == "child":
            return "extra-narrow"
        if relation == "parent":
            return "extra-broad"
        return "extra"
    relation = related_display_grade(display_set(reviewed), display_set(rerun))
    if relation:
        return relation
    return "unrelated"


def grade_index_codes(reviewed: Any, rerun: Any) -> str:
    if exact_equal(reviewed, rerun):
        return "exact"
    reviewed_codes = code_set(reviewed)
    rerun_codes = code_set(rerun)
    if reviewed_codes & rerun_codes:
        return "same-code"
    reviewed_displays = display_set(reviewed)
    rerun_displays = display_set(rerun)
    if reviewed_displays & rerun_displays:
        return "likely-equivalent"
    if rerun_codes - reviewed_codes and not reviewed_codes - rerun_codes:
        joined = " ".join(rerun_displays)
        if any(term in joined for term in ["radiograph", "x-ray", "x ray", "ct ", "mri", "ultrasound"]):
            return "modality-specific-overreach"
        return "unsupported-extra"
    relation = related_display_grade(reviewed_displays, rerun_displays)
    if relation == "parent":
        return "broader"
    if relation == "child":
        return "narrower"
    if relation:
        return "related-only"
    return "needs-ontology-review"


def grade_modalities(reviewed: Any, rerun: Any, model: dict[str, Any]) -> str:
    if exact_equal(reviewed, rerun):
        return "exact"
    reviewed_set = value_set(reviewed)
    rerun_set = value_set(rerun)
    missing = reviewed_set - rerun_set
    extra = rerun_set - reviewed_set
    text = " ".join(
        str(part)
        for part in [
            model.get("name"),
            model.get("description"),
            " ".join(model.get("synonyms") or []),
            " ".join(model.get("tags") or []),
        ]
        if part
    ).lower()
    if extra and "MR" in extra and any(term in text for term in ["lucent", "lucency", "radiolucent"]):
        return "descriptor-modality-conflict"
    if missing and not extra:
        return "missing-routine-modality"
    if extra and not missing:
        return "extra-nonroutine-modality"
    return "needs-review"


def grade_etiologies(reviewed: Any, rerun: Any) -> str:
    if exact_equal(reviewed, rerun):
        return "exact"
    reviewed_set = value_set(reviewed)
    rerun_set = value_set(rerun)
    missing = reviewed_set - rerun_set
    extra = rerun_set - reviewed_set
    if missing and not extra:
        return "missing-core-etiology"
    if extra and not missing:
        return "extra-speculative-etiology"
    if missing and extra:
        if any("neoplastic" in value or "inflammatory" in value or "vascular" in value for value in missing | extra):
            return "wrong-mechanism"
        return "adjacent-broad-etiology"
    return "needs-review"


def grade_mostly_exact(reviewed: Any, rerun: Any) -> str:
    if exact_equal(reviewed, rerun):
        return "exact"
    reviewed_set = value_set(reviewed)
    rerun_set = value_set(rerun)
    missing = reviewed_set - rerun_set
    extra = rerun_set - reviewed_set
    if missing and not extra:
        return "missing"
    if extra and not missing:
        return "extra"
    return "unrelated"


def grade_field(field: str, reviewed: Any, rerun: Any, model: dict[str, Any]) -> str:
    if field == "expected_time_course":
        return grade_time_course(reviewed, rerun)
    if field == "anatomic_locations":
        return grade_anatomic_locations(reviewed, rerun)
    if field == "index_codes":
        return grade_index_codes(reviewed, rerun)
    if field == "applicable_modalities":
        return grade_modalities(reviewed, rerun, model)
    if field == "etiologies":
        return grade_etiologies(reviewed, rerun)
    if field in MOSTLY_EXACT_FIELDS:
        return grade_mostly_exact(reviewed, rerun)
    return "exact" if exact_equal(reviewed, rerun) else "needs-review"


def compact_value(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, list):
        if all(isinstance(item, dict) and "code" in item for item in value):
            return ", ".join(f"{item.get('system')}:{item.get('code')} {item.get('display')}" for item in value)
        return ", ".join(str(item) for item in value)
    if isinstance(value, dict):
        return json.dumps(comparable(value), sort_keys=True)
    return str(value)


def read_statuses(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def audit_flags_for(run_dir: Path, slug: str) -> list[dict[str, Any]]:
    path = run_dir / "audits" / f"{slug}.audit.json"
    if not path.exists():
        return []
    data = load_json(path)
    flags = data.get("flags")
    return flags if isinstance(flags, list) else []


def review_for(run_dir: Path, slug: str) -> dict[str, Any]:
    path = run_dir / "reviews" / f"{slug}.metadata-review.json"
    return load_json(path) if path.exists() else {}


def build_summary(args: argparse.Namespace) -> dict[str, Any]:
    manifest = load_json(args.manifest)
    coverage = parse_coverage(args.coverage)
    statuses = read_statuses(args.run_dir / "status.jsonl")
    statuses_by_slug = {slug_from_path(status.get("path", "")): status for status in statuses}
    mismatches: list[ComparedField] = []
    compared_fields = 0
    compared_items = 0
    audit_flags: dict[str, list[dict[str, Any]]] = {}
    assignment_warnings: dict[str, list[str]] = {}

    for item in manifest.get("files", []):
        slug = slug_from_path(item["path"])
        coverage_row = coverage.get(slug)
        if coverage_row is None:
            continue
        fields = fields_for_themes(coverage_row.themes)
        if not fields:
            continue
        reviewed_path = args.source_defs / f"{slug}.fm.json"
        rerun_path = args.run_dir / "before-after" / f"{slug}.after.json"
        if not reviewed_path.exists() or not rerun_path.exists():
            continue
        compared_items += 1
        reviewed = load_json(reviewed_path)
        rerun = load_json(rerun_path)
        review = review_for(args.run_dir, slug)
        confidence_by_field = review.get("field_confidence") if isinstance(review.get("field_confidence"), dict) else {}
        warnings = review.get("warnings") or statuses_by_slug.get(slug, {}).get("warnings") or []
        if warnings:
            assignment_warnings[slug] = [str(warning) for warning in warnings]
        flags = audit_flags_for(args.run_dir, slug)
        if flags:
            audit_flags[slug] = flags
        for field in fields:
            compared_fields += 1
            reviewed_value = reviewed.get(field)
            rerun_value = rerun.get(field)
            grade = grade_field(field, reviewed_value, rerun_value, rerun)
            if grade == "exact":
                continue
            mismatches.append(
                ComparedField(
                    item=slug,
                    field=field,
                    themes=coverage_row.themes,
                    grade=grade,
                    confidence=confidence_by_field.get(field),
                    reviewed=reviewed_value,
                    rerun=rerun_value,
                    concern=coverage_row.concern,
                )
            )

    status_counts = Counter(str(status.get("status") or "missing") for status in statuses)
    field_counts = Counter(mismatch.field for mismatch in mismatches)
    item_counts = Counter(mismatch.item for mismatch in mismatches)
    theme_counts: Counter[str] = Counter()
    grade_counts = Counter(mismatch.grade for mismatch in mismatches)
    confidence_counts = Counter(str(mismatch.confidence or "missing") for mismatch in mismatches)
    for mismatch in mismatches:
        for theme in mismatch.themes:
            theme_counts[theme] += 1

    return {
        "inputs": {
            "manifest": display_path(args.manifest),
            "run_dir": display_path(args.run_dir),
            "source_defs": display_path(args.source_defs),
            "coverage": display_path(args.coverage),
        },
        "records_compared": compared_items,
        "fields_compared": compared_fields,
        "batch_status_counts": dict(sorted(status_counts.items())),
        "assignment_warning_count": sum(len(warnings) for warnings in assignment_warnings.values()),
        "assignment_warnings": assignment_warnings,
        "deterministic_audit_flag_count": sum(len(flags) for flags in audit_flags.values()),
        "deterministic_audit_flags": audit_flags,
        "mismatch_count": len(mismatches),
        "records_with_mismatch": len(item_counts),
        "mismatch_counts_by_field": dict(sorted(field_counts.items())),
        "mismatch_counts_by_item": dict(sorted(item_counts.items())),
        "mismatch_counts_by_theme": dict(sorted(theme_counts.items())),
        "mismatch_counts_by_grade": dict(sorted(grade_counts.items())),
        "mismatch_counts_by_confidence": dict(sorted(confidence_counts.items())),
        "mismatches": [
            {
                "item": mismatch.item,
                "field": mismatch.field,
                "themes": mismatch.themes,
                "grade": mismatch.grade,
                "confidence": mismatch.confidence,
                "reviewed": mismatch.reviewed,
                "rerun": mismatch.rerun,
                "reviewer_concern": mismatch.concern,
            }
            for mismatch in mismatches
        ],
    }


def write_csv(summary: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["item", "field", "themes", "grade", "confidence", "reviewed", "rerun", "reviewer_concern"],
        )
        writer.writeheader()
        for mismatch in summary["mismatches"]:
            writer.writerow(
                {
                    "item": mismatch["item"],
                    "field": mismatch["field"],
                    "themes": ", ".join(mismatch["themes"]),
                    "grade": mismatch["grade"],
                    "confidence": mismatch["confidence"] or "",
                    "reviewed": compact_value(mismatch["reviewed"]),
                    "rerun": compact_value(mismatch["rerun"]),
                    "reviewer_concern": mismatch["reviewer_concern"],
                }
            )


def write_markdown(summary: dict[str, Any], path: Path, csv_path: Path, json_path: Path) -> None:
    lines = [
        "# Metadata Enrichment Clean-Input Graded Comparison",
        "",
        "Status: Active",
        "Date: 2026-05-05",
        "",
        "## Purpose",
        "",
        "Compare the clean-input rerun against the reviewed source corrections using field-aware grades",
        "rather than raw exact equality alone. This is triage input for metadata-enrichment tool",
        "hardening; it is not approval to run the broader corpus.",
        "",
        "## Inputs and Outputs",
        "",
        f"- Manifest: `{summary['inputs']['manifest']}`",
        f"- Rerun directory: `{summary['inputs']['run_dir']}`",
        f"- Reviewed source defs: `{summary['inputs']['source_defs']}`",
        f"- Coverage matrix: `{summary['inputs']['coverage']}`",
        f"- Machine JSON: `{display_path(json_path)}`",
        f"- Mismatch table CSV: `{display_path(csv_path)}`",
        "",
        "## Summary",
        "",
        f"- Records compared: {summary['records_compared']}",
        f"- Fields compared: {summary['fields_compared']}",
        f"- Mismatched reviewed fields: {summary['mismatch_count']}",
        f"- Records with at least one mismatch: {summary['records_with_mismatch']}",
        f"- Assignment warnings: {summary['assignment_warning_count']}",
        f"- Deterministic audit flags: {summary['deterministic_audit_flag_count']}",
        "",
        "Batch status counts:",
        "",
    ]
    for status, count in summary["batch_status_counts"].items():
        lines.append(f"- `{status}`: {count}")
    lines.extend(["", "Mismatch counts by field:", ""])
    for field, count in summary["mismatch_counts_by_field"].items():
        lines.append(f"- `{field}`: {count}")
    lines.extend(["", "Mismatch counts by grade:", ""])
    for grade, count in summary["mismatch_counts_by_grade"].items():
        lines.append(f"- `{grade}`: {count}")
    lines.extend(["", "Mismatch counts by theme:", ""])
    for theme, count in summary["mismatch_counts_by_theme"].items():
        lines.append(f"- `{theme}`: {count}")
    lines.extend(["", "## Deterministic Audit Flags", ""])
    if summary["deterministic_audit_flags"]:
        for item, flags in summary["deterministic_audit_flags"].items():
            lines.append(f"- `{item}`: {len(flags)} flags")
    else:
        lines.append("- None")
    lines.extend(
        [
            "",
            "## Highest-Volume Items",
            "",
            "| Item | Mismatches |",
            "| --- | ---: |",
        ]
    )
    for item, count in sorted(
        summary["mismatch_counts_by_item"].items(),
        key=lambda pair: (-pair[1], pair[0]),
    )[:20]:
        lines.append(f"| `{markdown_escape(item)}` | {count} |")
    lines.extend(
        [
            "",
            "## Mismatch Table",
            "",
            "| Item | Field | Grade | Confidence | Reviewed | Rerun |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for mismatch in summary["mismatches"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{markdown_escape(mismatch['item'])}`",
                    f"`{markdown_escape(mismatch['field'])}`",
                    f"`{markdown_escape(mismatch['grade'])}`",
                    markdown_escape(mismatch["confidence"] or "missing"),
                    markdown_escape(compact_value(mismatch["reviewed"])),
                    markdown_escape(compact_value(mismatch["rerun"])),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Readiness Implication",
            "",
            "The clean-input rerun still has graded mismatches that require disposition before the broader",
            "corpus run. The CSV table is the working triage surface for deciding which mismatches are tool",
            "errors, reviewer-preferred judgments, defensible alternatives, source-data blocks, or comparison",
            "artifacts.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--run-dir", type=Path, default=DEFAULT_RUN_DIR)
    parser.add_argument("--source-defs", type=Path, default=DEFAULT_SOURCE_DEFS)
    parser.add_argument("--coverage", type=Path, default=DEFAULT_COVERAGE)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--markdown", type=Path, default=DEFAULT_MARKDOWN)
    args = parser.parse_args()

    summary = build_summary(args)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.output_dir / "metadata-clean-rerun-graded-comparison.json"
    csv_path = args.output_dir / "metadata-clean-rerun-mismatches.csv"
    json_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_csv(summary, csv_path)
    write_markdown(summary, args.markdown, csv_path, json_path)
    print(f"Wrote {display_path(json_path)}")
    print(f"Wrote {display_path(csv_path)}")
    print(f"Wrote {display_path(args.markdown)}")
    print(f"Compared {summary['records_compared']} records; mismatches={summary['mismatch_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
