# Review: head CT extra axial batch 3

9 models/mappings to review. For each, check name, description, synonyms, and direction-of-change values. Add your response below each entry.

---

### matched: pneumocephalus -> pneumocephalus

**Source file:** `defs/pneumocephalus.fm.json`  
**ID:** `OIFM_GMTS_007502`  
**Description:** Presence of air within the cranial cavity.  
**Synonyms:** intracranial air, pneumocranium  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller  
**Source CSV:** `id=HID2800`; `name=pneumocephalus`; `category=extra_axial`; `parent_id=HID2600`; `synonyms=intracranial air, pneumocranium`; `finding_type=observation`

**Assessment:** Existing GMTS model reused; CSV synonyms were added.

**Response:** 

---

### tension pneumocephalus

**Source file:** `defs/tension_pneumocephalus.fm.json`  
**ID:** `OIFM_OIDM_553278`  
**Description:** Pneumocephalus under pressure causing mass effect on intracranial structures, classically producing separated frontal lobes or other signs of clinically significant intracranial air tension.  
**Synonyms:** tension pneumocranium  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, worsened, improved  
**Source CSV:** `id=HID2805`; `name=tension_pneumocephalus`; `category=extra_axial`; `parent_id=HID2800`; `synonyms=tension pneumocranium`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### extra-axial calcification

**Source file:** `defs/extra_axial_calcification.fm.json`  
**ID:** `OIFM_OIDM_555547`  
**Description:** Calcification located in an extra-axial intracranial compartment or meningeal structure rather than within the brain parenchyma.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID2845`; `name=extra_axial_calcification`; `category=extra_axial`; `parent_id=HID2600`; `synonyms=(blank)`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### dural calcification

**Source file:** `defs/dural_calcification.fm.json`  
**ID:** `OIFM_OIDM_623745`  
**Description:** Calcification involving the dura mater, which may be physiologic, age-related, postsurgical, postinflammatory, or associated with adjacent pathology.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID2850`; `name=dural_calcification`; `category=extra_axial`; `parent_id=HID2845`; `synonyms=(blank)`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### falcine calcification

**Source file:** `defs/falcine_calcification.fm.json`  
**ID:** `OIFM_OIDM_950038`  
**Description:** Calcification involving the falx cerebri, commonly seen as a linear or nodular extra-axial midline calcification.  
**Synonyms:** falx calcification, calcified falx  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID2855`; `name=falcine_calcification`; `category=extra_axial`; `parent_id=HID2850`; `synonyms=falx calcification, calcified falx`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### tentorial calcification

**Source file:** `defs/tentorial_calcification.fm.json`  
**ID:** `OIFM_OIDM_898224`  
**Description:** Calcification involving the tentorium cerebelli, seen as extra-axial calcification along the tentorial leaflets.  
**Synonyms:** calcified tentorium  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID2860`; `name=tentorial_calcification`; `category=extra_axial`; `parent_id=HID2850`; `synonyms=calcified tentorium`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### falcine dysgenesis

**Source file:** `defs/falcine_dysgenesis.fm.json`  
**ID:** `OIFM_OIDM_211197`  
**Description:** Congenital abnormal development or absence of the falx cerebri, often associated with abnormal formation of the interhemispheric fissure.  
**Synonyms:** absent falx, partial falx, absent falx cerebri, falcine hypoplasia, absent interhemispheric fissure, partial interhemispheric fissure  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID2865`; `name=falcine_dysgenesis`; `category=extra_axial`; `parent_id=HID2600`; `synonyms=absent falx, partial falx, absent falx cerebri, falcine hypoplasia, absent interhemispheric fissure, partial interhemispheric fissure`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### extra-axial hemorrhage

**Source file:** `defs/extra_axial_hemorrhage.fm.json`  
**ID:** `OIFM_OIDM_355535`  
**Description:** Intracranial hemorrhage located outside the brain parenchyma, including subdural, epidural, subarachnoid, or other extra-axial blood products.  
**Synonyms:** extra-axial blood, extra-axial hematoma  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller, worsened, improved  
**Source CSV:** `id=HID2900`; `name=extra_axial_hemorrhage`; `category=extra_axial`; `parent_id=HID2600`; `synonyms=extra-axial blood, extra-axial hematoma`; `finding_type=diagnosis`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### matched: subdural_hemorrhage -> subdural hematoma

**Source file:** `defs/subdural_hematoma.fm.json`  
**ID:** `OIFM_MSFT_767776`  
**Description:** A collection of blood in the subdural space, between the dura mater and arachnoid membrane, typically appearing as a crescent-shaped extra-axial collection on CT. Acute hematomas are hyperdense, subacute isodense, and chronic hypodense relative to brain parenchyma.  
**Synonyms:** SDH, subdural hemorrhage  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved, increased, decreased  
**Source CSV:** `id=HID2950`; `name=subdural_hemorrhage`; `category=extra_axial`; `parent_id=HID2900`; `synonyms=subdural hematoma, SDH`; `finding_type=diagnosis`

**QUESTION:** Mapped to existing `subdural hematoma`, which already includes `subdural hemorrhage` and `SDH`. Confirm acceptable.

**Response:** 

---
