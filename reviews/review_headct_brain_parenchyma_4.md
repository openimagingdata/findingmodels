# Review: head CT brain_parenchyma batch 4

10 brain_parenchyma CSV decisions to review: 10 newly created models and 0 mappings to existing models. For each, check name, description, synonyms, direction-of-change values, and whether the CSV row should map to the listed OIFM ID. Add your response below each entry.

---

### abnormal enhancement
**Source file:** `defs/abnormal_enhancement.fm.json`  
**ID:** `OIFM_OIDM_103376`  
**Description:** Imaging observation of abnormal enhancement within the brain parenchyma on head CT or related neuroimaging.  
**Synonyms:** abnormal contrast uptake, pathologic enhancement  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0600`; `name=abnormal_enhancement`; `category=brain_parenchyma`; `parent_id=HID0200`; `synonyms=abnormal contrast uptake, pathologic enhancement`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### ring enhancement
**Source file:** `defs/ring_enhancement.fm.json`  
**ID:** `OIFM_OIDM_273483`  
**Description:** Imaging observation of ring enhancement within the brain parenchyma on head CT or related neuroimaging.  
**Synonyms:** rim enhancement  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0605`; `name=ring_enhancement`; `category=brain_parenchyma`; `parent_id=HID0600`; `synonyms=rim enhancement`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### cerebral edema
**Source file:** `defs/cerebral_edema.fm.json`  
**ID:** `OIFM_OIDM_888858`  
**Description:** Diagnosis of cerebral edema, as recognized on head CT or related neuroimaging.  
**Synonyms:** brain edema  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID0650`; `name=cerebral_edema`; `category=brain_parenchyma`; `parent_id=HID0200`; `synonyms=brain edema`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### vasogenic edema
**Source file:** `defs/vasogenic_edema.fm.json`  
**ID:** `OIFM_OIDM_680433`  
**Description:** Diagnosis of vasogenic edema, as recognized on head CT or related neuroimaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID0655`; `name=vasogenic_edema`; `category=brain_parenchyma`; `parent_id=HID0650`; `synonyms=(blank)`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### cytotoxic edema
**Source file:** `defs/cytotoxic_edema.fm.json`  
**ID:** `OIFM_OIDM_366851`  
**Description:** Diagnosis of cytotoxic edema, as recognized on head CT or related neuroimaging.  
**Synonyms:** cellular edema  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID0660`; `name=cytotoxic_edema`; `category=brain_parenchyma`; `parent_id=HID0650`; `synonyms=cellular edema`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### transependymal edema
**Source file:** `defs/transependymal_edema.fm.json`  
**ID:** `OIFM_OIDM_867424`  
**Description:** Diagnosis of transependymal edema, as recognized on head CT or related neuroimaging.  
**Synonyms:** interstitial edema, periventricular edema  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID0665`; `name=transependymal_edema`; `category=brain_parenchyma`; `parent_id=HID0650`; `synonyms=interstitial edema, periventricular edema`; `finding_type=diagnosis`; `oifm_id=(blank)`

**QUESTION:** Created a new transependymal edema model instead of mapping to pulmonary/interstitial edema, because the exact synonym hit was cross-body and misleading.

**Response:** 

---

### encephalomalacia
**Source file:** `defs/encephalomalacia.fm.json`  
**ID:** `OIFM_OIDM_821529`  
**Description:** Diagnosis of encephalomalacia, as recognized on head CT or related neuroimaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID0700`; `name=encephalomalacia`; `category=brain_parenchyma`; `parent_id=HID0200`; `synonyms=(blank)`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### cystic encephalomalacia
**Source file:** `defs/cystic_encephalomalacia.fm.json`  
**ID:** `OIFM_OIDM_732387`  
**Description:** Diagnosis of cystic encephalomalacia, as recognized on head CT or related neuroimaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID0705`; `name=cystic_encephalomalacia`; `category=brain_parenchyma`; `parent_id=HID0700`; `synonyms=(blank)`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### gliosis
**Source file:** `defs/gliosis.fm.json`  
**ID:** `OIFM_OIDM_240658`  
**Description:** Diagnosis of gliosis, as recognized on head CT or related neuroimaging.  
**Synonyms:** reactive gliosis  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID0710`; `name=gliosis`; `category=brain_parenchyma`; `parent_id=HID0200`; `synonyms=reactive gliosis`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### ischemic disease
**Source file:** `defs/ischemic_disease.fm.json`  
**ID:** `OIFM_OIDM_582223`  
**Description:** Diagnosis of ischemic disease, as recognized on head CT or related neuroimaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID0750`; `name=ischemic_disease`; `category=brain_parenchyma`; `parent_id=HID0200`; `synonyms=(blank)`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

