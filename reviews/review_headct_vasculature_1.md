# Review: head CT vasculature batch 1

10 vasculature CSV decisions to review: 9 newly created models and 1 mappings to existing models. For each, check name, description, synonyms, direction-of-change values, and whether the CSV row should map to the listed OIFM ID. Add your response below each entry.

---

### vascular abnormality
**Source file:** `defs/vascular_abnormality.fm.json`  
**ID:** `OIFM_OIDM_066373`  
**Description:** Broad grouping for vascular abnormality findings involving intracranial or head and neck vasculature on head CT, CTA, or related neurovascular imaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID4400`; `name=vascular_abnormality`; `category=vasculature`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`; `oifm_id=(blank)`

**Assessment:** Newly created from the vasculature CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### hyperdense artery sign
**Source file:** `defs/hyperdense_artery_sign.fm.json`  
**ID:** `OIFM_OIDM_048244`  
**Description:** Imaging observation of hyperdense artery sign involving intracranial or head and neck vasculature on head CT, CTA, or related neurovascular imaging.  
**Synonyms:** dense vessel sign, dot sign  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID4405`; `name=hyperdense_artery_sign`; `category=vasculature`; `parent_id=HID4400`; `synonyms=dense vessel sign, dot sign`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the vasculature CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### dense sinus sign
**Source file:** `defs/dense_sinus_sign.fm.json`  
**ID:** `OIFM_OIDM_058991`  
**Description:** Imaging observation of dense sinus sign involving intracranial or head and neck vasculature on head CT, CTA, or related neurovascular imaging.  
**Synonyms:** hyperdense sinus  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID4410`; `name=dense_sinus_sign`; `category=vasculature`; `parent_id=HID4400`; `synonyms=hyperdense sinus`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the vasculature CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### empty delta sign
**Source file:** `defs/empty_delta_sign.fm.json`  
**ID:** `OIFM_OIDM_135018`  
**Description:** Imaging observation of empty delta sign involving intracranial or head and neck vasculature on head CT, CTA, or related neurovascular imaging.  
**Synonyms:** empty triangle sign  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID4415`; `name=empty_delta_sign`; `category=vasculature`; `parent_id=HID4400`; `synonyms=empty triangle sign`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the vasculature CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### cord sign
**Source file:** `defs/cord_sign.fm.json`  
**ID:** `OIFM_OIDM_127628`  
**Description:** Imaging observation of cord sign involving intracranial or head and neck vasculature on head CT, CTA, or related neurovascular imaging.  
**Synonyms:** hyperdense cortical vein  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID4420`; `name=cord_sign`; `category=vasculature`; `parent_id=HID4400`; `synonyms=hyperdense cortical vein`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the vasculature CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### intracranial vascular calcification
**Source file:** `defs/intracranial_vascular_calcification.fm.json`  
**ID:** `OIFM_OIDM_958649`  
**Description:** Imaging observation of intracranial vascular calcification involving intracranial or head and neck vasculature on head CT, CTA, or related neurovascular imaging.  
**Synonyms:** arterial wall calcification  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID4425`; `name=intracranial_vascular_calcification`; `category=vasculature`; `parent_id=HID4400`; `synonyms=arterial wall calcification`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the vasculature CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### active contrast extravasation
**Source file:** `defs/active_contrast_extravasation.fm.json`  
**ID:** `OIFM_OIDM_105363`  
**Description:** Imaging observation of active contrast extravasation involving intracranial or head and neck vasculature on head CT, CTA, or related neurovascular imaging.  
**Synonyms:** spot sign, contrast blush, active extravasation  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID4430`; `name=active_contrast_extravasation`; `category=vasculature`; `parent_id=HID4400`; `synonyms=spot sign, contrast blush, active extravasation`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the vasculature CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### intracranial arterial stenosis
**Source file:** `defs/intracranial_arterial_stenosis.fm.json`  
**ID:** `OIFM_OIDM_687450`  
**Description:** Imaging observation of intracranial arterial stenosis involving intracranial or head and neck vasculature on head CT, CTA, or related neurovascular imaging.  
**Synonyms:** intracranial arterial narrowing  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID4435`; `name=intracranial_arterial_stenosis`; `category=vasculature`; `parent_id=HID4400`; `synonyms=intracranial arterial narrowing`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the vasculature CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### matched: large_vessel_occlusion -> Large Vessel Occlusion
**Source file:** `defs/large_vessel_occlusion.fm.json`  
**ID:** `OIFM_MSFT_761982`  
**Description:** A condition characterized by the blockage of a large blood vessel, typically affecting cerebral circulation and leading to stroke.  
**Synonyms:** LVO  
**Change from prior:** (missing)

**Source CSV:** `id=HID4450`; `name=large_vessel_occlusion`; `category=vasculature`; `parent_id=HID4400`; `synonyms=LVO`; `finding_type=observation`; `oifm_id=(blank)`

**QUESTION:** This row maps large vessel occlusion to the existing Large Vessel Occlusion model. Confirm use of this existing MSFT model despite its nonstandard first attribute name.

**Response:** 

---

### middle cerebral artery occlusion
**Source file:** `defs/middle_cerebral_artery_occlusion.fm.json`  
**ID:** `OIFM_OIDM_910617`  
**Description:** Imaging observation of middle cerebral artery occlusion involving intracranial or head and neck vasculature on head CT, CTA, or related neurovascular imaging.  
**Synonyms:** MCA occlusion  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID4455`; `name=middle_cerebral_artery_occlusion`; `category=vasculature`; `parent_id=HID4450`; `synonyms=MCA occlusion`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the vasculature CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**ISSUE:** Mechanical review flagged uppercase acronym/eponym synonyms. Confirm capitalization is intentional for standard abbreviations or proper names.

**Response:** 

