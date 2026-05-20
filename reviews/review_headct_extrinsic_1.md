# Review: head CT extrinsic batch 1

10 models/mappings to review. For each, check name, description, synonyms, and direction-of-change values. Add your response below each entry.

---

### matched: hardware -> implanted hardware

**Source file:** `defs/implanted_hardware.fm.json`  
**ID:** `OIFM_OIDM_133218`  
**Description:** Implanted medical device or surgical hardware visible on imaging, including clips, coils, stents, plates, screws, mesh, electrodes, catheters, or other radiopaque devices.  
**Synonyms:** hardware, implanted device  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID8800`; `name=hardware`; `category=extrinsic`; `parent_id=(blank)`; `synonyms=implanted device`; `finding_type=(blank)`

**QUESTION:** CSV row `hardware` mapped to scoped canonical name `implanted hardware`; confirm acceptable.

**Response:** 

---

### matched: vascular_clip -> vascular clip

**Source file:** `defs/vascular_clip.fm.json`  
**ID:** `OIFM_OIDM_510602`  
**Description:** Surgical clip applied to an intracranial or cervical vessel, aneurysm neck, or vascular structure, visible as metallic hardware on imaging.  
**Synonyms:** aneurysm clip, surgical clips intracranial, cerebrovascular clips  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID8805`; `name=vascular_clip`; `category=extrinsic`; `parent_id=HID8800`; `synonyms=aneurysm clip, surgical clips intracranial, cerebrovascular clips`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### matched: aneurysm_coil -> aneurysm coil

**Source file:** `defs/aneurysm_coil.fm.json`  
**ID:** `OIFM_OIDM_974314`  
**Description:** Endovascular coil mass placed within an aneurysm sac or vascular lesion for embolization, visible as metallic coil material on imaging.  
**Synonyms:** endovascular coil, embolization coil  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID8810`; `name=aneurysm_coil`; `category=extrinsic`; `parent_id=HID8800`; `synonyms=endovascular coil, embolization coil`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### matched: intrasaccular_flow_disruptor -> intrasaccular flow disruptor

**Source file:** `defs/intrasaccular_flow_disruptor.fm.json`  
**ID:** `OIFM_OIDM_240838`  
**Description:** Endovascular device placed within an aneurysm sac to disrupt inflow and promote thrombosis, such as a WEB or other intrasaccular embolization device.  
**Synonyms:** WEB device, WEB embolization device, Woven EndoBridge, Contour Neurovascular System  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID8815`; `name=intrasaccular_flow_disruptor`; `category=extrinsic`; `parent_id=HID8800`; `synonyms=WEB device, WEB embolization device, Woven EndoBridge, Contour Neurovascular System, intrasaccular flow disruptor`; `finding_type=observation`

**QUESTION:** Mechanical review flagged brand/device capitalization (`WEB`, `Woven EndoBridge`, `Contour Neurovascular System`); left as source terms.

**Response:** 

---

### matched: brachytherapy_seed -> brachytherapy seed

**Source file:** `defs/brachytherapy_seed.fm.json`  
**ID:** `OIFM_OIDM_090347`  
**Description:** Small implanted radioactive seed or tile used for local brachytherapy, visible as radiopaque material in or near a treatment bed.  
**Synonyms:** brachytherapy seeds, radioactive seed, radioactive seeds, I-125 seed, Cs-131 seed, GammaTile, permanent brachytherapy implant  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID8820`; `name=brachytherapy_seed`; `category=extrinsic`; `parent_id=HID8800`; `synonyms=brachytherapy seeds, radioactive seed, radioactive seeds, I-125 seed, Cs-131 seed, GammaTile, permanent brachytherapy implant`; `finding_type=observation`

**QUESTION:** Mechanical review flagged isotope/brand capitalization (`I-125`, `Cs-131`, `GammaTile`); left as source terms.

**Response:** 

---

### matched: plate -> surgical plate

**Source file:** `defs/surgical_plate.fm.json`  
**ID:** `OIFM_OIDM_625941`  
**Description:** Implanted fixation plate used for osseous reconstruction, cranioplasty, fracture fixation, or other surgical stabilization.  
**Synonyms:** plate, bone plate, miniplate, osteosynthesis plate, plate and screw construct  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID8825`; `name=plate`; `category=extrinsic`; `parent_id=HID8800`; `synonyms=bone plate, surgical plate, miniplate, osteosynthesis plate, plate and screw construct`; `finding_type=observation`

**QUESTION:** CSV row `plate` mapped to scoped canonical name `surgical plate`; mechanical review removed `surgical plate` as a self-synonym.

**Response:** 

---

### matched: screw -> surgical screw

**Source file:** `defs/surgical_screw.fm.json`  
**ID:** `OIFM_OIDM_698710`  
**Description:** Implanted screw used for osseous fixation, hardware anchoring, or surgical stabilization.  
**Synonyms:** screw, bone screw, cortical screw, fixation screw  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID8830`; `name=screw`; `category=extrinsic`; `parent_id=HID8800`; `synonyms=bone screw, cortical screw, surgical screw, fixation screw`; `finding_type=observation`

**QUESTION:** CSV row `screw` mapped to scoped canonical name `surgical screw`; mechanical review removed `surgical screw` as a self-synonym.

**Response:** 

---

### matched: mesh -> surgical mesh

**Source file:** `defs/surgical_mesh.fm.json`  
**ID:** `OIFM_OIDM_044172`  
**Description:** Implanted mesh material used for reconstruction, fixation, or repair, including cranial mesh or cranioplasty mesh.  
**Synonyms:** mesh, titanium mesh, cranial mesh, cranioplasty mesh, mesh plate  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID8835`; `name=mesh`; `category=extrinsic`; `parent_id=HID8800`; `synonyms=surgical mesh, titanium mesh, cranial mesh, cranioplasty mesh, mesh plate`; `finding_type=observation`

**QUESTION:** CSV row `mesh` mapped to scoped canonical name `surgical mesh`; mechanical review removed `surgical mesh` as a self-synonym.

**Response:** 

---

### matched: spinal_fusion_hardware -> spinal fixation hardware

**Source file:** `defs/spinal_fixation_hardware.fm.json`  
**ID:** `OIFM_OIDM_055031`  
**Description:** Orthopedic hardware securing or fusing the spine, visible as rods, screws, plates, or other spinal instrumentation on imaging.  
**Synonyms:** spinal instrumentation, spinal fixation, spinal fusion hardware, pedicle screws, pedicle screws and rods, spinal construct, cervical fixation rods, occipital plate  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID8840`; `name=spinal_fusion_hardware`; `category=extrinsic`; `parent_id=HID8800`; `synonyms=pedicle screws, pedicle screws and rods, spinal instrumentation, spinal construct, cervical fixation rods, occipital plate`; `finding_type=observation`

**QUESTION:** Mapped to existing `spinal fixation hardware`; description was broadened from radiograph-only wording and CSV synonyms were added.

**Response:** 

---

### matched: intracranial_stent -> intracranial stent

**Source file:** `defs/intracranial_stent.fm.json`  
**ID:** `OIFM_OIDM_614672`  
**Description:** Endovascular stent located within an intracranial artery or venous sinus, visible as vascular hardware on CT or angiographic imaging.  
**Synonyms:** intracranial vascular stent  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID8850`; `name=intracranial_stent`; `category=extrinsic`; `parent_id=HID8800`; `synonyms=intracranial vascular stent`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---
