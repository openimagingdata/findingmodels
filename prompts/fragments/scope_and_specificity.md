# Scope and specificity

When deciding what to model, three related questions come up:

1. Is this one finding, or several?
2. Is this subtype a value on the parent, or its own finding?
3. Is this name at the right level of abstraction?

## One finding, or several? (compound splitting)

A single model should not lump together findings that can occur independently. Signals:

- Names containing "and/or", "and", or slash separators
- Names joining two anatomic sites or two distinct entities

**Test:** can one part be present while the other is absent? If yes, they should be separate models.

- `mediastinal and/or hilar lymphadenopathy` → split into `mediastinal lymphadenopathy` and `hilar lymphadenopathy`
- `pneumonia with parapneumonic effusion` → `pneumonia` and `parapneumonic effusion`
- `encephalocele/meningocele` → two models

Counter-cases where combining is fine:

- A slash separating **locations or severities of the same finding** → simplify the name, make the distinction an attribute.
- A slash separating **truly interchangeable terms** → pick one, make the other a synonym. See `naming.md`.
- An umbrella category like `lines and tubes` may be acceptable as a combined observation category when no single member makes sense alone.

## Subtype: attribute value, or separate model?

When you encounter a potential subtype (e.g., `linear atelectasis` relative to `atelectasis`), decide between:

- **Attribute value on the parent.** Same observation with a qualifier → add as a value on a `morphology` or `type` attribute. "Linear atelectasis", "plate-like atelectasis", "round atelectasis" are all atelectasis with different shapes.
- **Separate finding model.** A fundamentally distinct observation that a radiologist would recognize as a different entity. `tension pneumothorax` isn't `pneumothorax, type: tension` — it has its own urgency, its own signs (mediastinal shift, hemidiaphragm depression), its own management implications.

**Decision question:** "Is this a fundamentally distinct observation, or the same observation with a qualifier?" **Practical signal:** you'd need *different attributes* to describe it. If the parent's attribute set doesn't fit, extract a new model.

Subtypes are **never** added as synonyms on the parent. See `synonym_rules.md`.

### Descriptor + entity: when the combined phrase is its own finding

A descriptor+entity combination can become its own finding when the combined term carries distinct clinical meaning beyond the sum of its parts.

**Test:** does a radiologist mean something different when they say "calcified nodule" versus "nodule with calcifications"? For that example, yes — `calcified nodule` implies a benign, fully calcified lesion, while `nodule with calcifications` implies a nodule that has some calcium but may still warrant follow-up. When the combined phrase has its own clinical meaning, it earns its own model; otherwise the descriptor is just an attribute value on the parent.

## Right level of abstraction

The guiding principle: **a finding is a noun phrase; everything else is an attribute.** A finding should be a stable noun phrase that gets the same characterizing attributes regardless of the specific instance.

### Too broad — not an imaging observation, or too vague without anatomic scope

- `infection` — a clinical category; the imaging findings are pneumonia, abscess, osteomyelitis, etc.
- `mass` — mass where? `pulmonary mass`, `mediastinal mass`, `renal mass`
- `calcification` — of what? `aortic calcification`, `mitral annular calcification`
- `fluid` — where? `pleural effusion`, `pericardial effusion`, `ascites`
- `hardware` — what kind? `pacemaker`, `spinal fixation`

### Too narrow — bakes attributes into the name

- `bibasilar consolidation` — location is an attribute on `airspace consolidation`
- `large right pleural effusion` — size and laterality are attributes on `pleural effusion`
- `acute left lower lobe pneumonia` — acuity, laterality, and lobe are attributes on `pneumonia`
- `new right subclavian central venous catheter` — `new` is change-from-prior, `right subclavian` is location, on `central venous catheter`
- `worsening interstitial edema` — `worsening` is a change-from-prior value on `interstitial pulmonary edema`

### Right level

- Pathology: `pleural effusion`, `pneumothorax`, `cardiomegaly`, `pulmonary nodule`, `lung mass`
- Devices: `pacemaker`, `chest tube`, `central venous catheter`
- Osseous: `rib fracture`, `compression fracture`, `clavicle fixation`
- Technique: `motion artifact`, `patient rotation`, `overpenetration`
- Scoped broad findings (for "no X" assertions): `chest wall fracture`, `upper abdominal abnormality`

### Multiple levels can coexist

`cardiac silhouette abnormality` (broad) and `cardiomegaly` (specific) can both be valid models — different levels of the same observation. The decision of which to model is a judgment call based on how radiologists actually report. If a term is used as a standalone observation in practice, it warrants its own model.

### Broad findings must be scoped to assessable anatomy

`fracture` is too broad. `chest wall fracture` is appropriately scoped for a chest radiograph. `upper abdominal abnormality` is appropriately scoped for a chest CT that includes the upper abdomen in the field of view.

## Scoring systems and measurement groupings

- **Scoring systems** (Lung-RADS, TI-RADS, PI-RADS, ESCC) are valid findings in their own right, modeled **separately** from the observations they assess. Different radiologists may describe the same nodule but assign different risk categories — systems need to reason about each independently.
- **Measurement groupings** (emphysema quantification, brain volumetry) are valid findings where the "finding" is the act of performing a structured quantitative assessment, and the attributes are the measurements within it.
