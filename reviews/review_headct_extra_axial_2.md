# Review: head CT extra axial batch 2

9 models/mappings to review. For each, check name, description, synonyms, and direction-of-change values. Add your response below each entry.

---

### intracranial dermoid cyst

**Source file:** `defs/intracranial_dermoid_cyst.fm.json`  
**ID:** `OIFM_OIDM_576584`  
**Description:** A congenital extra-axial inclusion cyst containing dermal elements and lipid-rich material, often located near the midline and potentially associated with fat droplets if ruptured.  
**Synonyms:** intracranial dermoid, dermoid tumor  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller  
**Source CSV:** `id=HID2715`; `name=dermoid_cyst`; `category=extra_axial`; `parent_id=HID2700`; `synonyms=intracranial dermoid, dermoid tumor`; `finding_type=diagnosis`

**Assessment:** Created scoped intracranial model instead of reusing broad CDE `Dermoid Cyst`; confirm acceptable.

**Response:** 

---

### intracranial lipoma

**Source file:** `defs/intracranial_lipoma.fm.json`  
**ID:** `OIFM_OIDM_078516`  
**Description:** A congenital fat-containing intracranial lesion, usually extra-axial and often located along midline cisternal or pericallosal regions.  
**Synonyms:** meningeal lipoma, lipomatous hamartoma  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller  
**Source CSV:** `id=HID2720`; `name=intracranial_lipoma`; `category=extra_axial`; `parent_id=HID2600`; `synonyms=meningeal lipoma, lipomatous hamartoma`; `finding_type=diagnosis`

**Assessment:** Created scoped intracranial model instead of reusing broad `Lipoma`; confirm acceptable.

**Response:** 

---

### matched: intracranial_fat -> intracranial fat

**Source file:** `defs/intracranial_fat.fm.json`  
**ID:** `OIFM_GMTS_007500`  
**Description:** Presence of fat tissue within the cranial vault.  
**Synonyms:** fat in brain, cranial fat, macroscopic intracranial fat, macroscopic midline fat, extra-axial fat, fat density intracranial  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller  
**Source CSV:** `id=HID2725`; `name=intracranial_fat`; `category=extra_axial`; `parent_id=HID2600`; `synonyms=macroscopic intracranial fat, macroscopic midline fat, extra-axial fat, fat density intracranial`; `finding_type=observation`

**Assessment:** Existing GMTS model reused; CSV synonyms were added and pre-existing synonym capitalization was normalized.

**Response:** 

---

### matched: extra_axial_lesion -> extra-axial lesion

**Source file:** `defs/extra_axial_lesion.fm.json`  
**ID:** `OIFM_GMTS_007296`  
**Description:** A lesion located outside the brain parenchyma  
**Synonyms:** extracerebral lesion, extra-axial mass  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller  
**Source CSV:** `id=HID2750`; `name=extra_axial_lesion`; `category=extra_axial`; `parent_id=HID2600`; `synonyms=extra-axial mass, extra-axial lesion`; `finding_type=observation`

**QUESTION:** Existing GMTS model reused and `extra-axial mass` was added as a synonym. Confirm broad lesion/mass mapping.

**Response:** 

---

### dural-based lesion

**Source file:** `defs/dural_based_lesion.fm.json`  
**ID:** `OIFM_OIDM_390171`  
**Description:** A focal lesion or mass with broad contact with the dura, suggesting dural origin or dural attachment on imaging.  
**Synonyms:** dural-based mass, dural mass  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller  
**Source CSV:** `id=HID2755`; `name=dural_based_lesion`; `category=extra_axial`; `parent_id=HID2750`; `synonyms=dural-based mass, dural mass`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### matched: cerebellopontine_angle_lesion -> cerebellopontine angle lesion

**Source file:** `defs/cerebellopontine_angle_lesion.fm.json`  
**ID:** `OIFM_GMTS_007408`  
**Description:** Abnormal area or mass located at the cerebellopontine angle.  
**Synonyms:** CPA lesion, CPA mass  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller  
**Source CSV:** `id=HID2760`; `name=cerebellopontine_angle_lesion`; `category=extra_axial`; `parent_id=HID2750`; `synonyms=CPA lesion, CPA mass`; `finding_type=observation`

**QUESTION:** Existing GMTS model reused and CSV synonyms were added. Mechanical review flagged capitalized `CPA`; I left it capitalized as a standard acronym. Confirm acceptable.

**Response:** 

---

### dural thickening

**Source file:** `defs/dural_thickening.fm.json`  
**ID:** `OIFM_OIDM_690677`  
**Description:** Abnormal thickening of the dura mater on imaging, which may be focal or diffuse and may reflect inflammatory, neoplastic, postoperative, traumatic, or other causes.  
**Synonyms:** pachymeningeal thickening  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased  
**Source CSV:** `id=HID2765`; `name=dural_thickening`; `category=extra_axial`; `parent_id=HID2600`; `synonyms=pachymeningeal thickening`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### matched: dural_enhancement -> pachymeningeal enhancement

**Source file:** `defs/pachymeningeal_enhancement.fm.json`  
**ID:** `OIFM_GMTS_018361`  
**Description:** Contrast enhancement of the dura mater.  
**Synonyms:** dural enhancement, dural contrast uptake  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller  
**Source CSV:** `id=HID2770`; `name=dural_enhancement`; `category=extra_axial`; `parent_id=HID2600`; `synonyms=pachymeningeal enhancement, dural contrast uptake`; `finding_type=observation`

**QUESTION:** Mapped to existing `pachymeningeal enhancement`; CSV terms were added as synonyms. Confirm dural enhancement should not be a separate model.

**Response:** 

---

### leptomeningeal enhancement

**Source file:** `defs/leptomeningeal_enhancement.fm.json`  
**ID:** `OIFM_OIDM_121473`  
**Description:** Abnormal contrast enhancement along the pia and arachnoid surfaces or within the subarachnoid spaces, suggesting inflammatory, infectious, neoplastic, or vascular meningeal involvement.  
**Synonyms:** pial enhancement, pia-arachnoid enhancement  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased  
**Source CSV:** `id=HID2775`; `name=leptomeningeal_enhancement`; `category=extra_axial`; `parent_id=HID2600`; `synonyms=pial enhancement, pia-arachnoid enhancement`; `finding_type=observation`

**Assessment:** Created generic model rather than reusing existing diffuse/focal variants; confirm acceptable.

**Response:** 

---
