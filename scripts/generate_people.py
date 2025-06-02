from findingmodel.contributor import Person
from pathlib import Path


def main():
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    output_file = project_root / "people.jsonl"

    persons = [
        {
            "github_username": "johndoe",
            "email": "john.doe@example.com",
            "name": "John Doe",
            "organization_code": "OIDM",
        },
        {
            "github_username": "janedoe",
            "email": "jane.doe@example.com",
            "name": "Jane Doe",
            "organization_code": "ACR",
            "url": "https://janedoe.example.com",
        },
    ]

    for person_data in persons:
        person = Person(
            github_username=person_data["github_username"],
            email=person_data["email"],
            name=person_data["name"],
            organization_code=person_data.get("organization_code"),
            url=person_data.get("url"),
        )
        person.save_jsonl(output_file)


if __name__ == "__main__":
    main()
