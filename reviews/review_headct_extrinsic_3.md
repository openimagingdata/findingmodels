# Review: head CT extrinsic batch 3

10 models/mappings to review. For each, check name, description, synonyms, and direction-of-change values. Add your response below each entry.

---

### matched: perihardware_lucency -> perihardware lucency

**Source file:** `defs/perihardware_lucency.fm.json`  
**ID:** `OIFM_OIDM_328976`  
**Description:** Lucency surrounding implanted hardware, screw, plate, or prosthetic component, which may suggest loosening, infection, or chronic motion depending on context.  
**Synonyms:** lucency around hardware, peri-implant lucency, periprosthetic lucency, peri-hardware lucency  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased  
**Source CSV:** `id=HID8910`; `name=perihardware_lucency`; `category=extrinsic`; `parent_id=HID8890`; `synonyms=lucency around hardware, peri-implant lucency, periprosthetic lucency, peri-hardware lucency`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### matched: support_apparatus -> support apparatus

**Source file:** `defs/support_apparatus.fm.json`  
**ID:** `OIFM_OIDM_591054`  
**Description:** Medical support device, line, tube, catheter, drain, or related apparatus visible on imaging.  
**Synonyms:** lines and tubes  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID9000`; `name=support_apparatus`; `category=extrinsic`; `parent_id=(blank)`; `synonyms=lines and tubes`; `finding_type=(blank)`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### matched: endotracheal_tube -> endotracheal tube

**Source file:** `defs/endotracheal_tube.fm.json`  
**ID:** `OIFM_OIDM_885204`  
**Description:** Airway tube positioned in the trachea through the mouth or nose for ventilation or airway protection.  
**Synonyms:** ETT, ET tube, orotracheal tube, nasotracheal tube  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID9005`; `name=endotracheal_tube`; `category=extrinsic`; `parent_id=HID9000`; `synonyms=ETT, ET tube, orotracheal tube, nasotracheal tube`; `finding_type=observation`

**QUESTION:** Mechanical review flagged `ETT`/`ET`; left as standard abbreviations.

**Response:** 

---

### matched: nasogastric_tube -> nasogastric tube

**Source file:** `defs/nasogastric_tube.fm.json`  
**ID:** `OIFM_OIDM_008669`  
**Description:** Tube placed through the nose into the stomach or proximal gastrointestinal tract for decompression, feeding, or medication administration.  
**Synonyms:** NG tube, nasoenteric tube, Dobhoff tube, orogastric tube, OG tube  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID9010`; `name=nasogastric_tube`; `category=extrinsic`; `parent_id=HID9000`; `synonyms=NG tube, nasoenteric tube, Dobhoff tube, orogastric tube, OG tube`; `finding_type=observation`

**QUESTION:** Mechanical review flagged `NG`, `Dobhoff`, and `OG`; left as standard abbreviation/eponym terms.

**Response:** 

---

### matched: subdural_drain -> subdural drain

**Source file:** `defs/subdural_drain.fm.json`  
**ID:** `OIFM_OIDM_992500`  
**Description:** Drainage catheter or evacuating port system placed in the subdural space for evacuation of subdural fluid or blood products.  
**Synonyms:** subdural catheter, subdural evacuating port system, SEPS drain  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID9015`; `name=subdural_drain`; `category=extrinsic`; `parent_id=HID9000`; `synonyms=subdural catheter, subdural evacuating port system, SEPS drain`; `finding_type=observation`

**QUESTION:** Mechanical review flagged `SEPS`; left as standard abbreviation.

**Response:** 

---

### matched: foreign_body -> foreign body

**Source file:** `defs/foreign_body.fm.json`  
**ID:** `OIFM_OIDM_031030`  
**Description:** Foreign material or object present within the body or soft tissues, not native anatomy and not an expected implanted medical device unless specified by context.  
**Synonyms:** foreign material, foreign object  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID9200`; `name=foreign_body`; `category=extrinsic`; `parent_id=(blank)`; `synonyms=foreign material, foreign object`; `finding_type=(blank)`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### matched: intracranial_foreign_body -> intracranial foreign body

**Source file:** `defs/intracranial_foreign_body.fm.json`  
**ID:** `OIFM_OIDM_676602`  
**Description:** Foreign body located within the cranial cavity or intracranial compartment.  
**Synonyms:** intracranial FB  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID9205`; `name=intracranial_foreign_body`; `category=extrinsic`; `parent_id=HID9200`; `synonyms=intracranial FB`; `finding_type=observation`

**QUESTION:** Mechanical review flagged `FB`; left as common abbreviation from source row.

**Response:** 

---

### matched: orbital_foreign_body -> orbital foreign body

**Source file:** `defs/orbital_foreign_body.fm.json`  
**ID:** `OIFM_OIDM_192351`  
**Description:** Foreign body located within the orbit or orbital soft tissues.  
**Synonyms:** intraorbital foreign body, orbital FB  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID9250`; `name=orbital_foreign_body`; `category=extrinsic`; `parent_id=HID9200`; `synonyms=intraorbital foreign body, orbital FB`; `finding_type=observation`

**QUESTION:** Mechanical review flagged `FB`; left as common abbreviation from source row.

**Response:** 

---

### matched: intraocular_foreign_body -> intraocular foreign body

**Source file:** `defs/intraocular_foreign_body.fm.json`  
**ID:** `OIFM_OIDM_133479`  
**Description:** Foreign body located within the globe.  
**Synonyms:** IOFB  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID9255`; `name=intraocular_foreign_body`; `category=extrinsic`; `parent_id=HID9250`; `synonyms=IOFB`; `finding_type=observation`

**QUESTION:** Mechanical review flagged `IOFB`; left as standard abbreviation.

**Response:** 

---

### matched: facial_foreign_body -> facial foreign body

**Source file:** `defs/facial_foreign_body.fm.json`  
**ID:** `OIFM_OIDM_789941`  
**Description:** Foreign body located within the facial soft tissues or superficial face.  
**Synonyms:** facial soft tissue foreign body  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID9260`; `name=facial_foreign_body`; `category=extrinsic`; `parent_id=HID9200`; `synonyms=facial soft tissue foreign body`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---
