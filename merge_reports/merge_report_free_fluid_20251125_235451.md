# Merge Report: Free Fluid
**Timestamp:** 2025-11-25 23:54:51

**Existing Model:** ascites (ID: OIFM_GMTS_000480)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 3
  - Volume
  - Location
  - Attenuation
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 7
- **Total final attributes:** 5

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence or absence of ascites
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Whether and how a ascites has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (7)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Hemoperitoneum
- **Name:** Hemoperitoneum
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 3. Organ Injury
- **Name:** Organ Injury
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 4. Pneumoperitoneum
- **Name:** Pneumoperitoneum
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 5. Volume
- **Name:** Volume
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Small, Moderate, Large
- **Max selected:** 1
- **Required:** True

### 6. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Upper abdominal, Perihepatic, Perisplenic, Morrison's pouch, Subphrenic
- **Max selected:** 1
- **Required:** True

### 7. Attenuation
- **Name:** Attenuation
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Simple, Complex
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

#### 2. presence vs Hemoperitoneum
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Hemoperitoneum' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

#### 3. presence vs Organ Injury
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Organ Injury' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

#### 4. presence vs Pneumoperitoneum
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Pneumoperitoneum' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

### New Attributes Added (3)

#### 1. Volume
- **Type:** AttributeType.CHOICE
- **Values:** Small, Moderate, Large

#### 2. Location
- **Type:** AttributeType.CHOICE
- **Values:** Upper abdominal, Perihepatic, Perisplenic, Morrison's pouch, Subphrenic

#### 3. Attenuation
- **Type:** AttributeType.CHOICE
- **Values:** Simple, Complex

### Required Attributes Added
None

---

## Final Attributes (5)

### 1. Volume
- **Name:** Volume
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Small, Moderate, Large
- **Max selected:** 1
- **Required:** True

### 2. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Upper abdominal, Perihepatic, Perisplenic, Morrison's pouch, Subphrenic
- **Max selected:** 1
- **Required:** True

### 3. Attenuation
- **Name:** Attenuation
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Simple, Complex
- **Max selected:** 1
- **Required:** True

### 4. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of ascites
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 5. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a ascites has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
