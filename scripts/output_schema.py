# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "findingmodel",
#     "oidm-common",
# ]
# [tool.uv.sources]
# findingmodel = { path = "../.metadata-runs/wheelhouse/current/findingmodel-1.0.4-py3-none-any.whl" }
# "oidm-common" = { path = "../.metadata-runs/wheelhouse/current/oidm_common-0.2.7-py3-none-any.whl" }
# ///
import json

from findingmodel import FindingModelFull

REQUIRED_METADATA_FIELDS = {
    "body_regions",
    "subspecialties",
    "etiologies",
    "entity_type",
    "applicable_modalities",
    "expected_time_course",
    "age_profile",
    "sex_specificity",
    "anatomic_locations",
}


def require_metadata_aware_package() -> None:
    missing = sorted(REQUIRED_METADATA_FIELDS - set(FindingModelFull.model_fields))
    if missing:
        raise RuntimeError(
            "scripts/output_schema.py must run with the metadata-aware findingmodel package. "
            f"Missing model fields: {', '.join(missing)}"
        )


def main():
    require_metadata_aware_package()
    # Get the schema of the FindingModelFull class
    schema = FindingModelFull.model_json_schema()
    print(json.dumps(schema, indent=2))

if __name__ == "__main__":
    main()
