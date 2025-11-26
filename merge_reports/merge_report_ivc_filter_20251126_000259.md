# Merge Report: Ivc Filter
**Timestamp:** 2025-11-26 00:02:59

**Existing Model:** Identification and Characterization of Vena Cava Filters (ID: OIFM_CDE_000104)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
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

## Existing Attributes (4)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. Filter count
- **Name:** Filter count
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Description:** Number of filter devices 
- **Unit:** unit
- **Range:** 0 - 5
- **Required:** False

### 3. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Anatomic location of filter(s) or filter components
- **Values:** infrarenal vena cava, suprarenal vena cava, right common iliac vein, left common iliac vein, right testicular vein, left testicular vein, right ovarian vein, left ovarian vein, right renal vein, left renal vein, superior vena cava, right atrium, right ventricle, left ventricle, interventricular septum, main pulmonary artery, right main pulmonary artery, left main pulmonary artery, segmental right pulmonary artery, segmental left pulmonary artery, indeterminate, unknown
- **Max selected:** 22
- **Required:** False

### 4. Complications
- **Name:** Complications
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Radiographically evident filter complications
- **Values:** absent, thrombosis, tilt, perforation, fracture, migration, pulmonary embolism, infection, malposition, incomplete deployment, indeterminate, unknown, other
- **Max selected:** 13
- **Required:** False

---

## Incoming Attributes (7)

### 1. Presence of IVC Filter
- **Name:** Presence of IVC Filter
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Thrombosis
- **Name:** Thrombosis
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 3. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Values:** New placement, Unchanged, Complication, Removed
- **Max selected:** 1
- **Required:** True

### 4. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Suprarenal, Infrarenal
- **Max selected:** 1
- **Required:** True

### 5. Type Finding
- **Name:** Type Finding
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Permanent, Retrievable
- **Max selected:** 1
- **Required:** True

### 6. Orientation
- **Name:** Orientation
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Appropriate, Tilted
- **Max selected:** 1
- **Required:** True

### 7. Complication
- **Name:** Complication
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** None, Tine Penetration, Migration, Tilted
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (2)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. Presence vs Presence of IVC Filter
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Presence of IVC Filter' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

#### 2. Presence vs Thrombosis
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Thrombosis' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

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

### 1. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Values:** New placement, Unchanged, Complication, Removed
- **Max selected:** 1
- **Required:** True

### 2. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Suprarenal, Infrarenal
- **Max selected:** 1
- **Required:** True

### 3. Type Finding
- **Name:** Type Finding
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Permanent, Retrievable
- **Max selected:** 1
- **Required:** True

### 4. Orientation
- **Name:** Orientation
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Appropriate, Tilted
- **Max selected:** 1
- **Required:** True

### 5. Complication
- **Name:** Complication
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** None, Tine Penetration, Migration, Tilted
- **Max selected:** 1
- **Required:** True

### 6. Filter count
- **Name:** Filter count
- **Type:** AttributeType.NUMERIC
- **Description:** Number of filter devices 
- **Unit:** unit
- **Range:** 0 - 5
- **Required:** False

### 7. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
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
