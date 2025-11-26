# Merge Report: Picc Finding
**Timestamp:** 2025-11-26 00:17:14

**Existing Model:** Chest Radiograph Lines and Tubes (ID: OIFM_CDE_000237)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 4
  - Change from prior
  - Side Finding
  - Distal tip location
  - Appropriate location
- **Required attributes added:** 0
- **Total existing attributes:** 5
- **Total incoming attributes:** 4
- **Total final attributes:** 9

---

## Existing Attributes (5)

### 1. Airway stent
- **Name:** Airway stent
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence and position of airway stent
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

### 2. Endotracheal tube
- **Name:** Endotracheal tube
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence and position of endotracheal tube on XRAY
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

### 3. Central venous catheter
- **Name:** Central venous catheter
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence and position of central venous catheter
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

### 4. Pulmonary artery catheter
- **Name:** Pulmonary artery catheter
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence and position of pulmonary artery catheter
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

### 5. Nasogastric tube
- **Name:** Nasogastric tube
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Presence and position of nasogastric tube
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (4)

### 1. Change from prior
- **Name:** Change from prior
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Any change in the PICC placement from the prior study
- **Values:** New placement, Unchanged, Retracted, Migrated, Removed
- **Max selected:** 1
- **Required:** True

### 2. Side Finding
- **Name:** Side Finding
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The side of the body where the PICC is inserted
- **Values:** Left upper extremity, Right upper extremity, Left lower extremity, Right lower extremity
- **Max selected:** 1
- **Required:** True

### 3. Distal tip location
- **Name:** Distal tip location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The location of the distal tip of the PICC
- **Values:** Subclavian vein, Brachiocephalic vein, SVC, Superior cavoatrial junction, Azygous vein, Inferior cavoatrial junction, Internal jugular vein
- **Max selected:** 1
- **Required:** True

### 4. Appropriate location
- **Name:** Appropriate location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Whether the location of the PICC is appropriate
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

### New Attributes Added (4)

#### 1. Change from prior
- **Type:** AttributeType.CHOICE
- **Values:** New placement, Unchanged, Retracted, Migrated, Removed
- **Description:** Any change in the PICC placement from the prior study

#### 2. Side Finding
- **Type:** AttributeType.CHOICE
- **Values:** Left upper extremity, Right upper extremity, Left lower extremity, Right lower extremity
- **Description:** The side of the body where the PICC is inserted

#### 3. Distal tip location
- **Type:** AttributeType.CHOICE
- **Values:** Subclavian vein, Brachiocephalic vein, SVC, Superior cavoatrial junction, Azygous vein, Inferior cavoatrial junction, Internal jugular vein
- **Description:** The location of the distal tip of the PICC

#### 4. Appropriate location
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No
- **Description:** Whether the location of the PICC is appropriate

### Required Attributes Added
None

---

## Final Attributes (9)

### 1. Change from prior
- **Name:** Change from prior
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Any change in the PICC placement from the prior study
- **Values:** New placement, Unchanged, Retracted, Migrated, Removed
- **Max selected:** 1
- **Required:** True

### 2. Side Finding
- **Name:** Side Finding
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The side of the body where the PICC is inserted
- **Values:** Left upper extremity, Right upper extremity, Left lower extremity, Right lower extremity
- **Max selected:** 1
- **Required:** True

### 3. Distal tip location
- **Name:** Distal tip location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The location of the distal tip of the PICC
- **Values:** Subclavian vein, Brachiocephalic vein, SVC, Superior cavoatrial junction, Azygous vein, Inferior cavoatrial junction, Internal jugular vein
- **Max selected:** 1
- **Required:** True

### 4. Appropriate location
- **Name:** Appropriate location
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** Whether the location of the PICC is appropriate
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 5. Endotracheal tube
- **Name:** Endotracheal tube
- **Type:** AttributeType.CHOICE
- **Description:** Presence and position of endotracheal tube on XRAY
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

### 6. Central venous catheter
- **Name:** Central venous catheter
- **Type:** AttributeType.CHOICE
- **Description:** Presence and position of central venous catheter
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

### 7. Pulmonary artery catheter
- **Name:** Pulmonary artery catheter
- **Type:** AttributeType.CHOICE
- **Description:** Presence and position of pulmonary artery catheter
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

### 8. Nasogastric tube
- **Name:** Nasogastric tube
- **Type:** AttributeType.CHOICE
- **Description:** Presence and position of nasogastric tube
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

### 9. Airway stent
- **Name:** Airway stent
- **Type:** AttributeType.CHOICE
- **Description:** Presence and position of airway stent
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

---
