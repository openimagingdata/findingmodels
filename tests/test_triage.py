"""Tests for CDEStaging DuckDB triage helpers."""

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from findingmodels.cdestaging_ct_chest.loaders import normalized_stem
from findingmodels.cdestaging_ct_chest.triage import (
    TriageCandidate,
    classify_candidates,
    detect_chunk_duplicate_stems,
    generate_search_targets,
    stems_to_skip,
    TriageRecord,
)


class GenerateSearchTargetsTests(unittest.TestCase):
    def test_json_stem_produces_canonical_and_subterm(self):
        targets = generate_search_targets("pleural_effusion", "Pleural Effusion")
        self.assertIn("Pleural Effusion", targets)
        self.assertTrue(len(targets) >= 2)
        self.assertLessEqual(len(targets), 3)

    def test_compound_stem_includes_key_subterm(self):
        targets = generate_search_targets("pulmonary_emboli", "Pulmonary Emboli")
        self.assertIn("Pulmonary Emboli", targets)
        self.assertTrue(any("emboli" in t.casefold() for t in targets))

    def test_deduplicates_targets(self):
        targets = generate_search_targets("emphysema", "emphysema")
        lowered = [t.casefold() for t in targets]
        self.assertEqual(len(lowered), len(set(lowered)))


class ClassifyCandidatesTests(unittest.TestCase):
    def test_exact_match_on_name(self):
        candidates = [
            TriageCandidate(oifm_id="OIFM_CDE_000254", name="Pleural Effusion"),
        ]
        decision, oifm_id, name, reason = classify_candidates(
            "Pleural Effusion", "pleural_effusion", candidates
        )
        self.assertEqual(decision, "exact_match")
        self.assertEqual(oifm_id, "OIFM_CDE_000254")
        self.assertEqual(name, "Pleural Effusion")
        self.assertIn("Exact name match", reason)

    def test_no_match_when_empty(self):
        decision, _, _, reason = classify_candidates("Foo", "foo", [])
        self.assertEqual(decision, "no_match")
        self.assertIn("No index candidates", reason)

    def test_ambiguous_when_multiple_exact_name_hits(self):
        candidates = [
            TriageCandidate(oifm_id="OIFM_A_1", name="Pleural Effusion"),
            TriageCandidate(oifm_id="OIFM_B_2", name="pleural effusion"),
        ]
        decision, _, _, reason = classify_candidates(
            "Pleural Effusion", "pleural_effusion", candidates
        )
        self.assertEqual(decision, "ambiguous")
        self.assertIn("Multiple exact-name", reason)


class StemsToSkipTests(unittest.TestCase):
    def test_skips_exact_match_and_user_skip(self):
        data = {
            "records": [
                {"stem": "pleural_effusion", "decision": "exact_match"},
                {"stem": "pneumothorax", "decision": "no_match"},
                {"stem": "cabg", "decision": "user_skip"},
                {"stem": "emphysema", "decision": "convert"},
            ]
        }
        skip = stems_to_skip(data)
        self.assertEqual(skip, {"pleural_effusion", "cabg"})


class ConvertSkipIntegrationTests(unittest.TestCase):
    def test_triage_file_skips_exact_match_sources(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            input_dir = tmp_path / "input"
            output_dir = tmp_path / "output"
            input_dir.mkdir()
            output_dir.mkdir()

            source = input_dir / "pleural-effusion.json"
            source.write_text(
                json.dumps({"finding_name": "Pleural Effusion", "attributes": []}),
                encoding="utf-8",
            )

            triage_path = tmp_path / "triage.json"
            triage_path.write_text(
                json.dumps(
                    {
                        "records": [
                            {
                                "stem": normalized_stem(source),
                                "decision": "exact_match",
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )

            from scripts.cdestaging_ct_chest_to_finding_model import run_batch

            with patch(
                "scripts.cdestaging_ct_chest_to_finding_model.convert_definition"
            ) as mock_convert:
                import asyncio

                exit_code = asyncio.run(
                    run_batch(
                        input_dir,
                        output_dir,
                        offset=0,
                        limit=None,
                        triage_file=triage_path,
                    )
                )
                mock_convert.assert_not_called()

            self.assertEqual(exit_code, 0)


class ChunkDuplicateTests(unittest.TestCase):
    def test_detects_duplicate_incoming_names(self):
        records = [
            TriageRecord(
                stem="pleural_effusion",
                source_path="a.json",
                incoming_name="Pleural Effusion",
                search_targets=[],
                decision="no_match",
            ),
            TriageRecord(
                stem="pleural_effusion_alt",
                source_path="b.json",
                incoming_name="pleural effusion",
                search_targets=[],
                decision="no_match",
            ),
        ]
        dupes = detect_chunk_duplicate_stems(records)
        self.assertEqual(len(dupes), 2)


if __name__ == "__main__":
    unittest.main()
