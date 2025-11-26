# Merge Report: Pulmonary Nodule
**Timestamp:** 2025-11-26 00:27:38

**Existing Model:** Pulmonary Nodule (ID: OIFM_CDE_000195)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 3
- **Review decisions made:** 3
  - Keep existing: 3
    - Change from priors (kept, status not added)
    - Morphology (kept, edges not added)
    - Location (kept, location not added)
- **New attributes added:** 5
  - morphology
  - calcification
  - cavitation
  - satellite_nodules
  - lymphadenopathy
- **Required attributes added:** 0
- **Total existing attributes:** 13
- **Total incoming attributes:** 11
- **Total final attributes:** 18

---

## ⚠️ Attributes Needing Review (3)

*These attributes were reviewed and decisions were made.*

### 1. Change from priors vs status
- **Relationship:** needs_review (confidence: 0.50)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** Both attributes are change_from_prior but have no_similarities. Existing does not have standard values. Requires human review.

- **Existing only values:** no priors, unchanged for less than 6 months, unchanged for 6-12 months, unchanged for 12-24 months, unchanged more than 24 months, larger since prior, smaller since prior
- **Incoming only values:** new, stable, enlarging, decreasing

### 2. Morphology vs edges
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The EXISTING attribute has values: ['smooth', 'lobulated', 'ill-defined', 'spiculated', 'perifissural', 'indeterminate', 'unknown'] while the INCOMING attribute has values: ['smooth', 'lobulated', 'spiculated']. The shared values between the two attributes are ['smooth', 'lobulated', 'spiculated']. The EXISTING attribute has additional unique values which include ['ill-defined', 'perifissural', 'indeterminate', 'unknown'], while the INCOMING attribute has no unique values of its own. Therefore, 'some incoming values are not in existing' is accurate as only a subset of the existing values is represented in incoming. Additionally, since both attributes share some values and each has unique values, the classification type is 'needs_review'.

- **Shared values:** smooth, lobulated, spiculated
- **Existing only values:** ill-defined, perifissural, indeterminate, unknown

### 3. Location vs location
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The values in the existing attribute include: ['indeterminate', 'left lung', 'left upper lobe', 'lingula', 'left lower lobe', 'right lung', 'right upper lobe', 'right middle lobe', 'right lower lobe', 'unknown']. The values in the incoming attribute are: ['right upper lobe', 'right middle lobe', 'right lower lobe', 'left upper lobe', 'left lower lobe', 'bilateral']. 

Shared values between the existing and incoming attributes are: ['right upper lobe', 'right middle lobe', 'right lower lobe', 'left upper lobe', 'left lower lobe']. 

Unique values in existing are: ['indeterminate', 'left lung', 'lingula', 'right lung', 'unknown'].

Unique values in incoming are: ['bilateral']. 

Because there are several shared values, but each attribute also has unique values that are not present in the other, this relationship is classified as 'needs_review'.

- **Shared values:** right upper lobe, right middle lobe, right lower lobe, left upper lobe, left lower lobe
- **Existing only values:** indeterminate, left lung, lingula, right lung, unknown
- **Incoming only values:** bilateral

---

## Existing Attributes (13)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Values:** absent, present, unknown, indeterminate
- **Max selected:** 1
- **Required:** False

### 2. Change from priors
- **Name:** Change from priors
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Values:** no priors, unchanged for less than 6 months, unchanged for 6-12 months, unchanged for 12-24 months, unchanged more than 24 months, larger since prior, smaller since prior
- **Max selected:** 1
- **Required:** False

### 3. Composition
- **Name:** Composition
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** solid, ground glass, part-solid, fat density, calcification, cavitation, cystic lucencies, air bronchgrams, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 4. Size
- **Name:** Size
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Description:** Average diameter in mm
- **Unit:** mm
- **Range:** 2 - 100
- **Required:** False

### 5. Solid component size
- **Name:** Solid component size
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Unit:** mm
- **Range:** 2 - 100
- **Required:** False

### 6. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** indeterminate, left lung, left upper lobe, lingula, left lower lobe, right lung, right upper lobe, right middle lobe, right lower lobe, unknown
- **Max selected:** 1
- **Required:** False

### 7. Morphology
- **Name:** Morphology
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** smooth, lobulated, Ill-defined, spiculated, perifissural, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 8. Plurality
- **Name:** Plurality
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** single, multiple
- **Max selected:** 1
- **Required:** False

### 9. Microcystic component
- **Name:** Microcystic component
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** present, absent, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 10. Volume
- **Name:** Volume
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Unit:** mm3
- **Range:** 1 - 150000
- **Required:** False

### 11. Suspicious appearance
- **Name:** Suspicious appearance
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** yes, no, indeterminate
- **Max selected:** 1
- **Required:** False

### 12. Min density
- **Name:** Min density
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Description:** Minimum - 1000, max +1000
- **Unit:** HU
- **Range:** 0 - 100
- **Required:** False

### 13. Max density
- **Name:** Max density
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Description:** Minimum   - 1000, max   +1000
- **Unit:** HU
- **Range:** 0 - 100
- **Required:** False

---

## Incoming Attributes (11)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence of the pulmonary nodule.
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 2. status
- **Name:** status
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Status of the pulmonary nodule.
- **Values:** new, stable, enlarging, decreasing
- **Max selected:** 1
- **Required:** True

### 3. number
- **Name:** number
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Number of pulmonary nodules.
- **Values:** single, multiple
- **Max selected:** 1
- **Required:** True

### 4. size Finding
- **Name:** size Finding
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Description:** Size of the pulmonary nodule.
- **Unit:** mm
- **Range:** 0 - 100
- **Required:** True

### 5. morphology
- **Name:** morphology
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Morphology of the pulmonary nodule.
- **Values:** solid, subsolid
- **Max selected:** 1
- **Required:** True

### 6. edges
- **Name:** edges
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Edges of the pulmonary nodule.
- **Values:** smooth, lobulated, spiculated
- **Max selected:** 1
- **Required:** True

### 7. location
- **Name:** location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Location of the pulmonary nodule.
- **Values:** right upper lobe, right middle lobe, right lower lobe, left upper lobe, left lower lobe, bilateral
- **Max selected:** 1
- **Required:** True

### 8. calcification
- **Name:** calcification
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Calcification of the pulmonary nodule.
- **Values:** present, absent, central, diffuse, laminated, popcorn
- **Max selected:** 1
- **Required:** True

### 9. cavitation
- **Name:** cavitation
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Cavitation of the pulmonary nodule.
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 10. satellite_nodules
- **Name:** satellite_nodules
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of satellite nodules.
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 11. lymphadenopathy
- **Name:** lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of lymphadenopathy.
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (3)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. Presence vs presence
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'presence' will be discarded.

- **Existing only values:** absent, present, unknown, indeterminate
- **Incoming only values:** present, absent

#### 2. Plurality vs number
- **Relationship:** identical (confidence: 0.90)
- **Recommendation:** no_merge
- **AI Reasoning:** Both attributes, Plurality and number, contain exactly the same values: 'single' and 'multiple'. Despite the different names, the actual values they contain are identical when compared case-insensitively. Therefore, All incoming values are in existing, and all existing values are in incoming, making this relationship 'identical'.

- **Shared values:** single, multiple

#### 3. Size vs size Finding
- **Relationship:** identical (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Both the existing and incoming attributes have no values defined. Since they both lack any values, they are considered to be identical because they have the same empty value set. Thus, it can be stated: 'All incoming values are in existing' since there are no values to compare. There are also no unique values in either attribute. This relationship type is classified as 'identical' as both attributes represent the same state of having no defined values.

### New Attributes Added (5)

#### 1. morphology
- **Type:** AttributeType.CHOICE
- **Values:** solid, subsolid
- **Description:** Morphology of the pulmonary nodule.

#### 2. calcification
- **Type:** AttributeType.CHOICE
- **Values:** present, absent, central, diffuse, laminated, popcorn
- **Description:** Calcification of the pulmonary nodule.

#### 3. cavitation
- **Type:** AttributeType.CHOICE
- **Values:** present, absent
- **Description:** Cavitation of the pulmonary nodule.

#### 4. satellite_nodules
- **Type:** AttributeType.CHOICE
- **Values:** present, absent
- **Description:** Presence of satellite nodules.

#### 5. lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Values:** present, absent
- **Description:** Presence of lymphadenopathy.

### Required Attributes Added
None

---

## Final Attributes (18)

### 1. Change from priors
- **Name:** Change from priors
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Values:** no priors, unchanged for less than 6 months, unchanged for 6-12 months, unchanged for 12-24 months, unchanged more than 24 months, larger since prior, smaller since prior
- **Max selected:** 1
- **Required:** False

### 2. Morphology
- **Name:** Morphology
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** smooth, lobulated, Ill-defined, spiculated, perifissural, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 3. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** indeterminate, left lung, left upper lobe, lingula, left lower lobe, right lung, right upper lobe, right middle lobe, right lower lobe, unknown
- **Max selected:** 1
- **Required:** False

### 4. morphology
- **Name:** morphology
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Morphology of the pulmonary nodule.
- **Values:** solid, subsolid
- **Max selected:** 1
- **Required:** True

### 5. calcification
- **Name:** calcification
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Calcification of the pulmonary nodule.
- **Values:** present, absent, central, diffuse, laminated, popcorn
- **Max selected:** 1
- **Required:** True

### 6. cavitation
- **Name:** cavitation
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Cavitation of the pulmonary nodule.
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 7. satellite_nodules
- **Name:** satellite_nodules
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of satellite nodules.
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 8. lymphadenopathy
- **Name:** lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of lymphadenopathy.
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 9. Composition
- **Name:** Composition
- **Type:** AttributeType.CHOICE
- **Values:** solid, ground glass, part-solid, fat density, calcification, cavitation, cystic lucencies, air bronchgrams, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 10. Size
- **Name:** Size
- **Type:** AttributeType.NUMERIC
- **Description:** Average diameter in mm
- **Unit:** mm
- **Range:** 2 - 100
- **Required:** False

### 11. Solid component size
- **Name:** Solid component size
- **Type:** AttributeType.NUMERIC
- **Unit:** mm
- **Range:** 2 - 100
- **Required:** False

### 12. Plurality
- **Name:** Plurality
- **Type:** AttributeType.CHOICE
- **Values:** single, multiple
- **Max selected:** 1
- **Required:** False

### 13. Microcystic component
- **Name:** Microcystic component
- **Type:** AttributeType.CHOICE
- **Values:** present, absent, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 14. Volume
- **Name:** Volume
- **Type:** AttributeType.NUMERIC
- **Unit:** mm3
- **Range:** 1 - 150000
- **Required:** False

### 15. Suspicious appearance
- **Name:** Suspicious appearance
- **Type:** AttributeType.CHOICE
- **Values:** yes, no, indeterminate
- **Max selected:** 1
- **Required:** False

### 16. Min density
- **Name:** Min density
- **Type:** AttributeType.NUMERIC
- **Description:** Minimum - 1000, max +1000
- **Unit:** HU
- **Range:** 0 - 100
- **Required:** False

### 17. Max density
- **Name:** Max density
- **Type:** AttributeType.NUMERIC
- **Description:** Minimum   - 1000, max   +1000
- **Unit:** HU
- **Range:** 0 - 100
- **Required:** False

### 18. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Values:** absent, present, unknown, indeterminate
- **Max selected:** 1
- **Required:** False

---
