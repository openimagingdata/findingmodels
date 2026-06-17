import logging

from typing import Dict



import findingmodels.compat  # noqa: F401 - patch findingmodel.index for findingmodel-ai
from findingmodel import FindingModelBase, FindingModelFull
from findingmodel.tools import add_ids_to_model

logger = logging.getLogger(__name__)



_SHORT_EXPANSIONS: Dict[str, str] = {

    "T0": "t0 stage",

    "T1": "t1 stage",

    "T2": "t2 stage",

    "T3": "t3 stage",

    "T4": "t4 stage",

    "T5": "t5 stage",

    "T6": "t6 stage",

    "T7": "t7 stage",

    "T8": "t8 stage",

    "T9": "t9 stage",

    "C1": "c1 vertebra",

    "C2": "c2 vertebra",

    "C3": "c3 vertebra",

    "C4": "c4 vertebra",

    "C5": "c5 vertebra",

    "C6": "c6 vertebra",

    "C7": "c7 vertebra",

    "L1": "l1 vertebra",

    "L2": "l2 vertebra",

    "L3": "l3 vertebra",

    "L4": "l4 vertebra",

    "L5": "l5 vertebra",

    "S1": "s1 vertebra",

    "S2": "s2 vertebra",

    "S3": "s3 vertebra",

    "S4": "s4 vertebra",

    "S5": "s5 vertebra",

    "A0": "a0 stage",

    "A1": "a1 stage",

    "A2": "a2 stage",

    "A3": "a3 stage",

    "A4": "a4 stage",

    "B1": "b1 stage",

    "B2": "b2 stage",

    "B3": "b3 stage",

    "M1": "m1 stage",

    "M2": "m2 stage",

    "M3": "m3 stage",

    "M4": "m4 stage",

    "F1": "f1 stage",

    "F2": "f2 stage",

    "F3": "f3 stage",

    "F4": "f4 stage",

    "Cabg": "coronary artery bypass graft",

    "Ipmn": "intraductal papillary mucinous neoplasm",

    "Picc": "peripherally inserted central catheter",

    "CVC": "central venous catheter",

    "ECMO": "extracorporeal membrane oxygenation cannula",

    "LVAD": "left ventricular assist device",

    "PFO": "patent foramen ovale closure",

    "UIP": "usual interstitial pneumonia pattern",

}





class CDEStagingCtChestJsonAdapter:



    @staticmethod

    def _truncate_description(description: str, max_length: int = 500) -> str:

        if not description or len(description) <= max_length:

            return description

        return description[: max_length - 4] + "..."



    @staticmethod

    def _normalize_finding_name(name: str) -> str:

        if name in _SHORT_EXPANSIONS:

            return _SHORT_EXPANSIONS[name]

        return name.replace("_", " ").strip().lower()



    @staticmethod

    def _normalize_attribute_name(name: str) -> str:

        if name in _SHORT_EXPANSIONS:

            return _SHORT_EXPANSIONS[name]

        cleaned = name.replace("_", " ").strip()

        if cleaned.lower().endswith(" finding"):

            cleaned = cleaned[: -len(" finding")].strip()

        return cleaned.lower()



    @staticmethod

    async def adapt_cdestaging_ct_chest_json(json_data: Dict, filename: str) -> FindingModelFull:

        finding_name = json_data["finding_name"]

        normalized_finding_name = CDEStagingCtChestJsonAdapter._normalize_finding_name(finding_name)

        if normalized_finding_name != finding_name:

            logger.debug("Finding name '%s' -> '%s'", finding_name, normalized_finding_name)



        description = json_data.get("description", "")

        if description and len(description) >= 5:

            description = CDEStagingCtChestJsonAdapter._truncate_description(description)

        else:

            description = f"Description for {normalized_finding_name}"



        finding_model_dict = {

            "name": normalized_finding_name,

            "description": description,

            "attributes": [],

        }



        for attribute in json_data.get("attributes", []):

            attr_name = CDEStagingCtChestJsonAdapter._normalize_attribute_name(attribute["name"])

            if attr_name != attribute["name"]:

                logger.debug(

                    "Attribute name '%s' -> '%s'",

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

                    value_name = str(value["name"]).replace("_", " ").strip().lower()

                    processed_value = {"name": value_name}

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


