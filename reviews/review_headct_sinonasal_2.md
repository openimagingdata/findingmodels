# Review: head CT sinonasal batch 2

10 sinonasal CSV decisions to review: 6 newly created models and 4 mappings to existing models. For each, check name, description, synonyms, direction-of-change values, and whether the CSV row should map to the listed OIFM ID. Add your response below each entry.

---

### sinus polyp
**Source file:** `defs/sinus_polyp.fm.json`  
**ID:** `OIFM_OIDM_200848`  
**Description:** Imaging observation of sinus polyp involving the nasal cavity or paranasal sinuses on head CT or related sinonasal imaging.  
**Synonyms:** solitary sinus polyp, paranasal sinus polyp, solitary sinonasal polyp, sinonasal polyp, mucosal polyp sinus  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID7648`; `name=sinus_polyp`; `category=sinonasal`; `parent_id=HID7600`; `synonyms=solitary sinus polyp, paranasal sinus polyp, solitary sinonasal polyp, sinonasal polyp, mucosal polyp sinus`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the sinonasal CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### antrochoanal polyp
**Source file:** `defs/antrochoanal_polyp.fm.json`  
**ID:** `OIFM_OIDM_386367`  
**Description:** Imaging observation of antrochoanal polyp involving the nasal cavity or paranasal sinuses on head CT or related sinonasal imaging.  
**Synonyms:** maxillary antrochoanal polyp, ACP, Killian polyp, maxillary choanal polyp  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID7649`; `name=antrochoanal_polyp`; `category=sinonasal`; `parent_id=HID7648`; `synonyms=maxillary antrochoanal polyp, ACP, Killian polyp, maxillary choanal polyp`; `finding_type=observation`; `oifm_id=(blank)`

**Assessment:** Newly created from the sinonasal CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**ISSUE:** Mechanical review flagged uppercase acronym/eponym synonyms. Confirm capitalization is intentional for standard abbreviations or proper names.

**Response:** 

---

### matched: sinonasal_polyposis -> nasal polyposis
**Source file:** `defs/nasal_polyposis.fm.json`  
**ID:** `OIFM_GMTS_025576`  
**Description:** The presence of polyps in the nasal cavity, often related to chronic inflammation.  
**Synonyms:** nasal polyps  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID7650`; `name=sinonasal_polyposis`; `category=sinonasal`; `parent_id=HID7600`; `synonyms=nasal polyposis, polypoid mucosal disease`; `finding_type=observation`; `oifm_id=(blank)`

**QUESTION:** This row maps sinonasal polyposis to nasal polyposis. Confirm sinonasal and nasal polyposis should share this model.

**Response:** 

---

### matched: sinonasal_lesion -> sinonasal lesion
**Source file:** `defs/sinonasal_lesion.fm.json`  
**ID:** `OIFM_GMTS_030854`  
**Description:** Abnormal tissue or mass in the sinonasal region.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID7655`; `name=sinonasal_lesion`; `category=sinonasal`; `parent_id=HID7600`; `synonyms=sinonasal mass, nasal mass, nasal cavity mass, nasal lesion`; `finding_type=observation`; `oifm_id=(blank)`

**QUESTION:** This row maps sinonasal lesion to the existing sinonasal lesion model. Confirm this direct mapping is acceptable.

**Response:** 

---

### matched: nasal_septal_perforation -> nasal septum perforation
**Source file:** `defs/nasal_septum_perforation.fm.json`  
**ID:** `OIFM_GMTS_008390`  
**Description:** A defect or hole in the nasal septum.  
**Synonyms:** nasal septal perforation  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller

**Source CSV:** `id=HID7660`; `name=nasal_septal_perforation`; `category=sinonasal`; `parent_id=HID7600`; `synonyms=septal perforation`; `finding_type=observation`; `oifm_id=(blank)`

**QUESTION:** This row maps nasal septal perforation to nasal septum perforation. Confirm naming difference is acceptable.

**Response:** 

---

### hemosinus
**Source file:** `defs/hemosinus.fm.json`  
**ID:** `OIFM_OIDM_269257`  
**Description:** Diagnosis of hemosinus, as recognized on head CT or related sinonasal imaging.  
**Synonyms:** sinus hemorrhage, blood in sinus  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID7665`; `name=hemosinus`; `category=sinonasal`; `parent_id=HID7600`; `synonyms=sinus hemorrhage, blood in sinus`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the sinonasal CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### matched: paranasal_sinusitis -> paranasal sinusitis
**Source file:** `defs/paranasal_sinusitis.fm.json`  
**ID:** `OIFM_OIDM_035625`  
**Description:** Mucosal thickening, fluid, or opacification within one or more paranasal sinuses reflecting acute or chronic inflammation. On CT, findings range from mild mucoperiosteal thickening to air-fluid levels and complete sinus opacification, sometimes with associated osseous remodeling or sclerosis in chronic disease.  
**Synonyms:** sinusitis, inflammatory sinus disease, rhinosinusitis  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, worsened, improved

**Source CSV:** `id=HID7700`; `name=paranasal_sinusitis`; `category=sinonasal`; `parent_id=HID7600`; `synonyms=sinusitis, inflammatory sinus disease`; `finding_type=diagnosis`; `oifm_id=(blank)`

**QUESTION:** This row maps paranasal sinusitis to the existing paranasal sinusitis model. Confirm direct mapping.

**Response:** 

---

### maxillary sinusitis
**Source file:** `defs/maxillary_sinusitis.fm.json`  
**ID:** `OIFM_OIDM_464803`  
**Description:** Diagnosis of maxillary sinusitis, as recognized on head CT or related sinonasal imaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID7705`; `name=maxillary_sinusitis`; `category=sinonasal`; `parent_id=HID7700`; `synonyms=(blank)`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the sinonasal CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### ethmoid sinusitis
**Source file:** `defs/ethmoid_sinusitis.fm.json`  
**ID:** `OIFM_OIDM_038877`  
**Description:** Diagnosis of ethmoid sinusitis, as recognized on head CT or related sinonasal imaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID7710`; `name=ethmoid_sinusitis`; `category=sinonasal`; `parent_id=HID7700`; `synonyms=(blank)`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the sinonasal CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

---

### frontal sinusitis
**Source file:** `defs/frontal_sinusitis.fm.json`  
**ID:** `OIFM_OIDM_130881`  
**Description:** Diagnosis of frontal sinusitis, as recognized on head CT or related sinonasal imaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved

**Source CSV:** `id=HID7715`; `name=frontal_sinusitis`; `category=sinonasal`; `parent_id=HID7700`; `synonyms=(blank)`; `finding_type=diagnosis`; `oifm_id=(blank)`

**Assessment:** Newly created from the sinonasal CSV row. Confirm name, scope, description, synonyms, and change-from-prior values.

**Response:** 

