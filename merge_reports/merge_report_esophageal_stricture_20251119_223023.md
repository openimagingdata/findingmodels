# Merge Report: Esophageal Stricture
**Timestamp:** 2025-11-19 22:30:23

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
- **Description:** Presence or absence of localized narrowing of esophagus
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a localized narrowing of esophagus has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (3)

### 1. descriptors
- **Name:** descriptors
- **Type:** AttributeType.CHOICE
- **Description:** Descriptors that may be used to characterize the esophageal stricture
- **Values:** patulous, distended, fluid-filled
- **Max selected:** 1
- **Required:** False

### 2. presence_of_stricture
- **Name:** presence_of_stricture
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether the esophageal stricture is present or absent
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 3. location_of_stricture
- **Name:** location_of_stricture
- **Type:** AttributeType.CHOICE
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
- **AI Reasoning:** The existing values for the attribute 'presence' are ['absent', 'present', 'indeterminate', 'unknown']. The incoming values for 'presence_of_stricture' are ['present', 'absent']. All incoming values ('present', 'absent') are contained within the existing values, since 'absent' and 'present' are present in the existing attribute. However, the existing attribute has additional values 'indeterminate' and 'unknown', which are not found in the incoming attribute. Therefore, the incoming attribute only contains a subset of the existing attribute's values. All incoming values are in existing. Incoming has no unique values: [] (it's a subset of the existing attribute). This makes the relationship a 'subset'.

- **Shared values:** present, absent
- **Existing only values:** indeterminate, unknown

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
- **Description:** Descriptors that may be used to characterize the esophageal stricture
- **Values:** patulous, distended, fluid-filled
- **Max selected:** 1
- **Required:** False

### 2. location_of_stricture
- **Name:** location_of_stricture
- **Type:** AttributeType.CHOICE
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
