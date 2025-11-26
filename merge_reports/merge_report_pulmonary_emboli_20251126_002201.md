# Merge Report: Pulmonary Emboli
**Timestamp:** 2025-11-26 00:22:01

**Existing Model:** pulmonary embolism (ID: OIFM_MSFT_932618)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 6
  - Stage
  - Location
  - Number
  - Burden
  - Right heart strain
  - Pulmonary hypertension
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 10
- **Total final attributes:** 8

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence or absence of pulmonary embolism
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Whether and how a pulmonary embolism has changed over time
- **Values:** unchanged, stable, increased, decreased, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (10)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Indicates whether pulmonary emboli are present or absent.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Pulmonary infarction
- **Name:** Pulmonary infarction
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Indicates the presence or absence of pulmonary infarction associated with pulmonary emboli.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 3. Pulmonary artery aneurysm
- **Name:** Pulmonary artery aneurysm
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Indicates the presence or absence of pulmonary artery aneurysm associated with pulmonary emboli.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 4. Pulmonary hemorrhage
- **Name:** Pulmonary hemorrhage
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Indicates the presence or absence of pulmonary hemorrhage associated with pulmonary emboli.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 5. Stage
- **Name:** Stage
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the stage of the pulmonary emboli.
- **Values:** Acute, Chronic, Subacute
- **Max selected:** 1
- **Required:** True

### 6. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the location of the pulmonary emboli.
- **Values:** Central, Right pulmonary artery, Left pulmonary artery, Lobar, Segmental, Subsegmental
- **Max selected:** 1
- **Required:** True

### 7. Number
- **Name:** Number
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the number of pulmonary emboli.
- **Values:** Single, Multiple
- **Max selected:** 1
- **Required:** True

### 8. Burden
- **Name:** Burden
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the burden of pulmonary emboli.
- **Values:** Low, Moderate, High
- **Max selected:** 1
- **Required:** True

### 9. Right heart strain
- **Name:** Right heart strain
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the presence or absence of right heart strain associated with pulmonary emboli.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 10. Pulmonary hypertension
- **Name:** Pulmonary hypertension
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the presence or absence of pulmonary hypertension associated with pulmonary emboli.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (4)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. presence vs Presence
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Presence' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

#### 2. presence vs Pulmonary infarction
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Pulmonary infarction' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

#### 3. presence vs Pulmonary artery aneurysm
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Pulmonary artery aneurysm' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Yes, No

#### 4. presence vs Pulmonary hemorrhage
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Pulmonary hemorrhage' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Yes, No

### New Attributes Added (6)

#### 1. Stage
- **Type:** AttributeType.CHOICE
- **Values:** Acute, Chronic, Subacute
- **Description:** Indicates the stage of the pulmonary emboli.

#### 2. Location
- **Type:** AttributeType.CHOICE
- **Values:** Central, Right pulmonary artery, Left pulmonary artery, Lobar, Segmental, Subsegmental
- **Description:** Indicates the location of the pulmonary emboli.

#### 3. Number
- **Type:** AttributeType.CHOICE
- **Values:** Single, Multiple
- **Description:** Indicates the number of pulmonary emboli.

#### 4. Burden
- **Type:** AttributeType.CHOICE
- **Values:** Low, Moderate, High
- **Description:** Indicates the burden of pulmonary emboli.

#### 5. Right heart strain
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No
- **Description:** Indicates the presence or absence of right heart strain associated with pulmonary emboli.

#### 6. Pulmonary hypertension
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No
- **Description:** Indicates the presence or absence of pulmonary hypertension associated with pulmonary emboli.

### Required Attributes Added
None

---

## Final Attributes (8)

### 1. Stage
- **Name:** Stage
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the stage of the pulmonary emboli.
- **Values:** Acute, Chronic, Subacute
- **Max selected:** 1
- **Required:** True

### 2. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the location of the pulmonary emboli.
- **Values:** Central, Right pulmonary artery, Left pulmonary artery, Lobar, Segmental, Subsegmental
- **Max selected:** 1
- **Required:** True

### 3. Number
- **Name:** Number
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the number of pulmonary emboli.
- **Values:** Single, Multiple
- **Max selected:** 1
- **Required:** True

### 4. Burden
- **Name:** Burden
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the burden of pulmonary emboli.
- **Values:** Low, Moderate, High
- **Max selected:** 1
- **Required:** True

### 5. Right heart strain
- **Name:** Right heart strain
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the presence or absence of right heart strain associated with pulmonary emboli.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 6. Pulmonary hypertension
- **Name:** Pulmonary hypertension
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Indicates the presence or absence of pulmonary hypertension associated with pulmonary emboli.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 7. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of pulmonary embolism
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 8. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a pulmonary embolism has changed over time
- **Values:** unchanged, stable, increased, decreased, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
