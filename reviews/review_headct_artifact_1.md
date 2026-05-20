# Review: head CT artifact batch 1

7 models/mappings to review. For each, check name, description, synonyms, and direction-of-change values. Add your response below each entry.

---

### artifact

**Source file:** `defs/artifact.fm.json`  
**ID:** `OIFM_OIDM_334144`  
**Description:** An image degradation or misleading image feature caused by acquisition, reconstruction, patient motion, hardware, contrast timing, or other technical factors rather than true anatomy or pathology.  
**Synonyms:** imaging artifact, image artifact  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID9400`; `name=artifact`; `category=artifact`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`

**Assessment:** New parent model for artifact rows; confirm acceptable as a modality-neutral technical/image-quality rollup.

**Response:** 

---

### metallic artifact

**Source file:** `defs/metallic_artifact.fm.json`  
**ID:** `OIFM_OIDM_165814`  
**Description:** Image artifact caused by metal or dense hardware, commonly producing streak, beam-hardening, or photon-starvation effects that obscure adjacent structures.  
**Synonyms:** metal artifact, hardware artifact, beam hardening from metal  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID9405`; `name=metallic_artifact`; `category=artifact`; `parent_id=HID9400`; `synonyms=metal artifact, hardware artifact, beam hardening from metal`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### matched: motion_artifact -> motion artifact

**Source file:** `defs/motion_artifact.fm.json`  
**ID:** `OIFM_OIDM_659997`  
**Description:** Image degradation caused by patient motion during acquisition, often producing blurring, misregistration, or streak-like degradation that can obscure anatomy.  
**Synonyms:** motion blur, patient motion, movement artifact, motion degradation  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID9410`; `name=motion_artifact`; `category=artifact`; `parent_id=HID9400`; `synonyms=movement artifact, patient motion, motion degradation`; `finding_type=observation`

**Assessment:** Existing model reused; description was broadened from radiograph-only wording and CSV synonyms were added.

**Response:** 

---

### beam hardening artifact

**Source file:** `defs/beam_hardening_artifact.fm.json`  
**ID:** `OIFM_OIDM_727869`  
**Description:** CT artifact caused by preferential absorption of lower-energy x-rays, producing streaks or dark bands near dense structures such as bone or metal.  
**Synonyms:** posterior fossa artifact, Hounsfield bar artifact, petrous bone artifact  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID9415`; `name=beam_hardening_artifact`; `category=artifact`; `parent_id=HID9400`; `synonyms=posterior fossa artifact, Hounsfield bar artifact, petrous bone artifact`; `finding_type=observation`

**QUESTION:** Mechanical review flagged `Hounsfield bar artifact` for capitalization; I left it capitalized as an eponym. Confirm acceptable.

**Response:** 

---

### volume averaging artifact

**Source file:** `defs/volume_averaging_artifact.fm.json`  
**ID:** `OIFM_OIDM_671641`  
**Description:** Apparent image finding caused by averaging of tissues with different attenuation within a voxel or slice thickness, rather than a true discrete abnormality.  
**Synonyms:** partial volume effect, partial volume artifact, partial volume averaging  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID9420`; `name=volume_averaging_artifact`; `category=artifact`; `parent_id=HID9400`; `synonyms=partial volume effect, partial volume artifact, partial volume averaging`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### suboptimal contrast timing

**Source file:** `defs/suboptimal_contrast_timing.fm.json`  
**ID:** `OIFM_OIDM_658293`  
**Description:** Non-diagnostic or limited vascular or parenchymal enhancement caused by mistiming of contrast bolus acquisition relative to the intended phase of imaging.  
**Synonyms:** poor bolus timing, suboptimal bolus, mistimed contrast bolus  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID9425`; `name=suboptimal_contrast_timing`; `category=artifact`; `parent_id=HID9400`; `synonyms=poor bolus timing, suboptimal bolus, mistimed contrast bolus`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---

### retained contrast

**Source file:** `defs/retained_contrast.fm.json`  
**ID:** `OIFM_OIDM_945616`  
**Description:** Residual iodinated contrast material visible from prior contrast administration, which may mimic or obscure acute hemorrhage or enhancement on CT.  
**Synonyms:** residual contrast from prior study, contrast staining, retained iodinated contrast  
**Change from prior:** unchanged, stable, new, resolved  
**Source CSV:** `id=HID9430`; `name=retained_contrast`; `category=artifact`; `parent_id=HID9400`; `synonyms=residual contrast from prior study, contrast staining, retained iodinated contrast`; `finding_type=observation`

**Assessment:** Looks reasonable as written; confirm acceptable.

**Response:** 

---
