# Review: head CT extra axial batch 5

9 models/mappings to review. For each, check name, description, synonyms, and direction-of-change values. Add your response below each entry.

---

### matched: leptomeningeal_metastasis -> meningeal metastasis

**Source file:** `defs/meningeal_metastasis.fm.json`  
**ID:** `OIFM_GMTS_025476`  
**Description:** Cancer spread to the meninges surrounding the brain and spinal cord.  
**Synonyms:** leptomeningeal carcinomatosis, metastasis to the meninges, leptomeningeal metastasis, carcinomatous meningitis, meningeal carcinomatosis  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller  
**Source CSV:** `id=HID3065`; `name=leptomeningeal_metastasis`; `category=extra_axial`; `parent_id=HID3050`; `synonyms=leptomeningeal carcinomatosis, carcinomatous meningitis, meningeal carcinomatosis`; `finding_type=diagnosis`

**QUESTION:** Mapped to existing `meningeal metastasis`; CSV synonyms were added. Confirm broader canonical name is acceptable.

**Response:** 

---

### extra-axial infection

**Source file:** `defs/extra_axial_infection.fm.json`  
**ID:** `OIFM_OIDM_481515`  
**Description:** Infectious or inflammatory process involving an extra-axial intracranial compartment or meningeal surface, including meningitis, empyema, or infected collections.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, worsened, improved  
**Source CSV:** `id=HID3100`; `name=extra_axial_infection`; `category=extra_axial`; `parent_id=HID2600`; `synonyms=(blank)`; `finding_type=diagnosis`

**Assessment:** New grouping model for extra-axial infections; confirm acceptable.

**Response:** 

---

### meningitis

**Source file:** `defs/meningitis.fm.json`  
**ID:** `OIFM_OIDM_676813`  
**Description:** Inflammation or infection of the meninges, which may manifest on imaging as leptomeningeal enhancement, sulcal FLAIR abnormality, hydrocephalus, or related complications.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, worsened, improved  
**Source CSV:** `id=HID3105`; `name=meningitis`; `category=extra_axial`; `parent_id=HID3100`; `synonyms=(blank)`; `finding_type=diagnosis`

**Assessment:** Created dedicated meningitis model rather than reusing broader `encephalitis and meningitis`; confirm acceptable.

**Response:** 

---

### matched: subdural_empyema -> subdural empyema

**Source file:** `defs/subdural_empyema.fm.json`  
**ID:** `OIFM_GMTS_007457`  
**Description:** Infection with pus accumulation in the subdural space.  
**Synonyms:** subdural abscess, infected subdural collection  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller  
**Source CSV:** `id=HID3110`; `name=subdural_empyema`; `category=extra_axial`; `parent_id=HID3100`; `synonyms=infected subdural collection`; `finding_type=diagnosis`

**Assessment:** Existing GMTS model reused; CSV synonym was added.

**Response:** 

---

### extra-axial anatomic variant

**Source file:** `defs/extra_axial_anatomic_variant.fm.json`  
**ID:** `OIFM_OIDM_283674`  
**Description:** A developmental or anatomic variant involving the extra-axial intracranial spaces, cisterns, meninges, or related structures.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID3200`; `name=extra_axial_anatomic_variant`; `category=extra_axial`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`

**Assessment:** New grouping model for extra-axial anatomic variants; confirm acceptable.

**Response:** 

---

### arachnoid granulation

**Source file:** `defs/arachnoid_granulation.fm.json`  
**ID:** `OIFM_OIDM_836917`  
**Description:** Benign protrusion of arachnoid membrane into a dural venous sinus or calvarial venous structure, often appearing as a rounded filling defect or CSF-density focus.  
**Synonyms:** Pacchionian granulation  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID3205`; `name=arachnoid_granulation`; `category=extra_axial`; `parent_id=HID3200`; `synonyms=Pacchionian granulation`; `finding_type=observation`

**QUESTION:** Mechanical review flagged capitalization; I left `Pacchionian` capitalized as an eponym. Confirm acceptable.

**Response:** 

---

### mega cisterna magna

**Source file:** `defs/mega_cisterna_magna.fm.json`  
**ID:** `OIFM_OIDM_634782`  
**Description:** A developmental posterior fossa variant characterized by an enlarged cisterna magna with otherwise normal cerebellar vermis and no significant mass effect.  
**Synonyms:** enlarged cisterna magna, prominent cisterna magna, megacisterna magna  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID3210`; `name=mega_cisterna_magna`; `category=extra_axial`; `parent_id=HID3200`; `synonyms=enlarged cisterna magna, prominent cisterna magna, megacisterna magna`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### extra-axial postsurgical change

**Source file:** `defs/extra_axial_postsurgical_change.fm.json`  
**ID:** `OIFM_OIDM_381585`  
**Description:** Expected or nonspecific postoperative alteration involving the meninges, dura, extra-axial spaces, or related intracranial surgical bed.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID3400`; `name=extra_axial_postsurgical_change`; `category=extra_axial`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`

**Assessment:** New grouping model for extra-axial postsurgical rows; confirm acceptable.

**Response:** 

---

### duraplasty

**Source file:** `defs/duraplasty.fm.json`  
**ID:** `OIFM_OIDM_007428`  
**Description:** Postoperative dural repair or graft material used to reconstruct or augment the dura, visible as expected postsurgical change on imaging.  
**Synonyms:** dural graft, dural repair, dural patch  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID3405`; `name=duraplasty`; `category=extra_axial`; `parent_id=HID3400`; `synonyms=dural graft, dural repair, dural patch`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---
