"""Tests for CDEStaging CT chest loaders."""

import unittest
from pathlib import Path

from findingmodels.cdestaging_ct_chest.loaders import dedupe_input_files, normalized_stem, prefer_source


class LoaderDedupeTests(unittest.TestCase):
    def test_normalized_stem_treats_hyphen_and_underscore_equivalent(self):
        self.assertEqual(
            normalized_stem(Path("chest-tube.json")),
            normalized_stem(Path("chest_tube.json")),
        )

    def test_prefer_json_over_markdown(self):
        md = Path("thyroid-nodule.md")
        js = Path("thyroid_nodule.json")
        self.assertEqual(prefer_source(md, js), js)
        self.assertEqual(prefer_source(js, md), js)

    def test_prefer_underscore_json_stem(self):
        hyphen = Path("chest-tube.json")
        underscore = Path("chest_tube.json")
        self.assertEqual(prefer_source(hyphen, underscore), underscore)

    def test_dedupe_drops_duplicate_sources(self):
        files = dedupe_input_files(
            [
                Path("chest-tube.json"),
                Path("chest_tube.json"),
                Path("thyroid-nodule.md"),
                Path("thyroid_nodule.json"),
            ]
        )
        names = {f.name for f in files}
        self.assertEqual(names, {"chest_tube.json", "thyroid_nodule.json"})


if __name__ == "__main__":
    unittest.main()
