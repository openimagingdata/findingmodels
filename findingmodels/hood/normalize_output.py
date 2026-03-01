"""Normalize hood output before FindingModelFull validation."""

import re
from typing import Any


def normalize_for_validation(model_dict: dict[str, Any]) -> dict[str, Any]:
    """
    Normalize a finding model dict for schema compliance before validation.

    - anatomic_locations: set to null if any item lacks system/code or has invalid shape.
    - contributors: fix MGB org format and ensure Organization entries are valid.
    """
    result = dict(model_dict)

    # --- anatomic_locations ---
    if "anatomic_locations" in result and result["anatomic_locations"] is not None:
        al = result["anatomic_locations"]
        if not isinstance(al, list):
            result["anatomic_locations"] = None
        else:
            valid = True
            for item in al:
                if not isinstance(item, dict):
                    valid = False
                    break
                has_system = "system" in item and isinstance(item.get("system"), str) and len(item.get("system", "")) >= 3
                has_code = "code" in item and isinstance(item.get("code"), str) and len(item.get("code", "")) >= 2
                is_no_results = item.get("code") == "NO_RESULTS"
                has_name_instead = "name" in item and ("system" not in item or "code" not in item)
                if not (has_system and has_code) or is_no_results or has_name_instead:
                    valid = False
                    break
            if not valid:
                result["anatomic_locations"] = None

    # --- contributors ---
    if "contributors" in result and result["contributors"] is not None:
        contributors = result["contributors"]
        if isinstance(contributors, list):
            normalized = []
            org_pattern = re.compile(r"^[A-Z]{3,4}$")
            for c in contributors:
                if not isinstance(c, dict):
                    normalized.append(c)
                    continue
                # Organization: name (min 5 chars), code (^[A-Z]{3,4}$)
                if "code" in c and "name" in c:
                    name = c.get("name", "")
                    code = c.get("code", "")
                    # Fix MGB org: "mgb" or missing/invalid code -> full format
                    if (isinstance(name, str) and name.lower() == "mgb") or (
                        isinstance(code, str) and code.upper() == "MGB" and (not name or len(str(name)) < 5)
                    ):
                        normalized.append({"name": "Massachusetts General Brigham", "code": "MGB"})
                        continue
                    # Ensure valid org: name min 5, code pattern
                    if isinstance(name, str) and len(name) >= 5 and isinstance(code, str) and org_pattern.match(code):
                        normalized.append(c)
                        continue
                # Person: keep as-is (validation will catch other issues)
                normalized.append(c)
            result["contributors"] = normalized

    return result
