# Merge Report: Pulmonary Nodule
**Timestamp:** 2025-11-19 23:09:44

**Existing Model:** Pulmonary Nodule (ID: OIFM_CDE_000195)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 2
- **Review decisions made:** 2
  - Keep existing: 2
    - Morphology (kept, edges not added)
    - Location (kept, location not added)
- **New attributes added:** 6
  - status
  - morphology
  - calcification
  - cavitation
  - satellite_nodules
  - lymphadenopathy
- **Required attributes added:** 0
- **Total existing attributes:** 13
- **Total incoming attributes:** 11
- **Total final attributes:** 19

---

## ⚠️ Attributes Needing Review (2)

*These attributes were reviewed and decisions were made.*

### 1. Morphology vs edges
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing attribute 'Morphology' has values: ['smooth', 'lobulated', 'Ill-defined', 'spiculated', 'perifissural', 'indeterminate', 'unknown'] and the incoming attribute 'edges' has values: ['smooth', 'lobulated', 'spiculated']. The shared values between the two attributes are ['smooth', 'lobulated', 'spiculated']. However, the existing attribute contains additional unique values that are not present in the incoming attribute: ['Ill-defined', 'perifissural', 'indeterminate', 'unknown']. Thus, the existing attribute is not a complete subset of the incoming, nor does the incoming have all the existing values, which classifies this relationship as 'needs_review'. The incoming attribute has no unique values that are not in the existing attribute.

- **Shared values:** smooth, lobulated, spiculated
- **Existing only values:** Ill-defined, perifissural, indeterminate, unknown

### 2. Location vs location
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing attribute values are: ['indeterminate', 'left lung', 'left upper lobe', 'lingula', 'left lower lobe', 'right lung', 'right upper lobe', 'right middle lobe', 'right lower lobe', 'unknown']. The incoming attribute values are: ['right upper lobe', 'right middle lobe', 'right lower lobe', 'left upper lobe', 'left lower lobe', 'bilateral']. 

Upon comparing the two attributes, the shared values are: ['right upper lobe', 'right middle lobe', 'right lower lobe', 'left upper lobe', 'left lower lobe']. 

The existing only values are: ['indeterminate', 'left lung', 'lingula', 'right lung', 'unknown'], and the incoming only value is: ['bilateral']. 

Since there are shared values but each attribute has unique values that are not in the other, the relationship is classified as 'needs_review'. Some incoming values are not in existing, specifically 'bilateral', and there are also unique existing values such as 'indeterminate', 'left lung', 'lingula', 'right lung', and 'unknown'. Therefore, we have both shared and unique values, justifying the 'needs_review' classification.

- **Shared values:** right upper lobe, right middle lobe, right lower lobe, left upper lobe, left lower lobe
- **Existing only values:** indeterminate, left lung, lingula, right lung, unknown
- **Incoming only values:** bilateral

---

## Existing Attributes (13)

### 1. Composition
- **Name:** Composition
- **Type:** AttributeType.CHOICE
- **Values:** solid, ground glass, part-solid, fat density, calcification, cavitation, cystic lucencies, air bronchgrams, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. Size
- **Name:** Size
- **Type:** AttributeType.NUMERIC
- **Description:** Average diameter in mm
- **Unit:** mm
- **Range:** 2 - 100
- **Required:** False

### 3. Solid component size
- **Name:** Solid component size
- **Type:** AttributeType.NUMERIC
- **Unit:** mm
- **Range:** 2 - 100
- **Required:** False

### 4. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Values:** indeterminate, left lung, left upper lobe, lingula, left lower lobe, right lung, right upper lobe, right middle lobe, right lower lobe, unknown
- **Max selected:** 1
- **Required:** False

### 5. Morphology
- **Name:** Morphology
- **Type:** AttributeType.CHOICE
- **Values:** smooth, lobulated, Ill-defined, spiculated, perifissural, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 6. Plurality
- **Name:** Plurality
- **Type:** AttributeType.CHOICE
- **Values:** single, multiple
- **Max selected:** 1
- **Required:** False

### 7. Microcystic component
- **Name:** Microcystic component
- **Type:** AttributeType.CHOICE
- **Values:** present, absent, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 8. Volume
- **Name:** Volume
- **Type:** AttributeType.NUMERIC
- **Unit:** mm3
- **Range:** 1 - 150000
- **Required:** False

### 9. Change from priors
- **Name:** Change from priors
- **Type:** AttributeType.CHOICE
- **Values:** no priors, unchanged for less than 6 months, unchanged for 6-12 months, unchanged for 12-24 months, unchanged more than 24 months, larger since prior, smaller since prior
- **Max selected:** 1
- **Required:** False

### 10. Suspicious appearance
- **Name:** Suspicious appearance
- **Type:** AttributeType.CHOICE
- **Values:** yes, no, indeterminate
- **Max selected:** 1
- **Required:** False

### 11. Min density
- **Name:** Min density
- **Type:** AttributeType.NUMERIC
- **Description:** Minimum - 1000, max +1000
- **Unit:** HU
- **Range:** 0 - 100
- **Required:** False

### 12. Max density
- **Name:** Max density
- **Type:** AttributeType.NUMERIC
- **Description:** Minimum   - 1000, max   +1000
- **Unit:** HU
- **Range:** 0 - 100
- **Required:** False

### 13. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Values:** absent, present, unknown, indeterminate
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (11)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence of the pulmonary nodule.
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 2. number
- **Name:** number
- **Type:** AttributeType.CHOICE
- **Description:** Number of pulmonary nodules.
- **Values:** single, multiple
- **Max selected:** 1
- **Required:** True

### 3. status
- **Name:** status
- **Type:** AttributeType.CHOICE
- **Description:** Status of the pulmonary nodule.
- **Values:** new, stable, enlarging, decreasing
- **Max selected:** 1
- **Required:** True

### 4. size Finding
- **Name:** size Finding
- **Type:** AttributeType.NUMERIC
- **Description:** Size of the pulmonary nodule.
- **Unit:** mm
- **Range:** 0 - 100
- **Required:** True

### 5. morphology
- **Name:** morphology
- **Type:** AttributeType.CHOICE
- **Description:** Morphology of the pulmonary nodule.
- **Values:** solid, subsolid
- **Max selected:** 1
- **Required:** True

### 6. edges
- **Name:** edges
- **Type:** AttributeType.CHOICE
- **Description:** Edges of the pulmonary nodule.
- **Values:** smooth, lobulated, spiculated
- **Max selected:** 1
- **Required:** True

### 7. location
- **Name:** location
- **Type:** AttributeType.CHOICE
- **Description:** Location of the pulmonary nodule.
- **Values:** right upper lobe, right middle lobe, right lower lobe, left upper lobe, left lower lobe, bilateral
- **Max selected:** 1
- **Required:** True

### 8. calcification
- **Name:** calcification
- **Type:** AttributeType.CHOICE
- **Description:** Calcification of the pulmonary nodule.
- **Values:** present, absent, central, diffuse, laminated, popcorn
- **Max selected:** 1
- **Required:** True

### 9. cavitation
- **Name:** cavitation
- **Type:** AttributeType.CHOICE
- **Description:** Cavitation of the pulmonary nodule.
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 10. satellite_nodules
- **Name:** satellite_nodules
- **Type:** AttributeType.CHOICE
- **Description:** Presence of satellite nodules.
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 11. lymphadenopathy
- **Name:** lymphadenopathy
- **Type:** AttributeType.CHOICE
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
- **Relationship:** subset (confidence: 0.90)
- **Recommendation:** no_merge
- **AI Reasoning:** To classify the relationship between the EXISTING and INCOMING attributes, I analyzed their values. The EXISTING attribute contains the values: ['absent', 'present', 'unknown', 'indeterminate'], while the INCOMING attribute contains the values: ['present', 'absent']. All values of the INCOMING attribute are present in the EXISTING attribute. However, the EXISTING attribute has additional values ('unknown' and 'indeterminate') that the INCOMING attribute does not have. Therefore, the INCOMING attribute is a subset of the EXISTING attribute. This means that the relationship is classified as 'subset.' All incoming values are in existing. Incoming has unique values: ['unknown', 'indeterminate'], which are not present in incoming. This confirms the classification as 'subset.'

- **Shared values:** present, absent
- **Existing only values:** unknown, indeterminate

#### 2. Plurality vs number
- **Relationship:** identical (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** The EXISTING attribute 'Plurality' has values ['single', 'multiple'], and the INCOMING attribute 'number' has exactly the same values ['single', 'multiple']. All values from the incoming attribute are in the existing attribute and vice-versa. There are no additional unique values in either attribute. Therefore, the relationship is classified as 'identical'. All incoming values are in existing. Incoming has no unique values.

- **Shared values:** single, multiple

#### 3. Size vs size Finding
- **Relationship:** identical (confidence: 0.90)
- **Recommendation:** no_merge
- **AI Reasoning:** Both the EXISTING and INCOMING attributes have no values, leading to a situation where the absence of values makes them effectively identical. There are no discrepancies because there are no values to compare, allowing us to conclude that both attributes are identical. This qualifies as an 'identical' relationship as there is no unique or differing information between the existing and incoming attributes.

### New Attributes Added (6)

#### 1. status
- **Type:** AttributeType.CHOICE
- **Values:** new, stable, enlarging, decreasing
- **Description:** Status of the pulmonary nodule.

#### 2. morphology
- **Type:** AttributeType.CHOICE
- **Values:** solid, subsolid
- **Description:** Morphology of the pulmonary nodule.

#### 3. calcification
- **Type:** AttributeType.CHOICE
- **Values:** present, absent, central, diffuse, laminated, popcorn
- **Description:** Calcification of the pulmonary nodule.

#### 4. cavitation
- **Type:** AttributeType.CHOICE
- **Values:** present, absent
- **Description:** Cavitation of the pulmonary nodule.

#### 5. satellite_nodules
- **Type:** AttributeType.CHOICE
- **Values:** present, absent
- **Description:** Presence of satellite nodules.

#### 6. lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Values:** present, absent
- **Description:** Presence of lymphadenopathy.

### Required Attributes Added
None

---

## Final Attributes (19)

### 1. Morphology
- **Name:** Morphology
- **Type:** AttributeType.CHOICE
- **Values:** smooth, lobulated, Ill-defined, spiculated, perifissural, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Values:** indeterminate, left lung, left upper lobe, lingula, left lower lobe, right lung, right upper lobe, right middle lobe, right lower lobe, unknown
- **Max selected:** 1
- **Required:** False

### 3. status
- **Name:** status
- **Type:** AttributeType.CHOICE
- **Description:** Status of the pulmonary nodule.
- **Values:** new, stable, enlarging, decreasing
- **Max selected:** 1
- **Required:** True

### 4. morphology
- **Name:** morphology
- **Type:** AttributeType.CHOICE
- **Description:** Morphology of the pulmonary nodule.
- **Values:** solid, subsolid
- **Max selected:** 1
- **Required:** True

### 5. calcification
- **Name:** calcification
- **Type:** AttributeType.CHOICE
- **Description:** Calcification of the pulmonary nodule.
- **Values:** present, absent, central, diffuse, laminated, popcorn
- **Max selected:** 1
- **Required:** True

### 6. cavitation
- **Name:** cavitation
- **Type:** AttributeType.CHOICE
- **Description:** Cavitation of the pulmonary nodule.
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 7. satellite_nodules
- **Name:** satellite_nodules
- **Type:** AttributeType.CHOICE
- **Description:** Presence of satellite nodules.
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 8. lymphadenopathy
- **Name:** lymphadenopathy
- **Type:** AttributeType.CHOICE
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

### 15. Change from priors
- **Name:** Change from priors
- **Type:** AttributeType.CHOICE
- **Values:** no priors, unchanged for less than 6 months, unchanged for 6-12 months, unchanged for 12-24 months, unchanged more than 24 months, larger since prior, smaller since prior
- **Max selected:** 1
- **Required:** False

### 16. Suspicious appearance
- **Name:** Suspicious appearance
- **Type:** AttributeType.CHOICE
- **Values:** yes, no, indeterminate
- **Max selected:** 1
- **Required:** False

### 17. Min density
- **Name:** Min density
- **Type:** AttributeType.NUMERIC
- **Description:** Minimum - 1000, max +1000
- **Unit:** HU
- **Range:** 0 - 100
- **Required:** False

### 18. Max density
- **Name:** Max density
- **Type:** AttributeType.NUMERIC
- **Description:** Minimum   - 1000, max   +1000
- **Unit:** HU
- **Range:** 0 - 100
- **Required:** False

### 19. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Values:** absent, present, unknown, indeterminate
- **Max selected:** 1
- **Required:** False

---
