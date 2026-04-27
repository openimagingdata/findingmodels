# Finding Model Schema

## Overview

This schema describes radiology findings, their attributes, and how they are structured for the Open Imaging Data Model. It enables semantic tagging and standardization for use in imaging reports and research.

---

## Main Finding Model Object

### Required Fields

- **oifm_id**:  
  *Type: string*  
  *Pattern: `^OIFM_[A-Z]{3,4}_[0-9]{6}$`*  
  Unique ID for the finding model.

- **name**:  
  *Type: string*  
  *Minimum length: 5*  
  Short, descriptive name for the finding model.

- **description**:  
  *Type: string*  
  *Minimum length: 5*  
  One or two sentences describing the finding.

- **attributes**:  
  *Type: array of `Attribute` objects (see below)*  
  List of attributes (choice or numeric) to characterize the finding.

### Optional Fields

- **synonyms**:  
  *Type: array of strings*  
  Other terms used to describe the finding.

- **tags**:  
  *Type: array of strings*  
  Tags for categorizing the finding.

- **body_regions**:
  *Type: array of `BodyRegion` enum values*
  Broad anatomic body regions where the finding applies. Valid values are `head`, `neck`, `chest`,
  `breast`, `abdomen`, `pelvis`, `spine`, `upper_extremity`, `lower_extremity`, and `whole_body`.

- **subspecialties**:
  *Type: array of `Subspecialty` enum values*
  RSNA-aligned specialty content codes relevant to the finding. Include every applicable retained
  code such as `NR`, `CH`, `GI`, `GU`, `MK`, `PD`, `ER`, `VA`, `OI`, or `SQ`.

- **etiologies**:
  *Type: array of `EtiologyCode` enum values*
  Reasonable etiologic categories for the finding, such as infectious/inflammatory, neoplastic,
  traumatic, vascular, degenerative, congenital/developmental, iatrogenic, idiopathic, or
  normal-variant categories.

- **entity_type**:
  *Type: `EntityType` enum value*
  The kind of modeled concept: finding, diagnosis, grouping, measurement, assessment,
  recommendation, or technique issue.

- **applicable_modalities**:
  *Type: array of `Modality` enum values*
  Imaging modalities where the finding can reasonably be assessed. Valid values are `XR`, `CT`,
  `MR`, `US`, `PET`, `NM`, `MG`, `RF`, and `DSA`.

- **expected_time_course**:
  *Type: `ExpectedTimeCourse` object*
  Expected temporal behavior, including optional duration (`hours`, `days`, `weeks`, `months`,
  `years`, or `permanent`) and optional modifiers such as progressive, evolving, resolving,
  intermittent, fluctuating, recurrent, or stable.

- **age_profile**:
  *Type: `AgeProfile` object*
  Age applicability profile. `applicability` is either `all_ages` or a list of applicable age stages;
  `more_common_in` can identify stages where the finding is especially common.

- **sex_specificity**:
  *Type: `SexSpecificity` enum value*
  Whether the finding is male-specific, female-specific, or sex-neutral.

- **anatomic_locations**:
  *Type: array of `IndexCode` objects*
  Ontology-coded anatomic locations relevant to the finding.

- **contributors**:  
  *Type: array of `Person` or `Organization` objects*  
  Users or organizations who contributed.

- **index_codes**:  
  *Type: array of `IndexCode` objects*  
  Links to standard ontologies (e.g., SNOMED, RadLex).

---

## Attribute Types

### 1. Choice Attribute (`ChoiceAttributeIded`)

A selectable attribute with predefined values (e.g., severity, shape).

- **oifma_id**: Unique attribute ID (pattern: `^OIFMA_[A-Z]{3,4}_[0-9]{6}$`)
- **name**: Short, descriptive name.
- **description**: Optional. Description of the attribute.
- **type**: Always `"choice"`.
- **values**: Array of `ChoiceValueIded` objects (see below).
- **required**: Boolean. Whether always required.
- **max_selected**: Integer. Maximum values selectable (default: 1).
- **index_codes**: Array of `IndexCode` objects. Optional. Links to ontologies.

#### Choice Value (`ChoiceValueIded`)

- **value_code**: Unique code for the value (pattern: `^OIFMA_[A-Z]{3,4}_[0-9]{6}\.\d+$`)
- **name**: Name of the value.
- **description**: Optional.
- **index_codes**: Optional array of IndexCode objects.

---

### 2. Numeric Attribute (`NumericAttributeIded`)

A range or measurement attribute (e.g., size, number of findings).

- **oifma_id**: Unique attribute ID.
- **name**: Short, descriptive name.
- **description**: Optional.
- **type**: Always `"numeric"`.
- **minimum**: Optional integer/number.
- **maximum**: Optional integer/number.
- **unit**: Optional string (unit of measure).
- **required**: Boolean.
- **index_codes**: Optional array of IndexCode objects.

---

## Supporting Types

### `IndexCode`

Links to standard ontology codes (e.g., SNOMED, RadLex).

- **system**: Name of the system (e.g., "SNOMED").
- **code**: Code in the system.
- **display**: Optional display name.

On canonical `index_codes`, codes should be exact or clinically substitutable matches for the full
model concept. Merely related, broader, narrower, or temporally qualified codes belong in enrichment
review artifacts, not in the canonical model JSON.

### `Person`

Contributor details.

- **github_username**: Required.
- **email**: Required.
- **name**: Required.
- **organization_code**: Required.
- **url**: Optional.

### `Organization`

- **name**: Required.
- **code**: Required, 3-4 uppercase letters.
- **url**: Optional.

---

## Example Structure

```json
{
  "oifm_id": "OIFM_ABCD_123456",
  "name": "Pulmonary Nodule",
  "description": "A round or oval growth in the lung.",
  "attributes": [
    {
      "type": "choice",
      "oifma_id": "OIFMA_ABCD_123456",
      "name": "Shape",
      "values": [
        {
          "value_code": "OIFMA_ABCD_123456.1",
          "name": "Round"
        },
        {
          "value_code": "OIFMA_ABCD_123456.2",
          "name": "Oval"
        }
      ]
    },
    {
      "type": "numeric",
      "oifma_id": "OIFMA_ABCD_654321",
      "name": "Size (cm)",
      "minimum": 0,
      "maximum": 10,
      "unit": "cm"
    }
  ]
}
```
