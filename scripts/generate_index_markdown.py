import subprocess
from findingmodel.index import Index
from pathlib import Path


def main():
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    output_file = project_root / "index.md"
    index = Index(base_directory=project_root)
    markdown = to_markdown(index)
    output_file.write_text(markdown)

    # Add the generated file to git
    subprocess.run(["git", "add", output_file], check=True)


def to_markdown(self) -> str:
    """Converts the index to a Markdown table."""
    header = f"""
# Finding Model Index

{self.__len__()} entries

| ID | Name | Synonyms | Tags | Contributors | Attributes |\n"""
    separator = "|----|------|----------|------|--------------|------------|\n"
    rows = []
    for entry in sorted(self.entries, key=lambda e: e.name.casefold()):
        md_filename = entry.filename.replace(".fm.json", ".md")
        entry_name_with_links = (
            f"[{entry.name}](text/{md_filename}) [JSON](defs/{entry.filename})"
        )
        row = f"| {entry.oifm_id} | {entry_name_with_links} | {', '.join(entry.synonyms or [])} | {', '.join(entry.tags or [])} | {', '.join(entry.contributors or [])} | {', '.join(attr.name for attr in entry.attributes)} |\n"
        rows.append(row)
    return header + separator + "".join(rows)


if __name__ == "__main__":
    main()
