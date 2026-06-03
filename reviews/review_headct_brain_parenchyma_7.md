# Review: head CT brain_parenchyma batch 7

10 brain_parenchyma CSV decisions to review: 7 newly created models and 3 mappings to existing models. For each, check name, description, synonyms, direction-of-change values, and whether the CSV row should map to the listed OIFM ID. Add your response below each entry.

---

### matched: small_vessel_ischemic_disease -> cerebral small vessel disease
**Source file:** `defs/cerebral_small_vessel_disease.fm.json`  
**ID:** `OIFM_OIDM_093125`  
**Description:** Cerebral small vessel disease is characterized by chronic ischemic changes of the brain due to small vessel pathology, typically presenting as diffuse or focal white matter hyperintensities with possible lacunes or microbleeds. The original phrasing 'small vessel ischemic disease' may be used to describe this finding in radiology reports.  
**Synonyms:** small vessel ischemic disease, ischemic small vessel disease, small-vessel disease, CSVD  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID1030`; `name=small_vessel_ischemic_disease`; `category=brain_parenchyma`; `parent_id=HID0750`; `synonyms=SVID, small vessel disease, chronic microvascular ischemic changes`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Existing-model mapping. Confirm this CSV row should map to the listed OIFM ID.

**Response:** 

---

### matched: hypoxic_ischemic_encephalopathy -> hypoxic-ischemic encephalopathy
**Source file:** `defs/hypoxic_ischemic_encephalopathy.fm.json`  
**ID:** `OIFM_OIDM_044611`  
**Description:** Diffuse brain injury resulting from global hypoxia and/or ischemia, characterized on CT by loss of gray-white matter differentiation, cerebral edema, basal ganglia hypoattenuation, and in severe cases the reversal sign.  
**Synonyms:** HIE, anoxic brain injury, hypoxic brain injury, hypoxic-ischemic brain injury, global hypoxic-ischemic injury  
**Change from prior:** unchanged, stable, new, resolved, worsened, improved

**Source CSV:** `id=HID1035`; `name=hypoxic_ischemic_encephalopathy`; `category=brain_parenchyma`; `parent_id=HID0750`; `synonyms=HIE, anoxic brain injury, hypoxic brain injury`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Existing-model mapping. Confirm this CSV row should map to the listed OIFM ID.

**Response:** 

---

### intracranial hemorrhage
**Source file:** `defs/intracranial_hemorrhage.fm.json`  
**ID:** `OIFM_OIDM_797056`  
**Description:** Diagnosis of intracranial hemorrhage, as recognized on head CT or related neuroimaging.  
**Synonyms:** ICH, intracranial bleeding  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID1050`; `name=intracranial_hemorrhage`; `category=brain_parenchyma`; `parent_id=HID0200`; `synonyms=ICH, intracranial bleeding`; `finding_type=diagnosis`; `oifm_id=(blank)`

**QUESTION:** Created a new intracranial hemorrhage rollup rather than mapping to intracerebral hemorrhage or quantified intracranial hemorrhage.

**ISSUE:** Mechanical review flagged uppercase acronym/eponym synonyms. Confirm capitalization is intentional for standard abbreviations or proper names.

**Response:** 

---

### matched: parenchymal_hematoma -> Intracerebral Hemorrhage
**Source file:** `defs/intracerebral_hemorrhage.fm.json`  
**ID:** `OIFM_MSFT_218756`  
**Description:** Intracerebral hemorrhage refers to bleeding that occurs within the brain tissue itself, often due to a ruptured blood vessel.  
**Synonyms:** ICH, cerebral hemorrhage  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID1055`; `name=parenchymal_hematoma`; `category=brain_parenchyma`; `parent_id=HID1050`; `synonyms=intraparenchymal hemorrhage, IPH, intracerebral hemorrhage, brain hemorrhage`; `finding_type=diagnosis`; `oifm_id=(blank)`

**QUESTION:** This row maps parenchymal hematoma to the existing intracerebral hemorrhage model. Confirm this equivalence is acceptable for head CT.

**Response:** 

---

### catheter tract hemorrhage
**Source file:** `defs/catheter_tract_hemorrhage.fm.json`  
**ID:** `OIFM_OIDM_448433`  
**Description:** Diagnosis of catheter tract hemorrhage, as recognized on head CT or related neuroimaging.  
**Synonyms:** catheter tract hematoma, tract hemorrhage, tract hematoma, EVD tract hemorrhage, ventriculostomy tract hemorrhage  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID1057`; `name=catheter_tract_hemorrhage`; `category=brain_parenchyma`; `parent_id=HID1055`; `synonyms=catheter tract hematoma, tract hemorrhage, tract hematoma, EVD tract hemorrhage, ventriculostomy tract hemorrhage`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**ISSUE:** Mechanical review flagged uppercase acronym/eponym synonyms. Confirm capitalization is intentional for standard abbreviations or proper names.

**Response:** 

---

### cerebral contusion
**Source file:** `defs/cerebral_contusion.fm.json`  
**ID:** `OIFM_OIDM_322629`  
**Description:** Diagnosis of cerebral contusion, as recognized on head CT or related neuroimaging.  
**Synonyms:** brain contusion, hemorrhagic contusion  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID1060`; `name=cerebral_contusion`; `category=brain_parenchyma`; `parent_id=HID0200`; `synonyms=brain contusion, hemorrhagic contusion`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### cerebral infection
**Source file:** `defs/cerebral_infection.fm.json`  
**ID:** `OIFM_OIDM_845319`  
**Description:** Diagnosis of cerebral infection, as recognized on head CT or related neuroimaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID1100`; `name=cerebral_infection`; `category=brain_parenchyma`; `parent_id=HID0200`; `synonyms=(blank)`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### cerebritis
**Source file:** `defs/cerebritis.fm.json`  
**ID:** `OIFM_OIDM_726585`  
**Description:** Diagnosis of cerebritis, as recognized on head CT or related neuroimaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID1105`; `name=cerebritis`; `category=brain_parenchyma`; `parent_id=HID1100`; `synonyms=(blank)`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### cerebral abscess
**Source file:** `defs/cerebral_abscess.fm.json`  
**ID:** `OIFM_OIDM_910183`  
**Description:** Diagnosis of cerebral abscess, as recognized on head CT or related neuroimaging.  
**Synonyms:** brain abscess  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID1110`; `name=cerebral_abscess`; `category=brain_parenchyma`; `parent_id=HID1100`; `synonyms=brain abscess`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### encephalitis
**Source file:** `defs/encephalitis.fm.json`  
**ID:** `OIFM_OIDM_445828`  
**Description:** Diagnosis of encephalitis, as recognized on head CT or related neuroimaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID1150`; `name=encephalitis`; `category=brain_parenchyma`; `parent_id=HID1100`; `synonyms=(blank)`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

