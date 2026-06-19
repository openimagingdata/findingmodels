# Review: CDEStaging chunk 1

10 entries to review (6 new, 4 existing matches, 0 skipped). For each, check the mapping or new model metadata. Add your response below each entry.

---

### aberrant subclavian artery

**Entry type:** new model  
**Source file:** `defs/from_cdestaging_ct_chest/aberrant_subclavian_artery.fm.json`  
**CDEStaging source:** `aberrant-subclavian-artery.md` (`md`)  
**ID:** `OIFM_MGB_387198`  
**Description:** An anomalous origin and course of the subclavian artery (arteria lusoria) characterized by side of origin, course relative to the trachea and esophagus, and associated complications such as compression, atherosclerosis, or aneurysmal dilation.  
**Synonyms:** arteria lusoria, aberrant subclavian  
**Change from prior:** unchanged, stable, new, resolved  
**Attributes:** 10  
**Anatomic locations:** 0 (or skipped)

**Assessment:** Applied cleanup: removed side-specific subtype synonyms, removed source-carried `aberrant subclavian status` in favor of standard `presence`, and winnowed `change from prior` to minimum values for a congenital variant. Confirm split esophageal/tracheal compression and `bilateral` side value are acceptable.

**Response:** 

---

### acromioclavicular joint degenerative changes

**Entry type:** new model  
**Source file:** `defs/from_cdestaging_ct_chest/acromioclavicular_joint_degenerative_changes.fm.json`  
**CDEStaging source:** `acromioclavicular-joint-degenerative-changes.md` (`md`)  
**ID:** `OIFM_MGB_065473`  
**Description:** Degenerative (osteoarthritic) changes affecting the acromioclavicular (AC) joint, characterized by joint space narrowing, osteophyte formation, subchondral sclerosis or cysts, capsular thickening, and distal clavicle osteolysis.  
**Synonyms:** ac joint degenerative changes, ac joint osteoarthritis, acromioclavicular osteoarthritis, acromioclavicular joint osteoarthritis, osteoarthritis of the acromioclavicular joint, acromioclavicular joint arthrosis, acromioclavicular arthrosis, acromioclavicular joint degeneration, degenerative changes of the acromioclavicular joint  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, worsened, improved  
**Attributes:** 9  
**Anatomic locations:** 0 (or skipped)

**Assessment:** Applied cleanup: removed source-carried `status` in favor of standard `change from prior`, removed `larger/smaller`, added `worsened/improved`, removed broad synonym `ac joint arthritis`, and added stricter AC joint osteoarthritis synonyms. Confirm source component attributes should remain inline.

**Response:** 

---

### adrenal thickening

**Entry type:** new model  
**Source file:** `defs/from_cdestaging_ct_chest/adrenal_thickening.fm.json`  
**CDEStaging source:** `adrenal-thickening.json` (`json`)  
**ID:** `OIFM_MGB_879496`  
**Description:** Diffuse or focal thickening of one or both adrenal glands on imaging, characterized by laterality, degree of thickening, and homogeneity.  
**Synonyms:** adrenal gland thickening, thickened adrenal gland, adrenal limb thickening, thickened adrenal limb  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, worsened, improved  
**Attributes:** 6  
**Anatomic locations:** 0 (or skipped)

**Assessment:** Applied cleanup: added description, synonyms, adrenal tags, CFP grammar fix, and removed `larger/smaller`. Confirm `lymphadenopathy` should remain as an inline associated-finding attribute.

**Response:** 

---

### cardiac annular calcifications

**Entry type:** new model  
**Source file:** `defs/from_cdestaging_ct_chest/annular_calcifications.fm.json`  
**CDEStaging source:** `annular-calcifications.json` (`json`)  
**ID:** `OIFM_MGB_753305`  
**Description:** Calcification involving a cardiac valve annulus, such as the mitral, aortic, tricuspid, or pulmonary valve annulus, as seen on chest CT. Severity and involved annulus may be specified.  
**Synonyms:** annular calcification, cardiac annular calcification, valvular annular calcification, valvular annular calcifications  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased  
**Attributes:** 8  
**Anatomic locations:** 0 (or skipped)

**Assessment:** Applied cleanup: renamed from `annular calcifications` to `cardiac annular calcifications`, added clinical description/synonyms/tags, fixed missing attribute descriptions, and removed `larger/smaller`. Confirm associated findings (`cardiomegaly`, `coronary artery disease`, `left atrial enlargement`, `pulmonary hypertension`) should remain inline rather than consolidated or extracted.

**Response:** 

---

### anterolisthesis

**Entry type:** new model  
**Source file:** `defs/from_cdestaging_ct_chest/anterolisthesis.fm.json`  
**CDEStaging source:** `anterolisthesis.md` (`md`)  
**ID:** `OIFM_MGB_651959`  
**Description:** Anterior displacement of one vertebral body relative to the one below (anterolisthesis). Describes presence, severity/grade, location within the spine, levels involved, and common associated findings such as foraminal narrowing or disc degeneration.  
**Synonyms:** anterior spondylolisthesis, anterolisthesis of spine, anterior vertebral translation, anterior vertebral listhesis, forward vertebral slippage  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, worsened, improved  
**Attributes:** 8  
**Anatomic locations:** 0 (or skipped)

**Assessment:** Applied cleanup: removed source-carried `status` in favor of standard `change from prior`, removed `larger/smaller`, added `worsened/improved`, removed ambiguous synonym `anterior subluxation`, and added stricter vertebral translation synonyms. Confirm `neural foraminal narrowing` and `disc degeneration` should remain inline.

**Response:** 

---

### aortic atherosclerosis

**Entry type:** new model  
**Source file:** `defs/from_cdestaging_ct_chest/aortic_atherosclerosis.fm.json`  
**CDEStaging source:** `aortic-atherosclerosis.json` (`json`)  
**ID:** `OIFM_MGB_988150`  
**Description:** Atherosclerotic plaque or calcification involving the aortic wall, characterized by severity, extent, location, and plaque morphology.  
**Synonyms:** atherosclerosis of the aorta, aortic atheromatous disease, aortic atheroma, aortic atherosclerotic disease  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, worsened, improved  
**Attributes:** 16  
**Anatomic locations:** 0 (or skipped)

**Assessment:** Applied cleanup: added description, synonyms, vascular/aortic tags, CFP grammar fix, removed `larger/smaller`, and added `worsened/improved`. Confirm related present/absent attributes should remain inline; `specific features` may overlap with `plaque characteristics`.

**Response:** 

---

### adrenal nodule (existing match)

**Entry type:** existing match  
**CDEStaging source:** `adrenal-nodule.json` (`json`)  
**Triage decision:** `exact_match`  
**Search targets:** `adrenal nodule`, `nodule`  
**Matched ID:** `OIFM_CDE_000003`  
**Matched name:** Adrenal Nodule  
**Matched model file:** (not in local defs)  
**Description:** Detection and characterization of an adrenal nodule.  
**Synonyms:** (none)  
**Change from prior:** (see matched model)

**Assessment:** DuckDB triage linked this CDEStaging source to an existing model; confirm the mapping is correct (no new model was created).

**Response:** 

---

### airway mucus plugging (existing match)

**Entry type:** existing match  
**CDEStaging source:** `airway-mucus-plugging.json` (`json`)  
**Triage decision:** `exact_match`  
**Search targets:** `airway mucus plugging`, `plugging`  
**Matched ID:** `OIFM_GMTS_015330`  
**Matched name:** mucoid impaction  
**Matched model file:** (not in local defs)  
**Description:** Plugging of bronchi with thick mucus, resulting in branching opacities.  
**Synonyms:** (none)  
**Change from prior:** (see matched model)

**Assessment:** DuckDB triage linked this CDEStaging source to an existing model; confirm the mapping is correct (no new model was created).

**Response:** 

---

### aortic dissection (existing match)

**Entry type:** existing match  
**CDEStaging source:** `aortic-dissection.md` (`md`)  
**Triage decision:** `exact_match`  
**Search targets:** `aortic dissection`, `dissection`  
**Matched ID:** `OIFM_MSFT_573630`  
**Matched name:** aortic dissection  
**Matched model file:** (not in local defs)  
**Description:** Aortic dissection is a critical condition characterized by the separation of the aortic wall layers due to an intimal tear, resulting in an intramural hematoma and potential rupture; it often presents with severe, acute chest or back pain and may lead to life-threatening complications.  
**Synonyms:** (none)  
**Change from prior:** (see matched model)

**Assessment:** DuckDB triage linked this CDEStaging source to an existing model; confirm the mapping is correct (no new model was created).

**Response:** 

---

### aortic measurements (existing match)

**Entry type:** existing match  
**CDEStaging source:** `aortic-measurements.json` (`json`)  
**Triage decision:** `exact_match`  
**Search targets:** `aortic measurements`, `measurements`  
**Matched ID:** `OIFM_CDE_000264`  
**Matched name:** Aortic Measurements  
**Matched model file:** (not in local defs)  
**Description:** Aortic Measurements  
**Synonyms:** (none)  
**Change from prior:** (see matched model)

**Assessment:** DuckDB triage linked this CDEStaging source to an existing model; confirm the mapping is correct (no new model was created).

**Response:** 
