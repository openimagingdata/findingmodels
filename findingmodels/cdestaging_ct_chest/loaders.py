"""File I/O for CDEStaging CT chest definition loading."""

import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple

SUPPORTED_ENCODINGS = ["utf-8", "latin-1", "cp1252"]


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
