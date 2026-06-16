"""Tests for CDEStaging CT chest postprocess."""

import json
import unittest
from pathlib import Path
from unittest.mock import AsyncMock, patch

from findingmodel import FindingModelFull

from findingmodels.cdestaging_ct_chest.postprocess import _apply_conventions, enrich_model


class ApplyConventionsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sample_path = Path("defs/from_cdestaging_ct_chest/pleural_effusion.fm.json")
        if not cls.sample_path.is_file():
            raise unittest.SkipTest("sample pleural_effusion.fm.json not available")

    def test_apply_conventions_pleural_effusion(self):
        model = FindingModelFull.model_validate(json.loads(self.sample_path.read_text()))
        enriched = _apply_conventions(model)
        names = [a.name for a in enriched.attributes]
        self.assertEqual(names[0], "presence")
        self.assertEqual(names[1], "change from prior")
        self.assertIn("side", names)
        self.assertFalse(any(n.endswith(" finding") for n in names))
        self.assertEqual(len(enriched.contributors or []), 2)
        self.assertEqual(enriched.name, "pleural effusion")


class AsyncEnrichModelTests(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls):
        cls.sample_path = Path("defs/from_cdestaging_ct_chest/pleural_effusion.fm.json")
        if not cls.sample_path.is_file():
            raise unittest.SkipTest("sample pleural_effusion.fm.json not available")

    @patch(
        "findingmodels.cdestaging_ct_chest.postprocess.enrich_anatomic_locations",
        new_callable=AsyncMock,
    )
    @patch(
        "findingmodels.cdestaging_ct_chest.postprocess.enrich_metadata_from_info",
        new_callable=AsyncMock,
    )
    async def test_json_path_calls_metadata_and_locations(
        self, mock_metadata, mock_locations
    ):
        model = FindingModelFull.model_validate(json.loads(self.sample_path.read_text()))
        mock_metadata.side_effect = lambda data, raw: {**data, "synonyms": ["effusion"]}
        mock_locations.side_effect = lambda data: {
            **data,
            "anatomic_locations": [
                {"system": "RADLEX", "code": "RID123", "display": "pleura"}
            ],
        }

        result = await enrich_model(
            model,
            source_type="json",
            raw_name="Pleural_Effusion",
            enrich_metadata=True,
            enrich_locations=True,
        )

        mock_metadata.assert_awaited_once()
        mock_locations.assert_awaited_once()
        self.assertEqual(result.synonyms, ["effusion"])
        self.assertEqual(len(result.anatomic_locations or []), 1)
        self.assertEqual(result.attributes[0].name, "presence")

    @patch(
        "findingmodels.cdestaging_ct_chest.postprocess.enrich_anatomic_locations",
        new_callable=AsyncMock,
    )
    @patch(
        "findingmodels.cdestaging_ct_chest.postprocess.enrich_metadata_from_info",
        new_callable=AsyncMock,
    )
    async def test_md_path_skips_metadata(self, mock_metadata, mock_locations):
        model = FindingModelFull.model_validate(json.loads(self.sample_path.read_text()))
        mock_locations.side_effect = lambda data: data

        await enrich_model(
            model,
            source_type="md",
            raw_name="pleural-effusion",
            enrich_metadata=True,
            enrich_locations=True,
        )

        mock_metadata.assert_not_called()
        mock_locations.assert_awaited_once()


if __name__ == "__main__":
    unittest.main()
