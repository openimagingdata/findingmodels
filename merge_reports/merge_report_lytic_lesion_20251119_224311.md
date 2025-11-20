# Merge Report: Lytic Lesion
**Timestamp:** 2025-11-19 22:43:11

**Existing Model:** lytic skeletal lesion (ID: OIFM_GMTS_025747)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 1
- **Review decisions made:** 1
  - Keep existing: 1
    - change from prior (kept, status not added)
- **New attributes added:** 9
  - location
  - size Finding
  - number
  - margin
  - density
  - extra-osseous extension
  - soft tissue component
  - pathologic fracture
  - surrounding bone sclerosis
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 11
- **Total final attributes:** 11

---

## ⚠️ Attributes Needing Review (1)

*These attributes were reviewed and decisions were made.*

### 1. change from prior vs status
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** I chose 'needs_review' because there are overlapping values between the existing and incoming attributes, but each has unique values that are not in the other. The shared values are 'stable' and 'decreased'. Existing has the values 'unchanged', 'new', 'resolved', 'increased', 'larger', and 'smaller' that are not in the incoming attribute. Conversely, the incoming attribute includes the value 'enlarging', which is not found in the existing attribute. Thus, all incoming values are not in existing, and incoming has unique values: ['enlarging']. This relationship is classified as 'needs_review'.

- **Shared values:** stable, decreased
- **Existing only values:** unchanged, new, resolved, increased, larger, smaller
- **Incoming only values:** enlarging

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of lytic skeletal lesion
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a lytic skeletal lesion has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (11)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether the lytic lesion is present or absent.
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 2. status
- **Name:** status
- **Type:** AttributeType.CHOICE
- **Description:** Describes the status of the lytic lesion.
- **Values:** stable, enlarging, decreased
- **Max selected:** 1
- **Required:** True

### 3. location
- **Name:** location
- **Type:** AttributeType.CHOICE
- **Description:** Specifies the location of the lytic lesion.
- **Values:** select list for bones, other
- **Max selected:** 1
- **Required:** False

### 4. size Finding
- **Name:** size Finding
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the size of the lytic lesion.
- **Values:** small, medium, large
- **Max selected:** 1
- **Required:** False

### 5. number
- **Name:** number
- **Type:** AttributeType.CHOICE
- **Description:** Specifies the number of lytic lesions.
- **Values:** single, multiple
- **Max selected:** 1
- **Required:** False

### 6. margin
- **Name:** margin
- **Type:** AttributeType.CHOICE
- **Description:** Describes the margin of the lytic lesion.
- **Values:** well-defined, ill-defined
- **Max selected:** 1
- **Required:** False

### 7. density
- **Name:** density
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the density of the lytic lesion.
- **Values:** high, low, mixed
- **Max selected:** 1
- **Required:** False

### 8. extra-osseous extension
- **Name:** extra-osseous extension
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether there is extra-osseous extension of the lytic lesion.
- **Values:** present, absent
- **Max selected:** 1
- **Required:** False

### 9. soft tissue component
- **Name:** soft tissue component
- **Type:** AttributeType.CHOICE
- **Description:** Specifies whether there is a soft tissue component associated with the lytic lesion.
- **Values:** yes, no
- **Max selected:** 1
- **Required:** False

### 10. pathologic fracture
- **Name:** pathologic fracture
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether there is a pathologic fracture associated with the lytic lesion.
- **Values:** yes, no
- **Max selected:** 1
- **Required:** False

### 11. surrounding bone sclerosis
- **Name:** surrounding bone sclerosis
- **Type:** AttributeType.CHOICE
- **Description:** Specifies whether there is surrounding bone sclerosis associated with the lytic lesion.
- **Values:** yes, no
- **Max selected:** 1
- **Required:** False

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (1)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. presence vs presence
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** I classified the relationship as 'subset' because all values in the INCOMING attribute are present in the EXISTING attribute. The EXISTING values are ['absent', 'present', 'indeterminate', 'unknown'] while the INCOMING values are ['present', 'absent']. Therefore, since 'present' and 'absent' are both found within the EXISTING values and the EXISTING values contain more unique values ('indeterminate' and 'unknown'), this confirms that INCOMING is indeed a subset. Specifically, all incoming values are in existing: ['present', 'absent'] are both included in ['absent', 'present', 'indeterminate', 'unknown']. The INCOMING attribute has no unique values not present in the EXISTING attribute; hence, the relationship is characterized as 'subset'.

- **Shared values:** absent, present
- **Existing only values:** indeterminate, unknown

### New Attributes Added (9)

#### 1. location
- **Type:** AttributeType.CHOICE
- **Values:** select list for bones, other
- **Description:** Specifies the location of the lytic lesion.

#### 2. size Finding
- **Type:** AttributeType.CHOICE
- **Values:** small, medium, large
- **Description:** Indicates the size of the lytic lesion.

#### 3. number
- **Type:** AttributeType.CHOICE
- **Values:** single, multiple
- **Description:** Specifies the number of lytic lesions.

#### 4. margin
- **Type:** AttributeType.CHOICE
- **Values:** well-defined, ill-defined
- **Description:** Describes the margin of the lytic lesion.

#### 5. density
- **Type:** AttributeType.CHOICE
- **Values:** high, low, mixed
- **Description:** Indicates the density of the lytic lesion.

#### 6. extra-osseous extension
- **Type:** AttributeType.CHOICE
- **Values:** present, absent
- **Description:** Indicates whether there is extra-osseous extension of the lytic lesion.

#### 7. soft tissue component
- **Type:** AttributeType.CHOICE
- **Values:** yes, no
- **Description:** Specifies whether there is a soft tissue component associated with the lytic lesion.

#### 8. pathologic fracture
- **Type:** AttributeType.CHOICE
- **Values:** yes, no
- **Description:** Indicates whether there is a pathologic fracture associated with the lytic lesion.

#### 9. surrounding bone sclerosis
- **Type:** AttributeType.CHOICE
- **Values:** yes, no
- **Description:** Specifies whether there is surrounding bone sclerosis associated with the lytic lesion.

### Required Attributes Added
None

---

## Final Attributes (11)

### 1. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a lytic skeletal lesion has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

### 2. location
- **Name:** location
- **Type:** AttributeType.CHOICE
- **Description:** Specifies the location of the lytic lesion.
- **Values:** select list for bones, other
- **Max selected:** 1
- **Required:** False

### 3. size Finding
- **Name:** size Finding
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the size of the lytic lesion.
- **Values:** small, medium, large
- **Max selected:** 1
- **Required:** False

### 4. number
- **Name:** number
- **Type:** AttributeType.CHOICE
- **Description:** Specifies the number of lytic lesions.
- **Values:** single, multiple
- **Max selected:** 1
- **Required:** False

### 5. margin
- **Name:** margin
- **Type:** AttributeType.CHOICE
- **Description:** Describes the margin of the lytic lesion.
- **Values:** well-defined, ill-defined
- **Max selected:** 1
- **Required:** False

### 6. density
- **Name:** density
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the density of the lytic lesion.
- **Values:** high, low, mixed
- **Max selected:** 1
- **Required:** False

### 7. extra-osseous extension
- **Name:** extra-osseous extension
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether there is extra-osseous extension of the lytic lesion.
- **Values:** present, absent
- **Max selected:** 1
- **Required:** False

### 8. soft tissue component
- **Name:** soft tissue component
- **Type:** AttributeType.CHOICE
- **Description:** Specifies whether there is a soft tissue component associated with the lytic lesion.
- **Values:** yes, no
- **Max selected:** 1
- **Required:** False

### 9. pathologic fracture
- **Name:** pathologic fracture
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether there is a pathologic fracture associated with the lytic lesion.
- **Values:** yes, no
- **Max selected:** 1
- **Required:** False

### 10. surrounding bone sclerosis
- **Name:** surrounding bone sclerosis
- **Type:** AttributeType.CHOICE
- **Description:** Specifies whether there is surrounding bone sclerosis associated with the lytic lesion.
- **Values:** yes, no
- **Max selected:** 1
- **Required:** False

### 11. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of lytic skeletal lesion
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

---
