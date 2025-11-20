# Merge Report: Hepatic Cyst
**Timestamp:** 2025-11-19 22:35:54

**Existing Model:** cystic liver lesion (ID: OIFM_GMTS_005486)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 1
- **Review decisions made:** 1
  - Keep existing: 1
    - change from prior (kept, Stability not added)
- **New attributes added:** 3
  - Multiplicity
  - Location
  - Size of largest cyst
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 4
- **Total final attributes:** 5

---

## ⚠️ Attributes Needing Review (1)

*These attributes were reviewed and decisions were made.*

### 1. change from prior vs Stability
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing attribute 'change from prior' has the values ['unchanged', 'stable', 'new', 'resolved', 'increased', 'decreased', 'larger', 'smaller'] and the incoming attribute 'Stability' has the values ['Unchanged', 'Increased', 'Decreased']. There are some shared values: 'unchanged', 'increased', and 'decreased' (case insensitive match). However, both attributes also have unique values: the existing attribute has 'stable', 'new', 'resolved', 'larger', 'smaller', while the incoming attribute has no unique values beyond what exists, since all incoming values are somewhere in existing. Thus, the relationship is classified as 'needs_review'. All incoming values are in existing, indicating some potential overlap, but not all values are shared; the unique values imply a distinction between the two. Incoming has no unique values: [] and existing has unique values: ['stable', 'new', 'resolved', 'larger', 'smaller'].

- **Shared values:** unchanged, increased, decreased
- **Existing only values:** stable, new, resolved, larger, smaller

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of cystic liver lesion
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a cystic liver lesion has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (4)

### 1. Multiplicity
- **Name:** Multiplicity
- **Type:** AttributeType.CHOICE
- **Description:** The number of cysts present.
- **Values:** Single, Multiple
- **Max selected:** 1
- **Required:** True

### 2. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Description:** The specific location of the cyst.
- **Values:** Hepatic (unspecified), Left hepatic lobe, Right hepatic lobe, Hepatic segment 1, Hepatic segment 2, Hepatic segment 3, Hepatic segment 4a, Hepatic segment 4b, Hepatic segment 5, Hepatic segment 6, Hepatic segment 7, Hepatic segment 8
- **Max selected:** 1
- **Required:** True

### 3. Size of largest cyst
- **Name:** Size of largest cyst
- **Type:** AttributeType.NUMERIC
- **Description:** The size of the largest cyst in centimeters.
- **Unit:** cm
- **Required:** True

### 4. Stability
- **Name:** Stability
- **Type:** AttributeType.CHOICE
- **Description:** The stability of the cyst.
- **Values:** Unchanged, Increased, Decreased
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

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

### 1. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a cystic liver lesion has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

### 2. Multiplicity
- **Name:** Multiplicity
- **Type:** AttributeType.CHOICE
- **Description:** The number of cysts present.
- **Values:** Single, Multiple
- **Max selected:** 1
- **Required:** True

### 3. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Description:** The specific location of the cyst.
- **Values:** Hepatic (unspecified), Left hepatic lobe, Right hepatic lobe, Hepatic segment 1, Hepatic segment 2, Hepatic segment 3, Hepatic segment 4a, Hepatic segment 4b, Hepatic segment 5, Hepatic segment 6, Hepatic segment 7, Hepatic segment 8
- **Max selected:** 1
- **Required:** True

### 4. Size of largest cyst
- **Name:** Size of largest cyst
- **Type:** AttributeType.NUMERIC
- **Description:** The size of the largest cyst in centimeters.
- **Unit:** cm
- **Required:** True

### 5. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of cystic liver lesion
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

---
