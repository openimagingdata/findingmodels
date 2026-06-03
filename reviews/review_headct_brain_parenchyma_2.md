# Review: head CT brain_parenchyma batch 2

10 brain_parenchyma CSV decisions to review: 9 newly created models and 1 mappings to existing models. For each, check name, description, synonyms, direction-of-change values, and whether the CSV row should map to the listed OIFM ID. Add your response below each entry.

---

### ventricular effacement
**Source file:** `defs/ventricular_effacement.fm.json`  
**ID:** `OIFM_OIDM_764784`  
**Description:** Imaging observation of ventricular effacement within the brain parenchyma on head CT or related neuroimaging.  
**Synonyms:** compressed ventricles, third ventricle narrowing, cerebral aqueduct narrowing, narrowing of the third ventricle and cerebral aqueduct, narrowing of the cerebral aqueduct  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0320`; `name=ventricular_effacement`; `category=brain_parenchyma`; `parent_id=HID0300`; `synonyms=compressed ventricles, third ventricle narrowing, cerebral aqueduct narrowing, narrowing of the third ventricle and cerebral aqueduct, narrowing of the cerebral aqueduct`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### herniation
**Source file:** `defs/herniation.fm.json`  
**ID:** `OIFM_OIDM_943505`  
**Description:** Imaging observation of herniation within the brain parenchyma on head CT or related neuroimaging.  
**Synonyms:** brain herniation, cerebral herniation  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0350`; `name=herniation`; `category=brain_parenchyma`; `parent_id=HID0300`; `synonyms=brain herniation, cerebral herniation`; `finding_type=observation`; `oifm_id=(blank)`

**QUESTION:** Created a new generic herniation model instead of mapping to encephalocele/meningocele, because that synonym hit reflects a different structural concept.

**Response:** 

---

### subfalcine herniation
**Source file:** `defs/subfalcine_herniation.fm.json`  
**ID:** `OIFM_OIDM_259932`  
**Description:** Imaging observation of subfalcine herniation within the brain parenchyma on head CT or related neuroimaging.  
**Synonyms:** subfalcine shift  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0355`; `name=subfalcine_herniation`; `category=brain_parenchyma`; `parent_id=HID0350`; `synonyms=subfalcine shift`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### matched: descending_transtentorial_herniation -> descending transtentorial herniation
**Source file:** `defs/descending_transtentorial_herniation.fm.json`  
**ID:** `OIFM_OIDM_441726`  
**Description:** Inferior displacement of the medial temporal lobe (uncus and parahippocampal gyrus) and/or diencephalon through the tentorial incisura, typically due to supratentorial mass effect. Secondary findings include effacement of the suprasellar and perimesencephalic cisterns, midbrain compression, and possible posterior cerebral artery territory infarction.  
**Synonyms:** descending transtentorial hernia  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, worsened, improved

**Source CSV:** `id=HID0400`; `name=descending_transtentorial_herniation`; `category=brain_parenchyma`; `parent_id=HID0350`; `synonyms=descending transtentorial hernia, DTH`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Existing-model mapping. Confirm this CSV row should map to the listed OIFM ID.

**Response:** 

---

### uncal herniation
**Source file:** `defs/uncal_herniation.fm.json`  
**ID:** `OIFM_OIDM_211678`  
**Description:** Imaging observation of uncal herniation within the brain parenchyma on head CT or related neuroimaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0450`; `name=uncal_herniation`; `category=brain_parenchyma`; `parent_id=HID0400`; `synonyms=(blank)`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### medialization of uncus
**Source file:** `defs/medialization_of_uncus.fm.json`  
**ID:** `OIFM_OIDM_213314`  
**Description:** Imaging observation of medialization of uncus within the brain parenchyma on head CT or related neuroimaging.  
**Synonyms:** uncal medialization, uncal displacement  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0455`; `name=medialization_of_uncus`; `category=brain_parenchyma`; `parent_id=HID0450`; `synonyms=uncal medialization, uncal displacement`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### central transtentorial herniation
**Source file:** `defs/central_transtentorial_herniation.fm.json`  
**ID:** `OIFM_OIDM_069851`  
**Description:** Imaging observation of central transtentorial herniation within the brain parenchyma on head CT or related neuroimaging.  
**Synonyms:** central herniation  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0460`; `name=central_transtentorial_herniation`; `category=brain_parenchyma`; `parent_id=HID0400`; `synonyms=central herniation`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### ascending transtentorial herniation
**Source file:** `defs/ascending_transtentorial_herniation.fm.json`  
**ID:** `OIFM_OIDM_856008`  
**Description:** Imaging observation of ascending transtentorial herniation within the brain parenchyma on head CT or related neuroimaging.  
**Synonyms:** upward transtentorial herniation, upward herniation, ascending transtentorial hernia  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0465`; `name=ascending_transtentorial_herniation`; `category=brain_parenchyma`; `parent_id=HID0350`; `synonyms=upward transtentorial herniation, upward herniation, ascending transtentorial hernia`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### cerebellar tonsillar herniation
**Source file:** `defs/cerebellar_tonsillar_herniation.fm.json`  
**ID:** `OIFM_OIDM_439355`  
**Description:** Imaging observation of cerebellar tonsillar herniation within the brain parenchyma on head CT or related neuroimaging.  
**Synonyms:** tonsillar herniation, foramen magnum herniation  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0470`; `name=cerebellar_tonsillar_herniation`; `category=brain_parenchyma`; `parent_id=HID0350`; `synonyms=tonsillar herniation, foramen magnum herniation`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### transalar herniation
**Source file:** `defs/transalar_herniation.fm.json`  
**ID:** `OIFM_OIDM_016167`  
**Description:** Imaging observation of transalar herniation within the brain parenchyma on head CT or related neuroimaging.  
**Synonyms:** transalar hernia, sphenoid wing herniation  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID0475`; `name=transalar_herniation`; `category=brain_parenchyma`; `parent_id=HID0350`; `synonyms=transalar hernia, sphenoid wing herniation`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the brain_parenchyma CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

