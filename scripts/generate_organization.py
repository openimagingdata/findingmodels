import subprocess
from findingmodel.contributor import Organization
from pathlib import Path


def main():
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    output_file = project_root / "organizations.jsonl"

    # Define the default organization data
    default_organizations = [
        {
            "name": "Microsoft",
            "code": "MSFT",
            "url": "https://microsoft.com/",
        },
        {"name": "Mass General Brigham", "code": "MGB", "url": "https://mgb.org/"},
    ]

    for org_data in default_organizations:
        org = Organization(
            name=org_data["name"], code=org_data["code"], url=org_data["url"]
        )
        org.save_jsonl(output_file)

    # Add the generated file to git
    subprocess.run(["git", "add", output_file], check=True)


if __name__ == "__main__":
    main()
