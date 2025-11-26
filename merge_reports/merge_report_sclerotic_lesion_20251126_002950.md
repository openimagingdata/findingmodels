# Merge Report: Sclerotic Lesion
**Timestamp:** 2025-11-26 00:29:50

**Existing Model:** solitary osteosclerotic bone lesion (ID: OIFM_GMTS_010984)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 2
  - location
  - density
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 4
- **Total final attributes:** 4

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence or absence of solitary osteosclerotic bone lesion
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Whether and how a solitary osteosclerotic bone lesion has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (4)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Indicates whether the sclerotic lesion is present or absent.
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 2. status
- **Name:** status
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Indicates the status of the sclerotic lesion.
- **Values:** stable, enlarging
- **Max selected:** 1
- **Required:** True

### 3. location
- **Name:** location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the location of the sclerotic lesion in the bone.
- **Values:** Not specified, Frontal bone, Occipital bone, Temporal bone, Parietal bone, Maxilla, Mandible
- **Max selected:** 1
- **Required:** False

### 4. density
- **Name:** density
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Description:** Indicates the density of the sclerotic lesion.
- **Unit:** HU
- **Range:** 1000 - None
- **Required:** False

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (2)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. presence vs presence
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'presence' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** present, absent

#### 2. change from prior vs status
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard change_from_prior values. Incoming attribute 'status' will be discarded.

- **Existing only values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Incoming only values:** stable, enlarging

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

### 1. location
- **Name:** location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the location of the sclerotic lesion in the bone.
- **Values:** Not specified, Frontal bone, Occipital bone, Temporal bone, Parietal bone, Maxilla, Mandible
- **Max selected:** 1
- **Required:** False

### 2. density
- **Name:** density
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Description:** Indicates the density of the sclerotic lesion.
- **Unit:** HU
- **Range:** 1000 - None
- **Required:** False

### 3. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of solitary osteosclerotic bone lesion
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 4. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a solitary osteosclerotic bone lesion has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
