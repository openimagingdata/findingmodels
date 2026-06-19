"""Tests for CDEStaging CT chest json_adapter."""

import unittest

from findingmodel import FindingModelFull

from findingmodels.cdestaging_ct_chest.json_adapter import CDEStagingCtChestJsonAdapter


class JsonAdapterPassthroughTests(unittest.IsolatedAsyncioTestCase):
    async def test_passthrough_synonyms_and_tags(self):
        json_data = {
            "finding_name": "pleural effusion",
            "description": "Fluid in the pleural space.",
            "synonyms": ["effusion", "pleural fluid"],
            "tags": ["chest", "fluid"],
            "attributes": [
                {
                    "name": "presence",
                    "type": "choice",
                    "values": [
                        {"name": "present", "description": "None"},
                        {"name": "absent", "description": "None"},
                    ],
                }
            ],
        }
        model = await CDEStagingCtChestJsonAdapter.adapt_cdestaging_ct_chest_json(
            json_data, "pleural-effusion.json"
        )
        self.assertIsInstance(model, FindingModelFull)
        self.assertEqual(model.synonyms, ["effusion", "pleural fluid"])
        self.assertEqual(model.tags, ["chest", "fluid"])

    async def test_omits_synonyms_tags_when_absent(self):
        json_data = {
            "finding_name": "pneumothorax",
            "description": "Air in the pleural space.",
            "attributes": [
                {
                    "name": "presence",
                    "type": "choice",
                    "values": [
                        {"name": "present", "description": "None"},
                        {"name": "absent", "description": "None"},
                    ],
                }
            ],
        }
        model = await CDEStagingCtChestJsonAdapter.adapt_cdestaging_ct_chest_json(
            json_data, "pneumothorax.json"
        )
        self.assertIsNone(model.synonyms)
        self.assertIsNone(model.tags)


if __name__ == "__main__":
    unittest.main()
