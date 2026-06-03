# Review: head CT brain_parenchyma batch 3

10 brain_parenchyma CSV decisions to review: 8 newly created models and 2 mappings to existing models. For each, check name, description, synonyms, direction-of-change values, and whether the CSV row should map to the listed OIFM ID. Add your response below each entry.

---

### extracranial herniation
**Source file:** `defs/extracranial_herniation.fm.json`  
**ID:** `OIFM_OIDM_617772`  
**Description:** Imaging observation of extracranial herniation within the brain parenchyma on head CT or related neuroimaging.  
**Synonyms:** transcalvarial herniation, external herniation, transdural herniation, transcranial herniation  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0480`; `name=extracranial_herniation`; `category=brain_parenchyma`; `parent_id=HID0350`; `synonyms=transcalvarial herniation, external herniation, transdural herniation, transcranial herniation`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### intra axial lesion
**Source file:** `defs/intra_axial_lesion.fm.json`  
**ID:** `OIFM_OIDM_582415`  
**Description:** Imaging observation of intra axial lesion within the brain parenchyma on head CT or related neuroimaging.  
**Synonyms:** brain lesion, intraparenchymal lesion, brain mass, intraparenchymal mass  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0500`; `name=intra_axial_lesion`; `category=brain_parenchyma`; `parent_id=HID0200`; `synonyms=brain lesion, intraparenchymal lesion, brain mass, intraparenchymal mass`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### intra axial cyst
**Source file:** `defs/intra_axial_cyst.fm.json`  
**ID:** `OIFM_OIDM_093105`  
**Description:** Imaging observation of intra axial cyst within the brain parenchyma on head CT or related neuroimaging.  
**Synonyms:** brain cyst, parenchymal cyst  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0505`; `name=intra_axial_cyst`; `category=brain_parenchyma`; `parent_id=HID0500`; `synonyms=brain cyst, parenchymal cyst`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### matched: cerebral_atrophy -> cerebral atrophy
**Source file:** `defs/cerebral_atrophy.fm.json`  
**ID:** `OIFM_OIDM_786384`  
**Description:** Cerebral atrophy denotes loss of cerebral parenchymal volume, often diffuse but can be regional. The original phrase provided, "cerebral volume loss", is a commonly used radiology descriptor for this finding.  
**Synonyms:** cerebral volume loss, global cerebral atrophy, brain atrophy, diffuse cerebral atrophy, cerebral parenchymal loss  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0550`; `name=cerebral_atrophy`; `category=brain_parenchyma`; `parent_id=HID0200`; `synonyms=brain atrophy, brain volume loss, cerebral volume loss`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Existing-model mapping. Confirm this CSV row should map to the listed OIFM ID.

**Response:** 

---

### matched: generalized_atrophy -> cerebral atrophy
**Source file:** `defs/cerebral_atrophy.fm.json`  
**ID:** `OIFM_OIDM_786384`  
**Description:** Cerebral atrophy denotes loss of cerebral parenchymal volume, often diffuse but can be regional. The original phrase provided, "cerebral volume loss", is a commonly used radiology descriptor for this finding.  
**Synonyms:** cerebral volume loss, global cerebral atrophy, brain atrophy, diffuse cerebral atrophy, cerebral parenchymal loss  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0555`; `name=generalized_atrophy`; `category=brain_parenchyma`; `parent_id=HID0550`; `synonyms=diffuse cerebral atrophy, global atrophy, diffuse brain atrophy, generalized cerebral atrophy, prominent ventricles and sulci, the ventricles and sulci are prominent, enlarged ventricles and sulci, prominent ventricles and cortical sulci`; `finding_type=observation`; `oifm_id=(blank)`

**QUESTION:** This row is a subtype/phrase-level match to the existing cerebral atrophy model. Confirm no separate generalized atrophy model is needed.

**Response:** 

---

### focal atrophy
**Source file:** `defs/focal_atrophy.fm.json`  
**ID:** `OIFM_OIDM_291655`  
**Description:** Imaging observation of focal atrophy within the brain parenchyma on head CT or related neuroimaging.  
**Synonyms:** regional atrophy, focal volume loss  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0560`; `name=focal_atrophy`; `category=brain_parenchyma`; `parent_id=HID0550`; `synonyms=regional atrophy, focal volume loss`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### enlarged perivascular space
**Source file:** `defs/enlarged_perivascular_space.fm.json`  
**ID:** `OIFM_OIDM_582546`  
**Description:** Imaging observation of enlarged perivascular space within the brain parenchyma on head CT or related neuroimaging.  
**Synonyms:** dilated Virchow-Robin space, prominent perivascular space, dilated perivascular space, enlarged perivascular spaces  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0565`; `name=enlarged_perivascular_space`; `category=brain_parenchyma`; `parent_id=HID0200`; `synonyms=dilated Virchow-Robin space, prominent perivascular space, dilated perivascular space, enlarged perivascular spaces`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**ISSUE:** Mechanical review flagged uppercase acronym/eponym synonyms. Confirm capitalization is intentional for standard abbreviations or proper names.

**Response:** 

---

### parenchymal calcification
**Source file:** `defs/parenchymal_calcification.fm.json`  
**ID:** `OIFM_OIDM_930805`  
**Description:** Imaging observation of parenchymal calcification within the brain parenchyma on head CT or related neuroimaging.  
**Synonyms:** brain parenchymal calcification, focal brain calcification  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0570`; `name=parenchymal_calcification`; `category=brain_parenchyma`; `parent_id=HID0200`; `synonyms=brain parenchymal calcification, focal brain calcification`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### thalamic fusion
**Source file:** `defs/thalamic_fusion.fm.json`  
**ID:** `OIFM_OIDM_219268`  
**Description:** Imaging observation of thalamic fusion within the brain parenchyma on head CT or related neuroimaging.  
**Synonyms:** fused thalami, thalamic non-separation  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0580`; `name=thalamic_fusion`; `category=brain_parenchyma`; `parent_id=HID0200`; `synonyms=fused thalami, thalamic non-separation`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### cerebral hemispheric fusion
**Source file:** `defs/cerebral_hemispheric_fusion.fm.json`  
**ID:** `OIFM_OIDM_937688`  
**Description:** Imaging observation of cerebral hemispheric fusion within the brain parenchyma on head CT or related neuroimaging.  
**Synonyms:** hemispheric fusion, hemispheric non-separation, midline hemispheric fusion, frontal lobe fusion  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0585`; `name=cerebral_hemispheric_fusion`; `category=brain_parenchyma`; `parent_id=HID0200`; `synonyms=hemispheric fusion, hemispheric non-separation, midline hemispheric fusion, frontal lobe fusion`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

