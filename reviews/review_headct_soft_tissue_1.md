# Review: head CT soft tissue batch 1

13 soft_tissue CSV decisions to review: 4 newly created models and 9 mappings to existing models. For each, check name, description, synonyms, direction-of-change values, and whether the CSV row should map to the listed OIFM ID. Add your response below each entry.

---

### soft tissue hematoma

**Source file:** `defs/soft_tissue_hematoma.fm.json`  
**ID:** `OIFM_OIDM_251841`  
**Description:** A localized collection of blood within the extracranial soft tissues, typically related to trauma, surgery, or coagulopathy.  
**Synonyms:** soft-tissue hematoma, soft tissue blood collection  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID7450`; `name=soft_tissue_hematoma`; `category=soft_tissue`; `parent_id=HID7400`; `synonyms=(blank)`; `finding_type=diagnosis`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### subgaleal hematoma

**Source file:** `defs/subgaleal_hematoma.fm.json`  
**ID:** `OIFM_OIDM_185082`  
**Description:** A hematoma in the potential space between the galea aponeurotica and the periosteum of the skull, typically visible as extracranial scalp swelling that can cross sutures.  
**Synonyms:** subgaleal hemorrhage, subaponeurotic hematoma, subaponeurotic hemorrhage  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID7455`; `name=subgaleal_hematoma`; `category=soft_tissue`; `parent_id=HID7450`; `synonyms=subgaleal hemorrhage`; `finding_type=diagnosis`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### cephalohematoma

**Source file:** `defs/cephalohematoma.fm.json`  
**ID:** `OIFM_OIDM_401242`  
**Description:** A subperiosteal blood collection along the calvarium, usually confined by cranial sutures and seen as a focal extracranial scalp hematoma.  
**Synonyms:** cephalhematoma, subperiosteal scalp hematoma, subperiosteal scalp hemorrhage  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID7460`; `name=cephalohematoma`; `category=soft_tissue`; `parent_id=HID7450`; `synonyms=cephalhematoma, subperiosteal hematoma`; `finding_type=diagnosis`

**QUESTION:** The source CSV included `subperiosteal hematoma`; I scoped this to `subperiosteal scalp hematoma` and `subperiosteal scalp hemorrhage` to avoid cross-body ambiguity. Confirm this narrower synonym choice.

**Response:** 

---

### tonsillolith

**Source file:** `defs/tonsillolith.fm.json`  
**ID:** `OIFM_OIDM_661237`  
**Description:** A calcified concretion within a tonsillar crypt, typically seen on CT as a small calcification in the palatine tonsil region.  
**Synonyms:** tonsillar calcification, tonsil stone, tonsillar concretion, palatine tonsil calcification  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID7555`; `name=tonsillolith`; `category=soft_tissue`; `parent_id=HID7550`; `synonyms=tonsillar calcification, tonsil stone, tonsillar concretion, palatine tonsil calcification`; `finding_type=observation`

**QUESTION:** Confirm that `tonsillar calcification` and `palatine tonsil calcification` should map to `tonsillolith`, rather than remaining as broader calcification language.

**Response:** 

---

### matched: soft_tissue_abnormality -> soft tissue abnormality

**Source file:** `defs/soft_tissue_abnormality.fm.json`  
**ID:** `OIFM_OIDM_221920`  
**Description:** Nonspecific abnormality of the soft tissues visible on chest radiograph.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID7400`; `name=soft_tissue_abnormality`; `category=soft_tissue`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`

**Assessment:** Direct match at the same broad level. Confirm this row should map to this existing model.

**Response:** 

---

### matched: soft_tissue_swelling -> soft tissue swelling

**Source file:** `defs/soft_tissue_swelling.fm.json`  
**ID:** `OIFM_OIDM_696759`  
**Description:** Increased volume or density of soft tissues, suggesting edema, hematoma, or mass effect on radiograph.  
**Synonyms:** soft tissue edema, soft tissue fullness  
**Change from prior:** unchanged, stable, new, resolved, worsened, improved, larger, smaller

**Source CSV:** `id=HID7405`; `name=soft_tissue_swelling`; `category=soft_tissue`; `parent_id=HID7400`; `synonyms=(blank)`; `finding_type=observation`

**Assessment:** Direct match. Confirm this row should map to this existing model.

**Response:** 

---

### matched: soft_tissue_edema -> soft tissue swelling

**Source file:** `defs/soft_tissue_swelling.fm.json`  
**ID:** `OIFM_OIDM_696759`  
**Description:** Increased volume or density of soft tissues, suggesting edema, hematoma, or mass effect on radiograph.  
**Synonyms:** soft tissue edema, soft tissue fullness  
**Change from prior:** unchanged, stable, new, resolved, worsened, improved, larger, smaller

**Source CSV:** `id=HID7410`; `name=soft_tissue_edema`; `category=soft_tissue`; `parent_id=HID7400`; `synonyms=(blank)`; `finding_type=diagnosis`

**QUESTION:** `soft tissue edema` is already a synonym on `soft tissue swelling`. Confirm that the CSV row should map to the swelling model rather than requiring a separate edema model.

**Response:** 

---

### matched: soft_tissue_lesion -> soft tissue mass

**Source file:** `defs/soft_tissue_mass.fm.json`  
**ID:** `OIFM_OIDM_299401`  
**Description:** A focal soft-tissue abnormality that appears as a discrete or ill-defined mass within soft tissues on imaging. It encompasses a spectrum of etiologies from benign to malignant; correlation with clinical history and further imaging or biopsy may be required for characterization.  
**Synonyms:** soft-tissue mass, soft tissue lesion, soft-tissue lesion, STM  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID7500`; `name=soft_tissue_lesion`; `category=soft_tissue`; `parent_id=HID7400`; `synonyms=(blank)`; `finding_type=(blank)`

**QUESTION:** `soft tissue lesion` is already a synonym on `soft tissue mass`. Confirm that lesion and mass are equivalent enough here for CSV mapping.

**Response:** 

---

### matched: soft_tissue_epidermal_inclusion_cyst -> Epidermal Inclusion Cyst

**Source file:** `defs/epidermal_inclusion_cyst.fm.json`  
**ID:** `OIFM_MGB_603715`  
**Description:** Presence of an epidermal inclusion cyst  
**Synonyms:** (none)  
**Change from prior:** (none found)

**Source CSV:** `id=HID7505`; `name=soft_tissue_epidermal_inclusion_cyst`; `category=soft_tissue`; `parent_id=HID7500`; `synonyms=sebaceous cyst, epidermal inclusion cyst, epidermoid inclusion cyst, infundibular cyst, scalp cyst`; `finding_type=diagnosis`

**QUESTION:** This appears to be the correct existing concept, but the existing model uses legacy casing and lacks a `change from prior` attribute. Confirm whether to map the CSV row as-is, or whether this model should be cleaned up in this batch.

**Response:** 

---

### matched: soft_tissue_lipoma -> Lipoma

**Source file:** `defs/lipoma.fm.json`  
**ID:** `OIFM_MGB_269106`  
**Description:** A lipoma is a benign tumor composed of fat cells. It is one of the most common benign tumors found in the body.  
**Synonyms:** (none)  
**Change from prior:** (none found)

**Source CSV:** `id=HID7510`; `name=soft_tissue_lipoma`; `category=soft_tissue`; `parent_id=HID7500`; `synonyms=(blank)`; `finding_type=diagnosis`

**QUESTION:** This appears to be the correct existing concept, but the existing model uses legacy casing and lacks a `change from prior` attribute. Confirm whether to map the CSV row as-is, or whether this model should be cleaned up in this batch.

**Response:** 

---

### matched: soft_tissue_dermoid_cyst -> Dermoid Cyst

**Source file:** `defs/dermoid_cyst.fm.json`  
**ID:** `OIFM_CDE_000216`  
**Description:** Dermoid Cyst detection on CT  
**Synonyms:** (none)  
**Change from prior:** (none found)

**Source CSV:** `id=HID7515`; `name=soft_tissue_dermoid_cyst`; `category=soft_tissue`; `parent_id=HID7500`; `synonyms=(blank)`; `finding_type=diagnosis`

**QUESTION:** This appears to be the correct existing concept, but the existing CDE model uses legacy casing and lacks a `change from prior` attribute. Confirm whether to map the CSV row as-is, or whether this model should be cleaned up in this batch.

**Response:** 

---

### matched: soft_tissue_calcification -> soft-tissue calcification

**Source file:** `defs/soft_tissue_calcification.fm.json`  
**ID:** `OIFM_GMTS_025786`  
**Description:** Calcium deposits within soft tissues, which can be due to various pathological processes.  
**Synonyms:** tissue calcification, dystrophic calcification  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID7550`; `name=soft_tissue_calcification`; `category=soft_tissue`; `parent_id=HID7400`; `synonyms=(blank)`; `finding_type=observation`

**Assessment:** Direct match. Confirm this row should map to this existing model.

**Response:** 

---

### matched: subcutaneous_emphysema -> subcutaneous emphysema

**Source file:** `defs/subcutaneous_emphysema.fm.json`  
**ID:** `OIFM_OIDM_755361`  
**Description:** Gas within the subcutaneous soft tissues, appearing as lucent streaks on chest radiograph.  
**Synonyms:** subcutaneous gas, soft tissue gas  
**Change from prior:** unchanged, stable, new, resolved, worsened, improved, increased, decreased

**Source CSV:** `id=HID7560`; `name=subcutaneous_emphysema`; `category=soft_tissue`; `parent_id=HID7400`; `synonyms=subcutaneous air, soft tissue gas, soft tissue emphysema`; `finding_type=observation`

**Assessment:** Direct match. Confirm this row should map to this existing model.

**Response:** 

---
