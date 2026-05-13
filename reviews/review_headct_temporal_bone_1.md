# Review: head CT temporal bone batch 1

19 temporal_bone CSV decisions to review. This category does not appear to have a prior batch review file: no `review_headct_temporal_bone*.md` file was present.

This is a triage handoff, not a finalized model-creation batch. Entries marked **new model candidate** or **question** need reviewer direction before model creation. Existing-match entries still need reviewer confirmation before CSV writeback.

---
### new model candidate: temporal_bone_abnormality

**Source CSV:** `id=HID8400`; `name=temporal_bone_abnormality`; `category=temporal_bone`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`

**Assessment:** No direct broad temporal-bone abnormality model found. Existing temporal-bone models are more specific.

**Response:**

---
### matched/question: mastoid_opacification -> mastoid air cell effusion

**Source file:** `defs/mastoid_air_cell_effusion.fm.json`  
**ID:** `OIFM_OIDM_228653`  
**Description:** Fluid within the mastoid air cell system visible on imaging, presenting as opacification of the mastoid region. This finding may reflect otitis media with effusion or mastoiditis; the original term "mastoid air cell fluid" illustrates this context.  
**Synonyms:** mastoid air cell fluid, fluid in mastoid air cells, mastoid effusion, mastoid air cell opacification  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID8405`; `name=mastoid_opacification`; `category=temporal_bone`; `parent_id=HID8400`; `synonyms=mastoid air cell opacification, opacified mastoid`; `finding_type=observation`

**Assessment:** Existing model has `mastoid air cell opacification` as a synonym, but its canonical name commits to effusion/fluid. Confirm whether generic `mastoid_opacification` should map to this model, or whether a separate observation model is needed with effusion/fluid as a subtype.

**Response:**

---
### matched: mastoid_fluid -> mastoid air cell effusion

**Source file:** `defs/mastoid_air_cell_effusion.fm.json`  
**ID:** `OIFM_OIDM_228653`  
**Description:** Fluid within the mastoid air cell system visible on imaging, presenting as opacification of the mastoid region. This finding may reflect otitis media with effusion or mastoiditis; the original term "mastoid air cell fluid" illustrates this context.  
**Synonyms:** mastoid air cell fluid, fluid in mastoid air cells, mastoid effusion, mastoid air cell opacification  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID8406`; `name=mastoid_fluid`; `category=temporal_bone`; `parent_id=HID8405`; `synonyms=mastoid effusion, fluid in mastoid air cells, mastoid air cell fluid`; `finding_type=observation`

**Assessment:** Direct synonym match. Confirm mapping and whether canonical should remain `mastoid air cell effusion` or shift toward CSV term `mastoid fluid`.

**Response:**

---
### question: hypopneumatized_mastoid

**Candidate files:** `defs/underdeveloped_mastoid.fm.json`, `defs/underdevelopment_of_mastoids.fm.json`  
**Candidate IDs:** `OIFM_GMTS_025530`, `OIFM_GMTS_008328`

**Source CSV:** `id=HID8410`; `name=hypopneumatized_mastoid`; `category=temporal_bone`; `parent_id=HID8400`; `synonyms=sclerotic mastoid, underpneumatized mastoid, poorly pneumatized mastoid, mastoid sclerosis`; `finding_type=observation`

**Question:** Existing models cover underdeveloped/hypoplastic mastoid air cells, but CSV synonyms also include `sclerotic mastoid` and `mastoid sclerosis`, which may reflect chronic acquired change rather than developmental hypoplasia. Should this map to an existing underdevelopment model, or should a new `hypopneumatized mastoid` model be created?

**Response:**

---
### question: middle_ear_opacification

**Candidate file:** `defs/soft_tissue_in_the_middle_ear.fm.json`  
**Candidate ID:** `OIFM_GMTS_008295`  
**Candidate description:** Presence of soft tissue density in the tympanic cavity, possibly indicating fluid or mass.  
**Candidate synonyms:** middle ear effusion, middle ear mass

**Source CSV:** `id=HID8415`; `name=middle_ear_opacification`; `category=temporal_bone`; `parent_id=HID8400`; `synonyms=opacified middle ear`; `finding_type=observation`

**Question:** `soft tissue in the middle ear` appears close to middle-ear opacification, but the current model also carries `middle ear mass` as a synonym. Should CSV `middle_ear_opacification` map to this existing model, or should a cleaner `middle ear opacification` observation model be created?

**Response:**

---
### matched/question: middle_ear_fluid -> soft tissue in the middle ear

**Source file:** `defs/soft_tissue_in_the_middle_ear.fm.json`  
**ID:** `OIFM_GMTS_008295`  
**Description:** Presence of soft tissue density in the tympanic cavity, possibly indicating fluid or mass.  
**Synonyms:** middle ear effusion, middle ear mass  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID8416`; `name=middle_ear_fluid`; `category=temporal_bone`; `parent_id=HID8415`; `synonyms=middle ear effusion, tympanic cavity fluid, middle ear fluid collection`; `finding_type=observation`

**Assessment:** Existing model has `middle ear effusion` as a synonym, but canonical scope is broader than fluid. Confirm mapping, or create a specific `middle ear fluid` / `middle ear effusion` model and remove the effusion synonym from the broader soft-tissue model.

**Response:**

---
### new model candidate: external_auditory_canal_opacification

**Source CSV:** `id=HID8420`; `name=external_auditory_canal_opacification`; `category=temporal_bone`; `parent_id=HID8400`; `synonyms=EAC soft tissue, ear canal opacification`; `finding_type=observation`

**Assessment:** No direct model found. Related models such as `external auditory canal tumor` and `external auditory canal stenosis` are different findings.

**Response:**

---
### new model candidate: ossicular_disruption

**Source CSV:** `id=HID8425`; `name=ossicular_disruption`; `category=temporal_bone`; `parent_id=HID8400`; `synonyms=ossicular dislocation, ossicular chain disruption`; `finding_type=observation`

**Assessment:** No direct model found.

**Response:**

---
### question: petrous_apex_lesion

**Candidate file:** `defs/destructive_lesion_in_petrous_apex.fm.json`  
**Candidate ID:** `OIFM_GMTS_008280`  
**Candidate description:** A lesion causing bone destruction in the petrous portion of the temporal bone.

**Source CSV:** `id=HID8430`; `name=petrous_apex_lesion`; `category=temporal_bone`; `parent_id=HID8400`; `synonyms=petrous apex mass`; `finding_type=observation`

**Question:** Existing candidate is a destructive petrous-apex lesion, which is more specific than generic `petrous_apex_lesion`. Create a new generic petrous apex lesion model?

**Response:**

---
### matched/question: temporal_bone_erosion -> temporal bone osteolysis

**Source file:** `defs/temporal_bone_osteolysis.fm.json`  
**ID:** `OIFM_GMTS_008274`  
**Description:** Destruction of the temporal bone usually due to infection or neoplasm.  
**Synonyms:** temporal bone lysis  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID8435`; `name=temporal_bone_erosion`; `category=temporal_bone`; `parent_id=HID8400`; `synonyms=temporal bone destruction`; `finding_type=observation`

**Assessment:** `Temporal bone osteolysis` appears close to temporal bone erosion/destruction, but terminology and scope may differ. Confirm mapping and whether `temporal bone erosion` / `temporal bone destruction` should be added as synonyms.

**Response:**

---
### matched: mastoiditis -> mastoiditis

**Source file:** `defs/mastoiditis.fm.json`  
**ID:** `OIFM_GMTS_008323`  
**Description:** Inflammation of the mastoid process.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID8450`; `name=mastoiditis`; `category=temporal_bone`; `parent_id=HID8400`; `synonyms=(blank)`; `finding_type=diagnosis`

**Assessment:** Direct name match. Confirm acceptable.

**Response:**

---
### new model candidate: coalescent_mastoiditis

**Source CSV:** `id=HID8455`; `name=coalescent_mastoiditis`; `category=temporal_bone`; `parent_id=HID8450`; `synonyms=coalescent mastoid disease`; `finding_type=diagnosis`

**Assessment:** No direct model found. Likely subtype of mastoiditis with bony septal destruction.

**Response:**

---
### new model candidate: otitis_media

**Source CSV:** `id=HID8460`; `name=otitis_media`; `category=temporal_bone`; `parent_id=HID8400`; `synonyms=middle ear infection`; `finding_type=diagnosis`

**Assessment:** No direct model found.

**Response:**

---
### matched: cholesteatoma -> cholesteatoma

**Source file:** `defs/cholesteatoma.fm.json`  
**ID:** `OIFM_GMTS_008301`  
**Description:** An abnormal growth of squamous epithelium in the middle ear and/or mastoid process.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID8465`; `name=cholesteatoma`; `category=temporal_bone`; `parent_id=HID8400`; `synonyms=(blank)`; `finding_type=diagnosis`

**Assessment:** Direct name match. Confirm acceptable.

**Response:**

---
### new model candidate: cholesterol_granuloma

**Source CSV:** `id=HID8470`; `name=cholesterol_granuloma`; `category=temporal_bone`; `parent_id=HID8400`; `synonyms=cholesterol cyst petrous`; `finding_type=diagnosis`

**Assessment:** No direct model found.

**Response:**

---
### new model candidate: temporal_bone_postsurgical_change

**Source CSV:** `id=HID8600`; `name=temporal_bone_postsurgical_change`; `category=temporal_bone`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`

**Assessment:** No direct broad postsurgical temporal-bone model found.

**Response:**

---
### new model candidate: mastoidectomy

**Source CSV:** `id=HID8650`; `name=mastoidectomy`; `category=temporal_bone`; `parent_id=HID8600`; `synonyms=post mastoidectomy, mastoidectomy defect`; `finding_type=observation`

**Assessment:** No direct model found.

**Response:**

---
### new model candidate: canal_wall_down_mastoidectomy

**Source CSV:** `id=HID8655`; `name=canal_wall_down_mastoidectomy`; `category=temporal_bone`; `parent_id=HID8650`; `synonyms=open cavity mastoidectomy, radical mastoidectomy, modified radical mastoidectomy`; `finding_type=observation`

**Assessment:** No direct model found. Reviewer should confirm whether `radical mastoidectomy` and `modified radical mastoidectomy` are equivalent enough to include as synonyms.

**Response:**

---
### new model candidate: canal_wall_up_mastoidectomy

**Source CSV:** `id=HID8660`; `name=canal_wall_up_mastoidectomy`; `category=temporal_bone`; `parent_id=HID8650`; `synonyms=intact canal wall mastoidectomy, closed mastoidectomy`; `finding_type=observation`

**Assessment:** No direct model found.

**Response:**

---
