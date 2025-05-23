# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "findingmodel",
# ]
# ///
from pathlib import Path

from findingmodel import FindingModelFull
from findingmodel.tools import add_standard_codes_to_finding_model

defs_dir = Path(__file__).parent.parent / "defs"
for fm_path in defs_dir.rglob("*.fm.json"):
    raw = fm_path.read_text()
    fm = FindingModelFull.model_validate_json(raw)
    add_standard_codes_to_finding_model(fm)
    fm_path.write_text(fm.model_dump_json(indent=2, exclude_none=True))