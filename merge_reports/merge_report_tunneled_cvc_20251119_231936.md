# Merge Report: Tunneled Cvc
**Timestamp:** 2025-11-19 23:19:36

**Existing Model:** Chest Radiograph Lines and Tubes (ID: OIFM_CDE_000237)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 12
  - Presence of tunneled CVC
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

### 1. Presence of tunneled CVC
- **Name:** Presence of tunneled CVC
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether a tunneled CVC is present or absent
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the status of the tunneled CVC
- **Values:** New placement, Unchanged, Migrated, Removed
- **Max selected:** 1
- **Required:** True

### 3. Appropriate location
- **Name:** Appropriate location
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether the tunneled CVC is in an appropriate location
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 4. Side Finding
- **Name:** Side Finding
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the side of the tunneled CVC
- **Values:** Left, Right
- **Max selected:** 1
- **Required:** True

### 5. Number of Lumens
- **Name:** Number of Lumens
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the number of lumens in the tunneled CVC
- **Values:** Single, Double, Triple
- **Max selected:** 1
- **Required:** True

### 6. Vein approach
- **Name:** Vein approach
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the vein approach for the tunneled CVC
- **Values:** Internal jugular, Subclavian
- **Max selected:** 1
- **Required:** True

### 7. Course
- **Name:** Course
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the course of the tunneled CVC
- **Values:** Appropriate, Kinking, Coiling
- **Max selected:** 1
- **Required:** True

### 8. Distal tip location
- **Name:** Distal tip location
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the distal tip location of the tunneled CVC
- **Values:** Subclavian vein, Brachiocephalic vein, SVC (superior vena cava), Superior cavoatrial junction, Azygous vein, Inferior cavoatrial junction, Internal jugular vein, IVC (inferior vena cava)
- **Max selected:** 1
- **Required:** True

### 9. Complications
- **Name:** Complications
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the complications associated with the tunneled CVC
- **Values:** None, Occlusion, Thrombosis (fibrin sheath), Catheter fracture, Tip Migration
- **Max selected:** 1
- **Required:** True

### 10. Hematoma
- **Name:** Hematoma
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the presence or absence of a hematoma associated with the tunneled CVC
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 11. Pneumothorax
- **Name:** Pneumothorax
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the presence or absence of a pneumothorax associated with the tunneled CVC
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 12. Hemothorax
- **Name:** Hemothorax
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the presence or absence of a hemothorax associated with the tunneled CVC
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

### New Attributes Added (12)

#### 1. Presence of tunneled CVC
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Indicates whether a tunneled CVC is present or absent

#### 2. Hematoma
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Indicates the presence or absence of a hematoma associated with the tunneled CVC

#### 3. Pneumothorax
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Indicates the presence or absence of a pneumothorax associated with the tunneled CVC

#### 4. Hemothorax
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** Indicates the presence or absence of a hemothorax associated with the tunneled CVC

#### 5. Status
- **Type:** AttributeType.CHOICE
- **Values:** New placement, Unchanged, Migrated, Removed
- **Description:** Indicates the status of the tunneled CVC

#### 6. Appropriate location
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No
- **Description:** Indicates whether the tunneled CVC is in an appropriate location

#### 7. Side Finding
- **Type:** AttributeType.CHOICE
- **Values:** Left, Right
- **Description:** Indicates the side of the tunneled CVC

#### 8. Number of Lumens
- **Type:** AttributeType.CHOICE
- **Values:** Single, Double, Triple
- **Description:** Indicates the number of lumens in the tunneled CVC

#### 9. Vein approach
- **Type:** AttributeType.CHOICE
- **Values:** Internal jugular, Subclavian
- **Description:** Indicates the vein approach for the tunneled CVC

#### 10. Course
- **Type:** AttributeType.CHOICE
- **Values:** Appropriate, Kinking, Coiling
- **Description:** Indicates the course of the tunneled CVC

#### 11. Distal tip location
- **Type:** AttributeType.CHOICE
- **Values:** Subclavian vein, Brachiocephalic vein, SVC (superior vena cava), Superior cavoatrial junction, Azygous vein, Inferior cavoatrial junction, Internal jugular vein, IVC (inferior vena cava)
- **Description:** Indicates the distal tip location of the tunneled CVC

#### 12. Complications
- **Type:** AttributeType.CHOICE
- **Values:** None, Occlusion, Thrombosis (fibrin sheath), Catheter fracture, Tip Migration
- **Description:** Indicates the complications associated with the tunneled CVC

### Required Attributes Added
None

---

## Final Attributes (17)

### 1. Presence of tunneled CVC
- **Name:** Presence of tunneled CVC
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether a tunneled CVC is present or absent
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Hematoma
- **Name:** Hematoma
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the presence or absence of a hematoma associated with the tunneled CVC
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 3. Pneumothorax
- **Name:** Pneumothorax
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the presence or absence of a pneumothorax associated with the tunneled CVC
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 4. Hemothorax
- **Name:** Hemothorax
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the presence or absence of a hemothorax associated with the tunneled CVC
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 5. Status
- **Name:** Status
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the status of the tunneled CVC
- **Values:** New placement, Unchanged, Migrated, Removed
- **Max selected:** 1
- **Required:** True

### 6. Appropriate location
- **Name:** Appropriate location
- **Type:** AttributeType.CHOICE
- **Description:** Indicates whether the tunneled CVC is in an appropriate location
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 7. Side Finding
- **Name:** Side Finding
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the side of the tunneled CVC
- **Values:** Left, Right
- **Max selected:** 1
- **Required:** True

### 8. Number of Lumens
- **Name:** Number of Lumens
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the number of lumens in the tunneled CVC
- **Values:** Single, Double, Triple
- **Max selected:** 1
- **Required:** True

### 9. Vein approach
- **Name:** Vein approach
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the vein approach for the tunneled CVC
- **Values:** Internal jugular, Subclavian
- **Max selected:** 1
- **Required:** True

### 10. Course
- **Name:** Course
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the course of the tunneled CVC
- **Values:** Appropriate, Kinking, Coiling
- **Max selected:** 1
- **Required:** True

### 11. Distal tip location
- **Name:** Distal tip location
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the distal tip location of the tunneled CVC
- **Values:** Subclavian vein, Brachiocephalic vein, SVC (superior vena cava), Superior cavoatrial junction, Azygous vein, Inferior cavoatrial junction, Internal jugular vein, IVC (inferior vena cava)
- **Max selected:** 1
- **Required:** True

### 12. Complications
- **Name:** Complications
- **Type:** AttributeType.CHOICE
- **Description:** Indicates the complications associated with the tunneled CVC
- **Values:** None, Occlusion, Thrombosis (fibrin sheath), Catheter fracture, Tip Migration
- **Max selected:** 1
- **Required:** True

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
