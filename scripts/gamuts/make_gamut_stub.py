# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "findingmodel",
# ]
# ///
import json
from pathlib import Path
import sys
from typing import NamedTuple

from findingmodel import FindingInfo, FindingModelFull
from findingmodel.common import model_file_name
from findingmodel.index import Index
from findingmodel.index_code import IndexCode
from findingmodel.tools import (
    add_ids_to_finding_model,
    add_standard_codes_to_finding_model,
    create_finding_model_stub_from_finding_info,
)


def stub_from_gamut(
    gamuts_id: str,
    name: str,
    seen_on_modalities: list[str],
    description: str,
    synonyms: list[str] | None,
    category: str,
    subcategories: list[str],
    region: str,
    **extra_args: dict,
) -> FindingModelFull:
    synonyms = synonyms or None
    info = FindingInfo(name=name, description=description, synonyms=synonyms)
    fm = create_finding_model_stub_from_finding_info(info)
    tags = [region, *seen_on_modalities, *subcategories, category]
    fm.tags = tags
    gamut_code = IndexCode(system="GAMUTS", code=gamuts_id, display=name)
    fm_ids = add_ids_to_finding_model(fm, source="GMTS")
    fm_ids.index_codes = [gamut_code]
    # Make a string of the gamuts_id zero-padded to 6 digits
    gamuts_id_string = gamuts_id.zfill(6)
    fm_ids.oifm_id = fm_ids.oifm_id[:-6] + gamuts_id_string
    add_standard_codes_to_finding_model(fm_ids)
    if fm_ids.oifm_id in synonyms_to_exclude:
        synonym = synonyms_to_exclude[fm_ids.oifm_id]
        if fm_ids.synonyms and synonym in fm_ids.synonyms:
            fm_ids.synonyms = [s for s in fm_ids.synonyms if s.casefold() != synonym.casefold()]
    return fm_ids

with open(Path(__file__).parent / "excluded_synonyms.txt", "r", encoding="utf-8") as f:
    synonyms_to_exclude: dict[str, str] = { }
    for line in [l.strip() for l in f.readlines() if l.strip()]:
        oifm_id, name, synonym = line.split(":")
        synonyms_to_exclude[oifm_id] = synonym

def read_gamut_jsonl(
    gamut_jsonl_file: Path,
    region: str,
    index: Index,
    already_exists: list[str],
    synonym_collisions: list[str],
    name_collisions: list[str],
    attribute_collisions: list[str],
    exclude_synonyms: list[str],
) -> None:
    label = gamut_jsonl_file.name[0:2]
    with open(gamut_jsonl_file, "r", encoding="utf-8") as f:
        for gamut_json in f.readlines():
            gamut_info = json.loads(gamut_json)
            if not gamut_info.get("gamuts_id"):
                print("Skipping entry without 'id'")
                continue
            if len(gamut_info.get("gamuts_id", "")) < 3:
                gamut_info["gamuts_id"] = gamut_info["gamuts_id"].zfill(3)
            if len(gamut_info.get("name", "")) < 5:
                gamut_info["name"] = gamut_info["name"] + "*"
            fm = stub_from_gamut(region=region, **gamut_info)
            fm_filename = model_file_name(fm.name)
            index.write_model_to_file(fm, filename=fm_filename, overwrite=True)
            try:
                index.add_entry(fm, fm_filename)
            except ValueError as e:
                if "Model ID" in e.args[0]:
                    already_exists.append(f"{label}-{fm.oifm_id}-{fm.name}")
                    continue
                elif "attribute IDs already exist" in e.args[0]:
                    # attribute_collisions.append(f"{label}-{fm.oifm_id}-{fm.name}")
                    fm = stub_from_gamut(region=region, **gamut_info)
                    index.add_entry(fm, fm_filename)
                    index.write_model_to_file(fm, filename=fm_filename, overwrite=True)
                    continue
                elif "Model name" in e.args[0]:
                    conflict = index[fm.name]
                    if conflict:
                        name_collisions.append(f"{label}-{fm.oifm_id}-{fm.name} conflicts with {conflict.oifm_id}-{conflict.name}")
                        exclude_synonyms.append(f"{conflict.oifm_id}:{conflict.name}:{fm.name.casefold()}")
                    else:
                        name_collisions.append(f"{label}-{fm.oifm_id}-{fm.name} has a name that conflicts but couldn't find it")
                    continue
                elif "synonym" in e.args[0]:
                    conflict, matching_synonym = None, None
                    for synonym in fm.synonyms or []:
                        conflict = index[synonym]
                        matching_synonym = synonym
                        if conflict:
                            break
                    if conflict:
                        synonym_collisions.append(f"{label}-{fm.oifm_id}-{fm.name} conflicts with {conflict.oifm_id}-{conflict.name}")
                        if matching_synonym:
                            exclude_synonyms.append(f"{fm.oifm_id}:{fm.name}:{matching_synonym.casefold()}")
                            exclude_synonyms.append(f"{conflict.oifm_id}:{conflict.name}:{matching_synonym.casefold()}")
                    else:
                        synonym_collisions.append(f"{label}-{fm.oifm_id}-{fm.name} has a synonym that conflicts but couldn't find it")
                    continue
                else:
                    print(f"In {gamut_jsonl_file.name} error adding {fm.name} with ID {fm.oifm_id} to index: {e}")
                    continue


def main() -> None:

    files = [
        ("cardiac", "ca_gamuts.jsonl"),
        ("abdomen", "gu_gamuts.jsonl"),
        ("abdomen", "gi_gamuts.jsonl"),
        ("head_neck", "hn_gamuts.jsonl"),
        ("musculoskeletal", "mk_gamuts.jsonl"),
        ("neuro", "nr_gamuts.jsonl"),
        ("pediatric", "pd_gamuts.jsonl"),
        ("vascular", "vi_gamuts.jsonl"),
        ("ultrasound", "us_gamuts.jsonl"),
    ]

    already_exists: list[str] = []
    synonym_collisions: list[str] = []
    name_collisions: list[str] = []
    attribute_collisions: list[str] = []
    exclude_synonyms: list[str] = []

    index = Index(Path(__file__).parent.parent)
    jsonl_dir = Path(__file__).parent.parent / "lists" / "gamuts_jsonl"

    for region, file_name in files:
        gamut_jsonl_file = jsonl_dir / file_name
        if not gamut_jsonl_file.exists():
            print(f"File {gamut_jsonl_file} does not exist.")
            sys.exit(1)

        print(f"Processing {gamut_jsonl_file} for region {region}...")
        read_gamut_jsonl(
            gamut_jsonl_file,
            region,
            index,
            already_exists,
            synonym_collisions,
            name_collisions,
            attribute_collisions,
            exclude_synonyms,
        )

    if synonym_collisions:
        print("Synonym collisions:")
        print("\n".join(f"  - {entry}" for entry in synonym_collisions))

    if name_collisions:
        print("Name collisions:")
        print("\n".join(f"  - {entry}" for entry in name_collisions))

    if attribute_collisions:
        print("Attribute ID collisions:")
        print("\n".join(f"  - {entry}" for entry in attribute_collisions))

    if exclude_synonyms:
        print("Excluded synonyms:")
        print("\n".join(exclude_synonyms))

if __name__ == "__main__":
    main()
