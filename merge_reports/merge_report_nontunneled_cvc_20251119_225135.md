# Merge Report: Nontunneled Cvc
**Timestamp:** 2025-11-19 22:51:35

**Existing Model:** Chest Radiograph Lines and Tubes (ID: OIFM_CDE_000237)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 12
  - Presence of Non-tunneled Central Venous Catheter (CVC)
  - Hematoma
  - Hemothorax
  - Status
  - Appropriate location
  - Side Finding
  - Number of Lumens
  - Vein approach
  - Course
  - Distal tip location
  - Complications
  - Pneumothorax
- **Required attributes added:** 0
- **Total existing attributes:** 5
- **Total incoming attributes:** 12
- **Total final attributes:** 17

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

## Incoming Attributes (12)

### 1. Presence of Non-tunneled Central Venous Catheter (CVC)
- **Name:** Presence of Non-tunneled Central Venous Catheter (CVC)
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Values:** New placement, Unchanged, Migrated, Removed
- **Max selected:** 1
- **Required:** False

### 3. Appropriate location
- **Name:** Appropriate location
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** False

### 4. Side Finding
- **Name:** Side Finding
- **Type:** AttributeType.CHOICE
- **Values:** Left, Right, Unknown
- **Max selected:** 1
- **Required:** False

### 5. Number of Lumens
- **Name:** Number of Lumens
- **Type:** AttributeType.CHOICE
- **Values:** Single, Double, Triple, Quad
- **Max selected:** 1
- **Required:** False

### 6. Vein approach
- **Name:** Vein approach
- **Type:** AttributeType.CHOICE
- **Values:** Internal jugular, Subclavian, Femoral
- **Max selected:** 1
- **Required:** False

### 7. Course
- **Name:** Course
- **Type:** AttributeType.CHOICE
- **Values:** Appropriate, Kinking, Coiling
- **Max selected:** 1
- **Required:** False

### 8. Distal tip location
- **Name:** Distal tip location
- **Type:** AttributeType.CHOICE
- **Values:** Subclavian vein, Brachiocephalic vein, SVC, Superior cavoatrial junction, Azygous vein, Inferior cavoatrial junction, Internal jugular vein, IVC
- **Max selected:** 1
- **Required:** False

### 9. Complications
- **Name:** Complications
- **Type:** AttributeType.CHOICE
- **Values:** None, Occlusion, Thrombosis (fibrin sheath), Catheter fracture, Tip Migration
- **Max selected:** 1
- **Required:** False

### 10. Hematoma
- **Name:** Hematoma
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 11. Pneumothorax
- **Name:** Pneumothorax
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 12. Hemothorax
- **Name:** Hemothorax
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

### New Attributes Added (12)

#### 1. Presence of Non-tunneled Central Venous Catheter (CVC)
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 2. Hematoma
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 3. Hemothorax
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 4. Status
- **Type:** AttributeType.CHOICE
- **Values:** New placement, Unchanged, Migrated, Removed

#### 5. Appropriate location
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No

#### 6. Side Finding
- **Type:** AttributeType.CHOICE
- **Values:** Left, Right, Unknown

#### 7. Number of Lumens
- **Type:** AttributeType.CHOICE
- **Values:** Single, Double, Triple, Quad

#### 8. Vein approach
- **Type:** AttributeType.CHOICE
- **Values:** Internal jugular, Subclavian, Femoral

#### 9. Course
- **Type:** AttributeType.CHOICE
- **Values:** Appropriate, Kinking, Coiling

#### 10. Distal tip location
- **Type:** AttributeType.CHOICE
- **Values:** Subclavian vein, Brachiocephalic vein, SVC, Superior cavoatrial junction, Azygous vein, Inferior cavoatrial junction, Internal jugular vein, IVC

#### 11. Complications
- **Type:** AttributeType.CHOICE
- **Values:** None, Occlusion, Thrombosis (fibrin sheath), Catheter fracture, Tip Migration

#### 12. Pneumothorax
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

### Required Attributes Added
None

---

## Final Attributes (17)

### 1. Presence of Non-tunneled Central Venous Catheter (CVC)
- **Name:** Presence of Non-tunneled Central Venous Catheter (CVC)
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Hematoma
- **Name:** Hematoma
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 3. Hemothorax
- **Name:** Hemothorax
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 4. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Values:** New placement, Unchanged, Migrated, Removed
- **Max selected:** 1
- **Required:** False

### 5. Appropriate location
- **Name:** Appropriate location
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** False

### 6. Side Finding
- **Name:** Side Finding
- **Type:** AttributeType.CHOICE
- **Values:** Left, Right, Unknown
- **Max selected:** 1
- **Required:** False

### 7. Number of Lumens
- **Name:** Number of Lumens
- **Type:** AttributeType.CHOICE
- **Values:** Single, Double, Triple, Quad
- **Max selected:** 1
- **Required:** False

### 8. Vein approach
- **Name:** Vein approach
- **Type:** AttributeType.CHOICE
- **Values:** Internal jugular, Subclavian, Femoral
- **Max selected:** 1
- **Required:** False

### 9. Course
- **Name:** Course
- **Type:** AttributeType.CHOICE
- **Values:** Appropriate, Kinking, Coiling
- **Max selected:** 1
- **Required:** False

### 10. Distal tip location
- **Name:** Distal tip location
- **Type:** AttributeType.CHOICE
- **Values:** Subclavian vein, Brachiocephalic vein, SVC, Superior cavoatrial junction, Azygous vein, Inferior cavoatrial junction, Internal jugular vein, IVC
- **Max selected:** 1
- **Required:** False

### 11. Complications
- **Name:** Complications
- **Type:** AttributeType.CHOICE
- **Values:** None, Occlusion, Thrombosis (fibrin sheath), Catheter fracture, Tip Migration
- **Max selected:** 1
- **Required:** False

### 12. Pneumothorax
- **Name:** Pneumothorax
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 13. Endotracheal tube
- **Name:** Endotracheal tube
- **Type:** AttributeType.CHOICE
- **Description:** Presence and position of endotracheal tube on XRAY
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

### 14. Central venous catheter
- **Name:** Central venous catheter
- **Type:** AttributeType.CHOICE
- **Description:** Presence and position of central venous catheter
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

### 15. Pulmonary artery catheter
- **Name:** Pulmonary artery catheter
- **Type:** AttributeType.CHOICE
- **Description:** Presence and position of pulmonary artery catheter
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

### 16. Nasogastric tube
- **Name:** Nasogastric tube
- **Type:** AttributeType.CHOICE
- **Description:** Presence and position of nasogastric tube
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

### 17. Airway stent
- **Name:** Airway stent
- **Type:** AttributeType.CHOICE
- **Description:** Presence and position of airway stent
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

---
