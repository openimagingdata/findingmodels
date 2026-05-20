# Review: head CT extra axial batch 4

9 models/mappings to review. For each, check name, description, synonyms, and direction-of-change values. Add your response below each entry.

---

### acute subdural hemorrhage

**Source file:** `defs/acute_subdural_hemorrhage.fm.json`  
**ID:** `OIFM_OIDM_368223`  
**Description:** Acute blood products in the subdural space, typically hyperattenuating on noncontrast CT and often crescentic along the cerebral convexity, falx, or tentorium.  
**Synonyms:** acute SDH, acute subdural hematoma  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller, worsened, improved  
**Source CSV:** `id=HID2955`; `name=acute_subdural_hemorrhage`; `category=extra_axial`; `parent_id=HID2950`; `synonyms=acute SDH, acute subdural hematoma`; `finding_type=diagnosis`

**QUESTION:** Mechanical review flagged `SDH`; I left it capitalized as a standard acronym. Confirm acceptable.

**Response:** 

---

### subacute subdural hemorrhage

**Source file:** `defs/subacute_subdural_hemorrhage.fm.json`  
**ID:** `OIFM_OIDM_362894`  
**Description:** Subacute blood products in the subdural space, typically evolving toward isoattenuation relative to brain parenchyma on CT depending on age of hemorrhage.  
**Synonyms:** subacute SDH, subacute subdural hematoma  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller, worsened, improved  
**Source CSV:** `id=HID2960`; `name=subacute_subdural_hemorrhage`; `category=extra_axial`; `parent_id=HID2950`; `synonyms=subacute SDH, subacute subdural hematoma`; `finding_type=diagnosis`

**QUESTION:** Mechanical review flagged `SDH`; I left it capitalized as a standard acronym. Confirm acceptable.

**Response:** 

---

### chronic subdural hemorrhage

**Source file:** `defs/chronic_subdural_hemorrhage.fm.json`  
**ID:** `OIFM_OIDM_795923`  
**Description:** Chronic blood products or residual hematoma in the subdural space, typically low attenuation on CT and often associated with membranes, septations, or recurrent bleeding.  
**Synonyms:** chronic SDH, chronic subdural hematoma  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller, worsened, improved  
**Source CSV:** `id=HID2965`; `name=chronic_subdural_hemorrhage`; `category=extra_axial`; `parent_id=HID2950`; `synonyms=chronic SDH, chronic subdural hematoma`; `finding_type=diagnosis`

**QUESTION:** Mechanical review flagged `SDH`; I left it capitalized as a standard acronym. Confirm acceptable.

**Response:** 

---

### subarachnoid hemorrhage

**Source file:** `defs/subarachnoid_hemorrhage.fm.json`  
**ID:** `OIFM_OIDM_975386`  
**Description:** Acute or chronic blood products within the subarachnoid space, including sulci, cisterns, or fissures, commonly visible as hyperattenuation on noncontrast CT in the acute setting.  
**Synonyms:** SAH, subarachnoid blood  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, worsened, improved  
**Source CSV:** `id=HID3000`; `name=subarachnoid_hemorrhage`; `category=extra_axial`; `parent_id=HID2900`; `synonyms=SAH, subarachnoid blood`; `finding_type=diagnosis`

**QUESTION:** Mechanical review flagged `SAH`; I left it capitalized as a standard acronym. Confirm acceptable.

**Response:** 

---

### perimesencephalic subarachnoid hemorrhage

**Source file:** `defs/perimesencephalic_subarachnoid_hemorrhage.fm.json`  
**ID:** `OIFM_OIDM_091292`  
**Description:** Subarachnoid hemorrhage centered in the perimesencephalic and prepontine cisterns, often with limited extension and a characteristic nonaneurysmal pattern when vascular imaging is negative.  
**Synonyms:** perimesencephalic SAH, pnSAH  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, worsened, improved  
**Source CSV:** `id=HID3005`; `name=perimesencephalic_subarachnoid_hemorrhage`; `category=extra_axial`; `parent_id=HID3000`; `synonyms=perimesencephalic SAH, pnSAH`; `finding_type=diagnosis`

**QUESTION:** Mechanical review flagged `SAH`/`pnSAH`; I left them capitalized as standard acronyms. Confirm acceptable.

**Response:** 

---

### epidural hemorrhage

**Source file:** `defs/epidural_hemorrhage.fm.json`  
**ID:** `OIFM_OIDM_713125`  
**Description:** Blood products in the epidural space between the inner table of the skull and dura, classically lentiform or biconvex on CT and often related to skull fracture or arterial injury.  
**Synonyms:** epidural hematoma, EDH  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller, worsened, improved  
**Source CSV:** `id=HID3010`; `name=epidural_hemorrhage`; `category=extra_axial`; `parent_id=HID2900`; `synonyms=epidural hematoma, EDH`; `finding_type=diagnosis`

**QUESTION:** Mechanical review flagged `EDH`; I left it capitalized as a standard acronym. Confirm acceptable.

**Response:** 

---

### extra-axial neoplasm

**Source file:** `defs/extra_axial_neoplasm.fm.json`  
**ID:** `OIFM_OIDM_693866`  
**Description:** A neoplasm located outside the brain parenchyma within an extra-axial intracranial compartment, including dural, meningeal, cranial nerve sheath, or cisternal tumors.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved  
**Source CSV:** `id=HID3050`; `name=extra_axial_neoplasm`; `category=extra_axial`; `parent_id=HID2600`; `synonyms=(blank)`; `finding_type=diagnosis`

**Assessment:** New grouping model for extra-axial neoplasms; confirm acceptable.

**Response:** 

---

### matched: meningioma -> meningioma

**Source file:** `defs/meningioma.fm.json`  
**ID:** `OIFM_OIDM_738859`  
**Description:** A typically benign, dural-based extra-axial neoplasm that on head CT appears as a well-circumscribed slightly hyperdense or isodense mass, often with calcification, homogeneous intense enhancement, and adjacent hyperostosis. It is the most common extra-axial intracranial tumor.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved, increased, decreased  
**Source CSV:** `id=HID3055`; `name=meningioma`; `category=extra_axial`; `parent_id=HID3050`; `synonyms=(blank)`; `finding_type=diagnosis`

**Assessment:** Existing model reused; confirm acceptable.

**Response:** 

---

### vestibular schwannoma

**Source file:** `defs/vestibular_schwannoma.fm.json`  
**ID:** `OIFM_OIDM_093050`  
**Description:** Benign nerve sheath tumor arising from the vestibular portion of cranial nerve VIII, typically centered in the internal auditory canal or cerebellopontine angle cistern.  
**Synonyms:** acoustic neuroma, acoustic schwannoma, CN VIII schwannoma  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved  
**Source CSV:** `id=HID3060`; `name=vestibular_schwannoma`; `category=extra_axial`; `parent_id=HID3050`; `synonyms=acoustic neuroma, acoustic schwannoma, CN VIII schwannoma`; `finding_type=diagnosis`

**QUESTION:** Mechanical review flagged `CN VIII`; I left it capitalized as a standard cranial nerve notation. Confirm acceptable.

**Response:** 

---
