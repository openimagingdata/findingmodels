# What a finding model is

A **finding model** is a structured, machine-readable definition of an observation a radiologist would name in a report. The library of these models is the knowledge base that lets downstream systems turn unstructured report text into structured observation objects.

## Two guiding principles

- **A finding is a noun phrase; everything else is an attribute.** A finding is the thing being described; *how* it is described (size, location, severity, change, morphology) is captured in attributes. If something reads as an adjective, a clause, or a state, it is not a finding. See `scope_and_specificity.md` for how this principle drives decisions about the right level of abstraction.
- **Findings exist in time.** A radiology report is a snapshot, but the findings it describes persist across exams. A pleural effusion seen today may be the same one from last week, now larger. Finding models provide the shared vocabulary that lets observations be tracked and associated across time — which is why every finding model has a `change from prior` attribute (see `presence_and_change.md`).

## What counts as a finding

A finding is any observation a radiologist would identify and name as a distinct statement in a report — **including negative observations** ("no fracture" → a `chest wall fracture` finding with `presence: absent`). The test: would a radiologist write "there is [X]" or "no [X]" as a standalone statement?

Findings include:

- **Pathology**: pleural effusion, intracranial hemorrhage, meniscal tear, renal mass
- **Physiologic/functional observations**: pulmonary vascular engorgement, cephalization
- **Devices and hardware**: pacemaker, chest tube, pedicle screws, ventricular shunt
- **Postsurgical states**: sternotomy, craniotomy, laminectomy
- **Anatomic variants**: azygos fissure, cervical rib, cavum septum pellucidum
- **Image-quality observations**: motion artifact, patient rotation, overpenetration
- **Diagnoses**: pneumonia, cystic fibrosis, osteoarthritis — radiologists use diagnostic terms as shorthand for recognizable imaging patterns, and those are first-class findings. Do not question whether a diagnosis "should" be a finding.

## What is NOT a finding

- **A state of a finding.** "Stable cardiac silhouette" is not a finding — "stable" is a change-from-prior value.
- **A qualified version of another finding.** "Large pleural effusion" is not a finding — "large" is a size attribute.
- **Normal anatomy.** "Cardiac silhouette" is anatomy; the finding is when something is abnormal about it.
- **Radiographic signs and interpretation techniques.** "Silhouette sign", "double density sign", "air-fluid level" — these are how radiologists reason, not what they observe. The finding is what the sign reveals.
- **Exam metadata and history.** Projection type, positioning, clinical history, recommendations.

A generic descriptor can *become* a finding when anatomic context makes it a reportable observation on its own: "air-fluid level" alone is not a finding, but "air-fluid levels in bowel" is.

## Anatomy of a finding model

- **Name** — canonical, lowercase, descriptive. Acronyms expanded, eponyms minimized, no brand names. See `naming.md`.
- **Description** — 1-2 concise clinical sentences written for a radiologist audience.
- **Synonyms** — alternative terms that mean the *exact same thing at the same level of specificity*. See `synonym_rules.md`.
- **Tags** — clinical categories (anatomy, modality, etiology) for organization.
- **Attributes** — structured properties. The first two are always `presence` and `change from prior` (see `presence_and_change.md`). The rest are domain-specific: size, location, severity, density, morphology, etc.
- **Index codes** — links to standard ontologies (SNOMED, RadLex, GAMUTS).
- **Contributors** — people and organizations who authored the definition.
- **IDs** — OIFM ID for the finding, OIFMA IDs for attributes, value codes for choice values. Machine-generated; never written by hand.

## Why quality matters

Errors in a finding model propagate into downstream clinical reasoning. A bad synonym maps the wrong concept to an observation. A nonsensical attribute produces meaningless structured data. A poorly scoped model conflates distinct clinical entities. Getting the conventions right is not cosmetic — it directly affects the reliability of systems that reason about patient care.
