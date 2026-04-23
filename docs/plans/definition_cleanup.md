# Definition Cleanup Plan

Status: **DRAFT — for review**

This plan covers cleaning up existing finding model definitions (primarily GMTS, CDE, and MGB sources) to align with the conventions distilled in `prompts/fragments/` (naming, synonym strictness, scope-and-specificity, presence-and-change, associated-vs-component). This is a separate workstream from creating new models.

## Scope

2,379 total models:
- GMTS: 1,934 (gamuts — the bulk of the work)
- OIDM: 264 (our models — already reviewed/fixed in the CXR findings session)
- CDE: 115 (ACR/RSNA Common Data Elements)
- MGB: 47 (Mass General Brigham)
- MSFT: 19 (Microsoft)

## Issue Categories

### 1. Capitalization (123 models — mostly CDE and MGB)

CDE and MGB models use Title Case: `"Acute Aortic Syndrome"`, `"Aortic Valve Replacement"`, `"Peripherally Inserted Central Catheter (Picc)"`.

**Action:** Lowercase all names. Move acronyms to synonyms.

Examples:
- `"Acute Aortic Syndrome"` → `"acute aortic syndrome"`
- `"Peripherally Inserted Central Catheter (Picc)"` → name: `"peripherally inserted central catheter"`, synonym: `"PICC"`
- `"AO Spine Subaxial Cervical Spine injury Classification"` → name: `"ao spine subaxial cervical spine injury classification"` (but see: this is really a scoring system, not a finding — may need reclassification)

### 2. Missing Standard Attributes (124 models — mostly CDE)

These models don't have `presence` as their first attribute. Two sub-categories:

**a) Models with domain-specific first attributes:**
CDE models often jump straight into clinical attributes: `"Acute Clavicle Fracture"` starts with `"side"`, `"Acute Diverticulitis"` starts with `"sigmoid colon wall thickness"`.

**Action:** Add `presence` and `change from prior` as first two attributes, with clinically appropriate direction-of-change values. Shift existing attributes after them.

**b) Models that aren't really findings:**
Some CDE entries are measurement protocols or scoring systems: `"Alpha Angle Measurement"`, `"Aortic Measurements"`, `"Automated Insall-Salvatti Index"`. These don't have presence/absence because they're not observations — they're quantification tools.

**Action:** Flag for reclassification. These may need a different model type or to be tagged differently.

### 3. "With" Clauses (71 models — all GMTS)

These embed associated findings or qualifiers into the name. Most are gamuts patterns describing a combination of findings that narrows a differential diagnosis.

**Sub-categories:**

**a) Finding + associated finding (should split):**
- `"arthritis with soft-tissue nodules"` → separate `"arthritis"` + `"soft-tissue nodules"`
- `"arthritis with osteoporosis"` → separate `"arthritis"` + `"osteoporosis"`
- `"arthritis with subluxation"` → separate `"arthritis"` + `"subluxation"`
- `"diffuse interstitial disease with pleural effusion"` → separate `"diffuse interstitial disease"` + `"pleural effusion"`

**b) Finding + qualifier that's really an attribute:**
- `"bowel wall thickening with heterogeneous enhancement"` → name: `"bowel wall thickening"`, attribute: enhancement pattern
- `"bowel wall thickening with homogeneous enhancement"` → same model, different attribute value
- `"bone lesion with fluid-fluid level"` → name: `"bone lesion"`, attribute: fluid-fluid level (present/absent)
- `"cystic renal mass with wall calcification"` → name: `"cystic renal mass"`, attribute: wall calcification

**c) Finding + context that's a gamuts differential pattern:**
- `"acyanotic congenital heart disease with increased pulmonary vascularity"` — this is a radiographic pattern used to narrow a differential (e.g., VSD vs ASD vs PDA). The "with increased pulmonary vascularity" is integral to the pattern.
- `"cyanotic congenital heart disease with precapillary hypertension vascularity"` — same idea.

**Action for (c):** These are genuinely gamuts-specific constructs. They may be better modeled as gamuts (differential diagnosis patterns) rather than finding models. Flag for discussion — they may need a different model type or to be deprecated as finding models and preserved as gamuts references only.

### 4. Population Qualifiers (84 models — all GMTS)

Names that embed age group or patient population:
- `"abdominal calcification in an infant or child"`
- `"cerebellar mass in a child"` vs `"cerebellar mass in an adult"`
- `"brain tumor in an infant"`
- `"bubbly lungs in infants and children"`
- `"cavitary lung lesion in an infant or child"`

Many of these exist as pairs (child version + adult version) for the same finding, because the differential diagnosis differs by age.

**Action (interim):** Strip the population qualifier from the name. Add a standardized tag (e.g., `"pediatric"`, `"neonatal"`, `"adult"`) so the population context isn't lost. When the age-range tagging feature (in progress on another branch) is ready, migrate these tags to explicit age ranges.

**Action (long-term):** Merge child/adult pairs into a single finding model where the underlying observation is the same. The differential diagnosis context (which differs by age) belongs in gamuts references, not in the finding model name.

Examples:
- `"cerebellar mass in a child"` + `"cerebellar mass in an adult"` → single model `"cerebellar mass"`, age-specific differential context in gamuts
- `"abdominal calcification in an infant or child"` → `"abdominal calcification"`, tag: `"pediatric"`

### 5. Parenthetical Qualifiers (10 models — mixed CDE/MGB)

Names with parenthetical acronyms, brand names, or scoring system identifiers:
- `"Cutaneous Cardiac Rhythm Monitor (Zio Patch)"` → name: `"cutaneous cardiac rhythm monitor"`, synonym: `"Zio Patch"`
- `"Peripherally Inserted Central Catheter (Picc)"` → name: `"peripherally inserted central catheter"`, synonym: `"PICC"`
- `"Epidural Spinal Cord Compression Scale (ESCC)"` → name: `"epidural spinal cord compression scale"`, synonym: `"ESCC"`
- `"Glasgow Coma Scale (GCS)"` → name: `"Glasgow coma scale"`, synonym: `"GCS"` (Glasgow is a proper noun — stays capitalized)
- `"MTA-Scale for Medial Temporal Lobe Atrophy (Scheltens Classification)"` → name: `"medial temporal lobe atrophy scale"`, synonyms: `"MTA scale"`, `"Scheltens classification"`
- `"Prostate Imaging Reporting and Data System (PI-RADS)"` → name: `"prostate imaging reporting and data system"`, synonym: `"PI-RADS"`

**Action:** Remove parentheticals, move contents to synonyms. Fix capitalization.

### 6. Comma-Separated Lists (7 models — all GMTS)

Names listing multiple entities:
- `"acquired absence of phalanx, digit, hand, or foot"`
- `"congenital absence of phalanx, digit, hand, or foot"`
- `"fragmented, irregular, or sclerotic carpal or tarsal bones"`
- `"erosion of the petrous ridge, pyramid, or apex"`
- `"lesions of the hypopharynx, larynx, and upper trachea"`
- `"lucent defect in bones of hands, wrists, feet, or ankles"`
- `"Morphometric CT Quantification of Liver, Spleen, and Abdominal Fat"`

**Action:** Case by case:
- Anatomic lists (phalanx/digit/hand/foot) → simplify to broadest applicable term or split by anatomy
- Descriptor lists (fragmented/irregular/sclerotic) → these are gamuts patterns listing the appearance; consider if one finding model with appearance as an attribute is better
- Multi-organ quantification → probably needs to be split per organ

### 7. Slash-Separated Alternatives (8 models — all GMTS)

- `"cleft lip/palate"` — leave as-is (clinically grouped)
- `"encephalocele/meningocele"` — split (genuinely different findings)
- `"leukodystrophy / leukoencephalopathy"` — pick one, synonym the other
- `"mandibular agenesis/dysgenesis"` — consider severity attribute instead
- `"csf-intensity sellar/suprasellar lesion"` — location becomes an attribute
- `"gyriform cortical/subcortical t1 hyperintensity"` — location becomes an attribute
- `"gyriform cortical/subcortical t2 hypointensity"` — same
- `"salivary gland/duct abnormality"` — split or make anatomy an attribute

### 8. And/Or Compounds (3 models)

- `"mediastinal and/or hilar lymph node enlargement"` — split into `"mediastinal lymph node enlargement"` and `"hilar lymph node enlargement"`
- `"carpal and/or tarsal fusion"` — split by anatomy
- `"small or dysplastic carpal and/or tarsal bones"` — complex; needs simplification and splitting

### 9. Gamuts-Specific Patterns That May Not Be Findings

Some GMTS entries describe differential diagnosis patterns rather than individual findings. These use constructions like:
- "X with Y" where Y narrows the differential
- Long descriptive phrases that read like textbook entries
- Names > 60 characters (14 models)

Examples:
- `"cystic and saccular lesions of bile ducts with dilatation of intrahepatic bile ducts"` (84 chars)
- `"cyanotic congenital heart disease with precapillary hypertension vascularity"` (76 chars)
- `"right to left shunt or admixture lesion in congenital heart disease"` (67 chars)
- `"diffuse interstitial lung disease with associated lymphadenopathy"` (65 chars)
- `"tumor like bone destruction with little periosteal reaction"` (59 chars)

**Action:** Review whether these should remain as finding models, be reclassified as gamuts patterns (a different model type), or be decomposed into constituent findings with the differential context preserved as gamuts references.

## Suggested Execution Order

1. **Capitalization + parentheticals** (133 models) — mechanical, safe, high confidence
2. **Missing standard attributes** (124 models) — mostly mechanical, but needs clinical judgment for direction-of-change values
3. **Population qualifiers** (84 models) — straightforward name simplification + tagging
4. **Synonym audit** — run the synonym strictness rules across all models (not yet counted)
5. **"With" clauses** (71 models) — needs case-by-case clinical judgment
6. **Comma/slash/and-or** (18 models) — small count, each needs individual attention
7. **Gamuts reclassification** (TBD) — needs broader design discussion about what model types we support

## Notes

- Each phase should use the review process (mechanical lint + LLM sub-agent review) before committing
- The OIDM models (264) have already been through this process in the CXR findings session
- Changes to GMTS models should preserve the original GMTS name as a synonym so that existing gamuts references still resolve
- The `model_file_name()` function in the library may need to be updated to handle consecutive-underscore prevention
