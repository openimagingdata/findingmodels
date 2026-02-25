"""File I/O operations for Hood definition loading."""

import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple

SUPPORTED_ENCODINGS = ["utf-8", "latin-1", "cp1252"]


def should_process_file(file_path: Path, all_files: List[Path]) -> bool:
    """Determine if a file should be processed, some files have MD and JSON versions.
    
    Args:
        file_path: Path to the file to check
        all_files: List of all file paths in the directory
        
    Returns:
        True if file should be processed, False otherwise
    """
    if file_path.suffix == ".json":
        # Skip .cde.json files
        if file_path.name.endswith(".cde.json"):
            return False
        # Process JSON files (they take priority)
        return True
    
    elif file_path.suffix == ".md":
        # Only process MD if no corresponding JSON exists
        json_path = file_path.with_suffix(".json")
        if json_path in all_files:
            return False  # Skip MD, JSON will be processed instead
        return True  # Process MD, no JSON exists
    
    return False


async def load_definition(file_path: Path) -> Tuple[Optional[Dict], Optional[str], str]:
    """Load and parse a definition file (MD or JSON).
    
    Args:
        file_path: Path to the definition file
        
    Returns:
        Tuple of (data_dict, markdown_content, file_type)
        - data_dict: Parsed JSON data (if JSON) or None (if MD)
        - markdown_content: Markdown content (if MD) or None (if JSON)
        - file_type: "json" or "md"
    """
    file_type = file_path.suffix[1:]  # Remove the dot
    
    if file_type == "json":
        # Try multiple encodings to handle Unicode issues
        for encoding in SUPPORTED_ENCODINGS:
            try:
                with open(file_path, "r", encoding=encoding) as f:
                    data = json.load(f)
                    return data, None, "json"
            except (UnicodeDecodeError, json.JSONDecodeError):
                continue
        raise ValueError(f"Failed to load JSON file {file_path} with any encoding")
    
    elif file_type == "md":
        # Read markdown content
        for encoding in SUPPORTED_ENCODINGS:
            try:
                with open(file_path, "r", encoding=encoding) as f:
                    content = f.read()
                    return None, content, "md"
            except UnicodeDecodeError:
                continue
        raise ValueError(f"Failed to load Markdown file {file_path} with any encoding")
    
    else:
        raise ValueError(f"Unsupported file type: {file_type}")
