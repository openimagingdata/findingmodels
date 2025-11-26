# Merge Report: Esophageal Stricture
**Timestamp:** 2025-11-25 23:53:24

**Existing Model:** localized narrowing of esophagus (ID: OIFM_GMTS_003934)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 2
  - descriptors
  - location_of_stricture
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 3
- **Total final attributes:** 4

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence or absence of localized narrowing of esophagus
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Whether and how a localized narrowing of esophagus has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (3)

### 1. presence_of_stricture
- **Name:** presence_of_stricture
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Indicates whether the esophageal stricture is present or absent
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 2. descriptors
- **Name:** descriptors
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Descriptors that may be used to characterize the esophageal stricture
- **Values:** patulous, distended, fluid-filled
- **Max selected:** 1
- **Required:** False

### 3. location_of_stricture
- **Name:** location_of_stricture
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The location of the esophageal stricture
- **Values:** proximal esophagus, middle esophagus, distal esophagus, gastroesophageal junction
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (1)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. presence vs presence_of_stricture
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'presence_of_stricture' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** present, absent

### New Attributes Added (2)

#### 1. descriptors
- **Type:** AttributeType.CHOICE
- **Values:** patulous, distended, fluid-filled
- **Description:** Descriptors that may be used to characterize the esophageal stricture

#### 2. location_of_stricture
- **Type:** AttributeType.CHOICE
- **Values:** proximal esophagus, middle esophagus, distal esophagus, gastroesophageal junction
- **Description:** The location of the esophageal stricture

### Required Attributes Added
None

---

## Final Attributes (4)

### 1. descriptors
- **Name:** descriptors
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Descriptors that may be used to characterize the esophageal stricture
- **Values:** patulous, distended, fluid-filled
- **Max selected:** 1
- **Required:** False

### 2. location_of_stricture
- **Name:** location_of_stricture
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The location of the esophageal stricture
- **Values:** proximal esophagus, middle esophagus, distal esophagus, gastroesophageal junction
- **Max selected:** 1
- **Required:** True

### 3. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of localized narrowing of esophagus
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 4. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a localized narrowing of esophagus has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
