# Merge Report: Nephrolithiasis
**Timestamp:** 2025-11-26 00:07:35

**Existing Model:** shadowing mass in renal collecting system (ID: OIFM_GMTS_016996)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 6
  - Number of Stones
  - Location
  - Stone Size
  - Hydroureter
  - Perinephric Stranding
  - Ureteral obstruction
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 8
- **Total final attributes:** 8

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence or absence of shadowing mass in renal collecting system
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Whether and how a shadowing mass in renal collecting system has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (8)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence of nephrolithiasis
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Hydronephrosis
- **Name:** Hydronephrosis
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence of hydronephrosis
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 3. Number of Stones
- **Name:** Number of Stones
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Number of kidney stones
- **Values:** Single, Multiple
- **Max selected:** 1
- **Required:** False

### 4. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Location of the kidney stones
- **Values:** Right kidney, Left kidney, Both kidneys
- **Max selected:** 1
- **Required:** False

### 5. Stone Size
- **Name:** Stone Size
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Size of the kidney stones
- **Values:** <5mm, 5-10mm, >10mm
- **Max selected:** 1
- **Required:** False

### 6. Hydroureter
- **Name:** Hydroureter
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of hydroureter
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 7. Perinephric Stranding
- **Name:** Perinephric Stranding
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of perinephric stranding
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 8. Ureteral obstruction
- **Name:** Ureteral obstruction
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of ureteral obstruction
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

#### 2. presence vs Hydronephrosis
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Hydronephrosis' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

### New Attributes Added (6)

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

#### 4. Hydroureter
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of hydroureter

#### 5. Perinephric Stranding
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of perinephric stranding

#### 6. Ureteral obstruction
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of ureteral obstruction

### Required Attributes Added
None

---

## Final Attributes (8)

### 1. Number of Stones
- **Name:** Number of Stones
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Number of kidney stones
- **Values:** Single, Multiple
- **Max selected:** 1
- **Required:** False

### 2. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Location of the kidney stones
- **Values:** Right kidney, Left kidney, Both kidneys
- **Max selected:** 1
- **Required:** False

### 3. Stone Size
- **Name:** Stone Size
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Size of the kidney stones
- **Values:** <5mm, 5-10mm, >10mm
- **Max selected:** 1
- **Required:** False

### 4. Hydroureter
- **Name:** Hydroureter
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of hydroureter
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 5. Perinephric Stranding
- **Name:** Perinephric Stranding
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of perinephric stranding
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 6. Ureteral obstruction
- **Name:** Ureteral obstruction
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence of ureteral obstruction
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 7. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of shadowing mass in renal collecting system
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 8. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a shadowing mass in renal collecting system has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
