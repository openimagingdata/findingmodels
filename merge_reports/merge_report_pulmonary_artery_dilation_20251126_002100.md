# Merge Report: Pulmonary Artery Dilation
**Timestamp:** 2025-11-26 00:21:00

**Existing Model:** large main pulmonary artery (ID: OIFM_GMTS_013910)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 4
  - Diameter
  - Location
  - Pulmonary Hypertension
  - Right Heart Strain
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 6
- **Total final attributes:** 6

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence or absence of large main pulmonary artery
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Whether and how a large main pulmonary artery has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (6)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Pulmonary Embolism
- **Name:** Pulmonary Embolism
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 3. Diameter
- **Name:** Diameter
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Unit:** mm
- **Range:** 0 - None
- **Required:** True

### 4. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Main pulmonary artery, Right pulmonary artery, Left pulmonary artery
- **Max selected:** 1
- **Required:** True

### 5. Pulmonary Hypertension
- **Name:** Pulmonary Hypertension
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Suspected, Confirmed
- **Max selected:** 1
- **Required:** False

### 6. Right Heart Strain
- **Name:** Right Heart Strain
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (2)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. presence vs Presence
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Presence' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

#### 2. presence vs Pulmonary Embolism
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Pulmonary Embolism' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

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

#### 4. Right Heart Strain
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

### Required Attributes Added
None

---

## Final Attributes (6)

### 1. Diameter
- **Name:** Diameter
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Unit:** mm
- **Range:** 0 - None
- **Required:** True

### 2. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Main pulmonary artery, Right pulmonary artery, Left pulmonary artery
- **Max selected:** 1
- **Required:** True

### 3. Pulmonary Hypertension
- **Name:** Pulmonary Hypertension
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Suspected, Confirmed
- **Max selected:** 1
- **Required:** False

### 4. Right Heart Strain
- **Name:** Right Heart Strain
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 5. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of large main pulmonary artery
- **Values:** absent, present, indeterminate, unknown
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
