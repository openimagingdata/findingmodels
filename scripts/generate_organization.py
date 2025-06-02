from findingmodel.contributor import Organization
from pathlib import Path


def main():
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    output_file = project_root / "organization.jsonl"
    org = Organization(name="Example Organization", code="OIDM")
    org.save_jsonl(output_file)


if __name__ == "__main__":
    main()
