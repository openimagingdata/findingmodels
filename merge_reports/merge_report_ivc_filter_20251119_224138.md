# Merge Report: Ivc Filter
**Timestamp:** 2025-11-19 22:41:38

**Existing Model:** Identification and Characterization of Vena Cava Filters (ID: OIFM_CDE_000104)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 2
- **Review decisions made:** 2
  - Keep existing: 2
    - Presence (kept, Presence of IVC Filter not added)
    - Presence (kept, Thrombosis not added)
- **New attributes added:** 5
  - Status
  - Location
  - Type Finding
  - Orientation
  - Complication
- **Required attributes added:** 0
- **Total existing attributes:** 4
- **Total incoming attributes:** 7
- **Total final attributes:** 9

---

## ⚠️ Attributes Needing Review (2)

*These attributes were reviewed and decisions were made.*

### 1. Presence vs Presence of IVC Filter
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing attribute has four values: ['absent', 'present', 'indeterminate', 'unknown']. The incoming attribute has two values: ['Present', 'Absent']. Comparing the two, I find that 'Present' and 'Absent' map to 'present' and 'absent' respectively in a case-insensitive manner. Therefore, the shared values are ['present', 'absent']. However, the existing attribute also includes 'indeterminate' and 'unknown', which are not present in the incoming attribute. Thus, there are some shared values, but each attribute has unique values not in the other: Existing has unique values: ['indeterminate', 'unknown']; Incoming has unique values: []. This justifies the classification as 'needs_review' because modifications or additional detail may be necessary to align them completely.

- **Shared values:** present, absent
- **Existing only values:** indeterminate, unknown

### 2. Presence vs Thrombosis
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing attribute has values: ['absent', 'present', 'indeterminate', 'unknown'] while the incoming attribute has values: ['Present', 'Absent']. There are some shared values: 'present' (case-insensitive) and 'absent' (case-insensitive), but the existing attribute has additional values: 'indeterminate' and 'unknown' that are not present in the incoming attribute. However, the existing attribute also includes values that the incoming attribute does not have unique values to themselves. Therefore, we cannot categorize this as 'enhanced' as the incoming does not include all existing values. It cannot be classified as 'subset' either as there are values unique to the existing attribute without overlap. All incoming values are in existing, but still, incoming has unique values that make us classify it as needs_review.

- **Shared values:** present, absent
- **Existing only values:** indeterminate, unknown

---

## Existing Attributes (4)

### 1. Filter count
- **Name:** Filter count
- **Type:** AttributeType.NUMERIC
- **Description:** Number of filter devices 
- **Unit:** unit
- **Range:** 0 - 5
- **Required:** False

### 2. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 3. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Description:** Anatomic location of filter(s) or filter components
- **Values:** infrarenal vena cava, suprarenal vena cava, right common iliac vein, left common iliac vein, right testicular vein, left testicular vein, right ovarian vein, left ovarian vein, right renal vein, left renal vein, superior vena cava, right atrium, right ventricle, left ventricle, interventricular septum, main pulmonary artery, right main pulmonary artery, left main pulmonary artery, segmental right pulmonary artery, segmental left pulmonary artery, indeterminate, unknown
- **Max selected:** 22
- **Required:** False

### 4. Complications
- **Name:** Complications
- **Type:** AttributeType.CHOICE
- **Description:** Radiographically evident filter complications
- **Values:** absent, thrombosis, tilt, perforation, fracture, migration, pulmonary embolism, infection, malposition, incomplete deployment, indeterminate, unknown, other
- **Max selected:** 13
- **Required:** False

---

## Incoming Attributes (7)

### 1. Presence of IVC Filter
- **Name:** Presence of IVC Filter
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Values:** New placement, Unchanged, Complication, Removed
- **Max selected:** 1
- **Required:** True

### 3. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Values:** Suprarenal, Infrarenal
- **Max selected:** 1
- **Required:** True

### 4. Type Finding
- **Name:** Type Finding
- **Type:** AttributeType.CHOICE
- **Values:** Permanent, Retrievable
- **Max selected:** 1
- **Required:** True

### 5. Orientation
- **Name:** Orientation
- **Type:** AttributeType.CHOICE
- **Values:** Appropriate, Tilted
- **Max selected:** 1
- **Required:** True

### 6. Complication
- **Name:** Complication
- **Type:** AttributeType.CHOICE
- **Values:** None, Tine Penetration, Migration, Tilted
- **Max selected:** 1
- **Required:** True

### 7. Thrombosis
- **Name:** Thrombosis
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

### New Attributes Added (5)

#### 1. Status
- **Type:** AttributeType.CHOICE
- **Values:** New placement, Unchanged, Complication, Removed

#### 2. Location
- **Type:** AttributeType.CHOICE
- **Values:** Suprarenal, Infrarenal

#### 3. Type Finding
- **Type:** AttributeType.CHOICE
- **Values:** Permanent, Retrievable

#### 4. Orientation
- **Type:** AttributeType.CHOICE
- **Values:** Appropriate, Tilted

#### 5. Complication
- **Type:** AttributeType.CHOICE
- **Values:** None, Tine Penetration, Migration, Tilted

### Required Attributes Added
None

---

## Final Attributes (9)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Values:** New placement, Unchanged, Complication, Removed
- **Max selected:** 1
- **Required:** True

### 3. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Values:** Suprarenal, Infrarenal
- **Max selected:** 1
- **Required:** True

### 4. Type Finding
- **Name:** Type Finding
- **Type:** AttributeType.CHOICE
- **Values:** Permanent, Retrievable
- **Max selected:** 1
- **Required:** True

### 5. Orientation
- **Name:** Orientation
- **Type:** AttributeType.CHOICE
- **Values:** Appropriate, Tilted
- **Max selected:** 1
- **Required:** True

### 6. Complication
- **Name:** Complication
- **Type:** AttributeType.CHOICE
- **Values:** None, Tine Penetration, Migration, Tilted
- **Max selected:** 1
- **Required:** True

### 7. Filter count
- **Name:** Filter count
- **Type:** AttributeType.NUMERIC
- **Description:** Number of filter devices 
- **Unit:** unit
- **Range:** 0 - 5
- **Required:** False

### 8. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Description:** Anatomic location of filter(s) or filter components
- **Values:** infrarenal vena cava, suprarenal vena cava, right common iliac vein, left common iliac vein, right testicular vein, left testicular vein, right ovarian vein, left ovarian vein, right renal vein, left renal vein, superior vena cava, right atrium, right ventricle, left ventricle, interventricular septum, main pulmonary artery, right main pulmonary artery, left main pulmonary artery, segmental right pulmonary artery, segmental left pulmonary artery, indeterminate, unknown
- **Max selected:** 22
- **Required:** False

### 9. Complications
- **Name:** Complications
- **Type:** AttributeType.CHOICE
- **Description:** Radiographically evident filter complications
- **Values:** absent, thrombosis, tilt, perforation, fracture, migration, pulmonary embolism, infection, malposition, incomplete deployment, indeterminate, unknown, other
- **Max selected:** 13
- **Required:** False

---
