# Finding Models: Compact Overview

Finding models are structured, machine-readable definitions for radiology findings. They turn unstructured radiology report text into structured, machine-accessible observation objects that downstream systems and agents use for clinical reasoning.

**A finding is something a radiologist would name as a distinct observation in a report** — including negative observations ("no fracture" → chest wall fracture, presence: absent). This covers pathology, devices, postsurgical states, anatomic variants, image quality issues, and diagnostic impressions. NOT a finding: a state ("stable cardiac silhouette"), a qualified version ("large pleural effusion"), normal anatomy, exam metadata, radiographic signs/techniques ("silhouette sign", "double density sign"), or descriptors that are attributes of another finding ("air-fluid level", "hematocrit level").

**A finding is a noun phrase; everything else is an attribute.** Findings must be at the right level of specificity — not too broad ("infection" is a clinical category, not an imaging observation; "calcification" needs anatomic scope), not too narrow ("bibasilar consolidation" bakes location into the name — location is an attribute on "airspace consolidation"). Multiple levels can coexist ("cardiac silhouette abnormality" and "cardiomegaly" are both valid). Broad findings must be scoped to assessable anatomy ("chest wall fracture" not just "fracture"). See `prompts/overview.md` for detailed examples.

**Each finding model defines:** a canonical name, synonyms (exact equivalents only — be aggressive collecting them but strict about correctness), a clinical description, attributes (presence, change from prior, plus domain-specific properties like size/severity/location), ontology links (SNOMED, RadLex), and contributor information.

**Why quality matters:** These definitions are the knowledge base that gives meaning to extracted observations. Incorrect synonyms, wrong names, or nonsensical attributes propagate errors into downstream clinical reasoning. Getting the conventions right (see `prompts/conventions.md`) is not cosmetic — it directly affects the reliability of systems that reason about patient care.

For the full context, see `prompts/overview.md`.
