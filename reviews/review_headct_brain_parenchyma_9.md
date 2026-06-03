# Review: head CT brain_parenchyma batch 9

10 brain_parenchyma CSV decisions to review: 5 newly created models and 5 mappings to existing models. For each, check name, description, synonyms, direction-of-change values, and whether the CSV row should map to the listed OIFM ID. Add your response below each entry.

---

### pineoblastoma
**Source file:** `defs/pineoblastoma.fm.json`  
**ID:** `OIFM_OIDM_037130`  
**Description:** Diagnosis of pineoblastoma, as recognized on head CT or related neuroimaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID1355`; `name=pineoblastoma`; `category=brain_parenchyma`; `parent_id=HID1350`; `synonyms=(blank)`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### pineocytoma
**Source file:** `defs/pineocytoma.fm.json`  
**ID:** `OIFM_OIDM_283209`  
**Description:** Diagnosis of pineocytoma, as recognized on head CT or related neuroimaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID1360`; `name=pineocytoma`; `category=brain_parenchyma`; `parent_id=HID1350`; `synonyms=(blank)`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### pineal parenchymal tumor of intermediate differentiation
**Source file:** `defs/pineal_parenchymal_tumor_of_intermediate_differentiation.fm.json`  
**ID:** `OIFM_OIDM_851009`  
**Description:** Diagnosis of pineal parenchymal tumor of intermediate differentiation, as recognized on head CT or related neuroimaging.  
**Synonyms:** PPTID  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID1365`; `name=pineal_parenchymal_tumor_of_intermediate_differentiation`; `category=brain_parenchyma`; `parent_id=HID1350`; `synonyms=PPTID`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**ISSUE:** Mechanical review flagged uppercase acronym/eponym synonyms. Confirm capitalization is intentional for standard abbreviations or proper names.

**Response:** 

---

### matched: diffuse_axonal_injury -> diffuse axonal injury
**Source file:** `defs/diffuse_axonal_injury.fm.json`  
**ID:** `OIFM_OIDM_296147`  
**Description:** Traumatic shear injury to cerebral axons from rotational acceleration-deceleration forces, manifesting on CT as punctate hemorrhages at the gray-white matter junction, corpus callosum, and dorsal brainstem. CT findings are often subtle or absent; MRI is more sensitive.  
**Synonyms:** DAI, shear injury, diffuse traumatic axonal injury  
**Change from prior:** unchanged, stable, new, resolved, worsened, improved

**Source CSV:** `id=HID1370`; `name=diffuse_axonal_injury`; `category=brain_parenchyma`; `parent_id=HID0200`; `synonyms=DAI, shear injury, diffuse traumatic axonal injury`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Existing-model mapping. Confirm this CSV row should map to the listed OIFM ID.

**Response:** 

---

### matched: congenital_brain_malformation -> congenital brain malformation
**Source file:** `defs/congenital_brain_malformation.fm.json`  
**ID:** `OIFM_GMTS_007508`  
**Description:** Structural anomalies of the brain formed during gestation.  
**Synonyms:** brain malformation  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID1680`; `name=congenital_brain_malformation`; `category=brain_parenchyma`; `parent_id=HID0200`; `synonyms=congenital brain anomaly`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Existing-model mapping. Confirm this CSV row should map to the listed OIFM ID.

**Response:** 

---

### posterior fossa malformation
**Source file:** `defs/posterior_fossa_malformation.fm.json`  
**ID:** `OIFM_OIDM_332001`  
**Description:** Diagnosis of posterior fossa malformation, as recognized on head CT or related neuroimaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID1685`; `name=posterior_fossa_malformation`; `category=brain_parenchyma`; `parent_id=HID1680`; `synonyms=(blank)`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### matched: chiari_malformation -> chiari malformation
**Source file:** `defs/chiari_malformation.fm.json`  
**ID:** `OIFM_OIDM_456265`  
**Description:** chiari malformation is downward displacement of the cerebellar tonsils through the foramen magnum, potentially causing brainstem crowding and syringomyelia in some patients (original phrasing: 'chiari malformation'). MRI is the preferred modality to confirm the diagnosis and assess associated craniovertebral anomalies.  
**Synonyms:** chiari malformation, arnold-chiari malformation, chiari i malformation, chiari type i malformation, arnold chiari malformation, CM  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID1400`; `name=chiari_malformation`; `category=brain_parenchyma`; `parent_id=HID1685`; `synonyms=(blank)`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Existing-model mapping. Confirm this CSV row should map to the listed OIFM ID.

**Response:** 

---

### matched: chiari_i_malformation -> chiari malformation
**Source file:** `defs/chiari_malformation.fm.json`  
**ID:** `OIFM_OIDM_456265`  
**Description:** chiari malformation is downward displacement of the cerebellar tonsils through the foramen magnum, potentially causing brainstem crowding and syringomyelia in some patients (original phrasing: 'chiari malformation'). MRI is the preferred modality to confirm the diagnosis and assess associated craniovertebral anomalies.  
**Synonyms:** chiari malformation, arnold-chiari malformation, chiari i malformation, chiari type i malformation, arnold chiari malformation, CM  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID1405`; `name=chiari_i_malformation`; `category=brain_parenchyma`; `parent_id=HID1400`; `synonyms=Chiari I, Chiari 1, Chiari malformation type I, Chiari malformation type 1`; `finding_type=diagnosis`; `oifm_id=(blank)`

**QUESTION:** This row maps chiari i malformation to the broader chiari malformation model based on existing synonyms. Confirm no separate type-I model is needed.

**Response:** 

---

### matched: chiari_ii_malformation -> chiari malformation
**Source file:** `defs/chiari_malformation.fm.json`  
**ID:** `OIFM_OIDM_456265`  
**Description:** chiari malformation is downward displacement of the cerebellar tonsils through the foramen magnum, potentially causing brainstem crowding and syringomyelia in some patients (original phrasing: 'chiari malformation'). MRI is the preferred modality to confirm the diagnosis and assess associated craniovertebral anomalies.  
**Synonyms:** chiari malformation, arnold-chiari malformation, chiari i malformation, chiari type i malformation, arnold chiari malformation, CM  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID1410`; `name=chiari_ii_malformation`; `category=brain_parenchyma`; `parent_id=HID1400`; `synonyms=Chiari II, Chiari 2, Chiari malformation type II, Chiari malformation type 2, Arnold-Chiari malformation`; `finding_type=diagnosis`; `oifm_id=(blank)`

**QUESTION:** This row maps chiari ii malformation to the broader chiari malformation model based on existing synonyms. Confirm no separate type-II model is needed.

**Response:** 

---

### chiari iii malformation
**Source file:** `defs/chiari_iii_malformation.fm.json`  
**ID:** `OIFM_OIDM_509940`  
**Description:** Diagnosis of chiari iii malformation, as recognized on head CT or related neuroimaging.  
**Synonyms:** Chiari III, Chiari 3, Chiari malformation type III, Chiari malformation type 3  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID1415`; `name=chiari_iii_malformation`; `category=brain_parenchyma`; `parent_id=HID1400`; `synonyms=Chiari III, Chiari 3, Chiari malformation type III, Chiari malformation type 3`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**ISSUE:** Mechanical review flagged uppercase acronym/eponym synonyms. Confirm capitalization is intentional for standard abbreviations or proper names.

**Response:** 

