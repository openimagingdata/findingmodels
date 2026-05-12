# Review: head CT dental batch 1

18 dental CSV decisions to review. This category does not appear to have been processed previously: no `review_headct_dental*.md` file was present and no git history mentioning dental batch processing was found.

This is a triage handoff, not a finalized model-creation batch. Entries marked **new model candidate** or **question** need reviewer direction before model creation.

---

### matched: periapical_lucency -> periapical radiolucency in jaw

**Source file:** `defs/periapical_radiolucency_in_jaw.fm.json`  
**ID:** `OIFM_GMTS_008918`  
**Description:** Area of increased radiolucency near the apex of a tooth root.  
**Synonyms:** periapical lucency  

**Source CSV:** `id=HID6005`; `name=periapical_lucency`; `category=dental`; `parent_id=HID6000`; `synonyms=periapical radiolucency`; `finding_type=observation`

**Assessment:** Direct synonym match. Confirm this CSV row should map to the existing model.

**Response:**

---

### matched: apical_periodontitis -> apical periodontitis

**Source file:** `defs/apical_periodontitis.fm.json`  
**ID:** `OIFM_OIDM_248519`  
**Description:** Inflammation or infection of the periapical tissues at the root of a tooth, typically secondary to pulpal necrosis. On head CT, seen as a periapical lucency at the tooth root, sometimes with surrounding sclerosis or an adjacent abscess collection and soft-tissue swelling.  
**Synonyms:** (none)

**Source CSV:** `id=HID6035`; `name=apical_periodontitis`; `category=dental`; `parent_id=HID6000`; `synonyms=periapical infection, dental infection, dentoalveolar infection, dental abscess, dentoalveolar abscess`; `finding_type=diagnosis`

**Assessment:** Direct name match. Reviewer should decide whether to add the CSV synonyms to this model.

**Response:**

---

### matched: dentigerous_cyst -> dentigerous cyst

**Source file:** `defs/dentigerous_cyst.fm.json`  
**ID:** `OIFM_OIDM_217343`  
**Description:** Odontogenic cyst appearing as a well-circumscribed unilocular lucency surrounding the crown of an unerupted or impacted tooth, most commonly a mandibular third molar, with attachment at the cementoenamel junction.  
**Synonyms:** pericoronal cyst

**Source CSV:** `id=HID6040`; `name=dentigerous_cyst`; `category=dental`; `parent_id=HID6000`; `synonyms=follicular cyst`; `finding_type=diagnosis`

**Assessment:** Direct name match. Reviewer should decide whether `follicular cyst` should be added as a synonym.

**Response:**

---

### matched/question: supernumerary_tooth -> hyperdontia

**Source file:** `defs/hyperdontia.fm.json`  
**ID:** `OIFM_GMTS_008780`  
**Description:** Presence of extra teeth.  
**Synonyms:** supernumerary teeth

**Source CSV:** `id=HID6205`; `name=supernumerary_tooth`; `category=dental`; `parent_id=HID6200`; `synonyms=mesiodens, extra tooth, accessory tooth`; `finding_type=observation`

**Question:** Should singular `supernumerary tooth` map to `hyperdontia`, with CSV synonyms added, or should a separate `supernumerary tooth` observation model be created?

**Response:**

---

### question: missing_tooth

**Candidate file:** `defs/anodontia_or_hypodontia.fm.json`  
**Candidate ID:** `OIFM_GMTS_025594`  
**Candidate description:** Partial or complete absence of teeth.  
**Candidate synonyms:** missing teeth

**Source CSV:** `id=HID6025`; `name=missing_tooth`; `category=dental`; `parent_id=HID6000`; `synonyms=absent tooth, missing teeth, edentulous, partially edentulous`; `finding_type=observation`

**Question:** Should acquired/incidental `missing tooth` on head CT map to `anodontia or hypodontia`, or is that too congenital/developmental and a new `missing tooth` model should be created?

**Response:**

---

### question: dental_caries

**Candidate file:** `defs/dental_defect.fm.json`  
**Candidate ID:** `OIFM_GMTS_025596`  
**Candidate description:** Defect in the structure of a tooth, which may be due to caries or developmental issues.

**Source CSV:** `id=HID6010`; `name=dental_caries`; `category=dental`; `parent_id=HID6000`; `synonyms=tooth decay, carious tooth, cavitated tooth`; `finding_type=observation`

**Question:** Should `dental caries` map to the broader `dental defect`, or should a specific `dental caries` model be created?

**Response:**

---

### new model candidate: dental_abnormality

**Source CSV:** `id=HID6000`; `name=dental_abnormality`; `category=dental`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`

**Assessment:** No direct model found. Likely broad parent concept for dental findings.

**Response:**

---

### new model candidate: impacted_tooth

**Source CSV:** `id=HID6015`; `name=impacted_tooth`; `category=dental`; `parent_id=HID6000`; `synonyms=unerupted tooth, embedded tooth, impacted molar`; `finding_type=observation`

**Assessment:** No direct model found. `dentigerous cyst` mentions impacted teeth but is a different diagnosis.

**Response:**

---

### new model candidate: retained_root

**Source CSV:** `id=HID6020`; `name=retained_root`; `category=dental`; `parent_id=HID6000`; `synonyms=retained root fragment, residual root, root remnant`; `finding_type=observation`

**Assessment:** No direct model found.

**Response:**

---

### new model candidate: periodontal_bone_loss

**Source CSV:** `id=HID6030`; `name=periodontal_bone_loss`; `category=dental`; `parent_id=HID6000`; `synonyms=alveolar bone loss, alveolar bone resorption`; `finding_type=observation`

**Assessment:** No direct model found. Related but not equivalent jaw/tooth models exist, such as `loss of lamina dura of teeth`.

**Response:**

---

### new model candidate: periodontitis

**Source CSV:** `id=HID6045`; `name=periodontitis`; `category=dental`; `parent_id=HID6000`; `synonyms=periodontal disease, chronic periodontitis`; `finding_type=diagnosis`

**Assessment:** No direct model found. Distinct from `apical periodontitis`.

**Response:**

---

### new model candidate: oroantral_fistula

**Source CSV:** `id=HID6050`; `name=oroantral_fistula`; `category=dental`; `parent_id=HID6000`; `synonyms=OAF, oro-antral fistula, odontogenic sinus fistula, dental-sinus fistula`; `finding_type=diagnosis`

**Assessment:** No direct model found.

**Response:**

---

### new model candidate: oroantral_communication

**Source CSV:** `id=HID6055`; `name=oroantral_communication`; `category=dental`; `parent_id=HID6000`; `synonyms=OAC, oro-antral communication, post-extraction oroantral defect`; `finding_type=diagnosis`

**Assessment:** No direct model found. Reviewer should decide whether this should be separate from `oroantral fistula`.

**Response:**

---

### new model candidate: dental_anatomic_variant

**Source CSV:** `id=HID6200`; `name=dental_anatomic_variant`; `category=dental`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`

**Assessment:** No direct model found. Likely broad parent concept for variant findings.

**Response:**

---

### new model candidate: dental_postsurgical_change

**Source CSV:** `id=HID6400`; `name=dental_postsurgical_change`; `category=dental`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`

**Assessment:** No direct model found. Likely broad parent concept for postsurgical findings.

**Response:**

---

### new model candidate: dental_extraction

**Source CSV:** `id=HID6405`; `name=dental_extraction`; `category=dental`; `parent_id=HID6400`; `synonyms=tooth extraction, prior dental extraction`; `finding_type=observation`

**Assessment:** No direct model found.

**Response:**

---

### new model candidate: dental_restoration

**Source CSV:** `id=HID6410`; `name=dental_restoration`; `category=dental`; `parent_id=HID6400`; `synonyms=dental filling, dental hardware, dental prosthesis`; `finding_type=observation`

**Assessment:** No direct model found.

**Response:**

---

### new model candidate: dental_implant

**Source CSV:** `id=HID6415`; `name=dental_implant`; `category=dental`; `parent_id=HID6400`; `synonyms=osseointegrated dental implant, dental post`; `finding_type=observation`

**Assessment:** No direct model found.

**Response:**

---
