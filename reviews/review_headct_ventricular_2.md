# Review: headct_ventricular (batch 2)

10 models to review. For each, check name, description, synonyms, and direction-of-change values. Add your response below each entry.

---

### intraventricular debris

**Source file:** `defs/intraventricular_debris.fm.json`  
**ID:** `OIFM_OIDM_888865`  
**Description:** Sediment or particulate material within the cerebral ventricles.  
**Synonyms:** `ventricular debris`, `intraventricular sediment`  
**Change from prior:** `unchanged`, `stable`, `new`, `resolved`, `increased`, `decreased`

**CSV source:** id=HID3710, category=ventricular, parent_id=HID3600, finding_type=observation
**CSV synonyms:** ventricular debris, intraventricular sediment

**Assessment:** New model created from CSV. Please confirm name, description, and synonyms are appropriate.

**Response:** drop `ventricular debris` — cross-body collision with cardiac ventricle. keep `intraventricular sediment`.

---

### intraventricular hemorrhage

**Source file:** `defs/intraventricular_hemorrhage.fm.json`  
**ID:** `OIFM_OIDM_050265`  
**Description:** Blood within the ventricular system of the brain, seen on CT as hyperdense material layering in the dependent portions of the ventricles (commonly the occipital horns) or as cast-like opacification filling the ventricles. Most often results from extension of intraparenchymal hemorrhage, aneurysm or AVM rupture, or trauma.  
**Synonyms:** `IVH`  
**Change from prior:** `unchanged`, `stable`, `new`, `resolved`, `larger`, `smaller`, `increased`, `decreased`, `worsened`, `improved`

**CSV source:** id=HID3820, category=ventricular, parent_id=HID3600, finding_type=diagnosis
**CSV synonyms:** IVH, ventricular hemorrhage, intraventricular blood products

**Assessment:** New model created from CSV. Please confirm name, description, and synonyms are appropriate.
**NOTE:** Capitalized acronyms as synonyms: `IVH` — verify these are standard abbreviations.

**Response:** ok. add `intraventricular blood products` as synonym — true equivalent radiology phrasing.

---

### intraventricular mass

**Source file:** `defs/intraventricular_mass.fm.json`  
**ID:** `OIFM_OIDM_032421`  
**Description:** A space-occupying lesion within the cerebral ventricular system.  
**Synonyms:** (none)  
**Change from prior:** `unchanged`, `stable`, `new`, `resolved`, `larger`, `smaller`

**CSV source:** id=HID3750, category=ventricular, parent_id=HID3600, finding_type=observation

**Assessment:** New model created from CSV. Please confirm name, description, and synonyms are appropriate.

**Response:** map CSV row to existing `intraventricular_lesion` (OIFM_GMTS_007340); retire the newly created `intraventricular_mass.fm.json`. per the soft_tissue_lesion precedent: lesion is the neutral generic term, mass implies size threshold.

mistakes to fix on the existing intraventricular_lesion model:
- flip finding_type to neutral — this is a morphologic-grouping intermediate parent (children include intraventricular_neoplasm and choroid_plexus_cyst), parallels sellar_mass and extra_axial_cyst.
- drop synonym `Ventricular mass` — cross-body collision with cardiac.
- drop synonym `Cerebral ventricle lesion` — awkward phrasing, not used.
- add `intraventricular mass` as synonym.
- description is sparse ("Abnormal mass located within the ventricular system of the brain."). rewrite to: "A space-occupying lesion within the cerebral ventricular system, encompassing neoplastic, cystic, and inflammatory etiologies."

---

### intraventricular neoplasm

**Source file:** `defs/intraventricular_neoplasm.fm.json`  
**ID:** `OIFM_OIDM_002069`  
**Description:** A tumor arising within or extending into the cerebral ventricular system.  
**Synonyms:** (none)  
**Change from prior:** `unchanged`, `stable`, `new`, `resolved`, `larger`, `smaller`

**CSV source:** id=HID3850, category=ventricular, parent_id=HID3600, finding_type=diagnosis

**Assessment:** New model created from CSV. Please confirm name, description, and synonyms are appropriate.

**Response:** add synonym `intraventricular tumor` — true equivalent. otherwise ok.

---

### monoventricle

**Source file:** `defs/monoventricle.fm.json`  
**ID:** `OIFM_OIDM_047255`  
**Description:** A single midline ventricular cavity rather than the normal paired lateral ventricles.  
**Synonyms:** `single midline ventricle`, `single ventricular cavity`, `holoventricle`  
**Change from prior:** `unchanged`, `stable`, `new`, `resolved`

**CSV source:** id=HID3665, category=ventricular, parent_id=HID3600, finding_type=observation
**CSV synonyms:** single midline ventricle, single ventricular cavity, holoventricle

**Assessment:** New model created from CSV. Please confirm name, description, and synonyms are appropriate.

**Response:** drop `single ventricular cavity` — cross-body collision with cardiac single ventricle (Fontan, HLHS). keep `single midline ventricle` (midline qualifier disambiguates) and `holoventricle`.

---

### normal pressure hydrocephalus

**Source file:** `defs/normal_pressure_hydrocephalus.fm.json`  
**ID:** `OIFM_OIDM_559938`  
**Description:** A syndrome of gait disturbance, cognitive decline, and urinary incontinence with ventriculomegaly and normal opening pressure on lumbar puncture.  
**Synonyms:** `NPH`  
**Change from prior:** `unchanged`, `stable`, `new`, `resolved`, `worsened`, `improved`

**CSV source:** id=HID3815, category=ventricular, parent_id=HID3800, finding_type=diagnosis
**CSV synonyms:** NPH

**Assessment:** New model created from CSV. Please confirm name, description, and synonyms are appropriate.
**NOTE:** Capitalized acronyms as synonyms: `NPH` — verify these are standard abbreviations.

**Response:** ok

---

### obstructive hydrocephalus

**Source file:** `defs/obstructive_hydrocephalus.fm.json`  
**ID:** `OIFM_GMTS_018270`  
**Description:** Accumulation of cerebrospinal fluid in the ventricles due to blockage.  
**Synonyms:** (none)  
**Change from prior:** `unchanged`, `stable`, `new`, `resolved`, `increased`, `decreased`, `larger`, `smaller`

**CSV source:** id=HID3805, category=ventricular, parent_id=HID3800, finding_type=diagnosis
**CSV synonyms:** non-communicating hydrocephalus, intraventricular obstructive hydrocephalus

**Assessment:** New model created from CSV. Please confirm name, description, and synonyms are appropriate.

**Response:** mapping ok. add CSV synonyms `non-communicating hydrocephalus` and `intraventricular obstructive hydrocephalus` — true equivalents.

description fix: rewrite "Accumulation of cerebrospinal fluid in the ventricles due to blockage." → "Hydrocephalus due to obstruction of CSF flow within the ventricular system, such as at the foramen of Monro, aqueduct of Sylvius, or fourth ventricular outflow."

---

### small ventricular caliber

**Source file:** `defs/small_ventricular_caliber.fm.json`  
**ID:** `OIFM_OIDM_458263`  
**Description:** Cerebral ventricles that are smaller than expected for age.  
**Synonyms:** `small ventricles`, `slit ventricles`, `slit-like ventricles`  
**Change from prior:** `unchanged`, `stable`, `new`, `resolved`, `larger`, `smaller`

**CSV source:** id=HID3660, category=ventricular, parent_id=HID3600, finding_type=observation
**CSV synonyms:** small ventricles, slit ventricles, slit-like ventricles

**Assessment:** New model created from CSV. Please confirm name, description, and synonyms are appropriate.

**Response:** ok

---

### subependymal nodule

**Source file:** `defs/subependymal_nodule.fm.json`  
**ID:** `OIFM_OIDM_816696`  
**Description:** A small nodular lesion along the ventricular ependymal lining.  
**Synonyms:** (none)  
**Change from prior:** `unchanged`, `stable`, `new`, `resolved`, `larger`, `smaller`

**CSV source:** id=HID3760, category=ventricular, parent_id=HID3600, finding_type=observation

**Assessment:** New model created from CSV. Please confirm name, description, and synonyms are appropriate.

**Response:** ok

---

### temporal horn entrapment

**Source file:** `defs/temporal_horn_entrapment.fm.json`  
**ID:** `OIFM_OIDM_065919`  
**Description:** An isolated temporal horn that is obstructed and no longer communicates with the remainder of the ventricular system.  
**Synonyms:** `trapped temporal horn`  
**Change from prior:** `unchanged`, `stable`, `new`, `resolved`

**CSV source:** id=HID3705, category=ventricular, parent_id=HID3700, finding_type=observation
**CSV synonyms:** trapped temporal horn

**Assessment:** New model created from CSV. Please confirm name, description, and synonyms are appropriate.

**Response:** ok — lexicalized site-specific subtype with distinct clinical context, parallels macroadenoma/partially_empty_sella precedents.

---
