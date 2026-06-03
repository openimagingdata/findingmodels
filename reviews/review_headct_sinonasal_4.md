# Review: head CT sinonasal batch 4

10 sinonasal CSV decisions to review: 9 newly created models and 1 mappings to existing models. For each, check name, description, synonyms, direction-of-change values, and whether the CSV row should map to the listed OIFM ID. Add your response below each entry.

---

### sinonasal carcinoma
**Source file:** `defs/sinonasal_carcinoma.fm.json`  
**ID:** `OIFM_OIDM_644756`  
**Description:** Diagnosis of sinonasal carcinoma, as recognized on head CT or related sinonasal imaging.  
**Synonyms:** nasal cavity carcinoma  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID7865`; `name=sinonasal_carcinoma`; `category=sinonasal`; `parent_id=HID7850`; `synonyms=nasal cavity carcinoma`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the sinonasal CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### sinonasal anatomic variant
**Source file:** `defs/sinonasal_anatomic_variant.fm.json`  
**ID:** `OIFM_OIDM_605598`  
**Description:** Broad grouping for sinonasal anatomic variant findings involving the nasal cavity or paranasal sinuses on head CT or related sinonasal imaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID8000`; `name=sinonasal_anatomic_variant`; `category=sinonasal`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`; `oifm_id=(blank)`

**Assessment:** Newly created from the sinonasal CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### matched: nasal_septal_deviation -> nasal septal deviation
**Source file:** `defs/nasal_septal_deviation.fm.json`  
**ID:** `OIFM_OIDM_884986`  
**Description:** Lateral displacement or curvature of the bony and/or cartilaginous nasal septum away from midline. A common sinonasal anatomic variant that is often clinically insignificant but may contribute to nasal obstruction or predispose to sinusitis.  
**Synonyms:** deviated nasal septum  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, worsened, improved

**Source CSV:** `id=HID8005`; `name=nasal_septal_deviation`; `category=sinonasal`; `parent_id=HID8000`; `synonyms=deviated nasal septum, DNS, septal deviation`; `finding_type=observation`; `oifm_id=(blank)`

**QUESTION:** This row maps nasal septal deviation to the existing nasal septal deviation model. Confirm direct mapping.

**Response:** 

---

### nasal septal spur
**Source file:** `defs/nasal_septal_spur.fm.json`  
**ID:** `OIFM_OIDM_376962`  
**Description:** Imaging observation of nasal septal spur involving the nasal cavity or paranasal sinuses on head CT or related sinonasal imaging.  
**Synonyms:** septal spur, bony nasal spur  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID8010`; `name=nasal_septal_spur`; `category=sinonasal`; `parent_id=HID8000`; `synonyms=septal spur, bony nasal spur`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the sinonasal CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### concha bullosa
**Source file:** `defs/concha_bullosa.fm.json`  
**ID:** `OIFM_OIDM_230209`  
**Description:** Imaging observation of concha bullosa involving the nasal cavity or paranasal sinuses on head CT or related sinonasal imaging.  
**Synonyms:** pneumatized middle turbinate, aerated concha  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID8015`; `name=concha_bullosa`; `category=sinonasal`; `parent_id=HID8000`; `synonyms=pneumatized middle turbinate, aerated concha`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the sinonasal CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### non pneumatized sinus
**Source file:** `defs/non_pneumatized_sinus.fm.json`  
**ID:** `OIFM_OIDM_547137`  
**Description:** Imaging observation of non pneumatized sinus involving the nasal cavity or paranasal sinuses on head CT or related sinonasal imaging.  
**Synonyms:** sinus aplasia, sinus hypoplasia  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID8020`; `name=non_pneumatized_sinus`; `category=sinonasal`; `parent_id=HID8000`; `synonyms=sinus aplasia, sinus hypoplasia`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the sinonasal CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### sinus wall dehiscence
**Source file:** `defs/sinus_wall_dehiscence.fm.json`  
**ID:** `OIFM_OIDM_686820`  
**Description:** Imaging observation of sinus wall dehiscence involving the nasal cavity or paranasal sinuses on head CT or related sinonasal imaging.  
**Synonyms:** sinus wall defect  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID8025`; `name=sinus_wall_dehiscence`; `category=sinonasal`; `parent_id=HID8000`; `synonyms=sinus wall defect`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the sinonasal CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### haller cell
**Source file:** `defs/haller_cell.fm.json`  
**ID:** `OIFM_OIDM_296922`  
**Description:** Imaging observation of haller cell involving the nasal cavity or paranasal sinuses on head CT or related sinonasal imaging.  
**Synonyms:** infraorbital ethmoid cell, infraorbital cell  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID8030`; `name=haller_cell`; `category=sinonasal`; `parent_id=HID8000`; `synonyms=infraorbital ethmoid cell, infraorbital cell`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the sinonasal CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### onodi cell
**Source file:** `defs/onodi_cell.fm.json`  
**ID:** `OIFM_OIDM_519518`  
**Description:** Imaging observation of onodi cell involving the nasal cavity or paranasal sinuses on head CT or related sinonasal imaging.  
**Synonyms:** sphenoethmoid cell  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID8035`; `name=onodi_cell`; `category=sinonasal`; `parent_id=HID8000`; `synonyms=sphenoethmoid cell`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the sinonasal CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### sinonasal postsurgical change
**Source file:** `defs/sinonasal_postsurgical_change.fm.json`  
**ID:** `OIFM_OIDM_452489`  
**Description:** Broad grouping for sinonasal postsurgical change findings involving the nasal cavity or paranasal sinuses on head CT or related sinonasal imaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID8200`; `name=sinonasal_postsurgical_change`; `category=sinonasal`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`; `oifm_id=(blank)`

**Assessment:** Newly created from the sinonasal CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

