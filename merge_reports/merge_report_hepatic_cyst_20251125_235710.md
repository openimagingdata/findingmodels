# Merge Report: Hepatic Cyst
**Timestamp:** 2025-11-25 23:57:10

**Existing Model:** cystic liver lesion (ID: OIFM_GMTS_005486)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 3
  - Multiplicity
  - Location
  - Size of largest cyst
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 4
- **Total final attributes:** 5

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence or absence of cystic liver lesion
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Whether and how a cystic liver lesion has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (4)

### 1. Stability
- **Name:** Stability
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** The stability of the cyst.
- **Values:** Unchanged, Increased, Decreased
- **Max selected:** 1
- **Required:** True

### 2. Multiplicity
- **Name:** Multiplicity
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The number of cysts present.
- **Values:** Single, Multiple
- **Max selected:** 1
- **Required:** True

### 3. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The specific location of the cyst.
- **Values:** Hepatic (unspecified), Left hepatic lobe, Right hepatic lobe, Hepatic segment 1, Hepatic segment 2, Hepatic segment 3, Hepatic segment 4a, Hepatic segment 4b, Hepatic segment 5, Hepatic segment 6, Hepatic segment 7, Hepatic segment 8
- **Max selected:** 1
- **Required:** True

### 4. Size of largest cyst
- **Name:** Size of largest cyst
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Description:** The size of the largest cyst in centimeters.
- **Unit:** cm
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (1)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. change from prior vs Stability
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard change_from_prior values. Incoming attribute 'Stability' will be discarded.

- **Existing only values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Incoming only values:** Unchanged, Increased, Decreased

### New Attributes Added (3)

#### 1. Multiplicity
- **Type:** AttributeType.CHOICE
- **Values:** Single, Multiple
- **Description:** The number of cysts present.

#### 2. Location
- **Type:** AttributeType.CHOICE
- **Values:** Hepatic (unspecified), Left hepatic lobe, Right hepatic lobe, Hepatic segment 1, Hepatic segment 2, Hepatic segment 3, Hepatic segment 4a, Hepatic segment 4b, Hepatic segment 5, Hepatic segment 6, Hepatic segment 7, Hepatic segment 8
- **Description:** The specific location of the cyst.

#### 3. Size of largest cyst
- **Type:** AttributeType.NUMERIC
- **Unit:** cm
- **Description:** The size of the largest cyst in centimeters.

### Required Attributes Added
None

---

## Final Attributes (5)

### 1. Multiplicity
- **Name:** Multiplicity
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The number of cysts present.
- **Values:** Single, Multiple
- **Max selected:** 1
- **Required:** True

### 2. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The specific location of the cyst.
- **Values:** Hepatic (unspecified), Left hepatic lobe, Right hepatic lobe, Hepatic segment 1, Hepatic segment 2, Hepatic segment 3, Hepatic segment 4a, Hepatic segment 4b, Hepatic segment 5, Hepatic segment 6, Hepatic segment 7, Hepatic segment 8
- **Max selected:** 1
- **Required:** True

### 3. Size of largest cyst
- **Name:** Size of largest cyst
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Description:** The size of the largest cyst in centimeters.
- **Unit:** cm
- **Required:** True

### 4. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of cystic liver lesion
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 5. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a cystic liver lesion has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
