"""Generate review markdown files for CDEStaging finding models."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from findingmodel.common import model_file_name

TRAILING_BREAK = "  "


def change_from_prior_values(model: dict) -> str:
    for attr in model.get("attributes", []):
        if attr.get("name", "").lower() in ("change from prior", "change_from_prior"):
            if attr.get("type") == "choice":
                return ", ".join(v.get("name", "") for v in attr.get("values", []))
    return "(not found)"


def source_type_for_stem(stem: str, cdestaging_dir: Path) -> tuple[str, str]:
    candidates = [
        cdestaging_dir / f"{stem}.json",
        cdestaging_dir / f"{stem}.md",
        cdestaging_dir / f"{stem.replace('_', '-')}.json",
        cdestaging_dir / f"{stem.replace('_', '-')}.md",
    ]
    for path in candidates:
        if path.exists():
            return path.name, path.suffix.lstrip(".")
    return "(unknown)", "unknown"


def resolve_matched_model_path(name: str, repo_root: Path) -> str | None:
    filename = model_file_name(name)
    for defs_dir in (repo_root / "defs", repo_root / "defs" / "from_cdestaging_ct_chest"):
        candidate = defs_dir / filename
        if candidate.exists():
            try:
                return candidate.relative_to(repo_root).as_posix()
            except ValueError:
                return candidate.as_posix()
    return None


def build_new_model_entry(
    model_path: Path,
    model: dict,
    *,
    cdestaging_dir: Path,
    repo_root: Path,
) -> str:
    try:
        display_path = model_path.relative_to(repo_root).as_posix()
    except ValueError:
        display_path = model_path.as_posix()

    stem = model_path.stem.replace(".fm", "")
    source_name, source_type = source_type_for_stem(stem, cdestaging_dir)
    synonyms = model.get("synonyms") or []
    synonym_text = ", ".join(synonyms) if synonyms else "(none)"
    locations = model.get("anatomic_locations") or []
    location_text = str(len(locations)) if locations else "0 (or skipped)"

    body = [
        f"### {model.get('name', stem)}",
        "",
        f"**Entry type:** new model{TRAILING_BREAK}",
        f"**Source file:** `{display_path}`{TRAILING_BREAK}",
        f"**CDEStaging source:** `{source_name}` (`{source_type}`){TRAILING_BREAK}",
        f"**ID:** `{model.get('oifm_id', '')}`{TRAILING_BREAK}",
        f"**Description:** {model.get('description', '')}{TRAILING_BREAK}",
        f"**Synonyms:** {synonym_text}{TRAILING_BREAK}",
        f"**Change from prior:** {change_from_prior_values(model)}{TRAILING_BREAK}",
        f"**Attributes:** {len(model.get('attributes', []))}{TRAILING_BREAK}",
        f"**Anatomic locations:** {location_text}",
        "",
        "**Assessment:** Looks reasonable as written; confirm acceptable.",
        "",
        "**Response:** ",
    ]
    return "\n".join(body)


def build_existing_match_entry(
    record: dict[str, Any],
    *,
    cdestaging_dir: Path,
    repo_root: Path,
) -> str:
    stem = record["stem"]
    source_name, source_type = source_type_for_stem(stem, cdestaging_dir)
    matched_name = record.get("matched_name") or "(unknown)"
    matched_id = record.get("matched_oifm_id") or ""
    searches = ", ".join(f"`{q}`" for q in record.get("search_targets", []))
    matched_path = resolve_matched_model_path(matched_name, repo_root) if matched_name != "(unknown)" else None

    description = ""
    synonyms: list[str] = []
    change_from_prior = "(see matched model)"
    for candidate in record.get("candidates", []):
        if candidate.get("oifm_id") == matched_id:
            description = candidate.get("description") or ""
            break
    if matched_path:
        try:
            model = json.loads((repo_root / matched_path).read_text(encoding="utf-8"))
            description = model.get("description") or description
            synonyms = model.get("synonyms") or []
            change_from_prior = change_from_prior_values(model)
        except (OSError, json.JSONDecodeError):
            pass

    synonym_text = ", ".join(synonyms) if synonyms else "(none)"
    matched_file_line = (
        f"**Matched model file:** `{matched_path}`{TRAILING_BREAK}"
        if matched_path
        else f"**Matched model file:** (not in local defs){TRAILING_BREAK}"
    )

    body = [
        f"### {record.get('incoming_name', stem)} (existing match)",
        "",
        f"**Entry type:** existing match{TRAILING_BREAK}",
        f"**CDEStaging source:** `{source_name}` (`{source_type}`){TRAILING_BREAK}",
        f"**Triage decision:** `{record.get('decision', '')}`{TRAILING_BREAK}",
        f"**Search targets:** {searches or '(none)'}{TRAILING_BREAK}",
        f"**Matched ID:** `{matched_id}`{TRAILING_BREAK}",
        f"**Matched name:** {matched_name}{TRAILING_BREAK}",
        matched_file_line,
        f"**Description:** {description}{TRAILING_BREAK}",
        f"**Synonyms:** {synonym_text}{TRAILING_BREAK}",
        f"**Change from prior:** {change_from_prior}",
        "",
        "**Assessment:** DuckDB triage linked this CDEStaging source to an existing model; "
        "confirm the mapping is correct (no new model was created).",
        "",
        "**Response:** ",
    ]
    return "\n".join(body)


def build_skipped_entry(record: dict[str, Any], *, cdestaging_dir: Path) -> str:
    stem = record["stem"]
    source_name, source_type = source_type_for_stem(stem, cdestaging_dir)
    searches = ", ".join(f"`{q}`" for q in record.get("search_targets", []))

    body = [
        f"### {record.get('incoming_name', stem)} (skipped)",
        "",
        f"**Entry type:** skipped{TRAILING_BREAK}",
        f"**CDEStaging source:** `{source_name}` (`{source_type}`){TRAILING_BREAK}",
        f"**Triage decision:** `{record.get('decision', '')}`{TRAILING_BREAK}",
        f"**Search targets:** {searches or '(none)'}{TRAILING_BREAK}",
        f"**Reason:** {record.get('reason', '')}",
        "",
        "**Assessment:** Convert skipped per triage decision; confirm skip is acceptable.",
        "",
        "**Response:** ",
    ]
    return "\n".join(body)


def build_entry(
    model_path: Path,
    model: dict,
    *,
    cdestaging_dir: Path,
    repo_root: Path,
) -> str:
    return build_new_model_entry(
        model_path, model, cdestaging_dir=cdestaging_dir, repo_root=repo_root
    )


def generate_review_file(
    label: str,
    model_paths: list[Path],
    output_path: Path,
    *,
    cdestaging_dir: Path,
    repo_root: Path,
    triage_file: Path | None = None,
) -> None:
    entries: list[str] = []
    new_count = 0
    existing_count = 0
    skipped_count = 0

    triage_stems_with_models: set[str] = set()
    for model_path in model_paths:
        model = json.loads(model_path.read_text(encoding="utf-8"))
        stem = model_path.stem.replace(".fm", "")
        triage_stems_with_models.add(stem)
        entries.append(
            build_new_model_entry(
                model_path, model, cdestaging_dir=cdestaging_dir, repo_root=repo_root
            )
        )
        new_count += 1

    if triage_file is not None:
        triage_data = json.loads(triage_file.read_text(encoding="utf-8"))
        for record in triage_data.get("records", []):
            decision = record.get("decision")
            stem = record.get("stem", "")
            if stem in triage_stems_with_models:
                continue
            if decision == "exact_match":
                entries.append(
                    build_existing_match_entry(
                        record, cdestaging_dir=cdestaging_dir, repo_root=repo_root
                    )
                )
                existing_count += 1
            elif decision in {"user_skip", "ambiguous"}:
                entries.append(build_skipped_entry(record, cdestaging_dir=cdestaging_dir))
                skipped_count += 1

    total = new_count + existing_count + skipped_count
    preamble = (
        f"# Review: {label}\n\n"
        f"{total} entries to review ({new_count} new, {existing_count} existing matches, "
        f"{skipped_count} skipped). For each, check the mapping or new model metadata. "
        "Add your response below each entry."
    )
    content = preamble + "\n\n---\n\n" + "\n\n---\n\n".join(entries) + "\n"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate CDEStaging review markdown for TUI")
    parser.add_argument("--label", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("models", nargs="*")
    parser.add_argument("--cdestaging-dir", default="../CDEStaging/definitions/hood_CT_chest")
    parser.add_argument(
        "--triage-file",
        default=None,
        help="Triage JSON report for existing-match and skipped entries",
    )
    args = parser.parse_args()

    model_paths = [Path(p) for p in args.models]
    triage_path = Path(args.triage_file) if args.triage_file else None
    generate_review_file(
        args.label,
        model_paths,
        Path(args.output),
        cdestaging_dir=Path(args.cdestaging_dir),
        repo_root=Path.cwd(),
        triage_file=triage_path,
    )
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
