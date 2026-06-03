# Review: head CT brain_parenchyma batch 5

10 brain_parenchyma CSV decisions to review: 9 newly created models and 1 mappings to existing models. For each, check name, description, synonyms, direction-of-change values, and whether the CSV row should map to the listed OIFM ID. Add your response below each entry.

---

### matched: infarct -> cerebral infarction
**Source file:** `defs/cerebral_infarction.fm.json`  
**ID:** `OIFM_GMTS_007619`  
**Description:** Death of brain tissue due to inadequate blood supply.  
**Synonyms:** stroke, brain infarct  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0800`; `name=infarct`; `category=brain_parenchyma`; `parent_id=HID0750`; `synonyms=cerebral infarct, cerebral infarction`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Existing-model mapping. Confirm this CSV row should map to the listed OIFM ID.

**Response:** 

---

### hemorrhagic transformation
**Source file:** `defs/hemorrhagic_transformation.fm.json`  
**ID:** `OIFM_OIDM_366454`  
**Description:** Diagnosis of hemorrhagic transformation, as recognized on head CT or related neuroimaging.  
**Synonyms:** hemorrhagic conversion  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID0850`; `name=hemorrhagic_transformation`; `category=brain_parenchyma`; `parent_id=HID0800`; `synonyms=hemorrhagic conversion`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### hemorrhagic infarct
**Source file:** `defs/hemorrhagic_infarct.fm.json`  
**ID:** `OIFM_OIDM_669559`  
**Description:** Diagnosis of hemorrhagic infarct, as recognized on head CT or related neuroimaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID0855`; `name=hemorrhagic_infarct`; `category=brain_parenchyma`; `parent_id=HID0850`; `synonyms=(blank)`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### lacunar infarct
**Source file:** `defs/lacunar_infarct.fm.json`  
**ID:** `OIFM_OIDM_251340`  
**Description:** Diagnosis of lacunar infarct, as recognized on head CT or related neuroimaging.  
**Synonyms:** lacune  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID0860`; `name=lacunar_infarct`; `category=brain_parenchyma`; `parent_id=HID0800`; `synonyms=lacune`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### territorial infarct
**Source file:** `defs/territorial_infarct.fm.json`  
**ID:** `OIFM_OIDM_266756`  
**Description:** Diagnosis of territorial infarct, as recognized on head CT or related neuroimaging.  
**Synonyms:** territorial infarction, large vascular territory infarct, large vessel territory infarct, major vascular territory infarct  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID0900`; `name=territorial_infarct`; `category=brain_parenchyma`; `parent_id=HID0800`; `synonyms=territorial infarction, large vascular territory infarct, large vessel territory infarct, major vascular territory infarct`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### middle cerebral artery territory infarct
**Source file:** `defs/middle_cerebral_artery_territory_infarct.fm.json`  
**ID:** `OIFM_OIDM_655715`  
**Description:** Diagnosis of middle cerebral artery territory infarct, as recognized on head CT or related neuroimaging.  
**Synonyms:** MCA territory infarct, MCA infarct, middle cerebral artery infarct  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID0905`; `name=middle_cerebral_artery_territory_infarct`; `category=brain_parenchyma`; `parent_id=HID0900`; `synonyms=MCA territory infarct, MCA infarct, middle cerebral artery infarct`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**ISSUE:** Mechanical review flagged uppercase acronym/eponym synonyms. Confirm capitalization is intentional for standard abbreviations or proper names.

**Response:** 

---

### posterior cerebral artery territory infarct
**Source file:** `defs/posterior_cerebral_artery_territory_infarct.fm.json`  
**ID:** `OIFM_OIDM_166472`  
**Description:** Diagnosis of posterior cerebral artery territory infarct, as recognized on head CT or related neuroimaging.  
**Synonyms:** PCA territory infarct, PCA infarct, posterior cerebral artery infarct  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID0910`; `name=posterior_cerebral_artery_territory_infarct`; `category=brain_parenchyma`; `parent_id=HID0900`; `synonyms=PCA territory infarct, PCA infarct, posterior cerebral artery infarct`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**ISSUE:** Mechanical review flagged uppercase acronym/eponym synonyms. Confirm capitalization is intentional for standard abbreviations or proper names.

**Response:** 

---

### anterior cerebral artery territory infarct
**Source file:** `defs/anterior_cerebral_artery_territory_infarct.fm.json`  
**ID:** `OIFM_OIDM_775774`  
**Description:** Diagnosis of anterior cerebral artery territory infarct, as recognized on head CT or related neuroimaging.  
**Synonyms:** ACA territory infarct, ACA infarct, anterior cerebral artery infarct  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID0915`; `name=anterior_cerebral_artery_territory_infarct`; `category=brain_parenchyma`; `parent_id=HID0900`; `synonyms=ACA territory infarct, ACA infarct, anterior cerebral artery infarct`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**ISSUE:** Mechanical review flagged uppercase acronym/eponym synonyms. Confirm capitalization is intentional for standard abbreviations or proper names.

**Response:** 

---

### posterior inferior cerebellar artery territory infarct
**Source file:** `defs/posterior_inferior_cerebellar_artery_territory_infarct.fm.json`  
**ID:** `OIFM_OIDM_644531`  
**Description:** Diagnosis of posterior inferior cerebellar artery territory infarct, as recognized on head CT or related neuroimaging.  
**Synonyms:** PICA territory infarct, PICA infarct, posterior inferior cerebellar artery infarct  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID0920`; `name=posterior_inferior_cerebellar_artery_territory_infarct`; `category=brain_parenchyma`; `parent_id=HID0900`; `synonyms=PICA territory infarct, PICA infarct, posterior inferior cerebellar artery infarct`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**ISSUE:** Mechanical review flagged uppercase acronym/eponym synonyms. Confirm capitalization is intentional for standard abbreviations or proper names.

**Response:** 

---

### anterior inferior cerebellar artery territory infarct
**Source file:** `defs/anterior_inferior_cerebellar_artery_territory_infarct.fm.json`  
**ID:** `OIFM_OIDM_909883`  
**Description:** Diagnosis of anterior inferior cerebellar artery territory infarct, as recognized on head CT or related neuroimaging.  
**Synonyms:** AICA territory infarct, AICA infarct, anterior inferior cerebellar artery infarct  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID0925`; `name=anterior_inferior_cerebellar_artery_territory_infarct`; `category=brain_parenchyma`; `parent_id=HID0900`; `synonyms=AICA territory infarct, AICA infarct, anterior inferior cerebellar artery infarct`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**ISSUE:** Mechanical review flagged uppercase acronym/eponym synonyms. Confirm capitalization is intentional for standard abbreviations or proper names.

**Response:** 

