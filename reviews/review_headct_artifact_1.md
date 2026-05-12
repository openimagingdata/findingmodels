# Review: head CT artifact batch 1

7 artifact CSV decisions to review. This category does not appear to have a prior batch review file: no `review_headct_artifact*.md` file was present. No category-specific artifact batch history was found.

This is a triage handoff, not a finalized model-creation batch. Entries marked **new model candidate** or **question** need reviewer direction before model creation.

---

### new model candidate: artifact

**Source CSV:** `id=HID9400`; `name=artifact`; `category=artifact`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`

**Assessment:** No direct broad artifact model found. Existing artifact models are specific types such as `motion artifact` and `grid artifact`.

**Response:**

---

### new model candidate: metallic_artifact

**Source CSV:** `id=HID9405`; `name=metallic_artifact`; `category=artifact`; `parent_id=HID9400`; `synonyms=metal artifact, hardware artifact, beam hardening from metal`; `finding_type=observation`

**Assessment:** No direct model found. Related to beam-hardening artifact, but specifically due to metal/hardware.

**Response:**

---

### matched: motion_artifact -> motion artifact

**Source file:** `defs/motion_artifact.fm.json`  
**ID:** `OIFM_OIDM_659997`  
**Description:** Blurring of the radiograph due to patient movement during exposure.  
**Synonyms:** motion blur, patient motion

**Source CSV:** `id=HID9410`; `name=motion_artifact`; `category=artifact`; `parent_id=HID9400`; `synonyms=movement artifact, patient motion, motion degradation`; `finding_type=observation`

**Assessment:** Direct name match. Reviewer should decide whether to add CSV synonyms `movement artifact` and `motion degradation`. Note that the current description says radiograph/XR, while this CSV category is head CT.

**Response:**

---

### new model candidate: beam_hardening_artifact

**Source CSV:** `id=HID9415`; `name=beam_hardening_artifact`; `category=artifact`; `parent_id=HID9400`; `synonyms=posterior fossa artifact, Hounsfield bar artifact, petrous bone artifact`; `finding_type=observation`

**Assessment:** No direct model found. This is common in head CT, especially near dense skull base/petrous bone.

**Response:**

---

### new model candidate: volume_averaging_artifact

**Source CSV:** `id=HID9420`; `name=volume_averaging_artifact`; `category=artifact`; `parent_id=HID9400`; `synonyms=partial volume effect, partial volume artifact, partial volume averaging`; `finding_type=observation`

**Assessment:** No direct model found.

**Response:**

---

### new model candidate: suboptimal_contrast_timing

**Source CSV:** `id=HID9425`; `name=suboptimal_contrast_timing`; `category=artifact`; `parent_id=HID9400`; `synonyms=poor bolus timing, suboptimal bolus, mistimed contrast bolus`; `finding_type=observation`

**Assessment:** No direct model found. Reviewer should decide whether this belongs under artifact/technique or a contrast-administration/vascular-opacification category.

**Response:**

---

### new model candidate: retained_contrast

**Source CSV:** `id=HID9430`; `name=retained_contrast`; `category=artifact`; `parent_id=HID9400`; `synonyms=residual contrast from prior study, contrast staining, retained iodinated contrast`; `finding_type=observation`

**Assessment:** No direct model found. Reviewer should decide whether `contrast staining` is equivalent enough to retained contrast from a prior study or should be treated separately.

**Response:**

---
