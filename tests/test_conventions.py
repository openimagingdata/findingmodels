"""Tests for findingmodels.conventions."""

import unittest

from findingmodels.conventions import (
    CHANGE_ATTRIBUTE_NAME,
    CHANGE_VALUE_NAMES,
    PRESENCE_ATTRIBUTE_NAME,
    create_change_from_prior_attribute,
    create_presence_attribute,
    ensure_standard_attributes,
    lowercase_model_dict,
    reorder_attributes,
)


class ConventionsTests(unittest.TestCase):
    def test_presence_and_change_are_first(self):
        attrs = [
            {"name": "size", "type": "choice", "values": [{"name": "small"}, {"name": "large"}]},
        ]
        result = ensure_standard_attributes(attrs, "pleural effusion")
        ordered = reorder_attributes(result)
        self.assertEqual(ordered[0]["name"], PRESENCE_ATTRIBUTE_NAME)
        self.assertEqual(ordered[1]["name"], CHANGE_ATTRIBUTE_NAME)
        self.assertEqual(ordered[2]["name"], "size")

    def test_presence_has_standard_values(self):
        attr = create_presence_attribute("pleural effusion")
        names = [v["name"] for v in attr["values"]]
        self.assertEqual(names, ["absent", "present", "indeterminate", "unknown"])

    def test_device_finding_has_full_change_values(self):
        attr = create_change_from_prior_attribute("peripherally inserted central catheter")
        names = [v["name"] for v in attr["values"]]
        self.assertEqual(list(CHANGE_VALUE_NAMES), names)

    def test_mass_finding_has_full_change_values(self):
        attr = create_change_from_prior_attribute("mediastinal mass")
        names = [v["name"] for v in attr["values"]]
        self.assertEqual(list(CHANGE_VALUE_NAMES), names)

    def test_lowercase_strips_finding_suffix(self):
        model = {
            "name": "Pleural Effusion",
            "attributes": [
                {
                    "name": "side Finding",
                    "type": "choice",
                    "values": [{"name": "Left"}, {"name": "Right"}],
                }
            ],
        }
        normalized = lowercase_model_dict(model)
        self.assertEqual(normalized["name"], "pleural effusion")
        self.assertEqual(normalized["attributes"][0]["name"], "side")
        self.assertEqual(normalized["attributes"][0]["values"][0]["name"], "left")

    def test_upgrade_yes_no_presence(self):
        attrs = [
            {
                "name": "Presence",
                "type": "choice",
                "values": [{"name": "yes"}, {"name": "no"}],
            },
            {"name": "density", "type": "choice", "values": [{"name": "solid"}, {"name": "cystic"}]},
        ]
        result = ensure_standard_attributes(attrs, "mediastinal mass")
        presence = result[0]
        names = {v["name"] for v in presence["values"]}
        self.assertTrue({"present", "absent", "indeterminate", "unknown"}.issubset(names))

    def test_change_from_prior_value_count(self):
        attr = create_change_from_prior_attribute("pleural effusion")
        names = [v["name"] for v in attr["values"]]
        self.assertEqual(list(CHANGE_VALUE_NAMES), names)

    def test_change_from_prior_strips_nonstandard_values(self):
        attrs = [
            {
                "name": "change from prior",
                "type": "choice",
                "values": [
                    {"name": "unchanged"},
                    {"name": "no prior"},
                ],
            },
        ]
        result = ensure_standard_attributes(attrs, "pleural effusion")
        change = result[1]
        names = [v["name"] for v in change["values"]]
        self.assertEqual(list(CHANGE_VALUE_NAMES), names)
        self.assertNotIn("no prior", names)


if __name__ == "__main__":
    unittest.main()
