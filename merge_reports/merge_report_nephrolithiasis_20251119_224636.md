# Merge Report: Nephrolithiasis
**Timestamp:** 2025-11-19 22:46:36

**Existing Model:** shadowing mass in renal collecting system (ID: OIFM_GMTS_016996)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 1
- **Review decisions made:** 1
  - Keep existing: 1
    - presence (kept, Presence not added)
- **New attributes added:** 7
  - Number of Stones
  - Location
  - Stone Size
  - Hydronephrosis
  - Hydroureter
  - Perinephric Stranding
  - Ureteral obstruction
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 8
- **Total final attributes:** 9

---

## ⚠️ Attributes Needing Review (1)

*These attributes were reviewed and decisions were made.*

### 1. presence vs Presence
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** I classified the relationship as 'needs_review' because while there are shared values between the EXISTING and INCOMING attributes, each also contains unique values not present in the other. The shared values are ['present', 'absent'], which are both present in the EXISTING attribute as well as the INCOMING attribute (case insensitive). However, the EXISTING attribute has additional values ['indeterminate', 'unknown'], which are not found in the INCOMING attribute, and the INCOMING attribute does not add any new values not already in EXISTING. Thus, they do not perfectly overlap, nor does one completely contain the other as subsets or enhancements. This leads to the classification of 'needs_review'.

- **Shared values:** present, absent
- **Existing only values:** indeterminate, unknown

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of shadowing mass in renal collecting system
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a shadowing mass in renal collecting system has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (8)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence of nephrolithiasis
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Number of Stones
- **Name:** Number of Stones
- **Type:** AttributeType.CHOICE
- **Description:** Number of kidney stones
- **Values:** Single, Multiple
- **Max selected:** 1
- **Required:** False

### 3. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Description:** Location of the kidney stones
- **Values:** Right kidney, Left kidney, Both kidneys
- **Max selected:** 1
- **Required:** False

### 4. Stone Size
- **Name:** Stone Size
- **Type:** AttributeType.CHOICE
- **Description:** Size of the kidney stones
- **Values:** <5mm, 5-10mm, >10mm
- **Max selected:** 1
- **Required:** False

### 5. Hydronephrosis
- **Name:** Hydronephrosis
- **Type:** AttributeType.CHOICE
- **Description:** Presence of hydronephrosis
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 6. Hydroureter
- **Name:** Hydroureter
- **Type:** AttributeType.CHOICE
- **Description:** Presence of hydroureter
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 7. Perinephric Stranding
- **Name:** Perinephric Stranding
- **Type:** AttributeType.CHOICE
- **Description:** Presence of perinephric stranding
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 8. Ureteral obstruction
- **Name:** Ureteral obstruction
- **Type:** AttributeType.CHOICE
- **Description:** Presence of ureteral obstruction
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

### New Attributes Added (7)

#### 1. Number of Stones
- **Type:** AttributeType.CHOICE
- **Values:** Single, Multiple
- **Description:** Number of kidney stones

#### 2. Location
- **Type:** AttributeType.CHOICE
- **Values:** Right kidney, Left kidney, Both kidneys
- **Description:** Location of the kidney stones

#### 3. Stone Size
- **Type:** AttributeType.CHOICE
- **Values:** <5mm, 5-10mm, >10mm
- **Description:** Size of the kidney stones

#### 4. Hydronephrosis
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of hydronephrosis

#### 5. Hydroureter
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of hydroureter

#### 6. Perinephric Stranding
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of perinephric stranding

#### 7. Ureteral obstruction
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of ureteral obstruction

### Required Attributes Added
None

---

## Final Attributes (9)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of shadowing mass in renal collecting system
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. Number of Stones
- **Name:** Number of Stones
- **Type:** AttributeType.CHOICE
- **Description:** Number of kidney stones
- **Values:** Single, Multiple
- **Max selected:** 1
- **Required:** False

### 3. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Description:** Location of the kidney stones
- **Values:** Right kidney, Left kidney, Both kidneys
- **Max selected:** 1
- **Required:** False

### 4. Stone Size
- **Name:** Stone Size
- **Type:** AttributeType.CHOICE
- **Description:** Size of the kidney stones
- **Values:** <5mm, 5-10mm, >10mm
- **Max selected:** 1
- **Required:** False

### 5. Hydronephrosis
- **Name:** Hydronephrosis
- **Type:** AttributeType.CHOICE
- **Description:** Presence of hydronephrosis
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 6. Hydroureter
- **Name:** Hydroureter
- **Type:** AttributeType.CHOICE
- **Description:** Presence of hydroureter
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 7. Perinephric Stranding
- **Name:** Perinephric Stranding
- **Type:** AttributeType.CHOICE
- **Description:** Presence of perinephric stranding
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 8. Ureteral obstruction
- **Name:** Ureteral obstruction
- **Type:** AttributeType.CHOICE
- **Description:** Presence of ureteral obstruction
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 9. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a shadowing mass in renal collecting system has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
