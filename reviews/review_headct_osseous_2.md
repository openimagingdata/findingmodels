# Review: head CT osseous batch 2

10 models/mappings to review. For each, check name, description, synonyms, and direction-of-change values. Add your response below each entry.

---

### orbital fracture

**Source file:** `defs/orbital_fracture.fm.json`  
**ID:** `OIFM_OIDM_525994`  
**Description:** Fracture involving one or more osseous walls of the orbit.  
**Synonyms:** orbital wall fracture  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5250`; `name=orbital_fracture`; `category=osseous`; `parent_id=HID5200`; `synonyms=orbital wall fracture`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### matched: orbital_blowout_fracture -> orbital blowout fracture

**Source file:** `defs/orbital_blowout_fracture.fm.json`  
**ID:** `OIFM_OIDM_070294`  
**Description:** Fracture of the orbital floor or medial wall resulting from blunt trauma that transmits pressure through the globe, typically with herniation of orbital fat or muscle into the adjacent paranasal sinus and associated sinus opacification from hemorrhage.  
**Synonyms:** blowout fracture, orbital floor fracture, orbital floor blowout  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5255`; `name=orbital_blowout_fracture`; `category=osseous`; `parent_id=HID5250`; `synonyms=blowout fracture, orbital floor fracture, orbital floor blowout`; `finding_type=observation`

**QUESTION:** Existing model reused; CSV orbital floor synonyms were added.

**Response:** 

---

### medial orbital wall fracture

**Source file:** `defs/medial_orbital_wall_fracture.fm.json`  
**ID:** `OIFM_OIDM_444719`  
**Description:** Fracture involving the medial orbital wall, most commonly the lamina papyracea.  
**Synonyms:** lamina papyracea fracture  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5260`; `name=medial_orbital_wall_fracture`; `category=osseous`; `parent_id=HID5250`; `synonyms=lamina papyracea fracture`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### nasal fracture

**Source file:** `defs/nasal_fracture.fm.json`  
**ID:** `OIFM_OIDM_231181`  
**Description:** Fracture involving the nasal bone or nasal bones.  
**Synonyms:** nasal bone fracture  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5265`; `name=nasal_fracture`; `category=osseous`; `parent_id=HID5200`; `synonyms=nasal bone fracture`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### zygomatic fracture

**Source file:** `defs/zygomatic_fracture.fm.json`  
**ID:** `OIFM_OIDM_268881`  
**Description:** Fracture involving the zygoma or zygomatic arch.  
**Synonyms:** zygomatic arch fracture, malar fracture  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5270`; `name=zygomatic_fracture`; `category=osseous`; `parent_id=HID5200`; `synonyms=zygomatic arch fracture, malar fracture`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### zygomaticomaxillary complex fracture

**Source file:** `defs/zygomaticomaxillary_complex_fracture.fm.json`  
**ID:** `OIFM_OIDM_159654`  
**Description:** Fracture pattern involving the zygomaticomaxillary complex, typically affecting the zygomatic arch, orbital rim or wall, and maxillary buttress attachments.  
**Synonyms:** ZMC fracture, tripod fracture, trimalar fracture  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5275`; `name=zygomaticomaxillary_complex_fracture`; `category=osseous`; `parent_id=HID5200`; `synonyms=ZMC fracture, tripod fracture, trimalar fracture`; `finding_type=observation`

**Assessment:** Mechanical review flagged `ZMC`; left capitalized as standard acronym.

**Response:** 

---

### maxillary fracture

**Source file:** `defs/maxillary_fracture.fm.json`  
**ID:** `OIFM_OIDM_528245`  
**Description:** Fracture involving the maxilla or maxillary sinus walls.  
**Synonyms:** maxillary wall fracture  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5280`; `name=maxillary_fracture`; `category=osseous`; `parent_id=HID5200`; `synonyms=maxillary wall fracture`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### le fort fracture

**Source file:** `defs/le_fort_fracture.fm.json`  
**ID:** `OIFM_OIDM_705267`  
**Description:** Midface fracture pattern involving the maxilla and facial buttresses, classically categorized as Le Fort I, II, or III depending on the fracture trajectory.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5285`; `name=le_fort_fracture`; `category=osseous`; `parent_id=HID5200`; `synonyms=Le Fort fracture`; `finding_type=observation`

**QUESTION:** Mechanical review removed canonical self-synonym `Le Fort fracture`; confirm no additional synonym is needed.

**Response:** 

---

### naso-orbito-ethmoid fracture

**Source file:** `defs/naso_orbito_ethmoid_fracture.fm.json`  
**ID:** `OIFM_OIDM_919194`  
**Description:** Fracture complex involving the nasal bones, medial orbital walls, and ethmoid region, often affecting the central midface and medial canthal attachments.  
**Synonyms:** NOE fracture  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5290`; `name=naso_orbito_ethmoid_fracture`; `category=osseous`; `parent_id=HID5200`; `synonyms=NOE fracture`; `finding_type=observation`

**Assessment:** Mechanical review flagged `NOE`; left capitalized as standard acronym.

**Response:** 

---

### temporal bone fracture

**Source file:** `defs/temporal_bone_fracture.fm.json`  
**ID:** `OIFM_OIDM_497032`  
**Description:** Fracture involving the temporal bone, including squamous, mastoid, petrous, or skull base portions.  
**Synonyms:** petrous bone fracture, petrous temporal fracture  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID5300`; `name=temporal_bone_fracture`; `category=osseous`; `parent_id=HID5050`; `synonyms=petrous bone fracture, petrous temporal fracture`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---
