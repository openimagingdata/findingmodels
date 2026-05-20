# Review: head CT extrinsic batch 2

10 models/mappings to review. For each, check name, description, synonyms, and direction-of-change values. Add your response below each entry.

---

### matched: flow_diverter -> flow diverter

**Source file:** `defs/flow_diverter.fm.json`  
**ID:** `OIFM_OIDM_916762`  
**Description:** Endovascular stent-like device placed across an aneurysm neck to divert blood flow and promote aneurysm thrombosis.  
**Synonyms:** Pipeline device, PED, FRED device, flow diversion device  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID8855`; `name=flow_diverter`; `category=extrinsic`; `parent_id=HID8850`; `synonyms=Pipeline device, PED, FRED device, flow diversion device`; `finding_type=observation`

**QUESTION:** Mechanical review flagged brand/acronym capitalization (`Pipeline`, `PED`, `FRED`); left as source terms.

**Response:** 

---

### matched: bypass_graft -> bypass graft

**Source file:** `defs/bypass_graft.fm.json`  
**ID:** `OIFM_OIDM_916912`  
**Description:** Surgical vascular bypass graft involving intracranial or extracranial-to-intracranial circulation.  
**Synonyms:** STA-MCA bypass, EC-IC bypass, extracranial-intracranial bypass, cerebral bypass graft  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID8860`; `name=bypass_graft`; `category=extrinsic`; `parent_id=HID8800`; `synonyms=STA-MCA bypass, EC-IC bypass, extracranial-intracranial bypass, cerebral bypass graft`; `finding_type=observation`

**QUESTION:** Mechanical review flagged bypass acronyms (`STA-MCA`, `EC-IC`); left as standard terms.

**Response:** 

---

### matched: deep_brain_stimulation_electrode -> deep brain stimulation electrode

**Source file:** `defs/deep_brain_stimulation_electrode.fm.json`  
**ID:** `OIFM_OIDM_879159`  
**Description:** Implanted electrode or lead placed in the brain for deep brain stimulation, typically connected to a neurostimulator system.  
**Synonyms:** DBS electrode, DBS lead, deep brain stimulator  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID8865`; `name=deep_brain_stimulation_electrode`; `category=extrinsic`; `parent_id=HID8800`; `synonyms=DBS electrode, DBS lead, deep brain stimulator`; `finding_type=observation`

**QUESTION:** Mechanical review flagged `DBS`; left as standard acronym.

**Response:** 

---

### matched: intracranial_pressure_monitor -> intracranial pressure monitor

**Source file:** `defs/intracranial_pressure_monitor.fm.json`  
**ID:** `OIFM_OIDM_767823`  
**Description:** Device or probe placed to monitor intracranial pressure, such as an ICP bolt or intraparenchymal pressure monitor.  
**Synonyms:** ICP monitor, ICP bolt, Camino bolt, ICP probe  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID8870`; `name=intracranial_pressure_monitor`; `category=extrinsic`; `parent_id=HID8800`; `synonyms=ICP monitor, ICP bolt, Camino bolt, ICP probe`; `finding_type=observation`

**QUESTION:** Mechanical review flagged `ICP` and `Camino`; left as standard acronym/brand term.

**Response:** 

---

### matched: ventricular_catheter -> ventricular catheter

**Source file:** `defs/ventricular_catheter.fm.json`  
**ID:** `OIFM_OIDM_222669`  
**Description:** Catheter with tip in or near the cerebral ventricular system, including ventriculostomy, external ventricular drain, or cerebrospinal fluid shunt catheter components.  
**Synonyms:** ventriculostomy catheter, EVD catheter, external ventricular drain catheter, VP shunt catheter, shunt catheter, CSF shunt catheter  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID8875`; `name=ventricular_catheter`; `category=extrinsic`; `parent_id=HID8800`; `synonyms=ventriculostomy catheter, EVD catheter, external ventricular drain catheter, VP shunt catheter, shunt catheter, CSF shunt catheter`; `finding_type=observation`

**QUESTION:** Mechanical review flagged `EVD`, `VP`, and `CSF`; left as standard acronyms.

**Response:** 

---

### matched: ventricular_access_reservoir -> ventricular access reservoir

**Source file:** `defs/ventricular_access_reservoir.fm.json`  
**ID:** `OIFM_OIDM_778592`  
**Description:** Subcutaneous reservoir connected to a ventricular catheter for cerebrospinal fluid access or intraventricular therapy.  
**Synonyms:** Ommaya reservoir, Rickham reservoir, subcutaneous CSF reservoir  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID8885`; `name=ventricular_access_reservoir`; `category=extrinsic`; `parent_id=HID8800`; `synonyms=Ommaya reservoir, Rickham reservoir, subcutaneous CSF reservoir`; `finding_type=observation`

**QUESTION:** Mechanical review flagged `Ommaya`, `Rickham`, and `CSF`; left as eponyms/acronym.

**Response:** 

---

### matched: hardware_abnormality -> hardware abnormality

**Source file:** `defs/hardware_abnormality.fm.json`  
**ID:** `OIFM_OIDM_027028`  
**Description:** Abnormality or complication involving implanted hardware, including failure, loosening, migration, displacement, or perihardware lucency.  
**Synonyms:** hardware complication, hardware-related complication  
**Change from prior:** unchanged, stable, new, resolved, worsened, improved  
**Source CSV:** `id=HID8890`; `name=hardware_abnormality`; `category=extrinsic`; `parent_id=(blank)`; `synonyms=hardware complication, hardware-related complication`; `finding_type=(blank)`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### matched: hardware_failure -> hardware failure

**Source file:** `defs/hardware_failure.fm.json`  
**ID:** `OIFM_OIDM_189489`  
**Description:** Structural failure of implanted hardware, such as fracture, breakage, or disruption of a device component.  
**Synonyms:** broken hardware, fractured hardware, hardware fracture, hardware breakage  
**Change from prior:** unchanged, stable, new, resolved, worsened, improved  
**Source CSV:** `id=HID8895`; `name=hardware_failure`; `category=extrinsic`; `parent_id=HID8890`; `synonyms=broken hardware, fractured hardware, hardware fracture, hardware breakage`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### matched: hardware_loosening -> hardware loosening

**Source file:** `defs/hardware_loosening.fm.json`  
**ID:** `OIFM_OIDM_140821`  
**Description:** Loosening of implanted hardware or prosthetic component, often suggested by motion, perihardware lucency, or loss of fixation.  
**Synonyms:** component loosening, implant loosening, prosthetic loosening  
**Change from prior:** unchanged, stable, new, resolved, worsened, improved  
**Source CSV:** `id=HID8900`; `name=hardware_loosening`; `category=extrinsic`; `parent_id=HID8890`; `synonyms=component loosening, implant loosening, prosthetic loosening`; `finding_type=diagnosis`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### matched: hardware_migration -> hardware migration

**Source file:** `defs/hardware_migration.fm.json`  
**ID:** `OIFM_OIDM_374335`  
**Description:** Change in position of implanted hardware or device component from its expected location.  
**Synonyms:** component migration, implant migration, hardware displacement, hardware backout, screw backout  
**Change from prior:** unchanged, stable, new, resolved, worsened, improved  
**Source CSV:** `id=HID8905`; `name=hardware_migration`; `category=extrinsic`; `parent_id=HID8890`; `synonyms=component migration, implant migration, hardware displacement, hardware backout, screw backout`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---
