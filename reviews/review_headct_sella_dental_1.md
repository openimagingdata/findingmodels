# Review: head CT sella and dental batch

32 CSV decisions to review: 27 newly created OIDM models and 5 mappings to existing models. For each, check name, description, synonyms, direction-of-change values, and whether the CSV row should map to the listed OIFM ID. Add your response below each entry.

---

### sellar abnormality

**Source file:** `defs/sellar_abnormality.fm.json`  
**ID:** `OIFM_OIDM_551013`  
**Description:** A nonspecific abnormality involving the sella turcica or pituitary fossa on imaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID2200`; `name=sellar_abnormality`; `category=sella_turcica`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`

**Assessment:** Newly created broad parent model. Confirm acceptable.

**Response:** ok

---

### matched: sellar_mass -> Sella Mass

**Source file:** `defs/sella_mass.fm.json`  
**ID:** `OIFM_CDE_000277`  
**Description:** Sellar Mass  
**Synonyms:** (none)  
**Change from prior:** (none found)

**Source CSV:** `id=HID2250`; `name=sellar_mass`; `category=sella_turcica`; `parent_id=HID2200`; `synonyms=suprasellar mass, intrasellar mass, sellar and suprasellar mass`; `finding_type=(blank)`

**QUESTION:** Existing CDE model appears to match the CSV concept, but has legacy casing and sparse metadata. Confirm mapping as-is, or request cleanup/renaming toward CSV terminology.

**Response:** mapping ok. rename `Sella Mass` → `sellar mass` (CSV form, standard adjectival phrasing); missing change from prior is separate metadata cleanup. don't add CSV synonyms `suprasellar mass` or `intrasellar mass` — site-specific anatomy that should be post-coordinated or listed as new terms. don't add `sellar and suprasellar mass`.

---

### pituitary adenoma

**Source file:** `defs/pituitary_adenoma.fm.json`  
**ID:** `OIFM_OIDM_685143`  
**Description:** A benign pituitary neuroendocrine tumor arising from the adenohypophysis, which may be seen on CT as a sellar or sellar-suprasellar mass.  
**Synonyms:** pituitary tumor  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID2300`; `name=pituitary_adenoma`; `category=sella_turcica`; `parent_id=HID2250`; `synonyms=pituitary tumor`; `finding_type=diagnosis`

**Assessment:** Newly created model. Confirm acceptable.

**Response:** drop `pituitary tumor` — too broad; encompasses pituitary carcinoma, metastases, and other sellar neoplasms. leave synonyms blank.

---

### pituitary macroadenoma

**Source file:** `defs/pituitary_macroadenoma.fm.json`  
**ID:** `OIFM_OIDM_913617`  
**Description:** A pituitary adenoma measuring at least 10 mm, typically presenting as an enlarged sellar mass that may extend into the suprasellar cistern or cavernous sinus.  
**Synonyms:** macroadenoma  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID2305`; `name=pituitary_macroadenoma`; `category=sella_turcica`; `parent_id=HID2300`; `synonyms=macroadenoma`; `finding_type=diagnosis`

**Assessment:** Newly created subtype model. Confirm that separate model is preferred over only modeling this as adenoma size/type.

**Response:** keep as separate subtype. macroadenoma is hard-thresholded at 10 mm with distinct management (surgical vs medical) and is heavily lexicalized — parallels compression fracture and lacunar infarct as origin-defining subtypes. recommend a sibling `pituitary microadenoma` child if not already present, since the pair is how the entity is named in practice.

---

### matched: expanded_sella -> sella turcica enlargement

**Source file:** `defs/sella_turcica_enlargement.fm.json`  
**ID:** `OIFM_GMTS_025584`  
**Description:** Increased size of the sella turcica, the bony cavity in the skull.  
**Synonyms:** enlarged sella turcica, expanded sella, expanded sella turcica, enlarged sella, sella enlargement, enlarged pituitary fossa, expanded pituitary fossa, ballooned sella, large sella turcica  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID2310`; `name=expanded_sella`; `category=sella_turcica`; `parent_id=HID2200`; `synonyms=enlarged sella, expanded sella turcica, sella enlargement, enlarged pituitary fossa, expanded pituitary fossa, ballooned sella`; `finding_type=observation`

**QUESTION:** Existing match is GAMUTS-derived. Because CSV terminology is preferred, confirm whether to map as-is, rename/normalize the model toward `expanded sella`, or create a new OIDM model.

**Response:** ok — rename was already done in headcts batch 2 (`large_sella_turcica` → `sella_turcica_enlargement`) and CSV synonyms are already in the list. map as-is.

---

### sellar calcification

**Source file:** `defs/sellar_calcification.fm.json`  
**ID:** `OIFM_OIDM_282360`  
**Description:** Calcification localized to the sellar or pituitary fossa region on CT.  
**Synonyms:** calcification in sella, sellar region calcification  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID2315`; `name=sellar_calcification`; `category=sella_turcica`; `parent_id=HID2200`; `synonyms=calcification in sella, sellar region calcification`; `finding_type=observation`

**Assessment:** Newly created model using CSV terminology. Confirm acceptable.

**Response:** ok

---

### empty sella

**Source file:** `defs/empty_sella.fm.json`  
**ID:** `OIFM_OIDM_132795`  
**Description:** CSF filling and expansion of the sella with flattening or nonvisualization of the pituitary gland, often seen as an incidental sellar finding on CT or MRI.  
**Synonyms:** empty pituitary fossa, CSF-filled sella  
**Change from prior:** unchanged, stable, new, resolved

**Source CSV:** `id=HID2350`; `name=empty_sella`; `category=sella_turcica`; `parent_id=HID2200`; `synonyms=empty pituitary fossa, CSF-filled sella`; `finding_type=diagnosis`

**Assessment:** Mechanical review noted uppercase `CSF`; this is an acronym and appears justified. Confirm acceptable.

**Response:** ok

---

### partially empty sella

**Source file:** `defs/partially_empty_sella.fm.json`  
**ID:** `OIFM_OIDM_158013`  
**Description:** Partial CSF filling of the sella with residual visible pituitary tissue, representing an incomplete form of empty sella.  
**Synonyms:** partial empty sella  
**Change from prior:** unchanged, stable, new, resolved

**Source CSV:** `id=HID2355`; `name=partially_empty_sella`; `category=sella_turcica`; `parent_id=HID2350`; `synonyms=partial empty sella`; `finding_type=diagnosis`

**Assessment:** Newly created model. Confirm acceptable.

**Response:** ok — lexicalized variant with distinct imaging pattern, parallels the macroadenoma/microadenoma case.

---

### pituitary hemorrhage

**Source file:** `defs/pituitary_hemorrhage.fm.json`  
**ID:** `OIFM_OIDM_653005`  
**Description:** Hemorrhage within the pituitary gland or sellar region, typically appearing as hyperattenuating sellar material on CT in the appropriate clinical setting.  
**Synonyms:** sellar hemorrhage  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID2360`; `name=pituitary_hemorrhage`; `category=sella_turcica`; `parent_id=HID2200`; `synonyms=sellar hemorrhage`; `finding_type=diagnosis`

**Assessment:** Newly created model. Confirm acceptable.

**Response:** ok

---

### pituitary apoplexy

**Source file:** `defs/pituitary_apoplexy.fm.json`  
**ID:** `OIFM_OIDM_123605`  
**Description:** Acute hemorrhage or infarction of the pituitary gland, often involving a pituitary adenoma and potentially presenting with sudden headache, visual symptoms, or endocrine dysfunction.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, worsened, improved

**Source CSV:** `id=HID2365`; `name=pituitary_apoplexy`; `category=sella_turcica`; `parent_id=HID2200`; `synonyms=(blank)`; `finding_type=diagnosis`

**Assessment:** Newly created diagnosis model. Confirm acceptable.

**Response:** ok

---

### craniopharyngioma

**Source file:** `defs/craniopharyngioma.fm.json`  
**ID:** `OIFM_OIDM_735880`  
**Description:** A benign epithelial tumor of the sellar or suprasellar region that may contain cystic components, calcification, or solid enhancing tissue on imaging.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID2370`; `name=craniopharyngioma`; `category=sella_turcica`; `parent_id=HID2200`; `synonyms=(blank)`; `finding_type=diagnosis`

**Assessment:** Newly created model. Confirm acceptable.

**Response:** ok

---

### rathke cleft cyst

**Source file:** `defs/rathke_cleft_cyst.fm.json`  
**ID:** `OIFM_OIDM_579714`  
**Description:** A benign cystic lesion arising from remnants of Rathke pouch, typically located in the sellar or suprasellar region.  
**Synonyms:** Rathke pouch cyst  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID2375`; `name=rathke_cleft_cyst`; `category=sella_turcica`; `parent_id=HID2200`; `synonyms=Rathke pouch cyst`; `finding_type=diagnosis`

**Assessment:** Mechanical review noted uppercase `Rathke`; this is a proper name and appears justified. Confirm acceptable.

**Response:** ok

---

### sellar postsurgical change

**Source file:** `defs/sellar_postsurgical_change.fm.json`  
**ID:** `OIFM_OIDM_179792`  
**Description:** Postoperative change involving the sella or pituitary fossa, usually after pituitary or skull base surgery.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved

**Source CSV:** `id=HID2400`; `name=sellar_postsurgical_change`; `category=sella_turcica`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`

**Assessment:** Newly created broad parent model. Confirm acceptable.

**Response:** ok

---

### transsphenoidal surgery

**Source file:** `defs/transsphenoidal_surgery.fm.json`  
**ID:** `OIFM_OIDM_634599`  
**Description:** Postsurgical changes related to a transsphenoidal or endonasal approach to the sella, commonly performed for pituitary or sellar lesions.  
**Synonyms:** post transsphenoidal resection, transsphenoidal approach changes, endoscopic endonasal surgery, endoscopic transsphenoidal surgery  
**Change from prior:** unchanged, stable, new, resolved

**Source CSV:** `id=HID2405`; `name=transsphenoidal_surgery`; `category=sella_turcica`; `parent_id=HID2400`; `synonyms=post transsphenoidal resection, transsphenoidal approach changes, endoscopic endonasal surgery, endoscopic transsphenoidal surgery`; `finding_type=observation`

**Assessment:** Newly created postsurgical model. Confirm acceptable.

**Response:** drop `endoscopic endonasal surgery` — too broad; the endonasal endoscopic approach is also used for sinus disease and non-sellar skull base targets. keep `endoscopic transsphenoidal surgery` (correctly scoped).

---

### dental abnormality

**Source file:** `defs/dental_abnormality.fm.json`  
**ID:** `OIFM_OIDM_322883`  
**Description:** A nonspecific abnormality involving the teeth or supporting dental structures visible on head CT.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID6000`; `name=dental_abnormality`; `category=dental`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`

**Assessment:** Newly created broad parent model. Confirm acceptable.

**Response:** ok

---

### matched: periapical_lucency -> periapical radiolucency in jaw

**Source file:** `defs/periapical_radiolucency_in_jaw.fm.json`  
**ID:** `OIFM_GMTS_008918`  
**Description:** Area of increased radiolucency near the apex of a tooth root.  
**Synonyms:** periapical lucency  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID6005`; `name=periapical_lucency`; `category=dental`; `parent_id=HID6000`; `synonyms=periapical radiolucency`; `finding_type=observation`

**QUESTION:** Existing match is GAMUTS-derived. Because CSV terminology is preferred, confirm whether to map as-is, rename/normalize toward `periapical lucency`, or create a new OIDM model.

**Response:** rename `periapical radiolucency in jaw` → `periapical lucency`. current GAMUTS name embeds anatomy that's already implied by `periapical` and isn't standard radiology phrasing — same pattern as `large_sella_turcica` → `sella_turcica_enlargement`. add `periapical radiolucency` as a synonym.

---

### dental caries

**Source file:** `defs/dental_caries.fm.json`  
**ID:** `OIFM_OIDM_547581`  
**Description:** Decay or demineralization of a tooth, often visible on CT as a focal defect or lucency in the dental crown or root.  
**Synonyms:** tooth decay, carious tooth, cavitated tooth  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, worsened, improved

**Source CSV:** `id=HID6010`; `name=dental_caries`; `category=dental`; `parent_id=HID6000`; `synonyms=tooth decay, carious tooth, cavitated tooth`; `finding_type=observation`

**Assessment:** Newly created model. Confirm acceptable.

**Response:** ok

---

### impacted tooth

**Source file:** `defs/impacted_tooth.fm.json`  
**ID:** `OIFM_OIDM_103644`  
**Description:** A tooth that has failed to erupt normally and remains partially or completely embedded within bone or soft tissue.  
**Synonyms:** unerupted tooth, embedded tooth, impacted molar  
**Change from prior:** unchanged, stable, new, resolved

**Source CSV:** `id=HID6015`; `name=impacted_tooth`; `category=dental`; `parent_id=HID6000`; `synonyms=unerupted tooth, embedded tooth, impacted molar`; `finding_type=observation`

**Assessment:** Newly created model. Confirm acceptable.

**Response:** drop `impacted molar` — site-specific subtype; which tooth is impacted should be post-coordinated as anatomic site rather than baked into a synonym. keep `unerupted tooth` and `embedded tooth`.

---

### retained root

**Source file:** `defs/retained_root.fm.json`  
**ID:** `OIFM_OIDM_213400`  
**Description:** Residual tooth root material remaining in the alveolar ridge after loss, fracture, or extraction of the tooth crown.  
**Synonyms:** retained root fragment, residual root, root remnant  
**Change from prior:** unchanged, stable, new, resolved

**Source CSV:** `id=HID6020`; `name=retained_root`; `category=dental`; `parent_id=HID6000`; `synonyms=retained root fragment, residual root, root remnant`; `finding_type=observation`

**Assessment:** Newly created model. Confirm acceptable.

**Response:** ok

---

### missing tooth

**Source file:** `defs/missing_tooth.fm.json`  
**ID:** `OIFM_OIDM_562532`  
**Description:** Absence of one or more expected teeth, whether congenital, postsurgical, traumatic, or acquired from dental disease.  
**Synonyms:** absent tooth, missing teeth, edentulous, partially edentulous  
**Change from prior:** unchanged, stable, new, resolved

**Source CSV:** `id=HID6025`; `name=missing_tooth`; `category=dental`; `parent_id=HID6000`; `synonyms=absent tooth, missing teeth, edentulous, partially edentulous`; `finding_type=observation`

**Assessment:** Newly created using CSV terminology instead of GAMUTS `anodontia or hypodontia`, since the CSV term is broader/report-oriented. Confirm acceptable.

**Response:** drop `edentulous` and `partially edentulous` — not equivalents; they refer to specific patterns (complete vs partial loss of all teeth) and should be a separate sibling diagnosis model `edentulism` if needed. keep `absent tooth` and `missing teeth` (just plural form).

---

### periodontal bone loss

**Source file:** `defs/periodontal_bone_loss.fm.json`  
**ID:** `OIFM_OIDM_372815`  
**Description:** Loss or resorption of alveolar bone supporting the teeth, typically related to periodontal disease.  
**Synonyms:** alveolar bone loss, alveolar bone resorption  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, worsened, improved

**Source CSV:** `id=HID6030`; `name=periodontal_bone_loss`; `category=dental`; `parent_id=HID6000`; `synonyms=alveolar bone loss, alveolar bone resorption`; `finding_type=observation`

**Assessment:** Newly created model. Confirm acceptable.

**Response:** ok

---

### matched: apical_periodontitis -> apical periodontitis

**Source file:** `defs/apical_periodontitis.fm.json`  
**ID:** `OIFM_OIDM_248519`  
**Description:** Inflammation or infection of the periapical tissues at the root of a tooth, typically secondary to pulpal necrosis. On head CT, seen as a periapical lucency at the tooth root, sometimes with surrounding sclerosis or an adjacent abscess collection and soft-tissue swelling.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, worsened, improved

**Source CSV:** `id=HID6035`; `name=apical_periodontitis`; `category=dental`; `parent_id=HID6000`; `synonyms=periapical infection, dental infection, dentoalveolar infection, dental abscess, dentoalveolar abscess`; `finding_type=diagnosis`

**QUESTION:** Existing OIDM model matches. Confirm mapping and whether any CSV synonyms should be added later; some may be broader than apical periodontitis.

**Response:** mapping ok. on face/head CT there is an imaging distinction we should preserve: apical periodontitis = periapical lucency at the root apex without soft-tissue component, whereas periapical abscess = the same lucency plus cortical disruption, adjacent soft-tissue swelling, and sometimes a rim-enhancing fluid collection.

recommend splitting:
- create a child diagnosis model `periapical abscess` for the acute suppurative form, with synonyms `dentoalveolar abscess`, `acute apical abscess`, `periapical infection`. `dental abscess` is colloquially the same in radiology reports
- tighten the existing apical_periodontitis description to remove "adjacent abscess collection"
- drop `dental infection` and `dentoalveolar infection` — both umbrella terms that encompass pulpitis, periodontitis, pericoronitis, osteomyelitis, and dental-source cellulitis.

---

### matched: dentigerous_cyst -> dentigerous cyst

**Source file:** `defs/dentigerous_cyst.fm.json`  
**ID:** `OIFM_OIDM_217343`  
**Description:** Odontogenic cyst appearing as a well-circumscribed unilocular lucency surrounding the crown of an unerupted or impacted tooth, most commonly a mandibular third molar, with attachment at the cementoenamel junction.  
**Synonyms:** pericoronal cyst  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID6040`; `name=dentigerous_cyst`; `category=dental`; `parent_id=HID6000`; `synonyms=follicular cyst`; `finding_type=diagnosis`

**QUESTION:** Existing OIDM model matches, but CSV synonym `follicular cyst` is potentially ambiguous across body regions. Confirm mapping as-is and whether to leave `follicular cyst` out.

**Response:** mapping ok; leave `follicular cyst` out — collides with ovarian follicular cyst (already adjudicated in headcts batch 1).

---

### periodontitis

**Source file:** `defs/periodontitis.fm.json`  
**ID:** `OIFM_OIDM_263308`  
**Description:** Inflammatory disease of the periodontal tissues that can produce alveolar bone loss, periodontal ligament widening, or other dental supporting-structure changes on imaging.  
**Synonyms:** periodontal disease, chronic periodontitis  
**Change from prior:** unchanged, stable, new, resolved, worsened, improved

**Source CSV:** `id=HID6045`; `name=periodontitis`; `category=dental`; `parent_id=HID6000`; `synonyms=periodontal disease, chronic periodontitis`; `finding_type=diagnosis`

**Assessment:** Newly created model. Confirm acceptable.

**Response:** drop `chronic periodontitis` — chronicity is an attribute, not part of the entity. keep `periodontal disease`.

---

### oroantral fistula

**Source file:** `defs/oroantral_fistula.fm.json`  
**ID:** `OIFM_OIDM_089707`  
**Description:** An epithelialized abnormal communication between the oral cavity and maxillary sinus, often related to dental extraction, infection, trauma, or surgery.  
**Synonyms:** OAF, oro-antral fistula, odontogenic sinus fistula, dental-sinus fistula  
**Change from prior:** unchanged, stable, new, resolved

**Source CSV:** `id=HID6050`; `name=oroantral_fistula`; `category=dental`; `parent_id=HID6000`; `synonyms=OAF, oro-antral fistula, odontogenic sinus fistula, dental-sinus fistula`; `finding_type=diagnosis`

**Assessment:** Mechanical review noted uppercase `OAF`; this is an acronym and appears justified. Confirm acceptable.

**Response:** ok

---

### oroantral communication

**Source file:** `defs/oroantral_communication.fm.json`  
**ID:** `OIFM_OIDM_193631`  
**Description:** A non-epithelialized communication or defect between the oral cavity and maxillary sinus, often after dental extraction or maxillary dental disease.  
**Synonyms:** OAC, oro-antral communication, post-extraction oroantral defect  
**Change from prior:** unchanged, stable, new, resolved

**Source CSV:** `id=HID6055`; `name=oroantral_communication`; `category=dental`; `parent_id=HID6000`; `synonyms=OAC, oro-antral communication, post-extraction oroantral defect`; `finding_type=diagnosis`

**Assessment:** Mechanical review noted uppercase `OAC`; this is an acronym and appears justified. Confirm acceptable.

**Response:** ok

---

### dental anatomic variant

**Source file:** `defs/dental_anatomic_variant.fm.json`  
**ID:** `OIFM_OIDM_831097`  
**Description:** A developmental or anatomic variant involving the teeth or dentition visible on head CT.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved

**Source CSV:** `id=HID6200`; `name=dental_anatomic_variant`; `category=dental`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`

**Assessment:** Newly created broad parent model. Confirm acceptable.

**Response:** ok

---

### supernumerary tooth

**Source file:** `defs/supernumerary_tooth.fm.json`  
**ID:** `OIFM_OIDM_876710`  
**Description:** An additional tooth beyond the expected normal dentition, which may be erupted or unerupted.  
**Synonyms:** mesiodens, extra tooth, accessory tooth  
**Change from prior:** unchanged, stable, new, resolved

**Source CSV:** `id=HID6205`; `name=supernumerary_tooth`; `category=dental`; `parent_id=HID6200`; `synonyms=mesiodens, extra tooth, accessory tooth`; `finding_type=observation`

**Assessment:** Newly created using CSV terminology instead of GAMUTS `hyperdontia`. Confirm acceptable.

**Response:** drop `mesiodens` — site-specific subtype (specifically a midline supernumerary tooth between the central incisors). recommend `mesiodens` as a child entry instead, since it's lexicalized and tracked separately. keep `extra tooth` and `accessory tooth`.

---

### dental postsurgical change

**Source file:** `defs/dental_postsurgical_change.fm.json`  
**ID:** `OIFM_OIDM_203881`  
**Description:** Postsurgical or postprocedural changes involving the teeth, alveolar ridge, or dental hardware.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved

**Source CSV:** `id=HID6400`; `name=dental_postsurgical_change`; `category=dental`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`

**Assessment:** Newly created broad parent model. Confirm acceptable.

**Response:** ok

---

### dental extraction

**Source file:** `defs/dental_extraction.fm.json`  
**ID:** `OIFM_OIDM_822672`  
**Description:** Postprocedural absence of a tooth related to dental extraction, often with an extraction socket or remodeling of the alveolar ridge.  
**Synonyms:** tooth extraction, prior dental extraction  
**Change from prior:** unchanged, stable, new, resolved

**Source CSV:** `id=HID6405`; `name=dental_extraction`; `category=dental`; `parent_id=HID6400`; `synonyms=tooth extraction, prior dental extraction`; `finding_type=observation`

**Assessment:** Newly created model. Confirm acceptable.

**Response:** ok

---

### dental restoration

**Source file:** `defs/dental_restoration.fm.json`  
**ID:** `OIFM_OIDM_166768`  
**Description:** Dental restorative material or prosthetic dental hardware, such as a filling, crown, bridge, or other dental repair, visible on CT.  
**Synonyms:** dental filling, dental hardware, dental prosthesis  
**Change from prior:** unchanged, stable, new, resolved

**Source CSV:** `id=HID6410`; `name=dental_restoration`; `category=dental`; `parent_id=HID6400`; `synonyms=dental filling, dental hardware, dental prosthesis`; `finding_type=observation`

**Assessment:** Newly created model. Confirm acceptable.

**Response:** drop `dental hardware` and `dental prosthesis` — both too broad. hardware encompasses orthodontic appliances and implants (a separate model here); prosthesis encompasses removable dentures and bridges, a different category. keep `dental filling`. orthodontic hardware and removable prostheses warrant separate sibling models if needed.

---

### dental implant

**Source file:** `defs/dental_implant.fm.json`  
**ID:** `OIFM_OIDM_676246`  
**Description:** An osseointegrated dental implant or post placed in the maxilla or mandible to support a dental prosthesis.  
**Synonyms:** osseointegrated dental implant, dental post  
**Change from prior:** unchanged, stable, new, resolved

**Source CSV:** `id=HID6415`; `name=dental_implant`; `category=dental`; `parent_id=HID6400`; `synonyms=osseointegrated dental implant, dental post`; `finding_type=observation`

**Assessment:** Newly created model. Confirm acceptable.

**Response:** ok

---
