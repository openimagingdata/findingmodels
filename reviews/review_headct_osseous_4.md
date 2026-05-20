# Review: head CT osseous batch 4

10 models/mappings to review. For each, check name, description, synonyms, and direction-of-change values. Add your response below each entry.

---

### calvarial osteoma

**Source file:** `defs/calvarial_osteoma.fm.json`  
**ID:** `OIFM_OIDM_935903`  
**Description:** Benign dense osseous tumor arising from the calvarium or skull, often appearing as a well-defined sclerotic exostosis.  
**Synonyms:** skull osteoma  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller  
**Source CSV:** `id=HID5405`; `name=calvarial_osteoma`; `category=osseous`; `parent_id=HID5400`; `synonyms=skull osteoma`; `finding_type=diagnosis`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### matched: calvarial_metastasis -> skull metastasis

**Source file:** `defs/skull_metastasis.fm.json`  
**ID:** `OIFM_GMTS_025475`  
**Description:** Secondary malignant lesions in the skull resulting from spread of cancer.  
**Synonyms:** calvarial metastasis, metastatic skull lesion, metastasis to the skull, cranial metastasis  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller  
**Source CSV:** `id=HID5410`; `name=calvarial_metastasis`; `category=osseous`; `parent_id=HID5400`; `synonyms=skull metastasis`; `finding_type=diagnosis`

**QUESTION:** Mapped to existing `skull metastasis`, which already includes `calvarial metastasis`; confirm canonical name is acceptable.

**Response:** 

---

### intraosseous hemangioma

**Source file:** `defs/intraosseous_hemangioma.fm.json`  
**ID:** `OIFM_OIDM_822124`  
**Description:** Benign vascular lesion within bone, in the skull often involving the diploic space and sometimes showing trabecular or sunburst internal architecture.  
**Synonyms:** calvarial hemangioma  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller  
**Source CSV:** `id=HID5415`; `name=intraosseous_hemangioma`; `category=osseous`; `parent_id=HID5400`; `synonyms=calvarial hemangioma`; `finding_type=diagnosis`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### intradiploic lipoma

**Source file:** `defs/intradiploic_lipoma.fm.json`  
**ID:** `OIFM_OIDM_188030`  
**Description:** Fat-containing lesion located within the diploic space of the skull.  
**Synonyms:** diploic lipoma  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller  
**Source CSV:** `id=HID5420`; `name=intradiploic_lipoma`; `category=osseous`; `parent_id=HID5400`; `synonyms=diploic lipoma`; `finding_type=diagnosis`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### multiple myeloma

**Source file:** `defs/multiple_myeloma.fm.json`  
**ID:** `OIFM_OIDM_048062`  
**Description:** Plasma cell malignancy that can involve the skull or other bones with lytic osseous lesions.  
**Synonyms:** myeloma  
**Change from prior:** unchanged, stable, new, resolved, worsened, improved  
**Source CSV:** `id=HID5425`; `name=multiple_myeloma`; `category=osseous`; `parent_id=HID5400`; `synonyms=myeloma`; `finding_type=diagnosis`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### plasmacytoma

**Source file:** `defs/plasmacytoma.fm.json`  
**ID:** `OIFM_OIDM_477248`  
**Description:** Solitary plasma cell neoplasm involving bone or soft tissue, which may appear as a focal lytic skull lesion when osseous.  
**Synonyms:** solitary bone plasmacytoma  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved  
**Source CSV:** `id=HID5430`; `name=plasmacytoma`; `category=osseous`; `parent_id=HID5400`; `synonyms=solitary bone plasmacytoma`; `finding_type=diagnosis`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### langerhans cell histiocytosis

**Source file:** `defs/langerhans_cell_histiocytosis.fm.json`  
**ID:** `OIFM_OIDM_664068`  
**Description:** Clonal histiocytic disorder that can involve the skull with punched-out lytic calvarial lesions, beveled edges, or soft-tissue components.  
**Synonyms:** LCH, eosinophilic granuloma, histiocytosis X  
**Change from prior:** unchanged, stable, new, resolved, worsened, improved  
**Source CSV:** `id=HID5435`; `name=langerhans_cell_histiocytosis`; `category=osseous`; `parent_id=HID5400`; `synonyms=LCH, eosinophilic granuloma, histiocytosis X`; `finding_type=diagnosis`

**Assessment:** Mechanical review flagged `LCH` and `histiocytosis X`; left as standard acronym/eponym-style synonym.

**Response:** 

---

### skull osteomyelitis

**Source file:** `defs/skull_osteomyelitis.fm.json`  
**ID:** `OIFM_OIDM_154564`  
**Description:** Infection of the skull or calvarial bone, potentially associated with bone erosion, sclerosis, soft-tissue inflammation, or adjacent sinus or scalp infection.  
**Synonyms:** calvarial osteomyelitis, cranial osteomyelitis  
**Change from prior:** unchanged, stable, new, resolved, worsened, improved  
**Source CSV:** `id=HID5440`; `name=skull_osteomyelitis`; `category=osseous`; `parent_id=HID5000`; `synonyms=calvarial osteomyelitis, cranial osteomyelitis`; `finding_type=diagnosis`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### fibrous dysplasia

**Source file:** `defs/fibrous_dysplasia.fm.json`  
**ID:** `OIFM_OIDM_341267`  
**Description:** Benign fibro-osseous disorder in which normal bone is replaced by fibrous tissue and immature woven bone, often producing expansile ground-glass osseous change in the skull or facial bones.  
**Synonyms:** fibrous dysplasia skull  
**Change from prior:** unchanged, stable, new, resolved, worsened, improved  
**Source CSV:** `id=HID5445`; `name=fibrous_dysplasia`; `category=osseous`; `parent_id=HID5000`; `synonyms=fibrous dysplasia skull`; `finding_type=diagnosis`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### paget disease of skull

**Source file:** `defs/paget_disease_of_skull.fm.json`  
**ID:** `OIFM_OIDM_338652`  
**Description:** Paget disease involving the skull, producing abnormal bone remodeling with calvarial thickening, expansion, sclerosis, or mixed lytic and sclerotic change.  
**Synonyms:** Paget skull, Paget disease calvarium  
**Change from prior:** unchanged, stable, new, resolved, worsened, improved  
**Source CSV:** `id=HID5450`; `name=paget_disease_of_skull`; `category=osseous`; `parent_id=HID5000`; `synonyms=Paget skull, Paget disease calvarium`; `finding_type=diagnosis`

**Assessment:** Mechanical review flagged capitalized `Paget`; left capitalized as eponym.

**Response:** 

---
