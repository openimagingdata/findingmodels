"""DuckDB triage helpers for CDEStaging CT chest batch conversion."""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Literal

from findingmodel import Index

from findingmodels.cdestaging_ct_chest.loaders import dedupe_input_files, normalized_stem, should_process_file

Decision = Literal["exact_match", "no_match", "ambiguous", "convert", "user_skip"]

SKIP_DECISIONS: frozenset[str] = frozenset({"exact_match", "user_skip"})


@dataclass
class TriageCandidate:
    oifm_id: str
    name: str
    description: str | None = None
    tags: list[str] | None = None
    query: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {k: v for k, v in asdict(self).items() if v is not None}


@dataclass
class TriageRecord:
    stem: str
    source_path: str
    incoming_name: str
    search_targets: list[str]
    decision: Decision
    matched_oifm_id: str | None = None
    matched_name: str | None = None
    candidates: list[TriageCandidate] = field(default_factory=list)
    reason: str = ""

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["candidates"] = [c.to_dict() if isinstance(c, TriageCandidate) else c for c in self.candidates]
        return data


@dataclass
class TriageReport:
    generated_at: str
    input_dir: str
    offset: int
    limit: int | None
    chunk_duplicate_stems: list[str] = field(default_factory=list)
    records: list[TriageRecord] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "generated_at": self.generated_at,
            "input_dir": self.input_dir,
            "offset": self.offset,
            "limit": self.limit,
            "chunk_duplicate_stems": self.chunk_duplicate_stems,
            "records": [r.to_dict() for r in self.records],
            "summary": summarize_report(self.records),
        }


def stem_to_display_name(stem: str) -> str:
    """Turn a normalized stem into a human-readable finding label."""
    return stem.replace("_", " ").strip()


def generate_search_targets(stem: str, incoming_name: str | None = None) -> list[str]:
    """Derive 2-3 complementary search targets for hybrid index lookup."""
    canonical = (incoming_name or stem_to_display_name(stem)).strip()
    targets: list[str] = []

    def add(value: str) -> None:
        cleaned = re.sub(r"\s+", " ", value).strip()
        if cleaned and cleaned.casefold() not in {t.casefold() for t in targets}:
            targets.append(cleaned)

    add(canonical)

    hyphen_variant = canonical.replace("_", "-")
    if hyphen_variant != canonical:
        add(hyphen_variant)

    words = [w for w in re.split(r"[\s_\-]+", canonical) if len(w) > 2]
    if len(words) >= 2:
        add(words[-1])
    elif len(words) == 1 and len(words[0]) > 6:
        add(words[0])

    return targets[:3]


def _normalize_label(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


def _labels_match(a: str, b: str) -> bool:
    return _normalize_label(a) == _normalize_label(b)


def _entry_matches_incoming(entry_name: str, incoming_name: str, stem: str) -> bool:
    if _labels_match(entry_name, incoming_name):
        return True
    if _labels_match(entry_name, stem_to_display_name(stem)):
        return True
    return _normalize_label(entry_name).replace(" ", "_") == stem.casefold()


def classify_candidates(
    incoming_name: str,
    stem: str,
    candidates: list[TriageCandidate],
) -> tuple[Decision, str | None, str | None, str]:
    """Heuristic pre-classification; agent may override ambiguous rows."""
    if not candidates:
        return "no_match", None, None, "No index candidates returned across search targets."

    exact_hits = [
        c
        for c in candidates
        if _entry_matches_incoming(c.name, incoming_name, stem)
    ]
    if len(exact_hits) == 1:
        hit = exact_hits[0]
        return (
            "exact_match",
            hit.oifm_id,
            hit.name,
            f"Exact name match on '{hit.name}' ({hit.oifm_id}).",
        )
    if len(exact_hits) > 1:
        ids = ", ".join(f"{c.name} ({c.oifm_id})" for c in exact_hits[:3])
        return "ambiguous", None, None, f"Multiple exact-name candidates: {ids}."

    top = candidates[:3]
    names = {_normalize_label(c.name) for c in top}
    if len(top) >= 2 and len(names) >= 2:
        return (
            "ambiguous",
            None,
            None,
            "Related candidates found; requires semantic judgment per search_and_triage.md.",
        )

    if len(top) == 1:
        only = top[0]
        return (
            "ambiguous",
            None,
            None,
            f"Single related candidate '{only.name}' ({only.oifm_id}); confirm exact match or create new.",
        )

    return "no_match", None, None, "Candidates discarded as non-matches."


def detect_chunk_duplicate_stems(records: list[TriageRecord]) -> list[str]:
    """Flag stems whose incoming names normalize to the same label within a chunk."""
    seen: dict[str, str] = {}
    duplicates: list[str] = []
    for record in records:
        key = _normalize_label(record.incoming_name)
        prior = seen.get(key)
        if prior is None:
            seen[key] = record.stem
        elif prior != record.stem and record.stem not in duplicates:
            duplicates.append(record.stem)
            if prior not in duplicates:
                duplicates.append(prior)
    return sorted(duplicates)


def summarize_report(records: list[TriageRecord]) -> dict[str, int]:
    counts = {"exact_match": 0, "no_match": 0, "ambiguous": 0, "convert": 0, "user_skip": 0}
    for record in records:
        counts[record.decision] = counts.get(record.decision, 0) + 1
    return counts


def load_triage_file(path: Path) -> dict[str, Any]:
    """Load a triage JSON report."""
    return json.loads(path.read_text(encoding="utf-8"))


def stems_to_skip(triage_data: dict[str, Any]) -> set[str]:
    """Return normalized stems that should not be converted."""
    skip: set[str] = set()
    for record in triage_data.get("records", []):
        if record.get("decision") in SKIP_DECISIONS:
            skip.add(record["stem"])
    return skip


def save_triage_report(report: TriageReport, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report.to_dict(), indent=2), encoding="utf-8")


async def incoming_name_for_source(file_path: Path) -> str:
    from findingmodels.cdestaging_ct_chest.loaders import load_definition

    data, _markdown, file_type = await load_definition(file_path)
    if file_type == "json" and data:
        return str(data.get("finding_name") or data.get("name") or stem_to_display_name(normalized_stem(file_path)))
    return stem_to_display_name(normalized_stem(file_path))


async def triage_source(
    file_path: Path,
    index: Index,
    *,
    search_limit: int = 2,
) -> TriageRecord:
    stem = normalized_stem(file_path)
    incoming_name = await incoming_name_for_source(file_path)
    search_targets = generate_search_targets(stem, incoming_name)

    pooled: dict[str, TriageCandidate] = {}
    for query in search_targets:
        results = await index.search(query, limit=search_limit)
        for entry in results:
            if entry.oifm_id not in pooled:
                pooled[entry.oifm_id] = TriageCandidate(
                    oifm_id=entry.oifm_id,
                    name=entry.name,
                    description=entry.description,
                    tags=list(entry.tags or []),
                    query=query,
                )

    candidates = list(pooled.values())
    decision, matched_oifm_id, matched_name, reason = classify_candidates(
        incoming_name, stem, candidates
    )

    return TriageRecord(
        stem=stem,
        source_path=str(file_path),
        incoming_name=incoming_name,
        search_targets=search_targets,
        decision=decision,
        matched_oifm_id=matched_oifm_id,
        matched_name=matched_name,
        candidates=candidates,
        reason=reason,
    )


def list_chunk_sources(
    input_dir: Path,
    *,
    offset: int = 0,
    limit: int | None = None,
) -> list[Path]:
    all_files = [f for f in input_dir.glob("*") if f.is_file()]
    eligible = [f for f in all_files if should_process_file(f, all_files)]
    files = dedupe_input_files(eligible)
    if offset:
        files = files[offset:]
    if limit is not None:
        files = files[:limit]
    return files


async def triage_chunk(
    input_dir: Path,
    *,
    offset: int = 0,
    limit: int | None = None,
    db_path: str | Path | None = None,
    search_limit: int = 2,
) -> TriageReport:
    files = list_chunk_sources(input_dir, offset=offset, limit=limit)
    records: list[TriageRecord] = []

    async with Index(db_path=db_path) as index:
        for file_path in files:
            records.append(
                await triage_source(file_path, index, search_limit=search_limit)
            )

    duplicates = detect_chunk_duplicate_stems(records)
    return TriageReport(
        generated_at=datetime.now(timezone.utc).isoformat(timespec="seconds"),
        input_dir=str(input_dir),
        offset=offset,
        limit=limit,
        chunk_duplicate_stems=duplicates,
        records=records,
    )
