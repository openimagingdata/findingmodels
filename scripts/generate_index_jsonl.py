import subprocess
from findingmodel.index import Index
from pathlib import Path


def main():
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    output_file = project_root / "index1.jsonl"
    index = Index(base_directory=project_root)
    index.populate_from_directory(project_root)
    index.export_to_jsonl(output_file)

    # Add the generated file to git
    subprocess.run(["git", "add", output_file], check=True)


if __name__ == "__main__":
    main()
