"""File I/O for CDEStaging CT chest definition loading."""

import json
import logging
from pathlib import Path
from typing import Dict, List, Optional, Tuple

logger = logging.getLogger(__name__)

SUPPORTED_ENCODINGS = ["utf-8", "latin-1", "cp1252"]


def normalized_stem(file_path: Path) -> str:
    """Normalize a source filename stem for output collision checks."""
    return file_path.stem.replace("-", "_").lower()


def prefer_source(existing: Path, candidate: Path) -> Path:
    """Pick one source when two files map to the same normalized stem."""
    if existing.suffix == ".md" and candidate.suffix == ".json":
        return candidate
    if existing.suffix == ".json" and candidate.suffix == ".md":
        return existing
    if candidate.stem.count("-") < existing.stem.count("-"):
        return candidate
    if existing.stem.count("-") < candidate.stem.count("-"):
        return existing
    return existing


def dedupe_input_files(files: List[Path]) -> List[Path]:
    """Drop sources that would write the same output .fm.json (prefer JSON, underscore stems)."""
    chosen: dict[str, Path] = {}
    skipped: list[tuple[Path, Path]] = []

    for file_path in sorted(files):
        stem = normalized_stem(file_path)
        prior = chosen.get(stem)
        if prior is None:
            chosen[stem] = file_path
            continue
        kept = prefer_source(prior, file_path)
        dropped = file_path if kept == prior else prior
        chosen[stem] = kept
        skipped.append((dropped, kept))

    for dropped, kept in skipped:
        logger.warning(
            "Skipping duplicate source %s (same output stem as %s; kept %s)",
            dropped.name,
            normalized_stem(kept),
            kept.name,
        )

    return sorted(chosen.values())


def should_process_file(file_path: Path, all_files: List[Path]) -> bool:
    """Determine if a file should be processed when MD and JSON versions coexist."""
    if file_path.suffix == ".json":
        if file_path.name.endswith(".cde.json"):
            return False
        return True

    if file_path.suffix == ".md":
        json_path = file_path.with_suffix(".json")
        if json_path in all_files:
            return False
        return True

    return False


async def load_definition(file_path: Path) -> Tuple[Optional[Dict], Optional[str], str]:
    """Load and parse a CDEStaging CT chest definition file (MD or JSON)."""
    file_type = file_path.suffix[1:]

    if file_type == "json":
        for encoding in SUPPORTED_ENCODINGS:
            try:
                with open(file_path, "r", encoding=encoding) as f:
                    data = json.load(f)
                    return data, None, "json"
            except (UnicodeDecodeError, json.JSONDecodeError):
                continue
        raise ValueError(f"Failed to load JSON file {file_path} with any encoding")

    if file_type == "md":
        for encoding in SUPPORTED_ENCODINGS:
            try:
                with open(file_path, "r", encoding=encoding) as f:
                    content = f.read()
                    return None, content, "md"
            except UnicodeDecodeError:
                continue
        raise ValueError(f"Failed to load Markdown file {file_path} with any encoding")

    raise ValueError(f"Unsupported file type: {file_type}")
