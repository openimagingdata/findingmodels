# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Generate the pilot feedback-to-tooling coverage worksheet."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INGEST = REPO_ROOT / ".metadata-runs" / "pilot-review-ingest.json"
DEFAULT_RESOLUTION = REPO_ROOT / "docs" / "plans" / "metadata-enrichment-phase-5-feedback-resolution-2026-05-01.md"
DEFAULT_OUTPUT = REPO_ROOT / "docs" / "plans" / "metadata-enrichment-feedback-tooling-coverage-2026-05-05.md"


@dataclass(frozen=True)
class Resolution:
    disposition: str
    note: str


def normalize_cell(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace("<br>", " ")).strip()


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def parse_resolution_table(path: Path) -> dict[str, Resolution]:
    rows: dict[str, Resolution] = {}
    in_table = False
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line.startswith("| Item | Themes | Reviewer note | Planned disposition | Resolution note |"):
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
        if len(cells) < 5:
            continue
        rows[cells[0]] = Resolution(disposition=cells[3], note=cells[4])
    return rows


def themes_for(comment: str) -> list[str]:
    text = comment.lower()
    themes: list[str] = []
    if any(
        word in text
        for word in [
            "time course",
            "timecourse",
            "duration",
            "permanent",
            "stable",
            "progressive",
            "resolve",
            "resolving",
            "weeks",
            "months",
            "years",
        ]
    ):
        themes.append("time course")
    if any(
        word in text
        for word in [
            "anatomic",
            "location",
            "locations",
            "body region",
            "region",
            "spine",
            "joint",
            "kidney",
            "lung",
            "chest",
            "neck",
            "axilla",
            "uterus",
            "skull",
            "first digit",
            "thumb",
            "hand",
        ]
    ):
        themes.append("anatomy")
    if any(word in text for word in ["index code", "index codes", "snomed", "loinc", "radlex", "radelement"]):
        themes.append("ontology/index code")
    if "modality" in text or "ultrasound" in text or "x-ray" in text or "lucency" in text or re.search(
        r"\b(ct|mr|mri|us)\b", text
    ):
        themes.append("modality")
    if any(word in text for word in ["subspecial", " sq", "mk", " oi", "gu imaging"]):
        themes.append("subspecialty")
    if any(word in text for word in ["age", "ages", "adolesc", "adult", "elderly", "newborn", "infant", "child", "neonate"]):
        themes.append("age")
    if any(word in text for word in ["sex", "sex-neutral", "neutral"]):
        themes.append("sex")
    if any(word in text for word in ["etiolog", "vascular", "inflammatory", "infectious", "ischemic", "mechanical", "neoplastic", "post-infectious", "post-exposure", "post-treatment"]):
        themes.append("etiology")
    if any(word in text for word in ["type should", "assessment", "measurement", "not even an imaging finding"]):
        themes.append("entity type/scope")
    return themes or ["general metadata quality"]


def categories_for(themes: list[str], comment: str) -> list[str]:
    text = comment.lower()
    categories: list[str] = []
    if any(theme in themes for theme in ["time course", "age", "sex", "etiology", "modality", "subspecialty", "entity type/scope"]):
        categories.append("prompt semantics")
    if "anatomy" in themes:
        categories.append("anatomy candidate generation")
        categories.append("deterministic audit")
    if "ontology/index code" in themes:
        categories.append("ontology/index-code selection")
        categories.append("ontology evidence checks")
    if any(theme in themes for theme in ["modality", "subspecialty", "sex", "entity type/scope"]):
        categories.append("deterministic audit")
    if any(term in text for term in ["do we not", "do we really not", "don't we have", "radelement", "dropped", "hippocampus", "thyroid bed", "renal collecting system", "first digit", "si joints", "axilla"]):
        categories.append("terminology/source-data gap")
    return sorted(dict.fromkeys(categories))


def coverage_state(resolution: Resolution, themes: list[str]) -> str:
    disposition = resolution.disposition.lower()
    note = resolution.note.lower()
    if disposition.startswith("deferred"):
        return "deferred with rationale"
    if disposition.startswith("not applicable"):
        return "not applicable with rationale"
    if "verified in v3 targeted review" in note:
        return "targeted rerun evidence exists"
    if "model-validated and markdown regenerated" in note or "targeted json and markdown validated" in note:
        return "source corrected; needs clean-input tool evidence"
    if "already has" in note:
        return "source verified; needs coverage decision"
    if themes == ["general metadata quality"]:
        return "needs coverage classification"
    return "source corrected; needs clean-input tool evidence"


def required_action(state: str, themes: list[str], categories: list[str]) -> str:
    if state == "targeted rerun evidence exists":
        return "Retain as rerun evidence; add regression coverage if this theme remains high-volume."
    if state == "deferred with rationale":
        if "terminology/source-data gap" in categories:
            return "Track missing terminology/source-code gap; verify warning and fallback behavior in targeted rerun."
        return "Keep rationale explicit; exclude from readiness blocker unless the same pattern is automatable."
    if state == "not applicable with rationale":
        return "No enrichment-tool fix now; keep for later non-finding/deprecation review."
    if "ontology/index code" in themes:
        return "Add ontology exactness/evidence coverage and include in clean-input rerun."
    if "anatomy" in themes:
        return "Add anatomy candidate/auditor coverage and include in clean-input rerun."
    if any(theme in themes for theme in ["time course", "age", "sex", "etiology", "modality", "subspecialty", "entity type/scope"]):
        return "Add prompt or deterministic-check coverage and include in clean-input rerun."
    return "Classify manually before larger-run readiness decision."


def generate(ingest_path: Path, resolution_path: Path) -> str:
    ingest = json.loads(ingest_path.read_text(encoding="utf-8"))
    resolutions = parse_resolution_table(resolution_path)
    feedback = ingest["actionable_feedback"]
    lines = [
        "# Metadata Enrichment Feedback-to-Tooling Coverage",
        "",
        "Status: Initial coverage matrix generated from review ingestion and the feedback resolution worksheet.",
        "Date: 2026-05-05",
        "",
        "## Purpose",
        "",
        "Track whether each actionable pilot-review comment has been converted into reusable tooling",
        "coverage, not merely corrected in the reviewed source file. A larger corpus run should not be",
        "recommended while high-impact review themes remain source-corrected only.",
        "",
        "## Sources",
        "",
        f"- Review ingestion: `{ingest_path.relative_to(REPO_ROOT)}`",
        f"- Resolution worksheet: `{resolution_path.relative_to(REPO_ROOT)}`",
        "",
        "## Coverage States",
        "",
        "- `targeted rerun evidence exists`: the improved tool produced an acceptable output in the",
        "  targeted rerun and the reviewer approved it.",
        "- `source corrected; needs clean-input tool evidence`: the source record was fixed, but this",
        "  document does not yet prove the tool would make or flag the same correction from clean input.",
        "- `deferred with rationale`: the source file intentionally keeps a fallback or omits a correction",
        "  because terminology or source-code support is missing.",
        "- `not applicable with rationale`: no enrichment-tool change is expected for this item in this",
        "  pass.",
        "",
        "## Summary",
        "",
    ]
    states: dict[str, int] = {}
    theme_counts: dict[str, int] = {}
    rows: list[str] = []
    missing_resolution: list[str] = []
    for item in feedback:
        slug = item["item_id"]
        comment = normalize_cell(item["comment"])
        resolution = resolutions.get(slug)
        if resolution is None:
            missing_resolution.append(slug)
            resolution = Resolution("missing", "No resolution worksheet row found.")
        themes = themes_for(comment)
        categories = categories_for(themes, comment)
        state = coverage_state(resolution, themes)
        action = required_action(state, themes, categories)
        states[state] = states.get(state, 0) + 1
        for theme in themes:
            theme_counts[theme] = theme_counts.get(theme, 0) + 1
        rows.append(
            "| "
            + " | ".join(
                [
                    markdown_escape(slug),
                    markdown_escape(", ".join(themes)),
                    markdown_escape(", ".join(categories)),
                    markdown_escape(resolution.disposition),
                    markdown_escape(state),
                    markdown_escape(action),
                    markdown_escape(comment),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            f"- Actionable review notes: {len(feedback)}",
            "- Coverage state counts: "
            + ", ".join(f"{state}: {count}" for state, count in sorted(states.items())),
            "- Theme counts: " + ", ".join(f"{theme}: {count}" for theme, count in sorted(theme_counts.items())),
        ]
    )
    if missing_resolution:
        lines.append("- Missing worksheet rows: " + ", ".join(sorted(missing_resolution)))
    lines.extend(
        [
            "",
            "## Matrix",
            "",
            "| Item | Themes | Tooling area | Source disposition | Coverage state | Required tool/evidence action | Reviewer concern |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    lines.extend(rows)
    lines.extend(
        [
            "",
            "## Immediate Implications",
            "",
            "- Rows marked `source corrected; needs clean-input tool evidence` are the main remaining work.",
            "  They require either prompt/code/auditor/test changes or a documented decision that the lesson",
            "  is not suitable for automation.",
            "- Rows marked `targeted rerun evidence exists` are useful evidence, but high-volume themes should",
            "  still receive regression coverage so later prompt edits do not lose the behavior.",
            "- Deferred terminology/source-code rows should become explicit follow-up work, not silent",
            "  enrichment failures.",
            "- This matrix is an engineering readiness artifact. It is not a replacement for the HTML review",
            "  app when human review is required.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ingest", type=Path, default=DEFAULT_INGEST)
    parser.add_argument("--resolution", type=Path, default=DEFAULT_RESOLUTION)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    content = generate(args.ingest, args.resolution)
    args.output.write_text(content, encoding="utf-8")
    print(f"Wrote {args.output.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
