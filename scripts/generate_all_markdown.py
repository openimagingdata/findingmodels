import subprocess
from findingmodel import FindingModelFull
from pathlib import Path


def main():
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    defs_dir = project_root / "defs"
    output_dir = project_root / "text"
    output_dir.mkdir(parents=True, exist_ok=True)

    for json_path in sorted(defs_dir.glob("*.fm.json")):
        fm = FindingModelFull.model_validate_json(json_path.read_text())
        markdown = fm.as_markdown()
        name = json_path.name[: -len(".fm.json")]
        out_file = output_dir / f"{name}.md"
        out_file.write_text(markdown, encoding="utf-8")

    # Add the generated file to git
    for md_file in output_dir.glob("*.md"):
        subprocess.run(["git", "add", str(md_file)], check=True)


if __name__ == "__main__":
    main()
