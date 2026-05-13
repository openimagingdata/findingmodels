# Review: head CT orbit batch 1

52 orbit CSV decisions to review. This category does not appear to have a prior batch review file: no `review_headct_orbit*.md` file was present.

This is a triage handoff, not a finalized model-creation batch. Entries marked **new model candidate** or **question** need reviewer direction before model creation. Existing-match entries still need reviewer confirmation before CSV writeback.

---
### new model candidate: orbital_abnormality

**Source CSV:** `id=HID6600`; `name=orbital_abnormality`; `category=orbit`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: orbital_fat_stranding

**Source CSV:** `id=HID6605`; `name=orbital_fat_stranding`; `category=orbit`; `parent_id=HID6600`; `synonyms=retrobulbar fat stranding, intraorbital fat stranding`; `finding_type=observation`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### matched: proptosis -> exophthalmos

**Source file:** `defs/exophthalmos.fm.json`  
**ID:** `OIFM_GMTS_024505`  
**Description:** Protrusion of the eyeball from the orbit  
**Synonyms:** proptosis, globe protrusion  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased

**Source CSV:** `id=HID6610`; `name=proptosis`; `category=orbit`; `parent_id=HID6600`; `synonyms=exophthalmos, globe protrusion, globe displacement anterior`; `finding_type=observation`

**Assessment:** Direct synonym match via `proptosis`, `exophthalmos`, and `globe protrusion`. Confirm CSV row should map to existing model; consider whether canonical should stay `exophthalmos` or move to CSV term `proptosis`.

**Response:**

---
### new model candidate: enophthalmos

**Source CSV:** `id=HID6615`; `name=enophthalmos`; `category=orbit`; `parent_id=HID6600`; `synonyms=posterior globe displacement, sunken globe`; `finding_type=observation`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### matched: extraocular_muscle_enlargement -> extraocular muscle enlargement

**Source file:** `defs/extraocular_muscle_enlargement.fm.json`  
**ID:** `OIFM_GMTS_018581`  
**Description:** Increased size of one or more muscles that control eye movement  
**Synonyms:** enlarged extraocular muscle, EOM enlargement  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID6620`; `name=extraocular_muscle_enlargement`; `category=orbit`; `parent_id=HID6600`; `synonyms=extraocular muscle thickening, enlarged extraocular muscles, enlarged extraocular muscle`; `finding_type=observation`

**Assessment:** Direct name/synonym match. Confirm CSV synonyms should be added if missing.

**Response:**

---
### new model candidate: extraocular_muscle_entrapment

**Source CSV:** `id=HID6625`; `name=extraocular_muscle_entrapment`; `category=orbit`; `parent_id=HID6600`; `synonyms=muscle incarceration, entrapped muscle`; `finding_type=observation`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### question: optic_nerve_sheath_enlargement

**Candidate file:** `defs/optic_nerve_sheath_lesion.fm.json`  
**Candidate ID:** `OIFM_GMTS_032035`  
**Candidate description:** A lesion affecting the sheath surrounding the optic nerve.  
**Candidate synonyms:** (none)

**Source CSV:** `id=HID6630`; `name=optic_nerve_sheath_enlargement`; `category=orbit`; `parent_id=HID6600`; `synonyms=optic nerve sheath dilation, optic nerve sheath distension, optic nerve sheath prominence`; `finding_type=observation`

**Question:** Existing `optic nerve sheath lesion` is related but broader; `optic nerve sheath enlargement` may be an observation model needed separately. Confirm create new model vs map to lesion.

**Response:**

---
### matched: optic_nerve_enlargement -> optic nerve enlargement

**Source file:** `defs/optic_nerve_enlargement.fm.json`  
**ID:** `OIFM_GMTS_008113`  
**Description:** Increased diameter of the optic nerve.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID6635`; `name=optic_nerve_enlargement`; `category=orbit`; `parent_id=HID6600`; `synonyms=optic nerve thickening, enlarged optic nerve`; `finding_type=observation`

**Assessment:** Direct name match. Confirm CSV synonyms should be added if missing.

**Response:**

---
### matched: superior_ophthalmic_vein_dilation -> enlarged superior ophthalmic vein

**Source file:** `defs/enlarged_superior_ophthalmic_vein.fm.json`  
**ID:** `OIFM_GMTS_018595`  
**Description:** Dilation or enlargement of the superior ophthalmic vein, often related to increased intracranial pressure.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID6640`; `name=superior_ophthalmic_vein_dilation`; `category=orbit`; `parent_id=HID6600`; `synonyms=dilated SOV, enlarged superior ophthalmic vein`; `finding_type=observation`

**Assessment:** Direct synonym-level match through `enlarged superior ophthalmic vein`. Confirm whether to map as-is or rename canonical toward `superior ophthalmic vein dilation`.

**Response:**

---
### matched/question: orbital_lesion -> orbital mass

**Source file:** `defs/orbital_mass.fm.json`  
**ID:** `OIFM_OIDM_208758`  
**Description:** An orbital mass is a space-occupying lesion within the orbit that may arise from lacrimal gland, extraocular muscles, or other orbital tissues and can be benign or malignant; imaging features aid in characterization and differential diagnosis, with 'orbital mass' serving as the exemplar original phrasing.  
**Synonyms:** orbital mass, orbital lesion, orbital tumor  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID6650`; `name=orbital_lesion`; `category=orbit`; `parent_id=HID6600`; `synonyms=orbital mass, retrobulbar mass, retrobulbar lesion, intraorbital mass, intraorbital lesion`; `finding_type=observation`

**Assessment:** `orbital lesion` is already a synonym on `orbital mass`, but by house precedent lesion is the neutral generic term and mass implies size/space-occupying threshold. Confirm mapping and whether to rename canonical to `orbital lesion`.

**Response:**

---
### question: lacrimal_gland_lesion

**Candidate file:** `defs/lacrimal_gland_enlargement.fm.json`  
**Candidate ID:** `OIFM_GMTS_008221`  
**Candidate description:** Increase in size of the lacrimal gland.  
**Candidate synonyms:** enlarged tear gland

**Source CSV:** `id=HID6655`; `name=lacrimal_gland_lesion`; `category=orbit`; `parent_id=HID6650`; `synonyms=lacrimal gland mass, lacrimal fossa mass, lacrimal fossa lesion`; `finding_type=observation`

**Question:** Existing `lacrimal gland enlargement` is related but not equivalent to a generic lacrimal gland lesion/mass. Confirm new `lacrimal gland lesion` model.

**Response:**

---
### matched/question: intraocular_lesion -> globe lesion

**Source file:** `defs/globe_lesion.fm.json`  
**ID:** `OIFM_GMTS_018561`  
**Description:** Lesion affecting the eye globe  
**Synonyms:** ocular lesion, eye globe lesion  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID6660`; `name=intraocular_lesion`; `category=orbit`; `parent_id=HID6600`; `synonyms=intraocular mass, globe mass, globe lesion`; `finding_type=observation`

**Assessment:** CSV synonyms include `globe lesion`, matching existing model. Confirm `intraocular lesion` should map to `globe lesion`, or whether `intraocular lesion` needs a separate broader/narrower model.

**Response:**

---
### new model candidate: orbital_emphysema

**Source CSV:** `id=HID6665`; `name=orbital_emphysema`; `category=orbit`; `parent_id=HID6600`; `synonyms=intraorbital air, orbital air`; `finding_type=observation`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: orbital_fat_herniation

**Source CSV:** `id=HID6670`; `name=orbital_fat_herniation`; `category=orbit`; `parent_id=HID6600`; `synonyms=orbital fat prolapse`; `finding_type=observation`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: globe_rupture

**Source CSV:** `id=HID6675`; `name=globe_rupture`; `category=orbit`; `parent_id=HID6600`; `synonyms=open globe, ruptured globe, open globe injury, globe disruption`; `finding_type=observation`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### matched: globe_calcification -> globe calcification

**Source file:** `defs/globe_calcification.fm.json`  
**ID:** `OIFM_GMTS_008203`  
**Description:** Calcium deposits within the globe of the eye.  
**Synonyms:** ocular calcification  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID6680`; `name=globe_calcification`; `category=orbit`; `parent_id=HID6600`; `synonyms=calcified globe, calcified lens, lens calcification`; `finding_type=observation`

**Assessment:** Direct name match. Reviewer should decide whether CSV synonyms `calcified lens` and `lens calcification` are true synonyms or should remain separate lens-specific findings.

**Response:**

---
### matched: lens_dislocation -> lens dislocation

**Source file:** `defs/lens_dislocation.fm.json`  
**ID:** `OIFM_GMTS_025548`  
**Description:** Displacement of the ocular lens from its normal position.  
**Synonyms:** ectopia lentis  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID6685`; `name=lens_dislocation`; `category=orbit`; `parent_id=HID6600`; `synonyms=lens subluxation, dislocated lens, ectopia lentis, displaced lens`; `finding_type=observation`

**Assessment:** Direct name match. Confirm CSV synonyms should be added if missing.

**Response:**

---
### question: traumatic_cataract

**Candidate file:** `defs/lens_opacity.fm.json`  
**Candidate ID:** `OIFM_GMTS_025549`  
**Candidate description:** Clouding of the lens, commonly known as cataract.  
**Candidate synonyms:** cataract

**Source CSV:** `id=HID6690`; `name=traumatic_cataract`; `category=orbit`; `parent_id=HID6600`; `synonyms=hypodense lens, lens swelling, lens edema`; `finding_type=observation`

**Question:** Existing `lens opacity`/`cataract` is related. CSV term `traumatic cataract` may be a diagnosis/subtype rather than synonym. Confirm create separate traumatic cataract model vs map to lens opacity.

**Response:**

---
### new model candidate: retinal_detachment

**Source CSV:** `id=HID6695`; `name=retinal_detachment`; `category=orbit`; `parent_id=HID6600`; `synonyms=detached retina`; `finding_type=observation`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: choroidal_detachment

**Source CSV:** `id=HID6700`; `name=choroidal_detachment`; `category=orbit`; `parent_id=HID6600`; `synonyms=choroidal effusion, suprachoroidal fluid`; `finding_type=observation`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: orbital_hemorrhage

**Source CSV:** `id=HID6750`; `name=orbital_hemorrhage`; `category=orbit`; `parent_id=HID6600`; `synonyms=(blank)`; `finding_type=diagnosis`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: retrobulbar_hemorrhage

**Source CSV:** `id=HID6800`; `name=retrobulbar_hemorrhage`; `category=orbit`; `parent_id=HID6750`; `synonyms=retro-ocular hemorrhage, retrobulbar hematoma`; `finding_type=diagnosis`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: intraconal_hemorrhage

**Source CSV:** `id=HID6805`; `name=intraconal_hemorrhage`; `category=orbit`; `parent_id=HID6800`; `synonyms=intraconal hematoma`; `finding_type=diagnosis`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: extraconal_hemorrhage

**Source CSV:** `id=HID6810`; `name=extraconal_hemorrhage`; `category=orbit`; `parent_id=HID6800`; `synonyms=extraconal hematoma`; `finding_type=diagnosis`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: subperiosteal_hemorrhage

**Source CSV:** `id=HID6815`; `name=subperiosteal_hemorrhage`; `category=orbit`; `parent_id=HID6750`; `synonyms=subperiosteal orbital hematoma`; `finding_type=diagnosis`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### matched: intraocular_hemorrhage -> intraocular hemorrhage

**Source file:** `defs/intraocular_hemorrhage.fm.json`  
**ID:** `OIFM_OIDM_535373`  
**Description:** Blood products within the globe, which may involve the anterior chamber (hyphema), vitreous, or subretinal space. On CT, appears as hyperdense material within the ocular compartments, often in the setting of trauma.  
**Synonyms:** intraocular blood products, intraocular blood, hemorrhage within the globe  
**Change from prior:** unchanged, stable, new, resolved, larger, smaller, worsened, improved, increased, decreased

**Source CSV:** `id=HID6850`; `name=intraocular_hemorrhage`; `category=orbit`; `parent_id=HID6750`; `synonyms=intraocular blood products`; `finding_type=diagnosis`

**Assessment:** Direct name/synonym match. Confirm acceptable.

**Response:**

---
### new model candidate: hyphema

**Source CSV:** `id=HID6855`; `name=hyphema`; `category=orbit`; `parent_id=HID6850`; `synonyms=anterior chamber hemorrhage`; `finding_type=diagnosis`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: vitreous_hemorrhage

**Source CSV:** `id=HID6860`; `name=vitreous_hemorrhage`; `category=orbit`; `parent_id=HID6850`; `synonyms=vitreous blood, intravitreal hemorrhage`; `finding_type=diagnosis`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: subretinal_hemorrhage

**Source CSV:** `id=HID6865`; `name=subretinal_hemorrhage`; `category=orbit`; `parent_id=HID6850`; `synonyms=subretinal blood`; `finding_type=diagnosis`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: choroidal_hemorrhage

**Source CSV:** `id=HID6870`; `name=choroidal_hemorrhage`; `category=orbit`; `parent_id=HID6850`; `synonyms=suprachoroidal hemorrhage, hemorrhagic choroidal detachment`; `finding_type=diagnosis`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: orbital_inflammation

**Source CSV:** `id=HID6900`; `name=orbital_inflammation`; `category=orbit`; `parent_id=HID6600`; `synonyms=orbital inflammatory disease`; `finding_type=diagnosis`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: preseptal_cellulitis

**Source CSV:** `id=HID6905`; `name=preseptal_cellulitis`; `category=orbit`; `parent_id=HID6900`; `synonyms=periorbital cellulitis`; `finding_type=diagnosis`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: orbital_cellulitis

**Source CSV:** `id=HID6910`; `name=orbital_cellulitis`; `category=orbit`; `parent_id=HID6900`; `synonyms=postseptal cellulitis, orbital phlegmon`; `finding_type=diagnosis`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: orbital_abscess

**Source CSV:** `id=HID6950`; `name=orbital_abscess`; `category=orbit`; `parent_id=HID6900`; `synonyms=orbital abscess collection`; `finding_type=diagnosis`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: subperiosteal_abscess

**Source CSV:** `id=HID6955`; `name=subperiosteal_abscess`; `category=orbit`; `parent_id=HID6950`; `synonyms=orbital subperiosteal abscess`; `finding_type=diagnosis`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: idiopathic_orbital_inflammation

**Source CSV:** `id=HID6960`; `name=idiopathic_orbital_inflammation`; `category=orbit`; `parent_id=HID6900`; `synonyms=orbital pseudotumor, non-specific orbital inflammation`; `finding_type=diagnosis`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: dacryoadenitis

**Source CSV:** `id=HID6965`; `name=dacryoadenitis`; `category=orbit`; `parent_id=HID6900`; `synonyms=lacrimal gland inflammation`; `finding_type=diagnosis`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: thyroid_eye_disease

**Source CSV:** `id=HID6970`; `name=thyroid_eye_disease`; `category=orbit`; `parent_id=HID6900`; `synonyms=Graves orbitopathy, thyroid orbitopathy, thyroid-associated orbitopathy`; `finding_type=diagnosis`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: orbital_myositis

**Source CSV:** `id=HID6975`; `name=orbital_myositis`; `category=orbit`; `parent_id=HID6900`; `synonyms=extraocular muscle myositis, orbital muscle inflammation`; `finding_type=diagnosis`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: posterior_scleritis

**Source CSV:** `id=HID6980`; `name=posterior_scleritis`; `category=orbit`; `parent_id=HID6900`; `synonyms=posterior scleral inflammation`; `finding_type=diagnosis`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: orbital_cavernous_venous_malformation

**Source CSV:** `id=HID6985`; `name=orbital_cavernous_venous_malformation`; `category=orbit`; `parent_id=HID6600`; `synonyms=orbital cavernous hemangioma, cavernous hemangioma orbit, orbital hemangioma, orbital venous malformation, cavernous venous malformation orbit`; `finding_type=diagnosis`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### question: orbital_dermoid

**Candidate file:** `defs/dermoid_cyst.fm.json`  
**Candidate ID:** `OIFM_CDE_000216`  
**Candidate description:** Dermoid Cyst detection on CT  
**Candidate synonyms:** (none)

**Source CSV:** `id=HID6990`; `name=orbital_dermoid`; `category=orbit`; `parent_id=HID6600`; `synonyms=orbital dermoid cyst, dermoid cyst orbit`; `finding_type=diagnosis`

**Question:** Existing `dermoid cyst` is body-wide and might cover orbital dermoid; CSV term is site-specific. Confirm map to existing dermoid cyst or create `orbital dermoid`.

**Response:**

---
### new model candidate: orbital_neoplasm

**Source CSV:** `id=HID7000`; `name=orbital_neoplasm`; `category=orbit`; `parent_id=HID6600`; `synonyms=(blank)`; `finding_type=diagnosis`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: orbital_lymphoma

**Source CSV:** `id=HID7005`; `name=orbital_lymphoma`; `category=orbit`; `parent_id=HID7000`; `synonyms=ocular adnexal lymphoma`; `finding_type=diagnosis`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: orbital_metastasis

**Source CSV:** `id=HID7010`; `name=orbital_metastasis`; `category=orbit`; `parent_id=HID7000`; `synonyms=orbital metastatic disease`; `finding_type=diagnosis`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: retinoblastoma

**Source CSV:** `id=HID7015`; `name=retinoblastoma`; `category=orbit`; `parent_id=HID7000`; `synonyms=(blank)`; `finding_type=diagnosis`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: phthisis_bulbi

**Source CSV:** `id=HID7020`; `name=phthisis_bulbi`; `category=orbit`; `parent_id=HID6600`; `synonyms=phthisical globe, end-stage globe`; `finding_type=diagnosis`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### matched: superior_ophthalmic_vein_thrombosis -> superior ophthalmic vein thrombosis

**Source file:** `defs/superior_ophthalmic_vein_thrombosis.fm.json`  
**ID:** `OIFM_GMTS_018598`  
**Description:** Thrombosis of the superior ophthalmic vein, often seen in orbital or cavernous sinus disease.  
**Synonyms:** (none)  
**Change from prior:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

**Source CSV:** `id=HID7025`; `name=superior_ophthalmic_vein_thrombosis`; `category=orbit`; `parent_id=HID6600`; `synonyms=SOV thrombosis`; `finding_type=diagnosis`

**Assessment:** Direct name match. Confirm whether `SOV thrombosis` should be added as synonym.

**Response:**

---
### new model candidate: orbital_postsurgical_change

**Source CSV:** `id=HID7200`; `name=orbital_postsurgical_change`; `category=orbit`; `parent_id=(blank)`; `synonyms=(blank)`; `finding_type=(blank)`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: lens_implant

**Source CSV:** `id=HID7205`; `name=lens_implant`; `category=orbit`; `parent_id=HID7200`; `synonyms=intraocular lens, IOL, pseudophakia`; `finding_type=observation`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: prosthetic_globe

**Source CSV:** `id=HID7210`; `name=prosthetic_globe`; `category=orbit`; `parent_id=HID7200`; `synonyms=ocular prosthesis, artificial eye, prosthetic eye`; `finding_type=observation`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
### new model candidate: intraocular_silicone

**Source CSV:** `id=HID7215`; `name=intraocular_silicone`; `category=orbit`; `parent_id=HID7200`; `synonyms=silicone oil in globe, intraocular silicone oil, vitreous silicone`; `finding_type=observation`

**Assessment:** No direct existing model found by exact name/synonym matching and targeted orbit-related text search. Create a new model if reviewer agrees the concept is in scope and not better represented by an existing broader model.

**Response:**

---
