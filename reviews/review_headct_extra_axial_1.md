# Review: head CT extra axial batch 1

9 models/mappings to review. For each, check name, description, synonyms, and direction-of-change values. Add your response below each entry.

---

### extra-axial abnormality

**Source file:** `defs/extra_axial_abnormality.fm.json`  
**ID:** `OIFM_OIDM_033418`  
**Description:** A nonspecific abnormality located outside the brain parenchyma but within the cranial cavity, involving the meninges, subarachnoid space, subdural space, epidural space, cisterns, or other extra-axial compartments.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID2600`; `name=extra_axial_abnormality`; `category=extra_axial`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`

**Assessment:** New parent model for extra-axial rows; confirm acceptable.

**Response:** 

---

### extra-axial collection

**Source file:** `defs/extra_axial_collection.fm.json`  
**ID:** `OIFM_OIDM_004178`  
**Description:** A fluid, blood, air, or mixed-density collection located outside the brain parenchyma within an extra-axial intracranial compartment.  
**Synonyms:** extra-axial fluid, extra-axial fluid collection  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller  
**Source CSV:** `id=HID2650`; `name=extra_axial_collection`; `category=extra_axial`; `parent_id=HID2600`; `synonyms=extra-axial fluid, extra-axial fluid collection`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### subdural collection

**Source file:** `defs/subdural_collection.fm.json`  
**ID:** `OIFM_OIDM_441121`  
**Description:** A collection located in the subdural space between the dura and arachnoid membranes, which may contain cerebrospinal fluid, blood products, pus, or mixed material depending on context.  
**Synonyms:** subdural fluid collection, subdural fluid, subdural fluid accumulation  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller  
**Source CSV:** `id=HID2653`; `name=subdural_collection`; `category=extra_axial`; `parent_id=HID2650`; `synonyms=subdural fluid collection, subdural fluid, subdural fluid accumulation`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### subdural hygroma

**Source file:** `defs/subdural_hygroma.fm.json`  
**ID:** `OIFM_OIDM_547091`  
**Description:** A low-attenuation cerebrospinal-fluid-like collection in the subdural space, typically related to trauma, surgery, or altered cerebrospinal fluid dynamics.  
**Synonyms:** subdural CSF collection, low-attenuation subdural fluid, low-density subdural fluid, low-attenuation subdural collection, CSF-density subdural collection  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller  
**Source CSV:** `id=HID2655`; `name=subdural_hygroma`; `category=extra_axial`; `parent_id=HID2653`; `synonyms=subdural CSF collection, low-attenuation subdural fluid, low-density subdural fluid, low-attenuation subdural collection, CSF-density subdural collection`; `finding_type=observation`

**QUESTION:** Mechanical review flagged capitalized `CSF`; I left it capitalized as a standard acronym. Confirm acceptable.

**Response:** 

---

### extra-axial cerebrospinal fluid collection

**Source file:** `defs/extra_axial_cerebrospinal_fluid_collection.fm.json`  
**ID:** `OIFM_OIDM_405424`  
**Description:** A cerebrospinal-fluid attenuation or signal collection located outside the brain parenchyma in an extra-axial compartment.  
**Synonyms:** extra-axial CSF collection  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller  
**Source CSV:** `id=HID2660`; `name=extra_axial_csf_collection`; `category=extra_axial`; `parent_id=HID2650`; `synonyms=(blank)`; `finding_type=observation`

**QUESTION:** Canonical name expands `CSF` to cerebrospinal fluid; synonym preserves the acronym. Confirm acceptable.

**Response:** 

---

### prominent extra-axial spaces

**Source file:** `defs/prominent_extra_axial_spaces.fm.json`  
**ID:** `OIFM_OIDM_053904`  
**Description:** Prominence or enlargement of the extra-axial cerebrospinal fluid spaces, including the subarachnoid spaces over the cerebral convexities or within the cisterns.  
**Synonyms:** enlarged subarachnoid spaces  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased  
**Source CSV:** `id=HID2665`; `name=prominent_extra_axial_spaces`; `category=extra_axial`; `parent_id=HID2650`; `synonyms=enlarged subarachnoid spaces`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### extra-axial cyst

**Source file:** `defs/extra_axial_cyst.fm.json`  
**ID:** `OIFM_OIDM_607585`  
**Description:** A cystic lesion located outside the brain parenchyma within an extra-axial intracranial compartment.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller  
**Source CSV:** `id=HID2700`; `name=extra_axial_cyst`; `category=extra_axial`; `parent_id=HID2600`; `synonyms=(blank)`; `finding_type=(blank)`

**Assessment:** New grouping model for extra-axial cystic lesions; confirm acceptable.

**Response:** 

---

### arachnoid cyst

**Source file:** `defs/arachnoid_cyst.fm.json`  
**ID:** `OIFM_OIDM_706918`  
**Description:** A benign cerebrospinal-fluid-filled extra-axial cyst lined by arachnoid membrane, commonly located in the middle cranial fossa, posterior fossa, or other subarachnoid spaces.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller  
**Source CSV:** `id=HID2705`; `name=arachnoid_cyst`; `category=extra_axial`; `parent_id=HID2700`; `synonyms=(blank)`; `finding_type=diagnosis`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### matched: epidermoid_cyst -> intracranial epidermoid cyst

**Source file:** `defs/intracranial_epidermoid_cyst.fm.json`  
**ID:** `OIFM_OIDM_224166`  
**Description:** Congenital extra-axial inclusion cyst lined by stratified squamous epithelium and filled with desquamated keratin debris, most often arising in the cerebellopontine angle or parasellar cisterns. On CT it typically appears as a well-defined, lobulated, nonenhancing extra-axial mass that follows cerebrospinal fluid attenuation and insinuates around adjacent vessels and nerves.  
**Synonyms:** intracranial epidermoid, intracranial epidermoid tumor, epidermoid, epidermoid tumor, intracranial pearly tumor  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, increased, decreased  
**Source CSV:** `id=HID2710`; `name=epidermoid_cyst`; `category=extra_axial`; `parent_id=HID2700`; `synonyms=epidermoid, epidermoid tumor`; `finding_type=diagnosis`

**QUESTION:** Existing intracranial epidermoid cyst reused; CSV shorter synonyms were added. Confirm mapping rather than creating generic epidermoid cyst.

**Response:** 

---
