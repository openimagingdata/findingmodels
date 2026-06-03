# Review: head CT orbit batch 1

10 orbit CSV decisions to review: 5 newly created models and 5 mappings to existing models. For each, check name, description, synonyms, direction-of-change values, and whether the CSV row should map to the listed OIFM ID. Add your response below each entry.

---

### orbital abnormality
**Source file:** `defs/orbital_abnormality.fm.json`  
**ID:** `OIFM_OIDM_103555`  
**Description:** Broad grouping for orbital abnormality findings involving the orbit or globe on head CT or related orbital imaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID6600`; `name=orbital_abnormality`; `category=orbit`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`; `oifm_id=(blank)`

**Assessment:** Newly created from the orbit CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### orbital fat stranding
**Source file:** `defs/orbital_fat_stranding.fm.json`  
**ID:** `OIFM_OIDM_162332`  
**Description:** Imaging observation of orbital fat stranding involving the orbit or globe on head CT or related orbital imaging.  
**Synonyms:** retrobulbar fat stranding, intraorbital fat stranding  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID6605`; `name=orbital_fat_stranding`; `category=orbit`; `parent_id=HID6600`; `synonyms=retrobulbar fat stranding, intraorbital fat stranding`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the orbit CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### matched: proptosis -> exophthalmos
**Source file:** `defs/exophthalmos.fm.json`  
**ID:** `OIFM_GMTS_024505`  
**Description:** Protrusion of the eyeball from the orbit  
**Synonyms:** proptosis, globe protrusion  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased

**Source CSV:** `id=HID6610`; `name=proptosis`; `category=orbit`; `parent_id=HID6600`; `synonyms=exophthalmos, globe protrusion, globe displacement anterior`; `finding_type=observation`; `oifm_id=(blank)`

**QUESTION:** This row maps proptosis to the existing exophthalmos model because proptosis is already an explicit synonym. Confirm this equivalence is acceptable.

**Response:** 

---

### enophthalmos
**Source file:** `defs/enophthalmos.fm.json`  
**ID:** `OIFM_OIDM_049092`  
**Description:** Imaging observation of enophthalmos involving the orbit or globe on head CT or related orbital imaging.  
**Synonyms:** posterior globe displacement, sunken globe  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID6615`; `name=enophthalmos`; `category=orbit`; `parent_id=HID6600`; `synonyms=posterior globe displacement, sunken globe`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the orbit CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### matched: extraocular_muscle_enlargement -> extraocular muscle enlargement
**Source file:** `defs/extraocular_muscle_enlargement.fm.json`  
**ID:** `OIFM_GMTS_018581`  
**Description:** Increased size of one or more muscles that control eye movement  
**Synonyms:** enlarged extraocular muscle, EOM enlargement  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID6620`; `name=extraocular_muscle_enlargement`; `category=orbit`; `parent_id=HID6600`; `synonyms=extraocular muscle thickening, enlarged extraocular muscles, enlarged extraocular muscle`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Existing-model mapping. Confirm this CSV row should map to the listed OIFM ID.

**Response:** 

---

### extraocular muscle entrapment
**Source file:** `defs/extraocular_muscle_entrapment.fm.json`  
**ID:** `OIFM_OIDM_941408`  
**Description:** Imaging observation of extraocular muscle entrapment involving the orbit or globe on head CT or related orbital imaging.  
**Synonyms:** muscle incarceration, entrapped muscle  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID6625`; `name=extraocular_muscle_entrapment`; `category=orbit`; `parent_id=HID6600`; `synonyms=muscle incarceration, entrapped muscle`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the orbit CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### optic nerve sheath enlargement
**Source file:** `defs/optic_nerve_sheath_enlargement.fm.json`  
**ID:** `OIFM_OIDM_181428`  
**Description:** Imaging observation of optic nerve sheath enlargement involving the orbit or globe on head CT or related orbital imaging.  
**Synonyms:** optic nerve sheath dilation, optic nerve sheath distension, optic nerve sheath prominence  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID6630`; `name=optic_nerve_sheath_enlargement`; `category=orbit`; `parent_id=HID6600`; `synonyms=optic nerve sheath dilation, optic nerve sheath distension, optic nerve sheath prominence`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the orbit CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### matched: optic_nerve_enlargement -> optic nerve enlargement
**Source file:** `defs/optic_nerve_enlargement.fm.json`  
**ID:** `OIFM_GMTS_008113`  
**Description:** Increased diameter of the optic nerve.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID6635`; `name=optic_nerve_enlargement`; `category=orbit`; `parent_id=HID6600`; `synonyms=optic nerve thickening, enlarged optic nerve`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Existing-model mapping. Confirm this CSV row should map to the listed OIFM ID.

**Response:** 

---

### matched: superior_ophthalmic_vein_dilation -> enlarged superior ophthalmic vein
**Source file:** `defs/enlarged_superior_ophthalmic_vein.fm.json`  
**ID:** `OIFM_GMTS_018595`  
**Description:** Dilation or enlargement of the superior ophthalmic vein, often related to increased intracranial pressure.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID6640`; `name=superior_ophthalmic_vein_dilation`; `category=orbit`; `parent_id=HID6600`; `synonyms=dilated SOV, enlarged superior ophthalmic vein`; `finding_type=observation`; `oifm_id=(blank)`

**QUESTION:** This row maps superior ophthalmic vein dilation to enlarged superior ophthalmic vein. Confirm dilation/enlargement are acceptable synonyms here.

**Response:** 

---

### matched: orbital_lesion -> orbital mass
**Source file:** `defs/orbital_mass.fm.json`  
**ID:** `OIFM_OIDM_208758`  
**Description:** An orbital mass is a space-occupying lesion within the orbit that may arise from lacrimal gland, extraocular muscles, or other orbital tissues and can be benign or malignant; imaging features aid in characterization and differential diagnosis, with 'orbital mass' serving as the exemplar original phrasing.  
**Synonyms:** orbital mass, orbital lesion, orbital tumor  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID6650`; `name=orbital_lesion`; `category=orbit`; `parent_id=HID6600`; `synonyms=orbital mass, retrobulbar mass, retrobulbar lesion, intraorbital mass, intraorbital lesion`; `finding_type=observation`; `oifm_id=(blank)`

**QUESTION:** This row maps orbital lesion to the existing orbital mass model because orbital lesion is already an explicit synonym. Confirm lesion is not too broad for this model.

**Response:** 

