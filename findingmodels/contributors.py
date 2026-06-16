"""Default contributor records for finding models in this project."""

from findingmodel.contributor import Organization, Person

HOOD_PERSON = Person(
    github_username="hoodcm",
    email="chood@mgh.harvard.edu",
    name="C. Michael Hood, MD",
    organization_code="MGB",
)

OIDM_ORGANIZATION = Organization(
    name="Open Imaging Data Model",
    code="OIDM",
    url="https://openimagingdata.org/",
)


def default_hood_contributors() -> list[Organization | Person]:
    """OIDM organization plus Hood person (standard for Hood CT chest batch)."""
    return [OIDM_ORGANIZATION, HOOD_PERSON]


def default_hood_contributors_as_dicts() -> list[dict]:
    """Contributor list as plain dicts for model_dump / JSON serialization."""
    return [c.model_dump(exclude_none=True) for c in default_hood_contributors()]
