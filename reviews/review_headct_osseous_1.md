# Review: head CT osseous batch 1

10 models/mappings to review. For each, check name, description, synonyms, and direction-of-change values. Add your response below each entry.

---

### matched: osseous_abnormality -> osseous abnormality

**Source file:** `defs/osseous_abnormality.fm.json`  
**ID:** `OIFM_OIDM_164927`  
**Description:** Nonspecific abnormality of bone identified on imaging.  
**Synonyms:** skeletal abnormality, bony abnormality  
**Change from prior:** unchanged, stable, new, resolved, worsened, improved  
**Source CSV:** `id=HID5000`; `name=osseous_abnormality`; `category=osseous`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`

**QUESTION:** Existing model reused; description was broadened from radiograph-only wording to imaging-neutral wording.

**Response:** 

---

### matched: fracture -> fracture

**Source file:** `defs/fracture.fm.json`  
**ID:** `OIFM_OIDM_739317`  
**Description:** Disruption of cortical bone continuity identified on imaging.  
**Synonyms:** bone fracture, cranial fracture  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller  
**Source CSV:** `id=HID5050`; `name=fracture`; `category=osseous`; `parent_id=HID5000`; `synonyms=cranial fracture`; `finding_type=observation`

**QUESTION:** Existing model reused; description was broadened from radiograph-only wording and CSV synonym `cranial fracture` was added.

**Response:** 

---

### calvarial fracture

**Source file:** `defs/calvarial_fracture.fm.json`  
**ID:** `OIFM_OIDM_922215`  
**Description:** Fracture involving the calvarium or skull vault, seen as a linear, comminuted, or displaced discontinuity of the cranial vault cortex on imaging.  
**Synonyms:** calvarial discontinuity  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5100`; `name=calvarial_fracture`; `category=osseous`; `parent_id=HID5050`; `synonyms=calvarial discontinuity`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### depressed fracture

**Source file:** `defs/depressed_fracture.fm.json`  
**ID:** `OIFM_OIDM_311358`  
**Description:** Calvarial fracture with inward displacement of one or more fracture fragments below the expected contour of the skull vault.  
**Synonyms:** depressed skull fracture, depressed calvarial fracture  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5105`; `name=depressed_fracture`; `category=osseous`; `parent_id=HID5100`; `synonyms=depressed skull fracture, depressed calvarial fracture`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### skull base fracture

**Source file:** `defs/skull_base_fracture.fm.json`  
**ID:** `OIFM_OIDM_085957`  
**Description:** Fracture involving the skull base, including the anterior, middle, or posterior cranial fossa floor or adjacent skull base foramina and canals.  
**Synonyms:** basilar skull fracture  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5150`; `name=skull_base_fracture`; `category=osseous`; `parent_id=HID5050`; `synonyms=basilar skull fracture`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### cribriform plate fracture

**Source file:** `defs/cribriform_plate_fracture.fm.json`  
**ID:** `OIFM_OIDM_587234`  
**Description:** Fracture involving the cribriform plate of the ethmoid bone, which may be associated with anterior skull base trauma or cerebrospinal fluid leak.  
**Synonyms:** cribriform fracture  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5155`; `name=cribriform_plate_fracture`; `category=osseous`; `parent_id=HID5150`; `synonyms=cribriform fracture`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### clivus fracture

**Source file:** `defs/clivus_fracture.fm.json`  
**ID:** `OIFM_OIDM_746790`  
**Description:** Fracture involving the clivus of the central skull base.  
**Synonyms:** clival fracture  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5160`; `name=clivus_fracture`; `category=osseous`; `parent_id=HID5150`; `synonyms=clival fracture`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### orbital roof fracture

**Source file:** `defs/orbital_roof_fracture.fm.json`  
**ID:** `OIFM_OIDM_431537`  
**Description:** Fracture involving the superior wall of the orbit, which also forms part of the anterior cranial fossa floor.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5165`; `name=orbital_roof_fracture`; `category=osseous`; `parent_id=HID5150`; `synonyms=(blank)`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### optic canal fracture

**Source file:** `defs/optic_canal_fracture.fm.json`  
**ID:** `OIFM_OIDM_150705`  
**Description:** Fracture involving the optic canal, with potential risk to the optic nerve or ophthalmic artery depending on displacement and associated injury.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5170`; `name=optic_canal_fracture`; `category=osseous`; `parent_id=HID5150`; `synonyms=(blank)`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### facial bone fracture

**Source file:** `defs/facial_bone_fracture.fm.json`  
**ID:** `OIFM_OIDM_124733`  
**Description:** Fracture involving one or more facial bones, including the orbit, nasal bones, zygoma, maxilla, or other midface structures.  
**Synonyms:** midface fracture  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5200`; `name=facial_bone_fracture`; `category=osseous`; `parent_id=HID5050`; `synonyms=midface fracture`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---
