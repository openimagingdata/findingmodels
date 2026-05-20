# Review: head CT temporal bone batch 1

10 models/mappings to review. For each, check name, description, synonyms, and direction-of-change values. Add your response below each entry.

---

### temporal bone abnormality

**Source file:** `defs/temporal_bone_abnormality.fm.json`  
**ID:** `OIFM_OIDM_490443`  
**Description:** A nonspecific abnormality involving the temporal bone or its associated mastoid, middle ear, external auditory canal, ossicular, or petrous apex structures.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID8400`; `name=temporal_bone_abnormality`; `category=temporal_bone`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`

**Assessment:** New parent model for temporal-bone rows; confirm acceptable.

**Response:** 

---

### mastoid opacification

**Source file:** `defs/mastoid_opacification.fm.json`  
**ID:** `OIFM_OIDM_475675`  
**Description:** Nonspecific opacification of the mastoid air cells on imaging, which may reflect fluid, inflammatory material, soft tissue, or postoperative change depending on context.  
**Synonyms:** opacified mastoid  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased  
**Source CSV:** `id=HID8405`; `name=mastoid_opacification`; `category=temporal_bone`; `parent_id=HID8400`; `synonyms=mastoid air cell opacification, opacified mastoid`; `finding_type=observation`

**QUESTION:** I did not include `mastoid air cell opacification` because it already exists on `mastoid air cell effusion`; confirm whether that synonym should stay with effusion or move here.

**Response:** 

---

### matched: mastoid_fluid -> mastoid air cell effusion

**Source file:** `defs/mastoid_air_cell_effusion.fm.json`  
**ID:** `OIFM_OIDM_228653`  
**Description:** Fluid within the mastoid air cell system visible on imaging, presenting as opacification of the mastoid region. This finding may reflect otitis media with effusion or mastoiditis; the original term "mastoid air cell fluid" illustrates this context.  
**Synonyms:** mastoid air cell fluid, fluid in mastoid air cells, mastoid effusion, mastoid air cell opacification  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller  
**Source CSV:** `id=HID8406`; `name=mastoid_fluid`; `category=temporal_bone`; `parent_id=HID8405`; `synonyms=mastoid effusion, fluid in mastoid air cells, mastoid air cell fluid`; `finding_type=observation`

**Assessment:** Existing model reused; confirm this mapping is acceptable.

**Response:** 

---

### matched: hypopneumatized_mastoid -> underdevelopment of mastoids

**Source file:** `defs/underdevelopment_of_mastoids.fm.json`  
**ID:** `OIFM_GMTS_008328`  
**Description:** Hypoplasia of the mastoid air cells on one or both sides.  
**Synonyms:** mastoid hypoplasia, hypopneumatized mastoid, sclerotic mastoid, underpneumatized mastoid, poorly pneumatized mastoid, mastoid sclerosis  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller  
**Source CSV:** `id=HID8410`; `name=hypopneumatized_mastoid`; `category=temporal_bone`; `parent_id=HID8400`; `synonyms=sclerotic mastoid, underpneumatized mastoid, poorly pneumatized mastoid, mastoid sclerosis`; `finding_type=observation`

**Assessment:** Existing GMTS model reused; CSV synonyms were added. Mechanical lint also normalized tag `head_neck` to `head neck`.

**Response:** 

---

### matched: middle_ear_opacification -> soft tissue in the middle ear

**Source file:** `defs/soft_tissue_in_the_middle_ear.fm.json`  
**ID:** `OIFM_GMTS_008295`  
**Description:** Presence of soft tissue density in the tympanic cavity, possibly indicating fluid or mass.  
**Synonyms:** middle ear effusion, middle ear mass, opacified middle ear, tympanic cavity fluid, middle ear fluid collection  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller  
**Source CSV:** `id=HID8415`; `name=middle_ear_opacification`; `category=temporal_bone`; `parent_id=HID8400`; `synonyms=opacified middle ear`; `finding_type=observation`

**QUESTION:** I mapped this to the existing broader `soft tissue in the middle ear` model and added the CSV synonym. Confirm whether we should keep that broad model rather than create a separate `middle ear opacification`.

**Response:** 

---

### matched: middle_ear_fluid -> soft tissue in the middle ear

**Source file:** `defs/soft_tissue_in_the_middle_ear.fm.json`  
**ID:** `OIFM_GMTS_008295`  
**Description:** Presence of soft tissue density in the tympanic cavity, possibly indicating fluid or mass.  
**Synonyms:** middle ear effusion, middle ear mass, opacified middle ear, tympanic cavity fluid, middle ear fluid collection  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller  
**Source CSV:** `id=HID8416`; `name=middle_ear_fluid`; `category=temporal_bone`; `parent_id=HID8415`; `synonyms=middle ear effusion, tympanic cavity fluid, middle ear fluid collection`; `finding_type=observation`

**QUESTION:** This is also mapped to `soft tissue in the middle ear`; confirm whether a dedicated `middle ear effusion` model is preferred instead.

**Response:** 

---

### external auditory canal opacification

**Source file:** `defs/external_auditory_canal_opacification.fm.json`  
**ID:** `OIFM_OIDM_691643`  
**Description:** Soft-tissue or fluid attenuation material filling or partly filling the external auditory canal on imaging.  
**Synonyms:** EAC soft tissue, ear canal opacification  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased  
**Source CSV:** `id=HID8420`; `name=external_auditory_canal_opacification`; `category=temporal_bone`; `parent_id=HID8400`; `synonyms=EAC soft tissue, ear canal opacification`; `finding_type=observation`

**QUESTION:** Mechanical review flagged `EAC soft tissue` for capitalization; I left `EAC` as an accepted acronym. Confirm acceptable.

**Response:** 

---

### ossicular disruption

**Source file:** `defs/ossicular_disruption.fm.json`  
**ID:** `OIFM_OIDM_848829`  
**Description:** Discontinuity, displacement, or dislocation of the middle ear ossicular chain visible on imaging, often related to trauma, erosion, or prior surgery.  
**Synonyms:** ossicular dislocation, ossicular chain disruption  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID8425`; `name=ossicular_disruption`; `category=temporal_bone`; `parent_id=HID8400`; `synonyms=ossicular dislocation, ossicular chain disruption`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### petrous apex lesion

**Source file:** `defs/petrous_apex_lesion.fm.json`  
**ID:** `OIFM_OIDM_172477`  
**Description:** A focal abnormality centered in the petrous apex of the temporal bone, such as a cystic, inflammatory, expansile, or neoplastic lesion.  
**Synonyms:** petrous apex mass  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller  
**Source CSV:** `id=HID8430`; `name=petrous_apex_lesion`; `category=temporal_bone`; `parent_id=HID8400`; `synonyms=petrous apex mass`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### matched: temporal_bone_erosion -> temporal bone osteolysis

**Source file:** `defs/temporal_bone_osteolysis.fm.json`  
**ID:** `OIFM_GMTS_008274`  
**Description:** Destruction of the temporal bone usually due to infection or neoplasm.  
**Synonyms:** temporal bone lysis, temporal bone erosion, temporal bone destruction  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller  
**Source CSV:** `id=HID8435`; `name=temporal_bone_erosion`; `category=temporal_bone`; `parent_id=HID8400`; `synonyms=temporal bone destruction`; `finding_type=observation`

**Assessment:** Existing GMTS model reused; CSV terms were added as synonyms. Mechanical lint also normalized tag `head_neck` to `head neck`.

**Response:** 

---
