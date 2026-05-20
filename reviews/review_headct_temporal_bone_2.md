# Review: head CT temporal bone batch 2

9 models/mappings to review. For each, check name, description, synonyms, and direction-of-change values. Add your response below each entry.

---

### matched: mastoiditis -> mastoiditis

**Source file:** `defs/mastoiditis.fm.json`  
**ID:** `OIFM_GMTS_008323`  
**Description:** Inflammation of the mastoid process.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller  
**Source CSV:** `id=HID8450`; `name=mastoiditis`; `category=temporal_bone`; `parent_id=HID8400`; `synonyms=(blank)`; `finding_type=diagnosis`

**Assessment:** Existing GMTS model reused. Mechanical lint normalized tag `head_neck` to `head neck`.

**Response:** 

---

### coalescent mastoiditis

**Source file:** `defs/coalescent_mastoiditis.fm.json`  
**ID:** `OIFM_OIDM_349548`  
**Description:** Complicated mastoiditis with destruction or coalescence of mastoid air cell septations, often with aggressive inflammatory change of the mastoid bone.  
**Synonyms:** coalescent mastoid disease  
**Change from prior:** unchanged, stable, new, resolved, worsened, improved  
**Source CSV:** `id=HID8455`; `name=coalescent_mastoiditis`; `category=temporal_bone`; `parent_id=HID8450`; `synonyms=coalescent mastoid disease`; `finding_type=diagnosis`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### otitis media

**Source file:** `defs/otitis_media.fm.json`  
**ID:** `OIFM_OIDM_678391`  
**Description:** Inflammation or infection of the middle ear, often associated with middle ear fluid or opacification on imaging.  
**Synonyms:** middle ear infection  
**Change from prior:** unchanged, stable, new, resolved, worsened, improved  
**Source CSV:** `id=HID8460`; `name=otitis_media`; `category=temporal_bone`; `parent_id=HID8400`; `synonyms=middle ear infection`; `finding_type=diagnosis`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### matched: cholesteatoma -> cholesteatoma

**Source file:** `defs/cholesteatoma.fm.json`  
**ID:** `OIFM_GMTS_008301`  
**Description:** An abnormal growth of squamous epithelium in the middle ear and/or mastoid process.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller  
**Source CSV:** `id=HID8465`; `name=cholesteatoma`; `category=temporal_bone`; `parent_id=HID8400`; `synonyms=(blank)`; `finding_type=diagnosis`

**Assessment:** Existing GMTS model reused. Mechanical lint normalized tag `head_neck` to `head neck`.

**Response:** 

---

### cholesterol granuloma

**Source file:** `defs/cholesterol_granuloma.fm.json`  
**ID:** `OIFM_OIDM_205071`  
**Description:** Expansile cystic inflammatory lesion containing cholesterol crystals, most often involving the petrous apex or middle ear/mastoid region.  
**Synonyms:** cholesterol cyst petrous  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller  
**Source CSV:** `id=HID8470`; `name=cholesterol_granuloma`; `category=temporal_bone`; `parent_id=HID8400`; `synonyms=cholesterol cyst petrous`; `finding_type=diagnosis`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### temporal bone postsurgical change

**Source file:** `defs/temporal_bone_postsurgical_change.fm.json`  
**ID:** `OIFM_OIDM_360934`  
**Description:** Expected or nonspecific postoperative alteration involving the temporal bone, mastoid, middle ear, external auditory canal, or related surgical bed.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID8600`; `name=temporal_bone_postsurgical_change`; `category=temporal_bone`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`

**Assessment:** New parent model for postoperative temporal-bone rows; confirm acceptable.

**Response:** 

---

### mastoidectomy

**Source file:** `defs/mastoidectomy.fm.json`  
**ID:** `OIFM_OIDM_635248`  
**Description:** Postoperative defect or surgical alteration related to mastoidectomy, including partial or complete removal of mastoid air cells.  
**Synonyms:** post mastoidectomy, mastoidectomy defect  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID8650`; `name=mastoidectomy`; `category=temporal_bone`; `parent_id=HID8600`; `synonyms=post mastoidectomy, mastoidectomy defect`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### canal wall down mastoidectomy

**Source file:** `defs/canal_wall_down_mastoidectomy.fm.json`  
**ID:** `OIFM_OIDM_038053`  
**Description:** Postoperative mastoidectomy cavity in which the posterior external auditory canal wall has been removed, creating an open mastoid bowl.  
**Synonyms:** open cavity mastoidectomy, radical mastoidectomy, modified radical mastoidectomy  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID8655`; `name=canal_wall_down_mastoidectomy`; `category=temporal_bone`; `parent_id=HID8650`; `synonyms=open cavity mastoidectomy, radical mastoidectomy, modified radical mastoidectomy`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### canal wall up mastoidectomy

**Source file:** `defs/canal_wall_up_mastoidectomy.fm.json`  
**ID:** `OIFM_OIDM_471826`  
**Description:** Postoperative mastoidectomy in which the posterior external auditory canal wall is preserved, maintaining the normal canal wall contour.  
**Synonyms:** intact canal wall mastoidectomy, closed mastoidectomy  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID8660`; `name=canal_wall_up_mastoidectomy`; `category=temporal_bone`; `parent_id=HID8650`; `synonyms=intact canal wall mastoidectomy, closed mastoidectomy`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---
