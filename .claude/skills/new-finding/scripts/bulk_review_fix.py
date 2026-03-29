#!/usr/bin/env python3
"""Bulk fix finding models based on review results.

Applies systematic fixes identified by the LLM review process:
1. Grammar: regenerate attribute/value descriptions from the model name
2. Wrong finding name in descriptions: replace old names with current name
3. Direction-of-change winnowing: remove inappropriate values by category
4. Bad synonyms: remove specific synonyms flagged as subtypes/wrong
5. Underscore contamination: replace underscores in descriptions

Usage:
    uv run .claude/skills/new-finding/scripts/bulk_review_fix.py [--dry-run]

With --dry-run, prints what would change without writing files.
"""

import argparse
import json
import re
import sys
from pathlib import Path


# --- Direction-of-change categories ---
# Each model gets classified into one of these categories, which determines
# which direction-of-change values to keep.

# Remove ALL direction values (unchanged/stable/new/resolved only)
REMOVE_ALL_DIRECTION = {
    # Devices/hardware
    "abdominal clips", "anterior cervical fusion device", "aortic stent",
    "axillary clips", "biceps tenodesis anchor", "biliary stent",
    "breast clips", "cerclage wire", "chest tube", "cholecystectomy clips",
    "clamshell sternotomy", "clavicle fixation", "central venous catheter",
    "double balloon esophageal catheter", "extracorporeal membrane oxygenation catheter",
    "enteric tube", "epicardial pacing wires", "epidural catheter",
    "esophageal probe", "esophageal tamponade tube", "feeding tube",
    "gastric band", "gastrostomy tube", "hemodialysis catheter",
    "implantable cardioverter defibrillator", "implantable cardioverter defibrillator leads",
    "implantable venous access port", "intra-aortic balloon pump",
    "intravascular line", "introducer sheath", "leadless pacemaker",
    "lung sutures", "mediastinal clips", "mediastinal drain",
    "metallic foreign body", "metallic markers", "mitral annuloplasty ring",
    "mitral valve clip", "mitral valve replacement", "monitoring leads",
    "neck clips", "pacemaker", "pacer leads", "pericardial drain",
    "percutaneous ventricular assist device", "pulmonary arterial catheter",
    "pulmonary surgical staple line", "retained surgical foreign body",
    "reverse total shoulder arthroplasty", "cerclage wire", "rib fixation",
    "rotator cuff anchor", "shoulder fixation", "shoulder replacement",
    "spinal catheter", "spinal fixation", "sternal fixation",
    "sternal sutures", "sternotomy wires", "subclavian stent",
    "substernal pectus bar", "superior vena cava stent", "support device",
    "surgical clip", "surgical clips", "suture anchors in humeral head",
    "temporary pacer wire", "transcatheter aortic valve replacement",
    "tricuspid annuloplasty ring", "tunneled catheter", "vascular stent",
    "ventricular shunt",
    # Congenital variants
    "accessory fissure", "azygos fissure", "azygos lobe", "bifid rib",
    "bridging rib", "costal fusion", "diaphragmatic eventration",
    "hemivertebra", "intrathoracic rib", "nipple shadow",
    # Postsurgical states
    "esophagectomy with gastric pull-up", "heart transplant", "lung transplant",
    "malunion", "pectus excavatum repair", "pneumonectomy",
    "resection of clavicle", "rib resection", "spinal fusion",
    "thoracotomy", "upper limb amputation", "vertebroplasty",
    # Technique/quality
    "clipped costophrenic angles", "clipped lateral soft tissues",
    "clipped lung apices", "grid artifact", "image marker absent",
    "image marker incorrect", "improper centering", "lungs incompletely imaged",
    "motion artifact", "obscured by chin", "obscured by external object",
    "obscured by laterality marker", "obscured by medical device",
    "overpenetrated", "rotated", "underpenetrated",
    # Static findings
    "calcified breast implant", "rosary ribs", "stable cardiac silhouette",
    "tracheal diverticulum", "thyroid bed clips",
    "postsurgical changes of VATS",
    # Scars/fixed findings
    "pulmonary scar",
}

# Remove larger/smaller, add worsened/improved (disease processes)
REPLACE_LARGER_WITH_WORSENED = {
    "abnormal anterior junction line", "abnormal aortic contour",
    "abnormal aortopulmonary window contour", "abnormal hilar contour",
    "abnormal left paraspinal line", "abnormal left paratracheal stripe",
    "abnormal mediastinal contour", "abnormal posterior junction line",
    "abnormal pulmonary artery contour", "abnormal right paraspinal line",
    "abnormal right paratracheal stripe",
    "air bronchograms", "airspace consolidation", "airway abnormality",
    "alveolar pulmonary edema", "aortic arch bulging", "aortic dilation",
    "aortic tortuosity", "aortic unfolding",
    "apical pleuroparenchymal scarring", "architectural distortion",
    "aspiration", "atelectasis", "bat-wing opacities",
    "bronchial occlusion", "cephalization",
    "compression fracture", "costophrenic angle blunting",
    "cystic fibrosis", "depressed hemidiaphragm",
    "diaphragmatic abnormality", "diffuse hazy opacities",
    "diffuse idiopathic skeletal hyperostosis",
    "diffuse increased lung attenuation", "diffuse increased lung lucency",
    "diffuse nodular opacities", "dilation of bowel", "distension of bowel",
    "distension of stomach", "double density sign",
    "elevation of hemidiaphragm", "emphysema",
    "fissure thickening", "flattening of hemidiaphragm",
    "globular cardiac silhouette", "height loss of vertebral body",
    "hyperinflation", "indistinct pulmonary vasculature",
    "interstitial pulmonary edema", "interstitial thickening",
    "kyphosis", "low lung volumes",
    "mediastinal abnormality", "obscuration of hemidiaphragm",
    "osseous abnormality", "osseous destruction", "osseous erosion",
    "osteopenia", "post resection volume loss",
    "pulmonary contusion", "pulmonary vascular abnormality",
    "pulmonary vascular engorgement", "sclerosis",
    "soft tissue swelling", "splaying of carina",
    "subcutaneous emphysema", "superior mediastinal fullness",
    "tension pneumothorax", "thoracic vertebra plana",
    "tracheal obstruction", "tracheal stenosis",
    "vanishing ribs", "volume loss",
    "wedging of vertebral body", "widening of rib interspaces",
    "bronchial wall thickening",
}

# Remove increased/decreased, keep larger/smaller (focal lesions)
REMOVE_INCREASED_DECREASED = {
    "bulla", "calcified nodule", "lung mass", "osseous lesion",
    "osseous lucency", "pericardial cyst", "pericardial fat pad",
    "mediastinal fat pad", "pleural nodule", "lytic osseous lesion",
    "sclerotic osseous lesion",
}

# Remove larger/smaller only, keep increased/decreased (diffuse processes)
REMOVE_LARGER_SMALLER_ONLY = {
    "aortic calcification", "costochondral calcification",
    "osteophyte formation", "pneumobilia",
    "pulmonary calcification", "pulmonary oligemia",
    "calcified pleural plaques",
    "tracheal calcification", "reduced lung markings",
    "reticular opacities", "reticulonodular opacity",
    "vertebral endplate irregularity", "widened cardiomediastinal silhouette",
    "diffuse nodular opacities",
}

# Remove all 4 direction values for osseous deformity (static structural)
REMOVE_ALL_DIRECTION.update({
    "osseous deformity", "Sprengel deformity", "congenital high scapula",
})

# --- Bad synonyms to remove ---
BAD_SYNONYMS = {
    "defs/amelia.fm.json": ["phocomelia"],
    "defs/fracture.fm.json": ["rib fracture", "bone fracture"],
    "defs/pacemaker.fm.json": ["dual chamber pacemaker", "single chamber pacemaker"],
    "defs/osseous_deformity.fm.json": [
        "clavicle deformity", "humeral head deformity",
        "rib deformity", "scapular deformity", "sternal deformity",
    ],
    "defs/osseous_erosion.fm.json": ["clavicle erosion", "humeral head erosion"],
    "defs/lytic_osseous_lesion.fm.json": ["lytic rib lesion", "destructive rib lesion"],
    "defs/mediastinal_clips.fm.json": ["hilar clips"],
    "defs/mediastinal_drain.fm.json": ["Jackson-Pratt drain", "JP drain", "Blake tube"],
    "defs/interstitial_pulmonary_edema.fm.json": ["Kerley lines"],
    "defs/implantable_cardioverter_defibrillator.fm.json": ["transvenous pacemaker"],
    "defs/bronchial_occlusion.fm.json": ["mucus plugging"],
    "defs/pleural_nodule.fm.json": ["pleural mass"],
    "defs/emphysema.fm.json": ["bullous emphysema", "bullous disease"],
}

# --- Known wrong-name replacements in descriptions ---
# old_text -> (files that have it, or None for all)
WRONG_NAME_REPLACEMENTS = {
    "Pulmonary opacity": [
        "defs/calcified_pleural_plaques.fm.json",
        "defs/low_lung_volumes.fm.json",
        "defs/pulmonary_laceration.fm.json",
        "defs/pulmonary_oligemia.fm.json",
        "defs/reduced_lung_markings.fm.json",
        "defs/reticular_opacities.fm.json",
        "defs/obscuration_of_hemidiaphragm.fm.json",
    ],
    "Cardiomegaly and mediastinal widening": [
        "defs/widened_cardiomediastinal_silhouette.fm.json",
    ],
    "Mediastinal findings": [
        "defs/superior_mediastinal_fullness.fm.json",
    ],
    "Impella device": [
        "defs/percutaneous_ventricular_assist_device.fm.json",
    ],
    "Nuss bar": [
        "defs/substernal_pectus_bar.fm.json",
    ],
}


def is_plural(name: str) -> bool:
    """Heuristic: does this finding name look like a plural noun?"""
    plural_endings = [
        "clips", "wires", "leads", "sutures", "markers", "anchors",
        "opacities", "nodes", "ribs", "volumes", "angles", "apices",
        "tissues", "bronchograms", "plaques", "changes", "nodules",
    ]
    last_word = name.split()[-1].lower()
    return last_word in plural_endings


def correct_article(name: str) -> str:
    """Generate correct article + name for description templates."""
    if is_plural(name):
        return name  # No article for plurals
    first_letter = name[0].lower()
    vowels = "aeiou"
    if first_letter in vowels:
        return f"an {name}"
    return name  # No article for most mass/uncountable nouns in medical English


def generate_descriptions(name: str) -> dict:
    """Generate correct descriptions for presence and change from prior attributes."""
    cap_name = name[0].upper() + name[1:]
    plural = is_plural(name)
    verb_is = "are" if plural else "is"
    verb_has = "have" if plural else "has"

    # For the "Whether and how..." description, figure out natural phrasing
    if plural:
        how_phrase = f"Whether and how {name} {verb_has} changed over time"
    else:
        first = name[0].lower()
        if first in "aeiou":
            how_phrase = f"Whether and how {name} has changed over time"
        else:
            how_phrase = f"Whether and how {name} has changed over time"

    return {
        "presence_desc": f"Presence or absence of {name}",
        "absent": f"{cap_name} {verb_is} absent",
        "present": f"{cap_name} {verb_is} present",
        "indeterminate": f"Presence of {name} cannot be determined",
        "unknown": f"Presence of {name} is unknown",  # "Presence" is always the subject here
        "change_desc": how_phrase,
        "unchanged": f"{cap_name} {verb_is} unchanged",
        "stable": f"{cap_name} {verb_is} stable",
        "new": f"{cap_name} {verb_is} new",
        "resolved": f"{cap_name} seen on a prior exam {verb_has} resolved",
        "increased": f"{cap_name} {verb_has} increased",
        "decreased": f"{cap_name} {verb_has} decreased",
        "larger": f"{cap_name} {verb_is} larger",
        "smaller": f"{cap_name} {verb_is} smaller",
        "worsened": f"{cap_name} {verb_has} worsened",
        "improved": f"{cap_name} {verb_has} improved",
    }


def classify_finding(name: str) -> str:
    """Classify a finding into a direction-of-change category."""
    if name in REMOVE_ALL_DIRECTION:
        return "none"
    if name in REPLACE_LARGER_WITH_WORSENED:
        return "worsened_improved"
    if name in REMOVE_INCREASED_DECREASED:
        return "larger_smaller"
    if name in REMOVE_LARGER_SMALLER_ONLY:
        return "increased_decreased"
    # Default: keep all (e.g., hiatal hernia, kidney stone, lung mass if not listed)
    return "all"


def fix_model(filepath: str, dry_run: bool = False) -> list[str]:
    """Fix a single model. Returns list of changes made."""
    p = Path(filepath)
    if not p.exists():
        return [f"SKIP: {filepath} not found"]

    d = json.loads(p.read_text())
    name = d.get("name", "")
    changes = []

    # --- Fix wrong finding name in descriptions ---
    for wrong_name, target_files in WRONG_NAME_REPLACEMENTS.items():
        if filepath in target_files:
            text = json.dumps(d)
            if wrong_name in text:
                # Generate correct name references
                cap_name = name[0].upper() + name[1:]
                text = text.replace(wrong_name, cap_name)
                d = json.loads(text)
                changes.append(f"Replaced '{wrong_name}' with '{cap_name}' in descriptions")

    # --- Fix underscore contamination in descriptions ---
    text = json.dumps(d)
    # Find underscored words in descriptions (but not in IDs or field names)
    underscore_patterns = [
        "Rosary_ribs", "Carina_splaying",
        "Anterior_junction_line_abnormal", "Hilar_contour_abnormal",
        "Aortic contour abnormal", "Aortopulmonary window contour abnormal",
        "Posterior junction line abnormal",
        "Abnormal_pulmonary_artery_contour",
    ]
    for pattern in underscore_patterns:
        if pattern in text:
            cap_name = name[0].upper() + name[1:]
            text = text.replace(pattern, cap_name)
            d = json.loads(text)
            changes.append(f"Replaced '{pattern}' with '{cap_name}'")

    # --- Remove bad synonyms ---
    if filepath in BAD_SYNONYMS:
        bad = BAD_SYNONYMS[filepath]
        current_syns = d.get("synonyms", [])
        new_syns = [s for s in current_syns if s not in bad]
        if len(new_syns) != len(current_syns):
            removed = [s for s in current_syns if s in bad]
            d["synonyms"] = new_syns if new_syns else None
            if d["synonyms"] is None:
                del d["synonyms"]
            changes.append(f"Removed bad synonyms: {removed}")

    # --- Fix grammar in descriptions (only where actually broken) ---
    descs = generate_descriptions(name)
    cap_name = name[0].upper() + name[1:]
    attrs = d.get("attributes", [])

    for attr in attrs:
        if attr.get("name") == "presence":
            for val in attr.get("values", []):
                vname = val.get("name", "")
                old_desc = val.get("description", "")
                if vname in descs and old_desc != descs[vname]:
                    # Only fix if the description has a grammar problem
                    # Skip "Presence of X" sentences — "Presence" is the subject, always singular
                    starts_with_presence = old_desc.startswith("Presence of ")
                    has_problem = (
                        (not starts_with_presence and " is " in old_desc and is_plural(name))  # plural verb agreement
                        or "_" in old_desc  # underscore contamination
                    )
                    if has_problem:
                        val["description"] = descs[vname]
                        changes.append(f"Fixed grammar: '{old_desc}' → '{descs[vname]}'")

        elif attr.get("name") == "change from prior":
            old_desc = attr.get("description", "")
            if old_desc != descs["change_desc"]:
                # Check for actual grammar problems in the "Whether and how" description
                has_problem = (
                    "a " + name[0].lower() in old_desc.lower() and name[0].lower() in "aeiou"  # "a a..." or "a e..."
                    or ("a " + name.split()[0].lower() in old_desc.lower() and is_plural(name))  # "a clips..."
                    or "_" in old_desc  # underscore
                    or " has " in old_desc and is_plural(name)  # "clips has" → "clips have"
                )
                if has_problem:
                    attr["description"] = descs["change_desc"]
                    changes.append(f"Fixed grammar: '{old_desc}' → '{descs['change_desc']}'")

            # Fix grammar in value descriptions (only where broken)
            for val in attr.get("values", []):
                vname = val.get("name", "")
                old_desc = val.get("description", "")
                if vname in descs and old_desc != descs[vname]:
                    has_problem = (
                        " is " in old_desc and is_plural(name)  # plural verb agreement
                        or " has " in old_desc and is_plural(name)  # plural verb
                        or "_" in old_desc  # underscore
                    )
                    if has_problem:
                        val["description"] = descs[vname]
                        changes.append(f"Fixed grammar: '{old_desc}' → '{descs[vname]}'")


            # --- Winnow direction-of-change values ---
            category = classify_finding(name)
            current_values = attr.get("values", [])
            base_names = {"unchanged", "stable", "new", "resolved"}

            if category == "none":
                # Keep only base values
                new_values = [v for v in current_values if v["name"] in base_names]
                removed = [v["name"] for v in current_values if v["name"] not in base_names]
                if removed:
                    changes.append(f"Removed direction values: {removed}")
                attr["values"] = new_values

            elif category == "worsened_improved":
                # Remove larger/smaller and increased/decreased, add worsened/improved
                keep = base_names | {"worsened", "improved"}
                remove = {"larger", "smaller", "increased", "decreased"}
                new_values = [v for v in current_values if v["name"] not in remove]
                removed = [v["name"] for v in current_values if v["name"] in remove]

                # Add worsened/improved if not present
                existing_names = {v["name"] for v in new_values}
                if "worsened" not in existing_names:
                    # Find the oifma_id for value_code generation
                    oifma_id = attr.get("oifma_id", "")
                    next_idx = len(new_values)
                    new_values.append({
                        "value_code": f"{oifma_id}.{next_idx}",
                        "name": "worsened",
                        "description": descs["worsened"],
                    })
                if "improved" not in existing_names:
                    oifma_id = attr.get("oifma_id", "")
                    next_idx = len(new_values)
                    new_values.append({
                        "value_code": f"{oifma_id}.{next_idx}",
                        "name": "improved",
                        "description": descs["improved"],
                    })

                if removed:
                    changes.append(f"Removed direction values: {removed}, added worsened/improved")
                attr["values"] = new_values

            elif category == "larger_smaller":
                # Remove increased/decreased, keep larger/smaller
                remove = {"increased", "decreased"}
                new_values = [v for v in current_values if v["name"] not in remove]
                removed = [v["name"] for v in current_values if v["name"] in remove]
                if removed:
                    changes.append(f"Removed direction values: {removed}")
                attr["values"] = new_values

            elif category == "increased_decreased":
                # Remove larger/smaller, keep increased/decreased
                remove = {"larger", "smaller"}
                new_values = [v for v in current_values if v["name"] not in remove]
                removed = [v["name"] for v in current_values if v["name"] in remove]
                if removed:
                    changes.append(f"Removed direction values: {removed}")
                attr["values"] = new_values

            # Renumber value codes sequentially
            oifma_id = attr.get("oifma_id", "")
            for i, val in enumerate(attr.get("values", [])):
                val["value_code"] = f"{oifma_id}.{i}"

    # --- Write if changes were made ---
    if changes and not dry_run:
        p.write_text(json.dumps(d, indent=2) + "\n")

    return changes


def main():
    parser = argparse.ArgumentParser(description="Bulk fix finding models from review")
    parser.add_argument("--dry-run", action="store_true", help="Print changes without writing")
    parser.add_argument("files", nargs="*", help="Specific files (default: all OIDM models)")
    args = parser.parse_args()

    if args.files:
        files = args.files
    else:
        # Find all OIDM models
        files = []
        for fp in sorted(Path("defs").glob("*.fm.json")):
            try:
                d = json.loads(fp.read_text())
                if d.get("oifm_id", "").startswith("OIFM_OIDM_"):
                    files.append(str(fp))
            except Exception:
                pass

    total_changed = 0
    total_changes = 0

    for filepath in files:
        changes = fix_model(filepath, dry_run=args.dry_run)
        if changes:
            total_changed += 1
            total_changes += len(changes)
            print(f"\n{filepath}:")
            for c in changes:
                print(f"  {c}")

    prefix = "[DRY RUN] " if args.dry_run else ""
    print(f"\n{prefix}Files changed: {total_changed}/{len(files)}, Total fixes: {total_changes}")


if __name__ == "__main__":
    main()
