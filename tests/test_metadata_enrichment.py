"""Tests for findingmodels.metadata_enrichment."""

import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, patch

from findingmodels.metadata_enrichment import (
    enrich_anatomic_locations,
    enrich_metadata_from_info,
    merge_string_lists,
)


class MergeStringListsTests(unittest.TestCase):
    def test_dedupes_case_insensitive(self):
        result = merge_string_lists(["Pleural Effusion"], ["pleural effusion", "effusion"])
        self.assertEqual(result, ["Pleural Effusion", "effusion"])

    def test_excludes_canonical_name(self):
        result = merge_string_lists(["effusion"], exclude="pleural effusion")
        self.assertEqual(result, ["effusion"])


class MetadataEnrichmentTests(unittest.IsolatedAsyncioTestCase):
    @patch("findingmodels.metadata_enrichment._create_stub_from_info")
    @patch("findingmodels.metadata_enrichment._fetch_finding_info", new_callable=AsyncMock)
    async def test_enrich_metadata_from_info(self, mock_info, mock_stub):
        mock_info.return_value = SimpleNamespace(
            name="pleural effusion",
            description="Fluid in the pleural space.",
            synonyms=["effusion", "pleural fluid"],
        )
        mock_stub.return_value = SimpleNamespace(tags=["chest", "fluid"])

        model = {
            "name": "Pleural Effusion",
            "description": "An accumulation of fluid in the pleural cavity.",
            "attributes": [],
        }
        result = await enrich_metadata_from_info(model, "Pleural_Effusion")

        self.assertEqual(result["name"], "pleural effusion")
        self.assertEqual(result["description"], "An accumulation of fluid in the pleural cavity.")
        self.assertIn("effusion", result["synonyms"])
        self.assertIn("chest", result["tags"])

    @patch("findingmodels.metadata_enrichment._create_stub_from_info")
    @patch("findingmodels.metadata_enrichment._fetch_finding_info", new_callable=AsyncMock)
    async def test_enrich_metadata_fills_short_description(self, mock_info, mock_stub):
        mock_info.return_value = SimpleNamespace(
            name="hepatic cyst",
            description="A fluid-filled lesion in the liver.",
            synonyms=["liver cyst"],
        )
        mock_stub.return_value = SimpleNamespace(tags=None)

        model = {"name": "hepatic cyst", "description": "x", "attributes": []}
        result = await enrich_metadata_from_info(model, "hepatic cyst")

        self.assertEqual(result["description"], "A fluid-filled lesion in the liver.")


class AnatomicLocationEnrichmentTests(unittest.IsolatedAsyncioTestCase):
    @patch("findingmodels.metadata_enrichment._search_anatomic_locations", new_callable=AsyncMock)
    async def test_enrich_anatomic_locations(self, mock_find):
        primary = MagicMock(concept_id="RADLEX:123")
        primary.as_index_code.return_value.model_dump.return_value = {
            "system": "RADLEX",
            "code": "RID123",
            "display": "pleura",
        }
        alternate = MagicMock(concept_id="NO_RESULTS")
        mock_find.return_value = MagicMock(
            primary_location=primary,
            alternate_locations=[alternate],
        )

        model = {
            "name": "pleural effusion",
            "description": "Fluid in pleural space.",
        }
        result = await enrich_anatomic_locations(model)

        self.assertEqual(len(result["anatomic_locations"]), 1)
        self.assertEqual(result["anatomic_locations"][0]["code"], "RID123")

    @patch("findingmodels.metadata_enrichment._search_anatomic_locations", new_callable=AsyncMock)
    async def test_no_results_sets_null(self, mock_find):
        primary = MagicMock(concept_id="NO_RESULTS")
        mock_find.return_value = MagicMock(
            primary_location=primary,
            alternate_locations=[],
        )

        model = {"name": "device finding", "description": "A device."}
        result = await enrich_anatomic_locations(model)

        self.assertIsNone(result["anatomic_locations"])

    async def test_skips_when_already_set(self):
        existing = [{"system": "RADLEX", "code": "RID999", "display": "lung"}]
        model = {"name": "nodule", "anatomic_locations": existing}
        result = await enrich_anatomic_locations(model)

        self.assertEqual(result["anatomic_locations"], existing)


if __name__ == "__main__":
    unittest.main()
