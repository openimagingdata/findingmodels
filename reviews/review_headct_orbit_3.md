# Review: head CT orbit batch 3

10 orbit CSV decisions to review: 9 newly created models and 1 mappings to existing models. For each, check name, description, synonyms, direction-of-change values, and whether the CSV row should map to the listed OIFM ID. Add your response below each entry.

---

### orbital hemorrhage
**Source file:** `defs/orbital_hemorrhage.fm.json`  
**ID:** `OIFM_OIDM_321389`  
**Description:** Diagnosis of orbital hemorrhage, as recognized on head CT or related orbital imaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID6750`; `name=orbital_hemorrhage`; `category=orbit`; `parent_id=HID6600`; `synonyms=(blank)`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the orbit CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### retrobulbar hemorrhage
**Source file:** `defs/retrobulbar_hemorrhage.fm.json`  
**ID:** `OIFM_OIDM_832683`  
**Description:** Diagnosis of retrobulbar hemorrhage, as recognized on head CT or related orbital imaging.  
**Synonyms:** retro-ocular hemorrhage, retrobulbar hematoma  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID6800`; `name=retrobulbar_hemorrhage`; `category=orbit`; `parent_id=HID6750`; `synonyms=retro-ocular hemorrhage, retrobulbar hematoma`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the orbit CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### intraconal hemorrhage
**Source file:** `defs/intraconal_hemorrhage.fm.json`  
**ID:** `OIFM_OIDM_006455`  
**Description:** Diagnosis of intraconal hemorrhage, as recognized on head CT or related orbital imaging.  
**Synonyms:** intraconal hematoma  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID6805`; `name=intraconal_hemorrhage`; `category=orbit`; `parent_id=HID6800`; `synonyms=intraconal hematoma`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the orbit CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### extraconal hemorrhage
**Source file:** `defs/extraconal_hemorrhage.fm.json`  
**ID:** `OIFM_OIDM_885429`  
**Description:** Diagnosis of extraconal hemorrhage, as recognized on head CT or related orbital imaging.  
**Synonyms:** extraconal hematoma  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID6810`; `name=extraconal_hemorrhage`; `category=orbit`; `parent_id=HID6800`; `synonyms=extraconal hematoma`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the orbit CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### subperiosteal hemorrhage
**Source file:** `defs/subperiosteal_hemorrhage.fm.json`  
**ID:** `OIFM_OIDM_803675`  
**Description:** Diagnosis of subperiosteal hemorrhage, as recognized on head CT or related orbital imaging.  
**Synonyms:** subperiosteal orbital hematoma  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID6815`; `name=subperiosteal_hemorrhage`; `category=orbit`; `parent_id=HID6750`; `synonyms=subperiosteal orbital hematoma`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the orbit CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### matched: intraocular_hemorrhage -> intraocular hemorrhage
**Source file:** `defs/intraocular_hemorrhage.fm.json`  
**ID:** `OIFM_OIDM_535373`  
**Description:** Blood products within the globe, which may involve the anterior chamber (hyphema), vitreous, or subretinal space. On CT, appears as hyperdense material within the ocular compartments, often in the setting of trauma.  
**Synonyms:** intraocular blood products, intraocular blood, hemorrhage within the globe  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved, increased, decreased

**Source CSV:** `id=HID6850`; `name=intraocular_hemorrhage`; `category=orbit`; `parent_id=HID6750`; `synonyms=intraocular blood products`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Existing-model mapping. Confirm this CSV row should map to the listed OIFM ID.

**Response:** 

---

### hyphema
**Source file:** `defs/hyphema.fm.json`  
**ID:** `OIFM_OIDM_600743`  
**Description:** Diagnosis of hyphema, as recognized on head CT or related orbital imaging.  
**Synonyms:** anterior chamber hemorrhage  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID6855`; `name=hyphema`; `category=orbit`; `parent_id=HID6850`; `synonyms=anterior chamber hemorrhage`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the orbit CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### vitreous hemorrhage
**Source file:** `defs/vitreous_hemorrhage.fm.json`  
**ID:** `OIFM_OIDM_581647`  
**Description:** Diagnosis of vitreous hemorrhage, as recognized on head CT or related orbital imaging.  
**Synonyms:** vitreous blood, intravitreal hemorrhage  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID6860`; `name=vitreous_hemorrhage`; `category=orbit`; `parent_id=HID6850`; `synonyms=vitreous blood, intravitreal hemorrhage`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the orbit CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### subretinal hemorrhage
**Source file:** `defs/subretinal_hemorrhage.fm.json`  
**ID:** `OIFM_OIDM_773498`  
**Description:** Diagnosis of subretinal hemorrhage, as recognized on head CT or related orbital imaging.  
**Synonyms:** subretinal blood  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID6865`; `name=subretinal_hemorrhage`; `category=orbit`; `parent_id=HID6850`; `synonyms=subretinal blood`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the orbit CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### choroidal hemorrhage
**Source file:** `defs/choroidal_hemorrhage.fm.json`  
**ID:** `OIFM_OIDM_144017`  
**Description:** Diagnosis of choroidal hemorrhage, as recognized on head CT or related orbital imaging.  
**Synonyms:** suprachoroidal hemorrhage, hemorrhagic choroidal detachment  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID6870`; `name=choroidal_hemorrhage`; `category=orbit`; `parent_id=HID6850`; `synonyms=suprachoroidal hemorrhage, hemorrhagic choroidal detachment`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the orbit CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

