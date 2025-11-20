# Merge Report: Pulmonary Artery Catheter
**Timestamp:** 2025-11-19 23:00:52

**Existing Model:** pulmonary artery catheterization (ID: OIFM_GMTS_030927)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 6
  - Status
  - Appropriate location
  - Insertion Site
  - Side Finding
  - Distal tip location
  - Balloon Inflation
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 7
- **Total final attributes:** 8

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of pulmonary artery catheterization
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a pulmonary artery catheterization has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (7)

### 1. Presence of Pulmonary Artery Catheter
- **Name:** Presence of Pulmonary Artery Catheter
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether a pulmonary artery catheter is present or absent
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the status of the pulmonary artery catheter
- **Values:** New placement, Unchanged, Complication, Removed
- **Max selected:** 1
- **Required:** True

### 3. Appropriate location
- **Name:** Appropriate location
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether the catheter is at the appropriate location
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 4. Insertion Site
- **Name:** Insertion Site
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the site of catheter insertion
- **Values:** Internal jugular, Subclavian, Femoral
- **Max selected:** 1
- **Required:** True

### 5. Side Finding
- **Name:** Side Finding
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the side of catheter placement
- **Values:** Left, Right, NA
- **Max selected:** 1
- **Required:** True

### 6. Distal tip location
- **Name:** Distal tip location
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the location of the distal tip of the catheter
- **Values:** Main pulmonary artery, Right pulmonary artery, Left pulmonary artery
- **Max selected:** 1
- **Required:** True

### 7. Balloon Inflation
- **Name:** Balloon Inflation
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether the balloon of the catheter is inflated or not at the time of imaging
- **Values:** Inflated, Not inflated
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (1)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. presence vs Presence of Pulmonary Artery Catheter
- **Relationship:** subset (confidence: 0.95)
- **Recommendation:** no_merge
- **AI Reasoning:** I classified the relationship as 'subset' because all values from the INCOMING attribute are found in the EXISTING attribute, and the EXISTING attribute has additional values. The EXISTING values are ['absent', 'present', 'indeterminate', 'unknown'], while the INCOMING values are ['Present', 'Absent']. When normalized for case, the shared values are 'absent' and 'present'. This demonstrates that all incoming values are in existing: 'All incoming values are in existing'. The EXISTING attribute includes unique values: ['indeterminate', 'unknown'], meaning the INCOMING attribute has no unique values. This confirms that the relationship is 'subset', where EXISTING has more values than INCOMING, thus the recommendation is 'no_merge'.

- **Shared values:** absent, present
- **Existing only values:** indeterminate, unknown

### New Attributes Added (6)

#### 1. Status
- **Type:** AttributeType.CHOICE
- **Values:** New placement, Unchanged, Complication, Removed
- **Description:** Indicates the status of the pulmonary artery catheter

#### 2. Appropriate location
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No
- **Description:** Indicates whether the catheter is at the appropriate location

#### 3. Insertion Site
- **Type:** AttributeType.CHOICE
- **Values:** Internal jugular, Subclavian, Femoral
- **Description:** Indicates the site of catheter insertion

#### 4. Side Finding
- **Type:** AttributeType.CHOICE
- **Values:** Left, Right, NA
- **Description:** Indicates the side of catheter placement

#### 5. Distal tip location
- **Type:** AttributeType.CHOICE
- **Values:** Main pulmonary artery, Right pulmonary artery, Left pulmonary artery
- **Description:** Indicates the location of the distal tip of the catheter

#### 6. Balloon Inflation
- **Type:** AttributeType.CHOICE
- **Values:** Inflated, Not inflated
- **Description:** Indicates whether the balloon of the catheter is inflated or not at the time of imaging

### Required Attributes Added
None

---

## Final Attributes (8)

### 1. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the status of the pulmonary artery catheter
- **Values:** New placement, Unchanged, Complication, Removed
- **Max selected:** 1
- **Required:** True

### 2. Appropriate location
- **Name:** Appropriate location
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether the catheter is at the appropriate location
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 3. Insertion Site
- **Name:** Insertion Site
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the site of catheter insertion
- **Values:** Internal jugular, Subclavian, Femoral
- **Max selected:** 1
- **Required:** True

### 4. Side Finding
- **Name:** Side Finding
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the side of catheter placement
- **Values:** Left, Right, NA
- **Max selected:** 1
- **Required:** True

### 5. Distal tip location
- **Name:** Distal tip location
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the location of the distal tip of the catheter
- **Values:** Main pulmonary artery, Right pulmonary artery, Left pulmonary artery
- **Max selected:** 1
- **Required:** True

### 6. Balloon Inflation
- **Name:** Balloon Inflation
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether the balloon of the catheter is inflated or not at the time of imaging
- **Values:** Inflated, Not inflated
- **Max selected:** 1
- **Required:** True

### 7. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of pulmonary artery catheterization
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 8. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a pulmonary artery catheterization has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
