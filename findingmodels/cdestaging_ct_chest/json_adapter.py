import logging
from typing import Dict, List

import findingmodels.compat  # noqa: F401 - patch findingmodel.index for findingmodel-ai
from dotenv import load_dotenv
from findingmodel import FindingModelBase, FindingModelFull
from findingmodel.tools import add_ids_to_model
from findingmodel_ai.authoring import create_info_from_name

load_dotenv()

logger = logging.getLogger(__name__)


class CDEStagingCtChestJsonAdapter:

    @staticmethod
    def _truncate_description(description: str, max_length: int = 500) -> str:
        if not description or len(description) <= max_length:
            return description
        return description[: max_length - 4] + "..."

    @staticmethod
    def _expand_short_name(name: str) -> str:
        expansions = {
            "T0": "T0 stage",
            "T1": "T1 stage",
            "T2": "T2 stage",
            "T3": "T3 stage",
            "T4": "T4 stage",
            "T5": "T5 stage",
            "T6": "T6 stage",
            "T7": "T7 stage",
            "T8": "T8 stage",
            "T9": "T9 stage",
            "C1": "C1 vertebra",
            "C2": "C2 vertebra",
            "C3": "C3 vertebra",
            "C4": "C4 vertebra",
            "C5": "C5 vertebra",
            "C6": "C6 vertebra",
            "C7": "C7 vertebra",
            "L1": "L1 vertebra",
            "L2": "L2 vertebra",
            "L3": "L3 vertebra",
            "L4": "L4 vertebra",
            "L5": "L5 vertebra",
            "S1": "S1 vertebra",
            "S2": "S2 vertebra",
            "S3": "S3 vertebra",
            "S4": "S4 vertebra",
            "S5": "S5 vertebra",
            "A0": "A0 stage",
            "A1": "A1 stage",
            "A2": "A2 stage",
            "A3": "A3 stage",
            "A4": "A4 stage",
            "B1": "B1 stage",
            "B2": "B2 stage",
            "B3": "B3 stage",
            "M1": "M1 stage",
            "M2": "M2 stage",
            "M3": "M3 stage",
            "M4": "M4 stage",
            "F1": "F1 stage",
            "F2": "F2 stage",
            "F3": "F3 stage",
            "F4": "F4 stage",
            "Cabg": "CABG surgery",
            "Ipmn": "IPMN lesion",
            "Picc": "PICC line",
            "CVC": "central venous catheter",
            "ECMO": "ECMO cannula",
            "LVAD": "LVAD device",
            "PFO": "PFO closure",
            "UIP": "UIP pattern",
        }

        if name in expansions:
            return expansions[name]
        if len(name) < 3:
            return f"{name} Value"
        if len(name) < 5:
            return f"{name} Finding"
        return name

    @staticmethod
    def _create_oidm_organization() -> Dict:
        return {
            "name": "Open Imaging Data Model",
            "code": "OIDM",
            "url": "https://openimagingdata.org",
        }

    @staticmethod
    def _create_mgb_organization() -> Dict:
        return {"name": "Massachusetts General Brigham", "code": "MGB"}

    @staticmethod
    def _create_person() -> Dict:
        return {
            "github_username": "hoodcm",
            "email": "chood@mgh.harvard.edu",
            "name": "C. Michael Hood, MD",
            "organization_code": "MGB",
        }

    @staticmethod
    def _create_default_contributors() -> List[Dict]:
        return [
            CDEStagingCtChestJsonAdapter._create_oidm_organization(),
            CDEStagingCtChestJsonAdapter._create_mgb_organization(),
            CDEStagingCtChestJsonAdapter._create_person(),
        ]

    @staticmethod
    async def adapt_cdestaging_ct_chest_json(json_data: Dict, filename: str) -> FindingModelFull:
        finding_name = json_data["finding_name"]

        expanded_finding_name = CDEStagingCtChestJsonAdapter._expand_short_name(finding_name)
        if expanded_finding_name != finding_name:
            logger.debug("Short name '%s' -> '%s'", finding_name, expanded_finding_name)

        description = json_data.get("description", "")
        if not description or len(description) < 5:
            try:
                finding_info = await create_info_from_name(expanded_finding_name)
                description = finding_info.description
                logger.debug("Generated description for '%s'", expanded_finding_name)
            except Exception as e:
                logger.warning("Could not generate description for '%s': %s", expanded_finding_name, e)
                description = f"Description for {expanded_finding_name}"
        else:
            description = CDEStagingCtChestJsonAdapter._truncate_description(description)

        finding_model_dict = {
            "name": expanded_finding_name.replace("_", " ").title(),
            "description": description,
            "attributes": [],
            "contributors": CDEStagingCtChestJsonAdapter._create_default_contributors(),
        }

        for attribute in json_data.get("attributes", []):
            attr_name = CDEStagingCtChestJsonAdapter._expand_short_name(attribute["name"])
            if attr_name != attribute["name"]:
                logger.debug(
                    "Short attribute name '%s' -> '%s'",
                    attribute["name"],
                    attr_name,
                )

            attr_description = attribute.get("description", "")
            if not attr_description or len(attr_description) < 5:
                attr_description = None
                logger.debug("Using default for short attribute description on '%s'", attr_name)
            else:
                attr_description = CDEStagingCtChestJsonAdapter._truncate_description(attr_description)

            adapted_attr = {
                "name": attr_name,
                "description": attr_description,
                "type": attribute["type"],
                "required": attribute.get("required", False),
            }

            if attribute["type"] == "choice":
                adapted_attr["max_selected"] = 1
                processed_values = []
                for value in attribute["values"]:
                    processed_value = {"name": value["name"]}
                    if "description" in value and value["description"] != value["name"]:
                        value_description = value["description"]
                        if value_description and len(value_description) >= 5:
                            processed_value["description"] = value_description
                    processed_values.append(processed_value)
                adapted_attr["values"] = processed_values
            elif attribute["type"] == "numeric":
                adapted_attr["minimum"] = attribute.get("minimum", 0)
                adapted_attr["maximum"] = attribute.get("maximum", 100)
                adapted_attr["unit"] = attribute.get("unit", "unit")

            finding_model_dict["attributes"].append(adapted_attr)

        if not finding_model_dict["attributes"]:
            logger.warning("No attributes found in %s", filename)

        base_model = FindingModelBase(**finding_model_dict)
        return add_ids_to_model(base_model, source="MGB")
