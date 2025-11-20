# Merge Report: Breast Mass
**Timestamp:** 2025-11-19 22:11:49

**Existing Model:** breast soft tissue lesion (ID: OIFM_MSFT_255181)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 1
- **Review decisions made:** 1
  - Keep existing: 1
    - presence (kept, Presence of Breast Mass not added)
- **New attributes added:** 11
  - Status
  - Quadrant
  - Size Finding
  - Shape
  - Margin
  - Density
  - Enhancement
  - Breast calcifications
  - Skin thickening
  - Nipple retraction
  - Axillary lymphadenopathy
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 13
- **Total final attributes:** 13

---

## ⚠️ Attributes Needing Review (1)

*These attributes were reviewed and decisions were made.*

### 1. presence vs Presence of Breast Mass
- **Relationship:** needs_review (confidence: 0.95)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing attribute has the values ['absent', 'present', 'indeterminate', 'unknown'], whereas the incoming attribute has the values ['Present', 'Absent']. After normalization for case sensitivity, the incoming values are ['absent', 'present']. The shared values between the existing and incoming attributes are ['absent', 'present']. However, the existing attribute also contains two unique values: ['indeterminate', 'unknown']. Therefore, the existing and incoming attributes share some values but also have unique values not present in the other. This meets the criteria for 'needs_review' since there are shared values with unique values in both attributes. All incoming values are in existing, and Incoming has no unique values: ['indeterminate', 'unknown'].

- **Shared values:** absent, present
- **Existing only values:** indeterminate, unknown

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of breast soft tissue lesion
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. location
- **Name:** location
- **Type:** AttributeType.CHOICE
- **Description:** Specifies the location of the breast soft tissue lesion.
- **Values:** right breast, left breast
- **Max selected:** 1
- **Required:** True

---

## Incoming Attributes (13)

### 1. Presence of Breast Mass
- **Name:** Presence of Breast Mass
- **Type:** AttributeType.CHOICE
- **Description:** Presence of breast mass in the breast.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Description:** Status of the breast mass.
- **Values:** New, Unchanged, Enlarging, Decreased
- **Max selected:** 1
- **Required:** True

### 3. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Description:** Location of the breast mass.
- **Values:** Right breast, Left breast
- **Max selected:** 1
- **Required:** True

### 4. Quadrant
- **Name:** Quadrant
- **Type:** AttributeType.CHOICE
- **Description:** Quadrant of the breast mass.
- **Values:** Upper outer, Upper inner, Lower outer, Lower inner, Central
- **Max selected:** 1
- **Required:** True

### 5. Size Finding
- **Name:** Size Finding
- **Type:** AttributeType.NUMERIC
- **Description:** Size of the breast mass.
- **Unit:** cm
- **Required:** False

### 6. Shape
- **Name:** Shape
- **Type:** AttributeType.CHOICE
- **Description:** Shape of the breast mass.
- **Values:** Round, Oval, Irregular
- **Max selected:** 1
- **Required:** False

### 7. Margin
- **Name:** Margin
- **Type:** AttributeType.CHOICE
- **Description:** Margin of the breast mass.
- **Values:** Circumscribed, Indistinct, Spiculated, Microlobulated
- **Max selected:** 1
- **Required:** False

### 8. Density
- **Name:** Density
- **Type:** AttributeType.CHOICE
- **Description:** Density of the breast mass.
- **Values:** Low, Iso, High, Fat-containing
- **Max selected:** 1
- **Required:** False

### 9. Enhancement
- **Name:** Enhancement
- **Type:** AttributeType.CHOICE
- **Description:** Enhancement of the breast mass.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 10. Breast calcifications
- **Name:** Breast calcifications
- **Type:** AttributeType.CHOICE
- **Description:** Presence of breast calcifications.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 11. Skin thickening
- **Name:** Skin thickening
- **Type:** AttributeType.CHOICE
- **Description:** Presence of skin thickening.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 12. Nipple retraction
- **Name:** Nipple retraction
- **Type:** AttributeType.CHOICE
- **Description:** Presence of nipple retraction.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 13. Axillary lymphadenopathy
- **Name:** Axillary lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Description:** Presence of axillary lymphadenopathy.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (1)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. location vs Location
- **Relationship:** identical (confidence: 0.90)
- **Recommendation:** no_merge
- **AI Reasoning:** I chose the relationship type 'identical' because both attributes have exactly the same values when case differences are normalized. The existing values are ['right breast', 'left breast'] and the incoming values are ['Right breast', 'Left breast']. After normalizing for case, all incoming values are in existing and all existing values are in incoming. Therefore, we confirm that all incoming values are in existing and all existing values are in incoming. This makes the relationship 'identical'.

- **Shared values:** right breast, left breast

### New Attributes Added (11)

#### 1. Status
- **Type:** AttributeType.CHOICE
- **Values:** New, Unchanged, Enlarging, Decreased
- **Description:** Status of the breast mass.

#### 2. Quadrant
- **Type:** AttributeType.CHOICE
- **Values:** Upper outer, Upper inner, Lower outer, Lower inner, Central
- **Description:** Quadrant of the breast mass.

#### 3. Size Finding
- **Type:** AttributeType.NUMERIC
- **Unit:** cm
- **Description:** Size of the breast mass.

#### 4. Shape
- **Type:** AttributeType.CHOICE
- **Values:** Round, Oval, Irregular
- **Description:** Shape of the breast mass.

#### 5. Margin
- **Type:** AttributeType.CHOICE
- **Values:** Circumscribed, Indistinct, Spiculated, Microlobulated
- **Description:** Margin of the breast mass.

#### 6. Density
- **Type:** AttributeType.CHOICE
- **Values:** Low, Iso, High, Fat-containing
- **Description:** Density of the breast mass.

#### 7. Enhancement
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Enhancement of the breast mass.

#### 8. Breast calcifications
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of breast calcifications.

#### 9. Skin thickening
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of skin thickening.

#### 10. Nipple retraction
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of nipple retraction.

#### 11. Axillary lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Presence of axillary lymphadenopathy.

### Required Attributes Added
None

---

## Final Attributes (13)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of breast soft tissue lesion
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Description:** Status of the breast mass.
- **Values:** New, Unchanged, Enlarging, Decreased
- **Max selected:** 1
- **Required:** True

### 3. Quadrant
- **Name:** Quadrant
- **Type:** AttributeType.CHOICE
- **Description:** Quadrant of the breast mass.
- **Values:** Upper outer, Upper inner, Lower outer, Lower inner, Central
- **Max selected:** 1
- **Required:** True

### 4. Size Finding
- **Name:** Size Finding
- **Type:** AttributeType.NUMERIC
- **Description:** Size of the breast mass.
- **Unit:** cm
- **Required:** False

### 5. Shape
- **Name:** Shape
- **Type:** AttributeType.CHOICE
- **Description:** Shape of the breast mass.
- **Values:** Round, Oval, Irregular
- **Max selected:** 1
- **Required:** False

### 6. Margin
- **Name:** Margin
- **Type:** AttributeType.CHOICE
- **Description:** Margin of the breast mass.
- **Values:** Circumscribed, Indistinct, Spiculated, Microlobulated
- **Max selected:** 1
- **Required:** False

### 7. Density
- **Name:** Density
- **Type:** AttributeType.CHOICE
- **Description:** Density of the breast mass.
- **Values:** Low, Iso, High, Fat-containing
- **Max selected:** 1
- **Required:** False

### 8. Enhancement
- **Name:** Enhancement
- **Type:** AttributeType.CHOICE
- **Description:** Enhancement of the breast mass.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 9. Breast calcifications
- **Name:** Breast calcifications
- **Type:** AttributeType.CHOICE
- **Description:** Presence of breast calcifications.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 10. Skin thickening
- **Name:** Skin thickening
- **Type:** AttributeType.CHOICE
- **Description:** Presence of skin thickening.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 11. Nipple retraction
- **Name:** Nipple retraction
- **Type:** AttributeType.CHOICE
- **Description:** Presence of nipple retraction.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 12. Axillary lymphadenopathy
- **Name:** Axillary lymphadenopathy
- **Type:** AttributeType.CHOICE
- **Description:** Presence of axillary lymphadenopathy.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 13. location
- **Name:** location
- **Type:** AttributeType.CHOICE
- **Description:** Specifies the location of the breast soft tissue lesion.
- **Values:** right breast, left breast
- **Max selected:** 1
- **Required:** True

---
