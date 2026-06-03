# Review: head CT brain_parenchyma batch 8

10 brain_parenchyma CSV decisions to review: 7 newly created models and 3 mappings to existing models. For each, check name, description, synonyms, direction-of-change values, and whether the CSV row should map to the listed OIFM ID. Add your response below each entry.

---

### viral encephalitis
**Source file:** `defs/viral_encephalitis.fm.json`  
**ID:** `OIFM_OIDM_258182`  
**Description:** Diagnosis of viral encephalitis, as recognized on head CT or related neuroimaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID1200`; `name=viral_encephalitis`; `category=brain_parenchyma`; `parent_id=HID1150`; `synonyms=(blank)`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### herpes simplex encephalitis
**Source file:** `defs/herpes_simplex_encephalitis.fm.json`  
**ID:** `OIFM_OIDM_633793`  
**Description:** Diagnosis of herpes simplex encephalitis, as recognized on head CT or related neuroimaging.  
**Synonyms:** herpes encephalitis, HSV encephalitis  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID1205`; `name=herpes_simplex_encephalitis`; `category=brain_parenchyma`; `parent_id=HID1200`; `synonyms=herpes encephalitis, HSV encephalitis`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**ISSUE:** Mechanical review flagged uppercase acronym/eponym synonyms. Confirm capitalization is intentional for standard abbreviations or proper names.

**Response:** 

---

### matched: neurocysticercosis -> neurocysticercosis
**Source file:** `defs/neurocysticercosis.fm.json`  
**ID:** `OIFM_OIDM_581255`  
**Description:** Parenchymal, subarachnoid, intraventricular, or spinal infection by Taenia solium larvae, appearing on head CT as cystic lesions that evolve through vesicular, colloidal, granular-nodular, and calcified nodular stages. Typically manifests as small cysts with or without a mural scolex, ring-enhancing lesions with surrounding edema, or punctate calcifications depending on stage.  
**Synonyms:** NCC, CNS cysticercosis  
**Change from prior:** unchanged, stable, new, resolved, worsened, improved, increased, decreased

**Source CSV:** `id=HID1210`; `name=neurocysticercosis`; `category=brain_parenchyma`; `parent_id=HID1100`; `synonyms=NCC`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Existing-model mapping. Confirm this CSV row should map to the listed OIFM ID.

**Response:** 

---

### brain neoplasm
**Source file:** `defs/brain_neoplasm.fm.json`  
**ID:** `OIFM_OIDM_901763`  
**Description:** Diagnosis of brain neoplasm, as recognized on head CT or related neuroimaging.  
**Synonyms:** brain tumor  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID1250`; `name=brain_neoplasm`; `category=brain_parenchyma`; `parent_id=HID0200`; `synonyms=brain tumor`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### matched: brain_metastasis -> brain metastasis
**Source file:** `defs/brain_metastasis.fm.json`  
**ID:** `OIFM_GMTS_006955`  
**Description:** Secondary malignant tumor in the brain originating from another site.  
**Synonyms:** metastasis to the brain, metastatic brain tumor  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID1255`; `name=brain_metastasis`; `category=brain_parenchyma`; `parent_id=HID1250`; `synonyms=cerebral metastasis, brain met`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Existing-model mapping. Confirm this CSV row should map to the listed OIFM ID.

**Response:** 

---

### matched: glioma -> Glioma
**Source file:** `defs/glioma.fm.json`  
**ID:** `OIFM_CDE_000115`  
**Description:** Glioma  
**Synonyms:** (none)  
**Change from prior:** (missing)

**Source CSV:** `id=HID1300`; `name=glioma`; `category=brain_parenchyma`; `parent_id=HID1250`; `synonyms=glial neoplasm`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Existing-model mapping. Confirm this CSV row should map to the listed OIFM ID.

**Response:** 

---

### astrocytoma
**Source file:** `defs/astrocytoma.fm.json`  
**ID:** `OIFM_OIDM_606726`  
**Description:** Diagnosis of astrocytoma, as recognized on head CT or related neuroimaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID1305`; `name=astrocytoma`; `category=brain_parenchyma`; `parent_id=HID1300`; `synonyms=(blank)`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### oligodendroglioma
**Source file:** `defs/oligodendroglioma.fm.json`  
**ID:** `OIFM_OIDM_899132`  
**Description:** Diagnosis of oligodendroglioma, as recognized on head CT or related neuroimaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID1310`; `name=oligodendroglioma`; `category=brain_parenchyma`; `parent_id=HID1300`; `synonyms=(blank)`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### glioblastoma
**Source file:** `defs/glioblastoma.fm.json`  
**ID:** `OIFM_OIDM_356038`  
**Description:** Diagnosis of glioblastoma, as recognized on head CT or related neuroimaging.  
**Synonyms:** GBM, glioblastoma multiforme  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID1315`; `name=glioblastoma`; `category=brain_parenchyma`; `parent_id=HID1300`; `synonyms=GBM, glioblastoma multiforme`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**ISSUE:** Mechanical review flagged uppercase acronym/eponym synonyms. Confirm capitalization is intentional for standard abbreviations or proper names.

**Response:** 

---

### pineal parenchymal tumor
**Source file:** `defs/pineal_parenchymal_tumor.fm.json`  
**ID:** `OIFM_OIDM_064149`  
**Description:** Diagnosis of pineal parenchymal tumor, as recognized on head CT or related neuroimaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID1350`; `name=pineal_parenchymal_tumor`; `category=brain_parenchyma`; `parent_id=HID1250`; `synonyms=(blank)`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

