# Merge Report: Pulmonary Emboli
**Timestamp:** 2025-11-19 23:03:55

**Existing Model:** pulmonary embolism (ID: OIFM_MSFT_932618)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 2
- **Review decisions made:** 2
  - Keep existing: 2
    - presence (kept, Presence not added)
    - presence (kept, Pulmonary infarction not added)
- **New attributes added:** 8
  - Pulmonary hypertension
  - Pulmonary artery aneurysm
  - Pulmonary hemorrhage
  - Stage
  - Location
  - Number
  - Burden
  - Right heart strain
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 10
- **Total final attributes:** 10

---

## ⚠️ Attributes Needing Review (2)

*These attributes were reviewed and decisions were made.*

### 1. presence vs Presence
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing values for the presence attribute are ['absent', 'present', 'indeterminate', 'unknown']. The incoming values are ['Present', 'Absent']. There is overlap between the two attributes, as 'Absent' and 'Present' from the incoming values correspond to 'absent' and 'present' in the existing values (case-insensitive). There are additional values in the existing attribute that are not present in the incoming attribute: 'indeterminate' and 'unknown'. Also, the incoming attribute has no unique values that are not present in the existing attribute. Therefore, this relationship falls under 'needs_review' rather than 'subset' or 'enhanced'. There is some matching, but also the uniqueness, allowing this classification.

- **Shared values:** Absent, Present
- **Existing only values:** indeterminate, unknown

### 2. presence vs Pulmonary infarction
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing attribute 'presence' has values: ['absent', 'present', 'indeterminate', 'unknown'], while the incoming attribute 'Pulmonary infarction' has values: ['Present', 'Absent']. 

Upon comparison, the shared values between the two attributes (case-insensitive) are 'present' and 'absent'. Both of these values exist in the existing attribute 'presence', but the existing attribute also contains additional values: 'indeterminate' and 'unknown'. 

All incoming values are in existing, but also, there are unique values in the existing attribute that are not present in the incoming attribute. Hence, the incoming attribute does not encompass all choices of the existing attribute. Since we have some shared values and unique values in both attributes, but the incoming does not have all values of the existing, this relationship is classified as 'needs_review'. 

Incoming has unique values: [] (none), meaning all incoming values are also in the existing. 

This does not fall under 'identical', 'enhanced', or 'subset' due to the presence of values unique to the existing attribute. Therefore, the relationship type 'needs_review' is most appropriate.

- **Shared values:** present, absent
- **Existing only values:** indeterminate, unknown

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of pulmonary embolism
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a pulmonary embolism has changed over time
- **Values:** unchanged, stable, increased, decreased, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (10)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether pulmonary emboli are present or absent.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Stage
- **Name:** Stage
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the stage of the pulmonary emboli.
- **Values:** Acute, Chronic, Subacute
- **Max selected:** 1
- **Required:** True

### 3. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the location of the pulmonary emboli.
- **Values:** Central, Right pulmonary artery, Left pulmonary artery, Lobar, Segmental, Subsegmental
- **Max selected:** 1
- **Required:** True

### 4. Number
- **Name:** Number
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the number of pulmonary emboli.
- **Values:** Single, Multiple
- **Max selected:** 1
- **Required:** True

### 5. Burden
- **Name:** Burden
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the burden of pulmonary emboli.
- **Values:** Low, Moderate, High
- **Max selected:** 1
- **Required:** True

### 6. Right heart strain
- **Name:** Right heart strain
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the presence or absence of right heart strain associated with pulmonary emboli.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 7. Pulmonary hypertension
- **Name:** Pulmonary hypertension
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the presence or absence of pulmonary hypertension associated with pulmonary emboli.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 8. Pulmonary infarction
- **Name:** Pulmonary infarction
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the presence or absence of pulmonary infarction associated with pulmonary emboli.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 9. Pulmonary artery aneurysm
- **Name:** Pulmonary artery aneurysm
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the presence or absence of pulmonary artery aneurysm associated with pulmonary emboli.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 10. Pulmonary hemorrhage
- **Name:** Pulmonary hemorrhage
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the presence or absence of pulmonary hemorrhage associated with pulmonary emboli.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

### New Attributes Added (8)

#### 1. Pulmonary hypertension
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No
- **Description:** Indicates the presence or absence of pulmonary hypertension associated with pulmonary emboli.

#### 2. Pulmonary artery aneurysm
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No
- **Description:** Indicates the presence or absence of pulmonary artery aneurysm associated with pulmonary emboli.

#### 3. Pulmonary hemorrhage
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No
- **Description:** Indicates the presence or absence of pulmonary hemorrhage associated with pulmonary emboli.

#### 4. Stage
- **Type:** AttributeType.CHOICE
- **Values:** Acute, Chronic, Subacute
- **Description:** Indicates the stage of the pulmonary emboli.

#### 5. Location
- **Type:** AttributeType.CHOICE
- **Values:** Central, Right pulmonary artery, Left pulmonary artery, Lobar, Segmental, Subsegmental
- **Description:** Indicates the location of the pulmonary emboli.

#### 6. Number
- **Type:** AttributeType.CHOICE
- **Values:** Single, Multiple
- **Description:** Indicates the number of pulmonary emboli.

#### 7. Burden
- **Type:** AttributeType.CHOICE
- **Values:** Low, Moderate, High
- **Description:** Indicates the burden of pulmonary emboli.

#### 8. Right heart strain
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No
- **Description:** Indicates the presence or absence of right heart strain associated with pulmonary emboli.

### Required Attributes Added
None

---

## Final Attributes (10)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of pulmonary embolism
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. Pulmonary hypertension
- **Name:** Pulmonary hypertension
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the presence or absence of pulmonary hypertension associated with pulmonary emboli.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 3. Pulmonary artery aneurysm
- **Name:** Pulmonary artery aneurysm
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the presence or absence of pulmonary artery aneurysm associated with pulmonary emboli.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 4. Pulmonary hemorrhage
- **Name:** Pulmonary hemorrhage
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the presence or absence of pulmonary hemorrhage associated with pulmonary emboli.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 5. Stage
- **Name:** Stage
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the stage of the pulmonary emboli.
- **Values:** Acute, Chronic, Subacute
- **Max selected:** 1
- **Required:** True

### 6. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the location of the pulmonary emboli.
- **Values:** Central, Right pulmonary artery, Left pulmonary artery, Lobar, Segmental, Subsegmental
- **Max selected:** 1
- **Required:** True

### 7. Number
- **Name:** Number
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the number of pulmonary emboli.
- **Values:** Single, Multiple
- **Max selected:** 1
- **Required:** True

### 8. Burden
- **Name:** Burden
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the burden of pulmonary emboli.
- **Values:** Low, Moderate, High
- **Max selected:** 1
- **Required:** True

### 9. Right heart strain
- **Name:** Right heart strain
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the presence or absence of right heart strain associated with pulmonary emboli.
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 10. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a pulmonary embolism has changed over time
- **Values:** unchanged, stable, increased, decreased, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
