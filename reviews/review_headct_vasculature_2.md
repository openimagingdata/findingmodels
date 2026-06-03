# Review: head CT vasculature batch 2

10 vasculature CSV decisions to review: 6 newly created models and 4 mappings to existing models. For each, check name, description, synonyms, direction-of-change values, and whether the CSV row should map to the listed OIFM ID. Add your response below each entry.

---

### internal carotid artery occlusion
**Source file:** `defs/internal_carotid_artery_occlusion.fm.json`  
**ID:** `OIFM_OIDM_529761`  
**Description:** Imaging observation of internal carotid artery occlusion involving intracranial or head and neck vasculature on head CT, CTA, or related neurovascular imaging.  
**Synonyms:** ICA occlusion, carotid occlusion  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID4460`; `name=internal_carotid_artery_occlusion`; `category=vasculature`; `parent_id=HID4450`; `synonyms=ICA occlusion, carotid occlusion`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the vasculature CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**ISSUE:** Mechanical review flagged uppercase acronym/eponym synonyms. Confirm capitalization is intentional for standard abbreviations or proper names.

**Response:** 

---

### basilar artery occlusion
**Source file:** `defs/basilar_artery_occlusion.fm.json`  
**ID:** `OIFM_OIDM_047634`  
**Description:** Imaging observation of basilar artery occlusion involving intracranial or head and neck vasculature on head CT, CTA, or related neurovascular imaging.  
**Synonyms:** BAO, basilar occlusion  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID4465`; `name=basilar_artery_occlusion`; `category=vasculature`; `parent_id=HID4450`; `synonyms=BAO, basilar occlusion`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the vasculature CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**ISSUE:** Mechanical review flagged uppercase acronym/eponym synonyms. Confirm capitalization is intentional for standard abbreviations or proper names.

**Response:** 

---

### intracranial dolichoectasia
**Source file:** `defs/intracranial_dolichoectasia.fm.json`  
**ID:** `OIFM_OIDM_577168`  
**Description:** Imaging observation of intracranial dolichoectasia involving intracranial or head and neck vasculature on head CT, CTA, or related neurovascular imaging.  
**Synonyms:** dolichoectasia  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID4470`; `name=intracranial_dolichoectasia`; `category=vasculature`; `parent_id=HID4400`; `synonyms=dolichoectasia`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the vasculature CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### matched: intracranial_aneurysm -> Cerebral Aneurysm
**Source file:** `defs/cerebral_aneurysm.fm.json`  
**ID:** `OIFM_MSFT_440456`  
**Description:** An abnormal bulging in a blood vessel in the brain that can lead to serious complications such as rupture or hemorrhage.  
**Synonyms:** Intracranial Aneurysm, Brain Aneurysm, Cerebral Aneurysm (CA)  
**Change from prior:** (missing)

**Source CSV:** `id=HID4500`; `name=intracranial_aneurysm`; `category=vasculature`; `parent_id=HID4400`; `synonyms=cerebral aneurysm`; `finding_type=diagnosis`; `oifm_id=(blank)`

**QUESTION:** This row maps intracranial aneurysm to the existing Cerebral Aneurysm model because intracranial aneurysm is an explicit synonym. Confirm this equivalence is acceptable.

**Response:** 

---

### saccular aneurysm
**Source file:** `defs/saccular_aneurysm.fm.json`  
**ID:** `OIFM_OIDM_231457`  
**Description:** Diagnosis of saccular aneurysm, as recognized on head CT, CTA, or related neurovascular imaging.  
**Synonyms:** berry aneurysm  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID4505`; `name=saccular_aneurysm`; `category=vasculature`; `parent_id=HID4500`; `synonyms=berry aneurysm`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the vasculature CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### fusiform aneurysm
**Source file:** `defs/fusiform_aneurysm.fm.json`  
**ID:** `OIFM_OIDM_324720`  
**Description:** Diagnosis of fusiform aneurysm, as recognized on head CT, CTA, or related neurovascular imaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID4510`; `name=fusiform_aneurysm`; `category=vasculature`; `parent_id=HID4500`; `synonyms=(blank)`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the vasculature CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### matched: cerebral_venous_thrombosis -> cerebral venous thrombosis
**Source file:** `defs/cerebral_venous_thrombosis.fm.json`  
**ID:** `OIFM_OIDM_945136`  
**Description:** Thrombosis of the intracranial venous system, encompassing the dural venous sinuses and/or cortical veins. On CT, suggestive findings include a hyperdense vessel sign on unenhanced imaging and the empty delta sign on contrast-enhanced imaging.  
**Synonyms:** CVT, intracranial venous thrombosis  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased

**Source CSV:** `id=HID4550`; `name=cerebral_venous_thrombosis`; `category=vasculature`; `parent_id=HID4400`; `synonyms=CVT`; `finding_type=diagnosis`; `oifm_id=(blank)`

**QUESTION:** This row maps cerebral venous thrombosis to the existing cerebral venous thrombosis model. Confirm direct mapping.

**Response:** 

---

### matched: dural_venous_sinus_thrombosis -> dural sinus thrombosis
**Source file:** `defs/dural_sinus_thrombosis.fm.json`  
**ID:** `OIFM_GMTS_017947`  
**Description:** The formation of a blood clot in one of the brain's dural venous sinuses.  
**Synonyms:** dural venous sinus thrombosis, Cerebral venous sinus thrombosis  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID4555`; `name=dural_venous_sinus_thrombosis`; `category=vasculature`; `parent_id=HID4550`; `synonyms=CVST`; `finding_type=diagnosis`; `oifm_id=(blank)`

**QUESTION:** This row maps dural venous sinus thrombosis to the existing dural sinus thrombosis model. Confirm wording equivalence is acceptable.

**Response:** 

---

### cortical vein thrombosis
**Source file:** `defs/cortical_vein_thrombosis.fm.json`  
**ID:** `OIFM_OIDM_641040`  
**Description:** Diagnosis of cortical vein thrombosis, as recognized on head CT, CTA, or related neurovascular imaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID4560`; `name=cortical_vein_thrombosis`; `category=vasculature`; `parent_id=HID4550`; `synonyms=(blank)`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the vasculature CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### matched: intracranial_vascular_malformation -> cerebrovascular malformation
**Source file:** `defs/cerebrovascular_malformation.fm.json`  
**ID:** `OIFM_GMTS_025616`  
**Description:** Abnormalities in the blood vessels of the brain.  
**Synonyms:** cerebral vascular malformation  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID4600`; `name=intracranial_vascular_malformation`; `category=vasculature`; `parent_id=HID4400`; `synonyms=vascular malformation`; `finding_type=diagnosis`; `oifm_id=(blank)`

**QUESTION:** This row maps intracranial vascular malformation to the existing cerebrovascular malformation model. Confirm this is preferred over broader vascular malformation.

**Response:** 

