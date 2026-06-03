# Review: head CT sinonasal batch 1

10 sinonasal CSV decisions to review: 8 newly created models and 2 mappings to existing models. For each, check name, description, synonyms, direction-of-change values, and whether the CSV row should map to the listed OIFM ID. Add your response below each entry.

---

### sinonasal abnormality
**Source file:** `defs/sinonasal_abnormality.fm.json`  
**ID:** `OIFM_OIDM_435405`  
**Description:** Broad grouping for sinonasal abnormality findings involving the nasal cavity or paranasal sinuses on head CT or related sinonasal imaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID7600`; `name=sinonasal_abnormality`; `category=sinonasal`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`; `oifm_id=(blank)`

**Assessment:** Newly created from the sinonasal CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### sinus mucosal thickening
**Source file:** `defs/sinus_mucosal_thickening.fm.json`  
**ID:** `OIFM_OIDM_225879`  
**Description:** Imaging observation of sinus mucosal thickening involving the nasal cavity or paranasal sinuses on head CT or related sinonasal imaging.  
**Synonyms:** mucosal thickening  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID7605`; `name=sinus_mucosal_thickening`; `category=sinonasal`; `parent_id=HID7600`; `synonyms=mucosal thickening`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the sinonasal CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### matched: sinus_opacification -> paranasal sinus opacification
**Source file:** `defs/paranasal_sinus_opacification.fm.json`  
**ID:** `OIFM_GMTS_008528`  
**Description:** Clouding of the sinus cavities often due to fluid or inflammation.  
**Synonyms:** sinus clouding, sinus opacity  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID7610`; `name=sinus_opacification`; `category=sinonasal`; `parent_id=HID7600`; `synonyms=opacified sinus`; `finding_type=observation`; `oifm_id=(blank)`

**QUESTION:** This row maps sinus opacification to the existing paranasal sinus opacification model. Confirm this broader anatomic wording is acceptable.

**Response:** 

---

### matched: sinus_air_fluid_level -> fluid level in a paranasal sinus
**Source file:** `defs/fluid_level_in_a_paranasal_sinus.fm.json`  
**ID:** `OIFM_GMTS_008538`  
**Description:** Presence of fluid detected in sinus cavity on imaging.  
**Synonyms:** sinus fluid level, sinusitis sign  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID7615`; `name=sinus_air_fluid_level`; `category=sinonasal`; `parent_id=HID7600`; `synonyms=air-fluid level in sinus, layering sinus fluid`; `finding_type=observation`; `oifm_id=(blank)`

**QUESTION:** This row maps sinus air fluid level to fluid level in a paranasal sinus. Confirm this existing model is acceptable despite the source row using air-fluid-level phrasing.

**Response:** 

---

### hyperattenuating sinus contents
**Source file:** `defs/hyperattenuating_sinus_contents.fm.json`  
**ID:** `OIFM_OIDM_497952`  
**Description:** Imaging observation of hyperattenuating sinus contents involving the nasal cavity or paranasal sinuses on head CT or related sinonasal imaging.  
**Synonyms:** hyperdense sinus contents, inspissated secretions, desiccated secretions  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID7620`; `name=hyperattenuating_sinus_contents`; `category=sinonasal`; `parent_id=HID7600`; `synonyms=hyperdense sinus contents, inspissated secretions, desiccated secretions`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the sinonasal CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### sinus wall thickening
**Source file:** `defs/sinus_wall_thickening.fm.json`  
**ID:** `OIFM_OIDM_242385`  
**Description:** Imaging observation of sinus wall thickening involving the nasal cavity or paranasal sinuses on head CT or related sinonasal imaging.  
**Synonyms:** sinus wall sclerosis, sclerotic sinus walls  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID7625`; `name=sinus_wall_thickening`; `category=sinonasal`; `parent_id=HID7600`; `synonyms=sinus wall sclerosis, sclerotic sinus walls`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the sinonasal CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### sinus wall erosion
**Source file:** `defs/sinus_wall_erosion.fm.json`  
**ID:** `OIFM_OIDM_935461`  
**Description:** Imaging observation of sinus wall erosion involving the nasal cavity or paranasal sinuses on head CT or related sinonasal imaging.  
**Synonyms:** sinus wall destruction, bony erosion sinus  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID7630`; `name=sinus_wall_erosion`; `category=sinonasal`; `parent_id=HID7600`; `synonyms=sinus wall destruction, bony erosion sinus`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the sinonasal CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### sinus expansion
**Source file:** `defs/sinus_expansion.fm.json`  
**ID:** `OIFM_OIDM_398753`  
**Description:** Imaging observation of sinus expansion involving the nasal cavity or paranasal sinuses on head CT or related sinonasal imaging.  
**Synonyms:** expanded sinus  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID7635`; `name=sinus_expansion`; `category=sinonasal`; `parent_id=HID7600`; `synonyms=expanded sinus`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the sinonasal CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### perisinus fat stranding
**Source file:** `defs/perisinus_fat_stranding.fm.json`  
**ID:** `OIFM_OIDM_859298`  
**Description:** Imaging observation of perisinus fat stranding involving the nasal cavity or paranasal sinuses on head CT or related sinonasal imaging.  
**Synonyms:** periantral fat infiltration, periantral fat stranding, extrasinus fat infiltration  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID7640`; `name=perisinus_fat_stranding`; `category=sinonasal`; `parent_id=HID7600`; `synonyms=periantral fat infiltration, periantral fat stranding, extrasinus fat infiltration`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the sinonasal CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### sinus retention cyst
**Source file:** `defs/sinus_retention_cyst.fm.json`  
**ID:** `OIFM_OIDM_769618`  
**Description:** Imaging observation of sinus retention cyst involving the nasal cavity or paranasal sinuses on head CT or related sinonasal imaging.  
**Synonyms:** mucous retention cyst, mucus retention cyst, sinus mucosal cyst  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID7645`; `name=sinus_retention_cyst`; `category=sinonasal`; `parent_id=HID7600`; `synonyms=mucous retention cyst, mucus retention cyst, sinus mucosal cyst`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the sinonasal CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

