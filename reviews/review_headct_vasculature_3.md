# Review: head CT vasculature batch 3

10 vasculature CSV decisions to review: 9 newly created models and 1 mappings to existing models. For each, check name, description, synonyms, direction-of-change values, and whether the CSV row should map to the listed OIFM ID. Add your response below each entry.

---

### arteriovenous malformation
**Source file:** `defs/arteriovenous_malformation.fm.json`  
**ID:** `OIFM_OIDM_853448`  
**Description:** Diagnosis of arteriovenous malformation, as recognized on head CT, CTA, or related neurovascular imaging.  
**Synonyms:** AVM, cerebral AVM, pial AVM  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID4605`; `name=arteriovenous_malformation`; `category=vasculature`; `parent_id=HID4600`; `synonyms=AVM, cerebral AVM, pial AVM`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the vasculature CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**ISSUE:** Mechanical review flagged uppercase acronym/eponym synonyms. Confirm capitalization is intentional for standard abbreviations or proper names.

**Response:** 

---

### matched: cavernous_malformation -> cerebral cavernous malformation
**Source file:** `defs/cerebral_cavernous_malformation.fm.json`  
**ID:** `OIFM_OIDM_224625`  
**Description:** A cluster of dilated, thin-walled low-flow vascular channels without intervening brain parenchyma, typically appearing on head CT as a subtle focal hyperdense lesion reflecting calcification or prior hemorrhage, or as an occult finding. MRI (especially GRE/SWI sequences) is substantially more sensitive for detection and characterization.  
**Synonyms:** cavernoma  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, increased, decreased

**Source CSV:** `id=HID4610`; `name=cavernous_malformation`; `category=vasculature`; `parent_id=HID4600`; `synonyms=cavernoma, cavernous hemangioma, cavernous angioma`; `finding_type=diagnosis`; `oifm_id=(blank)`

**QUESTION:** This row maps cavernous malformation to cerebral cavernous malformation. Confirm this neurovascular scope is acceptable for head CT.

**Response:** 

---

### dural arteriovenous fistula
**Source file:** `defs/dural_arteriovenous_fistula.fm.json`  
**ID:** `OIFM_OIDM_951059`  
**Description:** Diagnosis of dural arteriovenous fistula, as recognized on head CT, CTA, or related neurovascular imaging.  
**Synonyms:** DAVF, dural AVF, dural fistula  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID4615`; `name=dural_arteriovenous_fistula`; `category=vasculature`; `parent_id=HID4400`; `synonyms=DAVF, dural AVF, dural fistula`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the vasculature CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**ISSUE:** Mechanical review flagged uppercase acronym/eponym synonyms. Confirm capitalization is intentional for standard abbreviations or proper names.

**Response:** 

---

### intracranial arterial dissection
**Source file:** `defs/intracranial_arterial_dissection.fm.json`  
**ID:** `OIFM_OIDM_620740`  
**Description:** Diagnosis of intracranial arterial dissection, as recognized on head CT, CTA, or related neurovascular imaging.  
**Synonyms:** intracranial dissection  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID4620`; `name=intracranial_arterial_dissection`; `category=vasculature`; `parent_id=HID4400`; `synonyms=intracranial dissection`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the vasculature CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### vasospasm
**Source file:** `defs/vasospasm.fm.json`  
**ID:** `OIFM_OIDM_594350`  
**Description:** Diagnosis of vasospasm, as recognized on head CT, CTA, or related neurovascular imaging.  
**Synonyms:** cerebral vasospasm, arterial vasospasm  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID4625`; `name=vasospasm`; `category=vasculature`; `parent_id=HID4400`; `synonyms=cerebral vasospasm, arterial vasospasm`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the vasculature CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### moyamoya
**Source file:** `defs/moyamoya.fm.json`  
**ID:** `OIFM_OIDM_027440`  
**Description:** Diagnosis of moyamoya, as recognized on head CT, CTA, or related neurovascular imaging.  
**Synonyms:** moyamoya disease, moyamoya syndrome  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID4630`; `name=moyamoya`; `category=vasculature`; `parent_id=HID4400`; `synonyms=moyamoya disease, moyamoya syndrome`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the vasculature CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### carotid cavernous fistula
**Source file:** `defs/carotid_cavernous_fistula.fm.json`  
**ID:** `OIFM_OIDM_651223`  
**Description:** Diagnosis of carotid cavernous fistula, as recognized on head CT, CTA, or related neurovascular imaging.  
**Synonyms:** CCF, CC fistula  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID4635`; `name=carotid_cavernous_fistula`; `category=vasculature`; `parent_id=HID4400`; `synonyms=CCF, carotid cavernous fistula, CC fistula`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the vasculature CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**ISSUE:** Mechanical review flagged uppercase acronym/eponym synonyms. Confirm capitalization is intentional for standard abbreviations or proper names.

**Response:** 

---

### vein of galen malformation
**Source file:** `defs/vein_of_galen_malformation.fm.json`  
**ID:** `OIFM_OIDM_415157`  
**Description:** Diagnosis of vein of galen malformation, as recognized on head CT, CTA, or related neurovascular imaging.  
**Synonyms:** VGAM, vein of Galen aneurysmal malformation, vein of Galen aneurysmal dilatation  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID4640`; `name=vein_of_galen_malformation`; `category=vasculature`; `parent_id=HID4600`; `synonyms=VGAM, vein of Galen aneurysmal malformation, vein of Galen aneurysmal dilatation`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the vasculature CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**ISSUE:** Mechanical review flagged uppercase acronym/eponym synonyms. Confirm capitalization is intentional for standard abbreviations or proper names.

**Response:** 

---

### cerebral amyloid angiopathy
**Source file:** `defs/cerebral_amyloid_angiopathy.fm.json`  
**ID:** `OIFM_OIDM_315310`  
**Description:** Diagnosis of cerebral amyloid angiopathy, as recognized on head CT, CTA, or related neurovascular imaging.  
**Synonyms:** CAA, amyloid angiopathy  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID4645`; `name=cerebral_amyloid_angiopathy`; `category=vasculature`; `parent_id=HID4400`; `synonyms=CAA, amyloid angiopathy`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the vasculature CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**ISSUE:** Mechanical review flagged uppercase acronym/eponym synonyms. Confirm capitalization is intentional for standard abbreviations or proper names.

**Response:** 

---

### vascular anatomic variant
**Source file:** `defs/vascular_anatomic_variant.fm.json`  
**ID:** `OIFM_OIDM_390904`  
**Description:** Broad grouping for vascular anatomic variant findings involving intracranial or head and neck vasculature on head CT, CTA, or related neurovascular imaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID4800`; `name=vascular_anatomic_variant`; `category=vasculature`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`; `oifm_id=(blank)`

**Assessment:** Newly created from the vasculature CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

