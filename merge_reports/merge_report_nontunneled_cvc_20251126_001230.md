# Merge Report: Nontunneled Cvc
**Timestamp:** 2025-11-26 00:12:30

**Existing Model:** Chest Radiograph Lines and Tubes (ID: OIFM_CDE_000237)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 12
  - Presence of Non-tunneled Central Venous Catheter (CVC)
  - Hematoma
  - Pneumothorax
  - Hemothorax
  - Status
  - Appropriate location
  - Side Finding
  - Number of Lumens
  - Vein approach
  - Course
  - Distal tip location
  - Complications
- **Required attributes added:** 0
- **Total existing attributes:** 5
- **Total incoming attributes:** 12
- **Total final attributes:** 17

---

## Existing Attributes (5)

### 1. Endotracheal tube
- **Name:** Endotracheal tube
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence and position of endotracheal tube on XRAY
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

### 2. Central venous catheter
- **Name:** Central venous catheter
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence and position of central venous catheter
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

### 3. Pulmonary artery catheter
- **Name:** Pulmonary artery catheter
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence and position of pulmonary artery catheter
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

### 4. Nasogastric tube
- **Name:** Nasogastric tube
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence and position of nasogastric tube
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

### 5. Airway stent
- **Name:** Airway stent
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence and position of airway stent
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (12)

### 1. Presence of Non-tunneled Central Venous Catheter (CVC)
- **Name:** Presence of Non-tunneled Central Venous Catheter (CVC)
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Hematoma
- **Name:** Hematoma
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 3. Pneumothorax
- **Name:** Pneumothorax
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 4. Hemothorax
- **Name:** Hemothorax
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 5. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Values:** New placement, Unchanged, Migrated, Removed
- **Max selected:** 1
- **Required:** False

### 6. Appropriate location
- **Name:** Appropriate location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** False

### 7. Side Finding
- **Name:** Side Finding
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Left, Right, Unknown
- **Max selected:** 1
- **Required:** False

### 8. Number of Lumens
- **Name:** Number of Lumens
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Single, Double, Triple, Quad
- **Max selected:** 1
- **Required:** False

### 9. Vein approach
- **Name:** Vein approach
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Internal jugular, Subclavian, Femoral
- **Max selected:** 1
- **Required:** False

### 10. Course
- **Name:** Course
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Appropriate, Kinking, Coiling
- **Max selected:** 1
- **Required:** False

### 11. Distal tip location
- **Name:** Distal tip location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Subclavian vein, Brachiocephalic vein, SVC, Superior cavoatrial junction, Azygous vein, Inferior cavoatrial junction, Internal jugular vein, IVC
- **Max selected:** 1
- **Required:** False

### 12. Complications
- **Name:** Complications
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** None, Occlusion, Thrombosis (fibrin sheath), Catheter fracture, Tip Migration
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

#### 3. Pneumothorax
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 4. Hemothorax
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

#### 5. Status
- **Type:** AttributeType.CHOICE
- **Values:** New placement, Unchanged, Migrated, Removed

#### 6. Appropriate location
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No

#### 7. Side Finding
- **Type:** AttributeType.CHOICE
- **Values:** Left, Right, Unknown

#### 8. Number of Lumens
- **Type:** AttributeType.CHOICE
- **Values:** Single, Double, Triple, Quad

#### 9. Vein approach
- **Type:** AttributeType.CHOICE
- **Values:** Internal jugular, Subclavian, Femoral

#### 10. Course
- **Type:** AttributeType.CHOICE
- **Values:** Appropriate, Kinking, Coiling

#### 11. Distal tip location
- **Type:** AttributeType.CHOICE
- **Values:** Subclavian vein, Brachiocephalic vein, SVC, Superior cavoatrial junction, Azygous vein, Inferior cavoatrial junction, Internal jugular vein, IVC

#### 12. Complications
- **Type:** AttributeType.CHOICE
- **Values:** None, Occlusion, Thrombosis (fibrin sheath), Catheter fracture, Tip Migration

### Required Attributes Added
None

---

## Final Attributes (17)

### 1. Presence of Non-tunneled Central Venous Catheter (CVC)
- **Name:** Presence of Non-tunneled Central Venous Catheter (CVC)
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Hematoma
- **Name:** Hematoma
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 3. Pneumothorax
- **Name:** Pneumothorax
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 4. Hemothorax
- **Name:** Hemothorax
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 5. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Values:** New placement, Unchanged, Migrated, Removed
- **Max selected:** 1
- **Required:** False

### 6. Appropriate location
- **Name:** Appropriate location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** False

### 7. Side Finding
- **Name:** Side Finding
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Left, Right, Unknown
- **Max selected:** 1
- **Required:** False

### 8. Number of Lumens
- **Name:** Number of Lumens
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Single, Double, Triple, Quad
- **Max selected:** 1
- **Required:** False

### 9. Vein approach
- **Name:** Vein approach
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Internal jugular, Subclavian, Femoral
- **Max selected:** 1
- **Required:** False

### 10. Course
- **Name:** Course
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Appropriate, Kinking, Coiling
- **Max selected:** 1
- **Required:** False

### 11. Distal tip location
- **Name:** Distal tip location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Subclavian vein, Brachiocephalic vein, SVC, Superior cavoatrial junction, Azygous vein, Inferior cavoatrial junction, Internal jugular vein, IVC
- **Max selected:** 1
- **Required:** False

### 12. Complications
- **Name:** Complications
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** None, Occlusion, Thrombosis (fibrin sheath), Catheter fracture, Tip Migration
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
