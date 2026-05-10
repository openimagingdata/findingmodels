# Review: headct_ventricular (batch 3)

8 models to review. For each, check name, description, synonyms, and direction-of-change values. Add your response below each entry.

---

### ventricular abnormality

**Source file:** `defs/ventricular_abnormality.fm.json`  
**ID:** `OIFM_OIDM_246130`  
**Description:** Any deviation from normal appearance of the cerebral ventricles on head CT.  
**Synonyms:** (none)  
**Change from prior:** `unchanged`, `stable`, `new`, `resolved`

**CSV source:** id=HID3600, category=ventricular, parent_id=, finding_type=

**Assessment:** New model created from CSV. Please confirm name, description, and synonyms are appropriate.

**Response:** ok with description tweak: rewrite "Any deviation from normal appearance of the cerebral ventricles on head CT." → "Any deviation from normal appearance of the cerebral ventricles." this catch-all is shared between CT and MRI.

---

### ventricular anatomic variant

**Source file:** `defs/ventricular_anatomic_variant.fm.json`  
**ID:** `OIFM_OIDM_521516`  
**Description:** A normal developmental variant in the configuration or contents of the cerebral ventricles.  
**Synonyms:** (none)  
**Change from prior:** `unchanged`, `stable`, `new`, `resolved`

**CSV source:** id=HID4000, category=ventricular, parent_id=, finding_type=

**Assessment:** New model created from CSV. Please confirm name, description, and synonyms are appropriate.

**Response:** ok

---

### ventricular entrapment

**Source file:** `defs/ventricular_entrapment.fm.json`  
**ID:** `OIFM_OIDM_636011`  
**Description:** An isolated ventricle that is obstructed and no longer communicates freely with the remainder of the ventricular system.  
**Synonyms:** `trapped ventricle`, `isolated ventricle`  
**Change from prior:** `unchanged`, `stable`, `new`, `resolved`

**CSV source:** id=HID3700, category=ventricular, parent_id=HID3600, finding_type=observation
**CSV synonyms:** trapped ventricle, isolated ventricle

**Assessment:** New model created from CSV. Please confirm name, description, and synonyms are appropriate.

**Response:** ok

---

### ventricular horn hypoplasia

**Source file:** `defs/ventricular_horn_hypoplasia.fm.json`  
**ID:** `OIFM_OIDM_391545`  
**Description:** Underdeveloped or rudimentary cerebral ventricular horns.  
**Synonyms:** `rudimentary ventricular horn`, `rudimentary temporal horn`, `rudimentary occipital horn`, `underdeveloped ventricular horn`  
**Change from prior:** `unchanged`, `stable`, `new`, `resolved`

**CSV source:** id=HID3670, category=ventricular, parent_id=HID3600, finding_type=observation
**CSV synonyms:** rudimentary ventricular horn, rudimentary temporal horn, rudimentary occipital horn, underdeveloped ventricular horn

**Assessment:** New model created from CSV. Please confirm name, description, and synonyms are appropriate.

**Response:** drop `rudimentary temporal horn` and `rudimentary occipital horn` — site-specific synonyms embedding the specific horn; which horn should be post-coordinated as anatomic_site. keep `rudimentary ventricular horn` and `underdeveloped ventricular horn`.

---

### ventricular postsurgical change

**Source file:** `defs/ventricular_postsurgical_change.fm.json`  
**ID:** `OIFM_OIDM_994657`  
**Description:** Changes in the ventricular system related to prior neurosurgical intervention.  
**Synonyms:** (none)  
**Change from prior:** `unchanged`, `stable`, `new`, `resolved`

**CSV source:** id=HID4200, category=ventricular, parent_id=, finding_type=

**Assessment:** New model created from CSV. Please confirm name, description, and synonyms are appropriate.

**Response:** ok

---

### ventriculitis

**Source file:** `defs/ventriculitis.fm.json`  
**ID:** `OIFM_OIDM_279735`  
**Description:** Inflammation or infection of the ventricular ependymal lining.  
**Synonyms:** `pyocephalus`, `ventricular infection`, `ependymitis`  
**Change from prior:** `unchanged`, `stable`, `new`, `resolved`, `worsened`, `improved`

**CSV source:** id=HID3825, category=ventricular, parent_id=HID3600, finding_type=diagnosis
**CSV synonyms:** pyocephalus, ventricular infection, ependymitis

**Assessment:** New model created from CSV. Please confirm name, description, and synonyms are appropriate.

**Response:** drop `ventricular infection` — cross-body collision with cardiac. keep `pyocephalus` and `ependymitis`.

---

### ventriculomegaly

**Source file:** `defs/ventriculomegaly.fm.json`  
**ID:** `OIFM_OIDM_425021`  
**Description:** Enlargement of the cerebral ventricles beyond normal caliber.  
**Synonyms:** `enlarged ventricles`, `dilated ventricles`  
**Change from prior:** `unchanged`, `stable`, `new`, `resolved`, `larger`, `smaller`

**CSV source:** id=HID3650, category=ventricular, parent_id=HID3600, finding_type=observation
**CSV synonyms:** enlarged ventricles, dilated ventricles

**Assessment:** New model created from CSV. Please confirm name, description, and synonyms are appropriate.

**Response:** ok

---

### ventriculostomy

**Source file:** `defs/ventriculostomy.fm.json`  
**ID:** `OIFM_OIDM_361419`  
**Description:** An external ventricular drain placed into the cerebral ventricles for CSF diversion or pressure monitoring.  
**Synonyms:** `EVD`, `external ventricular drain`, `shunted ventricles`  
**Change from prior:** `unchanged`, `stable`, `new`, `resolved`

**CSV source:** id=HID4205, category=ventricular, parent_id=HID4200, finding_type=observation
**CSV synonyms:** EVD, external ventricular drain, shunted ventricles

**Assessment:** New model created from CSV. Please confirm name, description, and synonyms are appropriate.
**NOTE:** Capitalized acronyms as synonyms: `EVD` — verify these are standard abbreviations.

**Response:** rename canonical `ventriculostomy` → `external_ventricular_drain`. EVD is the entity actually being described; ventriculostomy is a broader procedure term that also covers endoscopic third ventriculostomy (a completely different operation — fenestration of third ventricle floor, not external drainage).

after rename:
- keep `EVD` and `ventriculostomy` as synonyms (abbreviation and colloquial equivalent)
- drop `external ventricular drain` from synonyms (now the canonical name)
- drop `shunted ventricles` — wrong entity; refers to permanent VP/VA shunts, not external drains.
- recommend `endoscopic_third_ventriculostomy` as a separate sibling entry if needed for extraction.

---
