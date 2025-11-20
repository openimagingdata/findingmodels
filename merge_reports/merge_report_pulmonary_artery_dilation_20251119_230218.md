# Merge Report: Pulmonary Artery Dilation
**Timestamp:** 2025-11-19 23:02:18

**Existing Model:** large main pulmonary artery (ID: OIFM_GMTS_013910)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 2
- **Review decisions made:** 2
  - Keep existing: 2
    - presence (kept, Presence not added)
    - presence (kept, Right Heart Strain not added)
- **New attributes added:** 4
  - Diameter
  - Location
  - Pulmonary Hypertension
  - Pulmonary Embolism
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 6
- **Total final attributes:** 6

---

## ⚠️ Attributes Needing Review (2)

*These attributes were reviewed and decisions were made.*

### 1. presence vs Presence
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing attribute values are ['absent', 'present', 'indeterminate', 'unknown'] and the incoming attribute values are ['Present', 'Absent']. The values share two matches: 'absent' (existing) and 'Present' (incoming, but case-insensitively equal to 'present' in existing). Therefore, we have some overlap. However, the existing attribute has additional unique values: 'indeterminate' and 'unknown'. Similarly, the incoming attribute has unique values 'Present' and 'Absent' from which 'Present' and 'Absent' (case-insensitively) correlate to values in the existing attribute. So, we have shared values and unique values in both attributes. Thus, this relationship should be classified as 'needs_review' due to the partial overlaps and unique values on both sides.

- **Shared values:** absent, present
- **Existing only values:** indeterminate, unknown
- **Incoming only values:** Present, Absent

### 2. presence vs Right Heart Strain
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing attribute 'presence' has values: ['absent', 'present', 'indeterminate', 'unknown']. The incoming attribute 'Right Heart Strain' has values: ['Present', 'Absent']. When we compare these attributes, the shared values are ['Present', 'Absent'], ignoring case sensitivity. Both attributes also have unique values: the existing attribute has ['indeterminate', 'unknown'], while the incoming attribute has no additional unique values beyond the shared ones. Therefore, we have some shared values, but each attribute has its own unique values, hence this relationship is classified as 'needs_review'. All incoming values: ['Present', 'Absent'] are not completely in existing since it lacks 'indeterminate' and 'unknown' from the existing. Incoming has no unique values since it only shares values with the existing and does not add anything new.

- **Shared values:** present, absent
- **Existing only values:** indeterminate, unknown

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of large main pulmonary artery
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a large main pulmonary artery has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (6)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Diameter
- **Name:** Diameter
- **Type:** AttributeType.NUMERIC
- **Unit:** mm
- **Range:** 0 - None
- **Required:** True

### 3. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Values:** Main pulmonary artery, Right pulmonary artery, Left pulmonary artery
- **Max selected:** 1
- **Required:** True

### 4. Pulmonary Hypertension
- **Name:** Pulmonary Hypertension
- **Type:** AttributeType.CHOICE
- **Values:** Suspected, Confirmed
- **Max selected:** 1
- **Required:** False

### 5. Right Heart Strain
- **Name:** Right Heart Strain
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 6. Pulmonary Embolism
- **Name:** Pulmonary Embolism
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

### New Attributes Added (4)

#### 1. Diameter
- **Type:** AttributeType.NUMERIC
- **Unit:** mm
- **Range:** 0 - None

#### 2. Location
- **Type:** AttributeType.CHOICE
- **Values:** Main pulmonary artery, Right pulmonary artery, Left pulmonary artery

#### 3. Pulmonary Hypertension
- **Type:** AttributeType.CHOICE
- **Values:** Suspected, Confirmed

#### 4. Pulmonary Embolism
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

### Required Attributes Added
None

---

## Final Attributes (6)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of large main pulmonary artery
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. Diameter
- **Name:** Diameter
- **Type:** AttributeType.NUMERIC
- **Unit:** mm
- **Range:** 0 - None
- **Required:** True

### 3. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Values:** Main pulmonary artery, Right pulmonary artery, Left pulmonary artery
- **Max selected:** 1
- **Required:** True

### 4. Pulmonary Hypertension
- **Name:** Pulmonary Hypertension
- **Type:** AttributeType.CHOICE
- **Values:** Suspected, Confirmed
- **Max selected:** 1
- **Required:** False

### 5. Pulmonary Embolism
- **Name:** Pulmonary Embolism
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 6. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a large main pulmonary artery has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
