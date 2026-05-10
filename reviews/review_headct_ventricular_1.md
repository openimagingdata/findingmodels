# Review: headct_ventricular (batch 1)

10 models to review. For each, check name, description, synonyms, and direction-of-change values. Add your response below each entry.

---

### cavum septum pellucidum

**Source file:** `defs/cavum_septum_pellucidum.fm.json`  
**ID:** `OIFM_OIDM_207400`  
**Description:** A normal variant midline CSF-filled cavity between the leaflets of the septum pellucidum.  
**Synonyms:** `CSP`, `cavum septi pellucidi`, `fifth ventricle`  
**Change from prior:** `unchanged`, `stable`, `new`, `resolved`

**CSV source:** id=HID4005, category=ventricular, parent_id=HID4000, finding_type=observation
**CSV synonyms:** CSP, cavum septi pellucidi, fifth ventricle

**Assessment:** New model created from CSV. Please confirm name, description, and synonyms are appropriate.
**NOTE:** Capitalized acronyms as synonyms: `CSP` — verify these are standard abbreviations.

**Response:** drop `fifth ventricle` — misnomer; CSP is not part of the ventricular system. keep `CSP` and `cavum septi pellucidi`.

---

### cavum velum interpositum

**Source file:** `defs/cavum_velum_interpositum.fm.json`  
**ID:** `OIFM_OIDM_089879`  
**Description:** A normal variant CSF-filled space in the pineal region superior to the third ventricle.  
**Synonyms:** `CVI`, `cavum veli interpositi`  
**Change from prior:** `unchanged`, `stable`, `new`, `resolved`

**CSV source:** id=HID4015, category=ventricular, parent_id=HID4000, finding_type=observation
**CSV synonyms:** CVI, cavum veli interpositi

**Assessment:** New model created from CSV. Please confirm name, description, and synonyms are appropriate.
**NOTE:** Capitalized acronyms as synonyms: `CVI` — verify these are standard abbreviations.

**Response:** drop `CVI` — collides with chronic venous insufficiency and cerebral vascular insufficiency. keep `cavum veli interpositi`.

---

### cavum vergae

**Source file:** `defs/cavum_vergae.fm.json`  
**ID:** `OIFM_OIDM_182213`  
**Description:** A normal variant posterior extension of the cavum septum pellucidum into the region of the corpus callosum splenium.  
**Synonyms:** `sixth ventricle`, `cavum psalterii`  
**Change from prior:** `unchanged`, `stable`, `new`, `resolved`

**CSV source:** id=HID4010, category=ventricular, parent_id=HID4000, finding_type=observation
**CSV synonyms:** sixth ventricle, cavum psalterii

**Assessment:** New model created from CSV. Please confirm name, description, and synonyms are appropriate.

**Response:** drop `sixth ventricle` — same misnomer as fifth ventricle on CSP; not part of the ventricular system. keep `cavum psalterii`.

description fix: rewrite "A normal variant posterior extension of the cavum septum pellucidum into the region of the corpus callosum splenium." → "A normal variant posterior extension of the cavum septum pellucidum, beneath the splenium of the corpus callosum."

---

### choroid plexus carcinoma

**Source file:** `defs/choroid_plexus_carcinoma.fm.json`  
**ID:** `OIFM_OIDM_021680`  
**Description:** A malignant tumor arising from the choroid plexus epithelium.  
**Synonyms:** `CPCa`  
**Change from prior:** `unchanged`, `stable`, `new`, `resolved`, `larger`, `smaller`

**CSV source:** id=HID3860, category=ventricular, parent_id=HID3850, finding_type=diagnosis
**CSV synonyms:** CPCa

**Assessment:** New model created from CSV. Please confirm name, description, and synonyms are appropriate.

**Response:** drop `CPCa` — not a commonly dictated abbreviation; loose collision with CPC.

---

### choroid plexus cyst

**Source file:** `defs/choroid_plexus_cyst.fm.json`  
**ID:** `OIFM_OIDM_568953`  
**Description:** A cyst arising from the choroid plexus within the ventricles.  
**Synonyms:** (none)  
**Change from prior:** `unchanged`, `stable`, `new`, `resolved`, `larger`, `smaller`

**CSV source:** id=HID3765, category=ventricular, parent_id=HID3600, finding_type=observation

**Assessment:** New model created from CSV. Please confirm name, description, and synonyms are appropriate.

**Response:** ok

---

### choroid plexus papilloma

**Source file:** `defs/choroid_plexus_papilloma.fm.json`  
**ID:** `OIFM_OIDM_595450`  
**Description:** A benign, highly vascular tumor arising from the choroid plexus epithelium.  
**Synonyms:** `CPP`  
**Change from prior:** `unchanged`, `stable`, `new`, `resolved`, `larger`, `smaller`

**CSV source:** id=HID3855, category=ventricular, parent_id=HID3850, finding_type=diagnosis
**CSV synonyms:** CPP

**Assessment:** New model created from CSV. Please confirm name, description, and synonyms are appropriate.
**NOTE:** Capitalized acronyms as synonyms: `CPP` — verify these are standard abbreviations.

**Response:** drop `CPP` — collides with cerebral perfusion pressure.

---

### colloid cyst

**Source file:** `defs/colloid_cyst.fm.json`  
**ID:** `OIFM_OIDM_879281`  
**Description:** A benign, well-circumscribed cystic lesion typically located at the foramen of Monro.  
**Synonyms:** (none)  
**Change from prior:** `unchanged`, `stable`, `new`, `resolved`, `larger`, `smaller`

**CSV source:** id=HID3755, category=ventricular, parent_id=HID3750, finding_type=observation

**Assessment:** New model created from CSV. Please confirm name, description, and synonyms are appropriate.

**Response:** ok

---

### communicating hydrocephalus

**Source file:** `defs/communicating_hydrocephalus.fm.json`  
**ID:** `OIFM_GMTS_018266`  
**Description:** Hydrocephalus where CSF flow is obstructed post the ventricles.  
**Synonyms:** `non-obstructive hydrocephalus`  
**Change from prior:** `unchanged`, `stable`, `new`, `resolved`, `increased`, `decreased`, `larger`, `smaller`

**CSV source:** id=HID3810, category=ventricular, parent_id=HID3800, finding_type=diagnosis
**CSV synonyms:** extraventricular obstructive hydrocephalus

**Assessment:** Matched to existing model. Please confirm this mapping is correct.

**Response:** mapping ok.

drop existing synonym `non-obstructive hydrocephalus` — legacy term; technically inaccurate since communicating hydrocephalus is obstructive at the arachnoid villi. add CSV synonym `extraventricular obstructive hydrocephalus` — true equivalent in modern phrasing.

description fix: rewrite "Hydrocephalus where CSF flow is obstructed post the ventricles." → "Hydrocephalus due to impaired CSF resorption or flow obstruction distal to the ventricular system, typically at the arachnoid granulations."

---

### ex vacuo ventricular dilation

**Source file:** `defs/ex_vacuo_ventricular_dilation.fm.json`  
**ID:** `OIFM_OIDM_138708`  
**Description:** Compensatory ventricular enlargement secondary to brain parenchymal volume loss, rather than obstructed CSF flow.  
**Synonyms:** `ex vacuo dilatation`, `compensatory ventriculomegaly`, `passive ventricular enlargement`  
**Change from prior:** `unchanged`, `stable`, `new`, `resolved`, `larger`, `smaller`

**CSV source:** id=HID3655, category=ventricular, parent_id=HID3650, finding_type=observation
**CSV synonyms:** ex vacuo dilatation, compensatory ventriculomegaly, passive ventricular enlargement

**Assessment:** New model created from CSV. Please confirm name, description, and synonyms are appropriate.

**Response:** ok

---

### hydrocephalus

**Source file:** `defs/hydrocephalus.fm.json`  
**ID:** `OIFM_GMTS_007816`  
**Description:** Accumulation of cerebrospinal fluid in the brain ventricles leading to increased pressure.  
**Synonyms:** `hydrocephaly`, `fetal ventriculomegaly`  
**Change from prior:** `unchanged`, `stable`, `new`, `resolved`, `increased`, `decreased`, `larger`, `smaller`

**CSV source:** id=HID3800, category=ventricular, parent_id=HID3600, finding_type=diagnosis

**Assessment:** Matched to existing model. Please confirm this mapping is correct.

**Response:** mapping ok.

drop synonym `fetal ventriculomegaly` — distinct prenatal observation that may or may not progress to hydrocephalus; different diagnostic commitment. keep `hydrocephaly`.

description fix: rewrite "Accumulation of cerebrospinal fluid in the brain ventricles leading to increased pressure." → "Abnormal accumulation of cerebrospinal fluid causing dilation of the ventricular system." (the "increased pressure" phrasing is wrong for NPH.)

---
