import subprocess
from findingmodel.contributor import Person
from pathlib import Path


def main():
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    output_file = project_root / "peoples.jsonl"

    default_persons = [
        {
            "github_username": "talkasab",
            "email": "tarik@alkasab.org",
            "name": "Tarik Alkasab, MD, PhD",
            "organization_code": "MGB",
        },
        {
            "github_username": "HeatherChase",
            "email": "heatherchase@microsoft.com",
            "name": "Heather Chase",
            "organization_code": "MSFT",
            "url": "https://www.linkedin.com/in/heatherwalkerchase/",
        },
        {
            "github_username": "hoodcm",
            "email": "chood@mgh.harvard.edu",
            "name": "C. Michael Hood, MD",
            "organization_code": "MGB",
        },
    ]

    for person_data in default_persons:
        person = Person(
            github_username=person_data["github_username"],
            email=person_data["email"],
            name=person_data["name"],
            organization_code=person_data.get("organization_code"),
            url=person_data.get("url"),
        )
        person.save_jsonl(output_file)

    # Add the generated file to git
    subprocess.run(["git", "add", output_file], check=True)


if __name__ == "__main__":
    main()
