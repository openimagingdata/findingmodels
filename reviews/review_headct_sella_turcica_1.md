# Review: head CT sella turcica batch 1

14 sella_turcica CSV decisions to review. This category does not appear to have a prior batch review file: no `review_headct_sella*.md` file was present. Git history has older general head CT quality-review commits, but no category-specific sella_turcica batch handoff was found.

This is a triage handoff, not a finalized model-creation batch. Entries marked **new model candidate** or **question** need reviewer direction before model creation.

---

### question: sellar_abnormality

**Candidate file:** `defs/sellar_lesion.fm.json`  
**Candidate ID:** `OIFM_GMTS_030847`  
**Candidate description:** An abnormality in the sella turcica, often affecting the pituitary gland.  
**Candidate synonyms:** pituitary mass

**Source CSV:** `id=HID2200`; `name=sellar_abnormality`; `category=sella_turcica`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`

**Question:** Should broad `sellar_abnormality` map to `sellar lesion`, or should a separate broad parent model be created?

**Response:**

---

### question: sellar_mass

**Candidate files:** `defs/sella_mass.fm.json`, `defs/isodense_sellar_lesion.fm.json`, `defs/sellar_lesion.fm.json`  
**Candidate IDs:** `OIFM_CDE_000277`, `OIFM_GMTS_033473`, `OIFM_GMTS_030847`

**Source CSV:** `id=HID2250`; `name=sellar_mass`; `category=sella_turcica`; `parent_id=HID2200`; `synonyms=suprasellar mass, intrasellar mass, sellar and suprasellar mass`; `finding_type=(blank)`

**Question:** Should this map to the CDE `Sella Mass` model despite legacy casing/attribute structure, to `sellar lesion`, or should a new OIDM `sellar mass` model be created?

**Response:**

---

### new model candidate: pituitary_adenoma

**Source CSV:** `id=HID2300`; `name=pituitary_adenoma`; `category=sella_turcica`; `parent_id=HID2250`; `synonyms=pituitary tumor`; `finding_type=diagnosis`

**Assessment:** No direct model found. Existing `sellar lesion` has `pituitary mass` synonym but is broader than adenoma.

**Response:**

---

### new model candidate: pituitary_macroadenoma

**Source CSV:** `id=HID2305`; `name=pituitary_macroadenoma`; `category=sella_turcica`; `parent_id=HID2300`; `synonyms=macroadenoma`; `finding_type=diagnosis`

**Assessment:** No direct model found. Reviewer should decide whether this should be separate from `pituitary adenoma`.

**Response:**

---

### matched: expanded_sella -> sella turcica enlargement

**Source file:** `defs/sella_turcica_enlargement.fm.json`  
**ID:** `OIFM_GMTS_025584`  
**Description:** Increased size of the sella turcica, the bony cavity in the skull.  
**Synonyms:** enlarged sella turcica, expanded sella, expanded sella turcica, enlarged sella, sella enlargement, enlarged pituitary fossa, expanded pituitary fossa, ballooned sella, large sella turcica

**Source CSV:** `id=HID2310`; `name=expanded_sella`; `category=sella_turcica`; `parent_id=HID2200`; `synonyms=enlarged sella, expanded sella turcica, sella enlargement, enlarged pituitary fossa, expanded pituitary fossa, ballooned sella`; `finding_type=observation`

**Assessment:** Direct synonym match. Confirm this CSV row should map to the existing model.

**Response:**

---

### question: sellar_calcification

**Candidate file:** `defs/parasellar_calcification.fm.json`  
**Candidate ID:** `OIFM_GMTS_006843`  
**Candidate description:** Calcification in the parasellar region, often associated with craniopharyngiomas or meningiomas.

**Source CSV:** `id=HID2315`; `name=sellar_calcification`; `category=sella_turcica`; `parent_id=HID2200`; `synonyms=calcification in sella, sellar region calcification`; `finding_type=observation`

**Question:** Should sellar calcification map to parasellar calcification, or is the location different enough to create a new `sellar calcification` model?

**Response:**

---

### new model candidate: empty_sella

**Source CSV:** `id=HID2350`; `name=empty_sella`; `category=sella_turcica`; `parent_id=HID2200`; `synonyms=empty pituitary fossa, CSF-filled sella`; `finding_type=diagnosis`

**Assessment:** No direct model found. `csf-intensity sellar/suprasellar lesion` is related but not equivalent.

**Response:**

---

### new model candidate: partially_empty_sella

**Source CSV:** `id=HID2355`; `name=partially_empty_sella`; `category=sella_turcica`; `parent_id=HID2350`; `synonyms=partial empty sella`; `finding_type=diagnosis`

**Assessment:** No direct model found. Reviewer should decide whether this should be separate from `empty sella`.

**Response:**

---

### new model candidate: pituitary_hemorrhage

**Source CSV:** `id=HID2360`; `name=pituitary_hemorrhage`; `category=sella_turcica`; `parent_id=HID2200`; `synonyms=sellar hemorrhage`; `finding_type=diagnosis`

**Assessment:** No direct model found.

**Response:**

---

### new model candidate: pituitary_apoplexy

**Source CSV:** `id=HID2365`; `name=pituitary_apoplexy`; `category=sella_turcica`; `parent_id=HID2200`; `synonyms=(blank)`; `finding_type=diagnosis`

**Assessment:** No direct model found. Related to pituitary hemorrhage but clinically distinct.

**Response:**

---

### new model candidate: craniopharyngioma

**Source CSV:** `id=HID2370`; `name=craniopharyngioma`; `category=sella_turcica`; `parent_id=HID2200`; `synonyms=(blank)`; `finding_type=diagnosis`

**Assessment:** No direct model found.

**Response:**

---

### new model candidate: rathke_cleft_cyst

**Source CSV:** `id=HID2375`; `name=rathke_cleft_cyst`; `category=sella_turcica`; `parent_id=HID2200`; `synonyms=Rathke pouch cyst`; `finding_type=diagnosis`

**Assessment:** No direct model found.

**Response:**

---

### question: sellar_postsurgical_change

**Candidate file:** `defs/pituitary_post_operative_sella.fm.json`  
**Candidate ID:** `OIFM_CDE_000274`  
**Candidate description:** Pituitary Post-Operative Sella

**Source CSV:** `id=HID2400`; `name=sellar_postsurgical_change`; `category=sella_turcica`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`

**Question:** Should this map to the existing CDE post-operative sella model despite legacy structure, or should a simpler OIDM postsurgical-change model be created?

**Response:**

---

### question: transsphenoidal_surgery

**Candidate file:** `defs/pituitary_post_operative_sella.fm.json`  
**Candidate ID:** `OIFM_CDE_000274`  
**Candidate note:** Existing model includes `trans-sphenoidal` as a surgical approach value.

**Source CSV:** `id=HID2405`; `name=transsphenoidal_surgery`; `category=sella_turcica`; `parent_id=HID2400`; `synonyms=post transsphenoidal resection, transsphenoidal approach changes, endoscopic endonasal surgery, endoscopic transsphenoidal surgery`; `finding_type=observation`

**Question:** Should this map to `pituitary post-operative sella`, or should a separate `transsphenoidal surgery` observation model be created?

**Response:**

---
