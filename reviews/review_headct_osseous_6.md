# Review: head CT osseous batch 6

9 models/mappings to review. For each, check name, description, synonyms, and direction-of-change values. Add your response below each entry.

---

### cranioplasty

**Source file:** `defs/cranioplasty.fm.json`  
**ID:** `OIFM_OIDM_430773`  
**Description:** Postoperative reconstruction or repair of a calvarial defect using autologous bone, mesh, plate, or other implant material.  
**Synonyms:** cranioplasty mesh, cranioplasty plate, skull reconstruction  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5710`; `name=cranioplasty`; `category=osseous`; `parent_id=HID5650`; `synonyms=cranioplasty mesh, cranioplasty plate, skull reconstruction`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### burr hole

**Source file:** `defs/burr_hole.fm.json`  
**ID:** `OIFM_OIDM_247440`  
**Description:** Small round calvarial defect created surgically by a burr hole or twist drill, commonly used for drainage, access, or device placement.  
**Synonyms:** burr hole defect, twist drill hole  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5715`; `name=burr_hole`; `category=osseous`; `parent_id=HID5650`; `synonyms=burr hole defect, twist drill hole`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### matched: cervical_spine_fusion -> cervical spine fusion

**Source file:** `defs/cervical_spine_fusion.fm.json`  
**ID:** `OIFM_GMTS_009764`  
**Description:** Surgical or congenital fusion of cervical vertebrae.  
**Synonyms:** fusion of cervical spine, cervical fusion, cervical vertebral fusion, cervical fixation, cervical spine instrumentation  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller  
**Source CSV:** `id=HID5720`; `name=cervical_spine_fusion`; `category=osseous`; `parent_id=HID5600`; `synonyms=cervical fixation, cervical spine instrumentation`; `finding_type=observation`

**QUESTION:** Existing GMTS model reused; CSV synonyms were added. Confirm this should cover postsurgical fusion in addition to congenital fusion.

**Response:** 

---

### open reduction internal fixation

**Source file:** `defs/open_reduction_internal_fixation.fm.json`  
**ID:** `OIFM_OIDM_938170`  
**Description:** Postoperative osseous fixation using plates, screws, or other hardware after open reduction of a fracture, including facial, maxillary, mandibular, or other craniofacial fixation.  
**Synonyms:** ORIF, open reduction and internal fixation, internal fixation, rigid fixation, plate and screw fixation, facial bone ORIF, maxillary ORIF, mandibular ORIF  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5725`; `name=open_reduction_internal_fixation`; `category=osseous`; `parent_id=HID5600`; `synonyms=ORIF, open reduction and internal fixation, internal fixation, rigid fixation, plate and screw fixation, facial bone ORIF, maxillary ORIF, mandibular ORIF`; `finding_type=observation`

**Assessment:** Mechanical review flagged `ORIF`; left capitalized as standard acronym.

**Response:** 

---

### occipitocervical fusion

**Source file:** `defs/occipitocervical_fusion.fm.json`  
**ID:** `OIFM_OIDM_087569`  
**Description:** Postoperative fusion spanning the occiput and upper cervical spine, typically with posterior instrumentation.  
**Synonyms:** OCF, occiput-to-cervical fusion, occipital-cervical fusion, occipital plate fixation  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5730`; `name=occipitocervical_fusion`; `category=osseous`; `parent_id=HID5600`; `synonyms=OCF, occiput-to-cervical fusion, occipital-cervical fusion, occipital plate fixation`; `finding_type=observation`

**Assessment:** Mechanical review flagged `OCF`; left capitalized as standard acronym.

**Response:** 

---

### osseous anatomic variant

**Source file:** `defs/osseous_anatomic_variant.fm.json`  
**ID:** `OIFM_OIDM_216407`  
**Description:** A developmental or anatomic variant involving skull, facial, or cervical osseous structures.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5800`; `name=osseous_anatomic_variant`; `category=osseous`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### matched: wormian_bone -> wormian bones

**Source file:** `defs/wormian_bones.fm.json`  
**ID:** `OIFM_GMTS_025593`  
**Description:** Accessory bones within the sutures of the skull, often associated with congenital disorders.  
**Synonyms:** wormian bone, multiple sutural bones, sutural bones, intrasutural bones  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller  
**Source CSV:** `id=HID5805`; `name=wormian_bone`; `category=osseous`; `parent_id=HID5800`; `synonyms=sutural bone, wormian bones`; `finding_type=observation`

**QUESTION:** Mapped singular CSV row to existing plural `wormian bones`; singular synonym was added.

**Response:** 

---

### persistent metopic suture

**Source file:** `defs/persistent_metopic_suture.fm.json`  
**ID:** `OIFM_OIDM_058112`  
**Description:** Persistence of the metopic suture beyond the expected age of fusion, seen as a midline frontal calvarial suture.  
**Synonyms:** unfused frontal suture  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5810`; `name=persistent_metopic_suture`; `category=osseous`; `parent_id=HID5800`; `synonyms=unfused frontal suture`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### enlarged parietal foramen

**Source file:** `defs/enlarged_parietal_foramen.fm.json`  
**ID:** `OIFM_OIDM_956084`  
**Description:** Congenital enlargement of one or both parietal foramina near the sagittal suture, often appearing as paired calvarial defects.  
**Synonyms:** biparietal foramina  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5815`; `name=enlarged_parietal_foramen`; `category=osseous`; `parent_id=HID5800`; `synonyms=biparietal foramina`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---
