# Review: head CT osseous batch 5

9 models/mappings to review. For each, check name, description, synonyms, and direction-of-change values. Add your response below each entry.

---

### hyperostosis frontalis interna

**Source file:** `defs/hyperostosis_frontalis_interna.fm.json`  
**ID:** `OIFM_OIDM_850757`  
**Description:** Benign thickening of the inner table of the frontal bone, typically bilateral and symmetric.  
**Synonyms:** HFI, frontal hyperostosis  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased  
**Source CSV:** `id=HID5455`; `name=hyperostosis_frontalis_interna`; `category=osseous`; `parent_id=HID5000`; `synonyms=HFI, frontal hyperostosis`; `finding_type=diagnosis`

**Assessment:** Mechanical review flagged `HFI`; left capitalized as standard acronym.

**Response:** 

---

### matched: craniosynostosis -> craniosynostosis

**Source file:** `defs/craniosynostosis.fm.json`  
**ID:** `OIFM_GMTS_006368`  
**Description:** Premature fusion of one or more cranial sutures.  
**Synonyms:** premature suture fusion, craniostenosis, fused suture  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5460`; `name=craniosynostosis`; `category=osseous`; `parent_id=HID5000`; `synonyms=premature suture fusion, craniostenosis, fused suture`; `finding_type=diagnosis`

**QUESTION:** Existing GMTS model reused; CSV synonyms were added. Mechanical review notes missing person contributor on reused GMTS model.

**Response:** 

---

### degenerative changes

**Source file:** `defs/degenerative_changes.fm.json`  
**ID:** `OIFM_OIDM_463032`  
**Description:** Chronic degenerative osseous or joint changes, including osteophytes, disc degeneration, facet arthropathy, or other age-related spondylotic findings.  
**Synonyms:** degenerative disease  
**Change from prior:** unchanged, stable, new, resolved, worsened, improved  
**Source CSV:** `id=HID5500`; `name=degenerative_changes`; `category=osseous`; `parent_id=HID5000`; `synonyms=degenerative disease`; `finding_type=diagnosis`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### cervical spine degenerative changes

**Source file:** `defs/cervical_spine_degenerative_changes.fm.json`  
**ID:** `OIFM_OIDM_200329`  
**Description:** Degenerative changes of the cervical spine, including spondylosis, disc space narrowing, uncovertebral hypertrophy, facet arthropathy, or osteophytes.  
**Synonyms:** cervical spondylosis, C-spine DJD  
**Change from prior:** unchanged, stable, new, resolved, worsened, improved  
**Source CSV:** `id=HID5505`; `name=cervical_spine_degenerative_changes`; `category=osseous`; `parent_id=HID5500`; `synonyms=cervical spondylosis, C-spine DJD`; `finding_type=diagnosis`

**Assessment:** Mechanical review flagged `C-spine DJD`; left capitalized as common abbreviation.

**Response:** 

---

### osseous postsurgical change

**Source file:** `defs/osseous_postsurgical_change.fm.json`  
**ID:** `OIFM_OIDM_671573`  
**Description:** Expected or nonspecific postoperative alteration involving bone or osseous structures of the skull, face, or cervical spine.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5600`; `name=osseous_postsurgical_change`; `category=osseous`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### calvarial surgery

**Source file:** `defs/calvarial_surgery.fm.json`  
**ID:** `OIFM_OIDM_335200`  
**Description:** Postoperative change involving the calvarium, including craniotomy, craniectomy, burr hole, cranioplasty, or other cranial surgical alteration.  
**Synonyms:** prior cranial surgery, calvarial surgical change  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5650`; `name=calvarial_surgery`; `category=osseous`; `parent_id=HID5600`; `synonyms=prior cranial surgery, calvarial surgical change`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### craniotomy

**Source file:** `defs/craniotomy.fm.json`  
**ID:** `OIFM_OIDM_269188`  
**Description:** Postoperative calvarial defect or bone flap related to craniotomy, typically with a replaceable or fixed skull flap.  
**Synonyms:** craniotomy defect, craniotomy flap, post craniotomy  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5655`; `name=craniotomy`; `category=osseous`; `parent_id=HID5650`; `synonyms=craniotomy defect, craniotomy flap, post craniotomy`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### craniectomy

**Source file:** `defs/craniectomy.fm.json`  
**ID:** `OIFM_OIDM_210642`  
**Description:** Postoperative calvarial defect from removal of a skull flap, commonly performed for decompression or surgical access.  
**Synonyms:** decompressive craniectomy, bone flap absent  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5700`; `name=craniectomy`; `category=osseous`; `parent_id=HID5650`; `synonyms=decompressive craniectomy, bone flap absent`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### hemicraniectomy

**Source file:** `defs/hemicraniectomy.fm.json`  
**ID:** `OIFM_OIDM_251139`  
**Description:** Large unilateral craniectomy involving one side of the calvarium, usually performed for decompression.  
**Synonyms:** hemicranectomy  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5705`; `name=hemicraniectomy`; `category=osseous`; `parent_id=HID5700`; `synonyms=hemicranectomy`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---
