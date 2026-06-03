# Review: head CT orbit batch 2

10 orbit CSV decisions to review: 7 newly created models and 3 mappings to existing models. For each, check name, description, synonyms, direction-of-change values, and whether the CSV row should map to the listed OIFM ID. Add your response below each entry.

---

### lacrimal gland lesion
**Source file:** `defs/lacrimal_gland_lesion.fm.json`  
**ID:** `OIFM_OIDM_969269`  
**Description:** Imaging observation of lacrimal gland lesion involving the orbit or globe on head CT or related orbital imaging.  
**Synonyms:** lacrimal gland mass, lacrimal fossa mass, lacrimal fossa lesion  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID6655`; `name=lacrimal_gland_lesion`; `category=orbit`; `parent_id=HID6650`; `synonyms=lacrimal gland mass, lacrimal fossa mass, lacrimal fossa lesion`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the orbit CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### matched: intraocular_lesion -> globe lesion
**Source file:** `defs/globe_lesion.fm.json`  
**ID:** `OIFM_GMTS_018561`  
**Description:** Lesion affecting the eye globe  
**Synonyms:** ocular lesion, eye globe lesion  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID6660`; `name=intraocular_lesion`; `category=orbit`; `parent_id=HID6600`; `synonyms=intraocular mass, globe mass, globe lesion`; `finding_type=observation`; `oifm_id=(blank)`

**QUESTION:** This row maps intraocular lesion to globe lesion. Confirm globe lesion is the intended existing model for intraocular lesion.

**Response:** 

---

### orbital emphysema
**Source file:** `defs/orbital_emphysema.fm.json`  
**ID:** `OIFM_OIDM_176713`  
**Description:** Imaging observation of orbital emphysema involving the orbit or globe on head CT or related orbital imaging.  
**Synonyms:** intraorbital air, orbital air  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID6665`; `name=orbital_emphysema`; `category=orbit`; `parent_id=HID6600`; `synonyms=intraorbital air, orbital air`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the orbit CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### orbital fat herniation
**Source file:** `defs/orbital_fat_herniation.fm.json`  
**ID:** `OIFM_OIDM_764992`  
**Description:** Imaging observation of orbital fat herniation involving the orbit or globe on head CT or related orbital imaging.  
**Synonyms:** orbital fat prolapse  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID6670`; `name=orbital_fat_herniation`; `category=orbit`; `parent_id=HID6600`; `synonyms=orbital fat prolapse`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the orbit CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### globe rupture
**Source file:** `defs/globe_rupture.fm.json`  
**ID:** `OIFM_OIDM_324483`  
**Description:** Imaging observation of globe rupture involving the orbit or globe on head CT or related orbital imaging.  
**Synonyms:** open globe, ruptured globe, open globe injury, globe disruption  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID6675`; `name=globe_rupture`; `category=orbit`; `parent_id=HID6600`; `synonyms=open globe, ruptured globe, open globe injury, globe disruption`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the orbit CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### matched: globe_calcification -> globe calcification
**Source file:** `defs/globe_calcification.fm.json`  
**ID:** `OIFM_GMTS_008203`  
**Description:** Calcium deposits within the globe of the eye.  
**Synonyms:** ocular calcification  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID6680`; `name=globe_calcification`; `category=orbit`; `parent_id=HID6600`; `synonyms=calcified globe, calcified lens, lens calcification`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Existing-model mapping. Confirm this CSV row should map to the listed OIFM ID.

**Response:** 

---

### matched: lens_dislocation -> lens dislocation
**Source file:** `defs/lens_dislocation.fm.json`  
**ID:** `OIFM_GMTS_025548`  
**Description:** Displacement of the ocular lens from its normal position.  
**Synonyms:** ectopia lentis  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID6685`; `name=lens_dislocation`; `category=orbit`; `parent_id=HID6600`; `synonyms=lens subluxation, dislocated lens, ectopia lentis, displaced lens`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Existing-model mapping. Confirm this CSV row should map to the listed OIFM ID.

**Response:** 

---

### traumatic cataract
**Source file:** `defs/traumatic_cataract.fm.json`  
**ID:** `OIFM_OIDM_225997`  
**Description:** Imaging observation of traumatic cataract involving the orbit or globe on head CT or related orbital imaging.  
**Synonyms:** hypodense lens, lens swelling, lens edema  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID6690`; `name=traumatic_cataract`; `category=orbit`; `parent_id=HID6600`; `synonyms=hypodense lens, lens swelling, lens edema`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the orbit CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### retinal detachment
**Source file:** `defs/retinal_detachment.fm.json`  
**ID:** `OIFM_OIDM_119674`  
**Description:** Imaging observation of retinal detachment involving the orbit or globe on head CT or related orbital imaging.  
**Synonyms:** detached retina  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID6695`; `name=retinal_detachment`; `category=orbit`; `parent_id=HID6600`; `synonyms=detached retina`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the orbit CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### choroidal detachment
**Source file:** `defs/choroidal_detachment.fm.json`  
**ID:** `OIFM_OIDM_640459`  
**Description:** Imaging observation of choroidal detachment involving the orbit or globe on head CT or related orbital imaging.  
**Synonyms:** choroidal effusion, suprachoroidal fluid  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID6700`; `name=choroidal_detachment`; `category=orbit`; `parent_id=HID6600`; `synonyms=choroidal effusion, suprachoroidal fluid`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the orbit CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

