# Merge Report: Sclerotic Lesion
**Timestamp:** 2025-11-19 23:12:32

**Existing Model:** multiple osteosclerotic bone lesions (ID: OIFM_GMTS_011005)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 1
- **Review decisions made:** 1
  - Keep existing: 1
    - change from prior (kept, status not added)
- **New attributes added:** 2
  - location
  - density
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 4
- **Total final attributes:** 4

---

## ⚠️ Attributes Needing Review (1)

*These attributes were reviewed and decisions were made.*

### 1. change from prior vs status
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing attribute has the values ['unchanged', 'stable', 'new', 'resolved', 'increased', 'decreased', 'larger', 'smaller']. The incoming attribute has the values ['stable', 'enlarging']. There is one shared value 'stable' between the two attributes. Each attribute has unique values: The existing attribute has unique values ['unchanged', 'new', 'resolved', 'increased', 'decreased', 'larger', 'smaller'], which are not present in the incoming attribute. The incoming attribute has the unique value 'enlarging' that is not present in the existing attribute. Therefore, this relationship is classified as 'needs_review' because there are shared values, but each attribute also has values that are unique to them. However, the incoming attribute does not have every value from the existing attribute, and vice versa.

- **Shared values:** stable
- **Existing only values:** unchanged, new, resolved, increased, decreased, larger, smaller
- **Incoming only values:** enlarging

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of multiple osteosclerotic bone lesions
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a multiple osteosclerotic bone lesions has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (4)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether the sclerotic lesion is present or absent.
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 2. status
- **Name:** status
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the status of the sclerotic lesion.
- **Values:** stable, enlarging
- **Max selected:** 1
- **Required:** True

### 3. location
- **Name:** location
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the location of the sclerotic lesion in the bone.
- **Values:** Not specified, Frontal bone, Occipital bone, Temporal bone, Parietal bone, Maxilla, Mandible
- **Max selected:** 1
- **Required:** False

### 4. density
- **Name:** density
- **Type:** AttributeType.NUMERIC
- **Description:** Indicates the density of the sclerotic lesion.
- **Unit:** HU
- **Range:** 1000 - None
- **Required:** False

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (1)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. presence vs presence
- **Relationship:** subset (confidence: 0.90)
- **Recommendation:** no_merge
- **AI Reasoning:** The EXISTING attribute has the values: ['absent', 'present', 'indeterminate', 'unknown']. The INCOMING attribute has the values: ['present', 'absent']. All incoming values (present, absent) are found within the existing values. However, the existing attribute has additional values (indeterminate, unknown) that are not present in the incoming attribute. Thus, the relationship is classified as 'subset' because all incoming values are contained in existing, and existing has more unique values. All incoming values are in existing. Incoming has no unique values.

- **Shared values:** present, absent
- **Existing only values:** indeterminate, unknown

### New Attributes Added (2)

#### 1. location
- **Type:** AttributeType.CHOICE
- **Values:** Not specified, Frontal bone, Occipital bone, Temporal bone, Parietal bone, Maxilla, Mandible
- **Description:** Indicates the location of the sclerotic lesion in the bone.

#### 2. density
- **Type:** AttributeType.NUMERIC
- **Unit:** HU
- **Range:** 1000 - None
- **Description:** Indicates the density of the sclerotic lesion.

### Required Attributes Added
None

---

## Final Attributes (4)

### 1. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a multiple osteosclerotic bone lesions has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

### 2. location
- **Name:** location
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the location of the sclerotic lesion in the bone.
- **Values:** Not specified, Frontal bone, Occipital bone, Temporal bone, Parietal bone, Maxilla, Mandible
- **Max selected:** 1
- **Required:** False

### 3. density
- **Name:** density
- **Type:** AttributeType.NUMERIC
- **Description:** Indicates the density of the sclerotic lesion.
- **Unit:** HU
- **Range:** 1000 - None
- **Required:** False

### 4. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of multiple osteosclerotic bone lesions
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

---
