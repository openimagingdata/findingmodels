# Merge Report: Ecmo Cannula
**Timestamp:** 2025-11-19 22:26:39

**Existing Model:** Chest Radiograph Lines and Tubes (ID: OIFM_CDE_000237)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 8
  - Presence of ECMO Cannula
  - Status
  - Cannulation Site
  - Appropriate location
  - Side Finding
  - Vein approach (if venous)
  - Artery approach (if arterial)
  - Distal tip location (venous)
- **Required attributes added:** 0
- **Total existing attributes:** 5
- **Total incoming attributes:** 8
- **Total final attributes:** 13

---

## Existing Attributes (5)

### 1. Endotracheal tube
- **Name:** Endotracheal tube
- **Type:** AttributeType.CHOICE
- **Description:** Presence and position of endotracheal tube on XRAY
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

### 2. Central venous catheter
- **Name:** Central venous catheter
- **Type:** AttributeType.CHOICE
- **Description:** Presence and position of central venous catheter
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

### 3. Pulmonary artery catheter
- **Name:** Pulmonary artery catheter
- **Type:** AttributeType.CHOICE
- **Description:** Presence and position of pulmonary artery catheter
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

### 4. Nasogastric tube
- **Name:** Nasogastric tube
- **Type:** AttributeType.CHOICE
- **Description:** Presence and position of nasogastric tube
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

### 5. Airway stent
- **Name:** Airway stent
- **Type:** AttributeType.CHOICE
- **Description:** Presence and position of airway stent
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (8)

### 1. Presence of ECMO Cannula
- **Name:** Presence of ECMO Cannula
- **Type:** AttributeType.CHOICE
- **Description:** Whether the ECMO cannula is present or absent
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Description:** The status of the ECMO cannula
- **Values:** New placement, Unchanged, Migrated, Removed
- **Max selected:** 1
- **Required:** True

### 3. Cannulation Site
- **Name:** Cannulation Site
- **Type:** AttributeType.CHOICE
- **Description:** The site of cannulation
- **Values:** Venous, Arterial
- **Max selected:** 1
- **Required:** True

### 4. Appropriate location
- **Name:** Appropriate location
- **Type:** AttributeType.CHOICE
- **Description:** Whether the cannula placement is appropriate or not
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 5. Side Finding
- **Name:** Side Finding
- **Type:** AttributeType.CHOICE
- **Description:** The side of the cannulation
- **Values:** Left, Right, NA
- **Max selected:** 1
- **Required:** True

### 6. Vein approach (if venous)
- **Name:** Vein approach (if venous)
- **Type:** AttributeType.CHOICE
- **Description:** The approach used for venous cannulation
- **Values:** Internal jugular, External jugular, Subclavian, Femoral
- **Max selected:** 1
- **Required:** False

### 7. Artery approach (if arterial)
- **Name:** Artery approach (if arterial)
- **Type:** AttributeType.CHOICE
- **Description:** The approach used for arterial cannulation
- **Values:** Femoral, Subclavian, Carotid
- **Max selected:** 1
- **Required:** False

### 8. Distal tip location (venous)
- **Name:** Distal tip location (venous)
- **Type:** AttributeType.CHOICE
- **Description:** The location of the distal tip in venous cannulation
- **Values:** Right atrium, SVC, IVC
- **Max selected:** 1
- **Required:** False

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

### New Attributes Added (8)

#### 1. Presence of ECMO Cannula
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Whether the ECMO cannula is present or absent

#### 2. Status
- **Type:** AttributeType.CHOICE
- **Values:** New placement, Unchanged, Migrated, Removed
- **Description:** The status of the ECMO cannula

#### 3. Cannulation Site
- **Type:** AttributeType.CHOICE
- **Values:** Venous, Arterial
- **Description:** The site of cannulation

#### 4. Appropriate location
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No
- **Description:** Whether the cannula placement is appropriate or not

#### 5. Side Finding
- **Type:** AttributeType.CHOICE
- **Values:** Left, Right, NA
- **Description:** The side of the cannulation

#### 6. Vein approach (if venous)
- **Type:** AttributeType.CHOICE
- **Values:** Internal jugular, External jugular, Subclavian, Femoral
- **Description:** The approach used for venous cannulation

#### 7. Artery approach (if arterial)
- **Type:** AttributeType.CHOICE
- **Values:** Femoral, Subclavian, Carotid
- **Description:** The approach used for arterial cannulation

#### 8. Distal tip location (venous)
- **Type:** AttributeType.CHOICE
- **Values:** Right atrium, SVC, IVC
- **Description:** The location of the distal tip in venous cannulation

### Required Attributes Added
None

---

## Final Attributes (13)

### 1. Presence of ECMO Cannula
- **Name:** Presence of ECMO Cannula
- **Type:** AttributeType.CHOICE
- **Description:** Whether the ECMO cannula is present or absent
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Description:** The status of the ECMO cannula
- **Values:** New placement, Unchanged, Migrated, Removed
- **Max selected:** 1
- **Required:** True

### 3. Cannulation Site
- **Name:** Cannulation Site
- **Type:** AttributeType.CHOICE
- **Description:** The site of cannulation
- **Values:** Venous, Arterial
- **Max selected:** 1
- **Required:** True

### 4. Appropriate location
- **Name:** Appropriate location
- **Type:** AttributeType.CHOICE
- **Description:** Whether the cannula placement is appropriate or not
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 5. Side Finding
- **Name:** Side Finding
- **Type:** AttributeType.CHOICE
- **Description:** The side of the cannulation
- **Values:** Left, Right, NA
- **Max selected:** 1
- **Required:** True

### 6. Vein approach (if venous)
- **Name:** Vein approach (if venous)
- **Type:** AttributeType.CHOICE
- **Description:** The approach used for venous cannulation
- **Values:** Internal jugular, External jugular, Subclavian, Femoral
- **Max selected:** 1
- **Required:** False

### 7. Artery approach (if arterial)
- **Name:** Artery approach (if arterial)
- **Type:** AttributeType.CHOICE
- **Description:** The approach used for arterial cannulation
- **Values:** Femoral, Subclavian, Carotid
- **Max selected:** 1
- **Required:** False

### 8. Distal tip location (venous)
- **Name:** Distal tip location (venous)
- **Type:** AttributeType.CHOICE
- **Description:** The location of the distal tip in venous cannulation
- **Values:** Right atrium, SVC, IVC
- **Max selected:** 1
- **Required:** False

### 9. Endotracheal tube
- **Name:** Endotracheal tube
- **Type:** AttributeType.CHOICE
- **Description:** Presence and position of endotracheal tube on XRAY
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

### 10. Central venous catheter
- **Name:** Central venous catheter
- **Type:** AttributeType.CHOICE
- **Description:** Presence and position of central venous catheter
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

### 11. Pulmonary artery catheter
- **Name:** Pulmonary artery catheter
- **Type:** AttributeType.CHOICE
- **Description:** Presence and position of pulmonary artery catheter
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

### 12. Nasogastric tube
- **Name:** Nasogastric tube
- **Type:** AttributeType.CHOICE
- **Description:** Presence and position of nasogastric tube
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

### 13. Airway stent
- **Name:** Airway stent
- **Type:** AttributeType.CHOICE
- **Description:** Presence and position of airway stent
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

---
