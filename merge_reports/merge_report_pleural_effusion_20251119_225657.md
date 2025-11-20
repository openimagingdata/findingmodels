# Merge Report: Pleural Effusion
**Timestamp:** 2025-11-19 22:56:57

**Existing Model:** Pleural Effusion (ID: OIFM_CDE_000254)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 5
  - side Finding
  - size Finding
  - density
  - chronicity
  - associated_features
- **Required attributes added:** 1
- **Total existing attributes:** 1
- **Total incoming attributes:** 5
- **Total final attributes:** 7

---

## Existing Attributes (1)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Description:** Is pleural effusion present?
- **Values:** present, absent, indeterminant, unknown
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (5)

### 1. side Finding
- **Name:** side Finding
- **Type:** AttributeType.CHOICE
- **Description:** The side of the pleural effusion.
- **Values:** left, right, bilateral
- **Max selected:** 1
- **Required:** True

### 2. size Finding
- **Name:** size Finding
- **Type:** AttributeType.CHOICE
- **Description:** The size of the pleural effusion.
- **Values:** small, moderate, large
- **Max selected:** 1
- **Required:** True

### 3. density
- **Name:** density
- **Type:** AttributeType.CHOICE
- **Description:** The density of the pleural effusion.
- **Values:** fluid density, intermediate density (>30 HU), hemothorax
- **Max selected:** 1
- **Required:** True

### 4. chronicity
- **Name:** chronicity
- **Type:** AttributeType.CHOICE
- **Description:** The chronicity of the pleural effusion.
- **Values:** new, chronic
- **Max selected:** 1
- **Required:** True

### 5. associated_features
- **Name:** associated_features
- **Type:** AttributeType.CHOICE
- **Description:** The associated features of the pleural effusion.
- **Values:** loculation, pleural thickening, pleural enhancement, presence of gas, atelectasis of the underlying lungs
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

### New Attributes Added (5)

#### 1. side Finding
- **Type:** AttributeType.CHOICE
- **Values:** left, right, bilateral
- **Description:** The side of the pleural effusion.

#### 2. size Finding
- **Type:** AttributeType.CHOICE
- **Values:** small, moderate, large
- **Description:** The size of the pleural effusion.

#### 3. density
- **Type:** AttributeType.CHOICE
- **Values:** fluid density, intermediate density (>30 HU), hemothorax
- **Description:** The density of the pleural effusion.

#### 4. chronicity
- **Type:** AttributeType.CHOICE
- **Values:** new, chronic
- **Description:** The chronicity of the pleural effusion.

#### 5. associated_features
- **Type:** AttributeType.CHOICE
- **Values:** loculation, pleural thickening, pleural enhancement, presence of gas, atelectasis of the underlying lungs
- **Description:** The associated features of the pleural effusion.

### Required Attributes Added (1)

#### change from prior
- **Type:** choice
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

---

## Final Attributes (7)

### 1. side Finding
- **Name:** side Finding
- **Type:** AttributeType.CHOICE
- **Description:** The side of the pleural effusion.
- **Values:** left, right, bilateral
- **Max selected:** 1
- **Required:** True

### 2. size Finding
- **Name:** size Finding
- **Type:** AttributeType.CHOICE
- **Description:** The size of the pleural effusion.
- **Values:** small, moderate, large
- **Max selected:** 1
- **Required:** True

### 3. density
- **Name:** density
- **Type:** AttributeType.CHOICE
- **Description:** The density of the pleural effusion.
- **Values:** fluid density, intermediate density (>30 HU), hemothorax
- **Max selected:** 1
- **Required:** True

### 4. chronicity
- **Name:** chronicity
- **Type:** AttributeType.CHOICE
- **Description:** The chronicity of the pleural effusion.
- **Values:** new, chronic
- **Max selected:** 1
- **Required:** True

### 5. associated_features
- **Name:** associated_features
- **Type:** AttributeType.CHOICE
- **Description:** The associated features of the pleural effusion.
- **Values:** loculation, pleural thickening, pleural enhancement, presence of gas, atelectasis of the underlying lungs
- **Max selected:** 1
- **Required:** True

### 6. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Description:** Is pleural effusion present?
- **Values:** present, absent, indeterminant, unknown
- **Max selected:** 1
- **Required:** False

### 7. change from prior
- **Name:** change from prior
- **Type:** choice
- **Description:** Whether and how a Pleural Effusion has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
