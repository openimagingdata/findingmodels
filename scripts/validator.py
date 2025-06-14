# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "findingmodel",
# ]
# ///

import json
from findingmodel import FindingModelFull
from findingmodel.common import model_file_name, normalize_name
from findingmodel.contributor import Person, Organization
from pathlib import Path

from pydantic_core import ValidationError

DEFS_DIR = Path(__file__).parent.parent / "defs"
TEXT_DIR = Path(__file__).parent.parent / "text"
INDEX_MARKDOWN_FILE = Path(__file__).parent.parent / "index.md"
IDS_FILE = Path(__file__).parent.parent / "ids.json"

def write_finding_model(model: FindingModelFull, filename: str | Path | None) -> None:
    """
    Write a FindingModelFull instance to the defs directory.

    Args:
        model (FindingModelFull): The finding model instance to write.
    """
    if filename is None:
        filename = DEFS_DIR / model_file_name(model.name)
    elif isinstance(filename, str):
        if not filename.endswith(".fm.json"):
            filename += ".fm.json"
        filename = DEFS_DIR / filename
    elif isinstance(filename, Path):
        if not filename.name.endswith(".fm.json"):
            filename = filename.with_suffix(".fm.json")
        if not filename.is_absolute():
            filename = DEFS_DIR / filename.name
    if not filename.exists():
        raise FileNotFoundError(f"File '{filename}' does not exist. Cannot write model.")
    existing_json = filename.read_text(encoding="utf-8")
    generated_json = model.model_dump_json(indent=2, exclude_none=True)
    if existing_json == generated_json:
        return
    filename.write_text(generated_json, encoding="utf-8")

def write_markdown(model: FindingModelFull, filename: str | Path | None = None) -> None:
    """
    Write the markdown representation of a FindingModelFull instance.

    Args:
        model (FindingModelFull): The finding model instance to write.
        filename (str | Path | None): The output filename. If None, defaults to the model name.
    """
    if filename is None:
        filename = TEXT_DIR / f"{normalize_name(model.name)}.md"
    elif isinstance(filename, str):
        if not filename.endswith(".md"):
            filename += ".md"
        filename = TEXT_DIR / filename
    elif isinstance(filename, Path):
        if not filename.name.endswith(".md"):
            filename = filename.with_suffix(".md")
        if not filename.is_absolute():
            filename = TEXT_DIR / filename.name

    markdown = model.as_markdown()
    existing_markdown = filename.read_text(encoding="utf-8") if filename.exists() else ""
    if existing_markdown == markdown:
        return
    filename.write_text(markdown, encoding="utf-8")

def markdown_table_row(model: FindingModelFull) -> str:
    cells: list[str] = []
    json_filename = model_file_name(model.name)
    md_filename = json_filename.replace(".fm.json", ".md")

    entry_name_with_links = (
            f"{model.name}<br/>[Text](text/{md_filename}) [JSON](defs/{json_filename})"
        )
    cells.append(model.oifm_id)
    cells.append(entry_name_with_links)
    cells.append(", ".join(model.synonyms or []))
    cells.append(", ".join(model.tags or []))
    if model.contributors is None:
        cells.append("")
    else:
        cont_strings = []
        for contributor in model.contributors:
            if isinstance(contributor, Person):
                cont_strings.append(contributor.name)
            elif isinstance(contributor, Organization):
                cont_strings.append(contributor.name)
        cells.append(", ".join(cont_strings))
    cells.append(", ".join(attr.name for attr in model.attributes))
    return "| " + " | ".join(cells) + " |"

def main() -> list[str]:
    """
    Main function to load all finding models from the defs directory and write their markdown representations.
    """
    TEXT_DIR.mkdir(parents=True, exist_ok=True)

    errors = []
    json_paths = sorted(DEFS_DIR.glob("*.fm.json"))
    # Use tqdm to show progress
    oifm_ids: dict[str,str] = {}
    attribute_ids: dict[str,tuple[str, str]] = {}
    table_rows: list[str] = []
    for json_path in json_paths:
        # Validate JSON file and create FindingModelFull instance
        try:
            model = FindingModelFull.model_validate_json(json_path.read_text(encoding="utf-8"))
        except ValidationError as e:
            errors.append(f"Error validating {json_path}: {e}")
            continue

        # Validate ID uniqueness
        if model.oifm_id in oifm_ids:
            errors.append(f"{json_path}: dup ID: {model.oifm_id} : {oifm_ids[model.oifm_id]}")
        oifm_ids[model.oifm_id] = json_path.name
        for attr in model.attributes:
            if attr.oifma_id in attribute_ids:
                errors.append(f"{json_path}: dup attribute ID: {attr.oifma_id} : {attribute_ids[attr.oifma_id]}")
            attribute_ids[attr.oifma_id] = (json_path.name, attr.name)

        # Write the model to JSON and markdown files
        write_markdown(model)
        write_finding_model(model, filename=json_path)
        
        # Append the markdown table row for the index
        table_rows.append(markdown_table_row(model))
    
    # If there are validation errors, print them
    if errors:
        return errors

    # Write the Markdown index file
    header = f"# Finding Model Index\n\n{len(table_rows)} entries\n\n| ID | Name | Synonyms | Tags | Contributors | Attributes |\n"
    separator = "|----|------|----------|------|--------------|------------|\n"
    index_markdown = header + separator + "\n".join(table_rows)
    INDEX_MARKDOWN_FILE.write_text(index_markdown, encoding="utf-8")

    # Write the IDs file
    ids_content = {
        "oifm_ids": oifm_ids,
        "attribute_ids": attribute_ids,
    }
    IDS_FILE.write_text(json.dumps(ids_content, ensure_ascii=True), encoding="utf-8")
    return []

if __name__ == "__main__":
    import sys
    import subprocess

    errors = main()
    if errors:
        print("Validation errors found:")
        for error in errors:
            print(f" - {error}")
        sys.exit(1)

    # Check if we should add generated files to git
    # This is useful when running as a pre-commit hook
    add_to_git = "--with-git-adds" in sys.argv
    
    if add_to_git:
        # Add generated/updated files to git staging area
        files_to_add = [
            "defs/",  # All JSON files in defs directory
            "text/",  # All markdown files in text directory
            "index.md",  # Main index file
            "ids.json",  # IDs tracking file
        ]
        
        try:
            # Add the files to git staging area
            subprocess.run(["git", "add"] + files_to_add, check=True, cwd=Path(__file__).parent.parent)
            print(f"Added generated files to git staging area: {', '.join(files_to_add)}")
        except subprocess.CalledProcessError as e:
            print(f"Warning: Failed to add files to git staging area: {e}")
            # Don't fail the pre-commit hook if git add fails
    
    print("Validation completed successfully.")

