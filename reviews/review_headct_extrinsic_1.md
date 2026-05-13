# Review: head CT extrinsic batch 1

30 extrinsic CSV decisions to review. This category does not appear to have a prior batch review file: no `review_headct_extrinsic*.md` file was present.

This is a triage handoff, not a finalized model-creation batch. Entries marked **new model candidate** or **question** need reviewer direction before model creation. Existing-match entries still need reviewer confirmation before CSV writeback.

---
### new model candidate: hardware

**Source CSV:** `id=HID8800`; `name=hardware`; `category=extrinsic`; `parent_id=(blank)`; `synonyms=implanted device`; `finding_type=(blank)`

**Assessment:** No direct generic cross-modality hardware/device model found. Existing hardware models are modality- or body-region-specific.

**Response:**

---
### new model candidate: vascular_clip

**Source CSV:** `id=HID8805`; `name=vascular_clip`; `category=extrinsic`; `parent_id=HID8800`; `synonyms=aneurysm clip, surgical clips intracranial, cerebrovascular clips`; `finding_type=observation`

**Assessment:** No direct intracranial/cerebrovascular clip model found. Existing clip models are region-specific outside the head/brain.

**Response:**

---
### new model candidate: aneurysm_coil

**Source CSV:** `id=HID8810`; `name=aneurysm_coil`; `category=extrinsic`; `parent_id=HID8800`; `synonyms=endovascular coil, embolization coil`; `finding_type=observation`

**Assessment:** No direct aneurysm coil or embolization coil model found.

**Response:**

---
### new model candidate: intrasaccular_flow_disruptor

**Source CSV:** `id=HID8815`; `name=intrasaccular_flow_disruptor`; `category=extrinsic`; `parent_id=HID8800`; `synonyms=WEB device, WEB embolization device, Woven EndoBridge, Contour Neurovascular System, intrasaccular flow disruptor`; `finding_type=observation`

**Assessment:** No direct model found. Reviewer should confirm whether brand/product names such as `WEB device`, `Woven EndoBridge`, and `Contour Neurovascular System` should be included as synonyms.

**Response:**

---
### new model candidate: brachytherapy_seed

**Source CSV:** `id=HID8820`; `name=brachytherapy_seed`; `category=extrinsic`; `parent_id=HID8800`; `synonyms=brachytherapy seeds, radioactive seed, radioactive seeds, I-125 seed, Cs-131 seed, GammaTile, permanent brachytherapy implant`; `finding_type=observation`

**Assessment:** No direct model found. Reviewer should confirm whether isotope/product terms and `GammaTile` should be included as synonyms.

**Response:**

---
### new model candidate: plate

**Source CSV:** `id=HID8825`; `name=plate`; `category=extrinsic`; `parent_id=HID8800`; `synonyms=bone plate, surgical plate, miniplate, osteosynthesis plate, plate and screw construct`; `finding_type=observation`

**Assessment:** No direct generic plate hardware model found.

**Response:**

---
### new model candidate: screw

**Source CSV:** `id=HID8830`; `name=screw`; `category=extrinsic`; `parent_id=HID8800`; `synonyms=bone screw, cortical screw, surgical screw, fixation screw`; `finding_type=observation`

**Assessment:** No direct generic screw hardware model found.

**Response:**

---
### new model candidate: mesh

**Source CSV:** `id=HID8835`; `name=mesh`; `category=extrinsic`; `parent_id=HID8800`; `synonyms=surgical mesh, titanium mesh, cranial mesh, cranioplasty mesh, mesh plate`; `finding_type=observation`

**Assessment:** No direct cranial/surgical mesh model found.

**Response:**

---
### matched/question: spinal_fusion_hardware -> spinal fixation hardware

**Source file:** `defs/spinal_fixation_hardware.fm.json`  
**ID:** `OIFM_OIDM_055031`  
**Description:** Orthopedic hardware securing the spine, visible as rods, screws, and plates on radiograph.  
**Synonyms:** spinal instrumentation, spinal fixation  
**Change from prior:** unchanged, stable, new, resolved

**Source CSV:** `id=HID8840`; `name=spinal_fusion_hardware`; `category=extrinsic`; `parent_id=HID8800`; `synonyms=pedicle screws, pedicle screws and rods, spinal instrumentation, spinal construct, cervical fixation rods, occipital plate`; `finding_type=observation`

**Assessment:** Existing `spinal fixation hardware` matches the general concept through `spinal instrumentation`, but its description is radiograph-scoped and CSV includes specific component/site phrases. Confirm mapping and which CSV synonyms are acceptable.

**Response:**

---
### question: intracranial_stent

**Candidate files:** `defs/vascular_stent.fm.json`, `defs/arterial_stent.fm.json`  
**Candidate IDs:** `OIFM_OIDM_053884`, `OIFM_MGB_512163`

**Source CSV:** `id=HID8850`; `name=intracranial_stent`; `category=extrinsic`; `parent_id=HID8800`; `synonyms=intracranial vascular stent`; `finding_type=observation`

**Question:** Existing stent models are broader body-wide vascular/arterial stents. Should intracranial stent map to a broader stent model with anatomic site post-coordinated, or should a dedicated `intracranial stent` model be created?

**Response:**

---
### new model candidate: flow_diverter

**Source CSV:** `id=HID8855`; `name=flow_diverter`; `category=extrinsic`; `parent_id=HID8850`; `synonyms=Pipeline device, PED, FRED device, flow diversion device`; `finding_type=observation`

**Assessment:** No direct flow-diverter model found. Reviewer should confirm whether brand/device acronyms should be included as synonyms.

**Response:**

---
### new model candidate: bypass_graft

**Source CSV:** `id=HID8860`; `name=bypass_graft`; `category=extrinsic`; `parent_id=HID8800`; `synonyms=STA-MCA bypass, EC-IC bypass, extracranial-intracranial bypass, cerebral bypass graft`; `finding_type=observation`

**Assessment:** No direct cerebral bypass graft model found. Existing systemic/cardiac shunt models are not equivalent.

**Response:**

---
### new model candidate: deep_brain_stimulation_electrode

**Source CSV:** `id=HID8865`; `name=deep_brain_stimulation_electrode`; `category=extrinsic`; `parent_id=HID8800`; `synonyms=DBS electrode, DBS lead, deep brain stimulator`; `finding_type=observation`

**Assessment:** No direct model found.

**Response:**

---
### new model candidate: intracranial_pressure_monitor

**Source CSV:** `id=HID8870`; `name=intracranial_pressure_monitor`; `category=extrinsic`; `parent_id=HID8800`; `synonyms=ICP monitor, ICP bolt, Camino bolt, ICP probe`; `finding_type=observation`

**Assessment:** No direct model found. Reviewer should confirm `Camino bolt` as acceptable device-name synonym.

**Response:**

---
### question: ventricular_catheter

**Candidate file:** `defs/ventriculoperitoneal_shunt.fm.json`  
**Candidate ID:** `OIFM_OIDM_193529`  
**Candidate description:** Shunt catheter draining cerebrospinal fluid from a cerebral ventricle, with tubing visible on chest radiograph.  
**Candidate synonyms:** VP shunt, ventricular shunt

**Source CSV:** `id=HID8875`; `name=ventricular_catheter`; `category=extrinsic`; `parent_id=HID8800`; `synonyms=ventriculostomy catheter, EVD catheter, external ventricular drain catheter, VP shunt catheter, shunt catheter, CSF shunt catheter`; `finding_type=observation`

**Question:** Existing VP shunt model is a specific permanent shunt and does not cover EVD/ventriculostomy catheters. Create a broader `ventricular catheter` model, or map VP-shunt phrases separately?

**Response:**

---
### new model candidate: ventricular_access_reservoir

**Source CSV:** `id=HID8885`; `name=ventricular_access_reservoir`; `category=extrinsic`; `parent_id=HID8800`; `synonyms=Ommaya reservoir, Rickham reservoir, subcutaneous CSF reservoir`; `finding_type=observation`

**Assessment:** No direct model found.

**Response:**

---
### new model candidate: hardware_abnormality

**Source CSV:** `id=HID8890`; `name=hardware_abnormality`; `category=extrinsic`; `parent_id=(blank)`; `synonyms=hardware complication, hardware-related complication`; `finding_type=(blank)`

**Assessment:** No direct broad hardware-abnormality model found.

**Response:**

---
### new model candidate: hardware_failure

**Source CSV:** `id=HID8895`; `name=hardware_failure`; `category=extrinsic`; `parent_id=HID8890`; `synonyms=broken hardware, fractured hardware, hardware fracture, hardware breakage`; `finding_type=observation`

**Assessment:** No direct model found.

**Response:**

---
### new model candidate: hardware_loosening

**Source CSV:** `id=HID8900`; `name=hardware_loosening`; `category=extrinsic`; `parent_id=HID8890`; `synonyms=component loosening, implant loosening, prosthetic loosening`; `finding_type=diagnosis`

**Assessment:** No direct generic hardware-loosening model found.

**Response:**

---
### new model candidate: hardware_migration

**Source CSV:** `id=HID8905`; `name=hardware_migration`; `category=extrinsic`; `parent_id=HID8890`; `synonyms=component migration, implant migration, hardware displacement, hardware backout, screw backout`; `finding_type=observation`

**Assessment:** No direct model found.

**Response:**

---
### new model candidate: perihardware_lucency

**Source CSV:** `id=HID8910`; `name=perihardware_lucency`; `category=extrinsic`; `parent_id=HID8890`; `synonyms=lucency around hardware, peri-implant lucency, periprosthetic lucency, peri-hardware lucency`; `finding_type=observation`

**Assessment:** No direct generic perihardware-lucency model found. Existing periprosthetic lucency models are joint-specific.

**Response:**

---
### question: support_apparatus

**Candidate file:** `defs/chest_radiograph_lines_and_tubes.fm.json`  
**Candidate ID:** `OIFM_CDE_000237`  
**Candidate description:** Chest Radiograph Lines and Tubes

**Source CSV:** `id=HID9000`; `name=support_apparatus`; `category=extrinsic`; `parent_id=(blank)`; `synonyms=lines and tubes`; `finding_type=(blank)`

**Question:** Existing candidate is chest-radiograph-specific and legacy. Create a general `support apparatus` or `lines and tubes` parent model for head CT?

**Response:**

---
### question: endotracheal_tube

**Candidate file:** `defs/endotracheal_tube_placement.fm.json`  
**Candidate ID:** `OIFM_CDE_000179`  
**Candidate description:** Placement of endotracheal (ET) tube

**Source CSV:** `id=HID9005`; `name=endotracheal_tube`; `category=extrinsic`; `parent_id=HID9000`; `synonyms=ETT, ET tube, orotracheal tube, nasotracheal tube`; `finding_type=observation`

**Question:** Existing CDE model is placement-focused and legacy. Should this map to it, or should a simpler `endotracheal tube` device model be created?

**Response:**

---
### question: nasogastric_tube

**Candidate files:** `defs/enteric_tube.fm.json`, `defs/feeding_tube.fm.json`  
**Candidate IDs:** `OIFM_OIDM_590312`, `OIFM_OIDM_185348`

**Source CSV:** `id=HID9010`; `name=nasogastric_tube`; `category=extrinsic`; `parent_id=HID9000`; `synonyms=NG tube, nasoenteric tube, Dobhoff tube, orogastric tube, OG tube`; `finding_type=observation`

**Question:** Existing `enteric tube` is broader and `feeding tube` is narrower; CSV mixes NG/OG/nasoenteric/Dobhoff. Should this map to `enteric tube`, or should a specific `nasogastric tube` model be created with narrower synonyms?

**Response:**

---
### new model candidate: subdural_drain

**Source CSV:** `id=HID9015`; `name=subdural_drain`; `category=extrinsic`; `parent_id=HID9000`; `synonyms=subdural catheter, subdural evacuating port system, SEPS drain`; `finding_type=observation`

**Assessment:** No direct model found.

**Response:**

---
### new model candidate: foreign_body

**Source CSV:** `id=HID9200`; `name=foreign_body`; `category=extrinsic`; `parent_id=(blank)`; `synonyms=foreign material, foreign object`; `finding_type=(blank)`

**Assessment:** No direct generic foreign-body model found. Existing models are metallic or retained-surgical foreign bodies, which are narrower.

**Response:**

---
### new model candidate: intracranial_foreign_body

**Source CSV:** `id=HID9205`; `name=intracranial_foreign_body`; `category=extrinsic`; `parent_id=HID9200`; `synonyms=intracranial FB`; `finding_type=observation`

**Assessment:** No direct intracranial foreign body model found.

**Response:**

---
### new model candidate: orbital_foreign_body

**Source CSV:** `id=HID9250`; `name=orbital_foreign_body`; `category=extrinsic`; `parent_id=HID9200`; `synonyms=intraorbital foreign body, orbital FB`; `finding_type=observation`

**Assessment:** No direct orbital foreign body model found.

**Response:**

---
### new model candidate: intraocular_foreign_body

**Source CSV:** `id=HID9255`; `name=intraocular_foreign_body`; `category=extrinsic`; `parent_id=HID9250`; `synonyms=IOFB`; `finding_type=observation`

**Assessment:** No direct intraocular foreign body model found.

**Response:**

---
### new model candidate: facial_foreign_body

**Source CSV:** `id=HID9260`; `name=facial_foreign_body`; `category=extrinsic`; `parent_id=HID9200`; `synonyms=facial soft tissue foreign body`; `finding_type=observation`

**Assessment:** No direct facial foreign body model found.

**Response:**

---
