# Merge Report: Chest Tube
**Timestamp:** 2025-11-19 22:18:34

**Existing Model:** Chest Radiograph Lines and Tubes (ID: OIFM_CDE_000237)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 11
  - presence
  - pneumothorax
  - pleural_effusion
  - hemothorax
  - rib_fracture
  - status
  - side Finding
  - location
  - current_tip_position
  - previous_tip_position
  - pulmonary_bleb
- **Required attributes added:** 0
- **Total existing attributes:** 5
- **Total incoming attributes:** 11
- **Total final attributes:** 16

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

## Incoming Attributes (11)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 2. status
- **Name:** status
- **Type:** AttributeType.CHOICE
- **Values:** new, unchanged, complication, resolved, removed
- **Max selected:** 1
- **Required:** True

### 3. side Finding
- **Name:** side Finding
- **Type:** AttributeType.CHOICE
- **Values:** right, left
- **Max selected:** 1
- **Required:** True

### 4. location
- **Name:** location
- **Type:** AttributeType.CHOICE
- **Values:** apical, basal, anterior, posterior, medial, lateral
- **Max selected:** 1
- **Required:** True

### 5. current_tip_position
- **Name:** current_tip_position
- **Type:** AttributeType.CHOICE
- **Values:** pleural space, intraparenchymal, chest wall
- **Max selected:** 1
- **Required:** True

### 6. previous_tip_position
- **Name:** previous_tip_position
- **Type:** AttributeType.CHOICE
- **Values:** pleural space, intraparenchymal, chest wall
- **Max selected:** 1
- **Required:** True

### 7. pneumothorax
- **Name:** pneumothorax
- **Type:** AttributeType.CHOICE
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 8. pleural_effusion
- **Name:** pleural_effusion
- **Type:** AttributeType.CHOICE
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 9. hemothorax
- **Name:** hemothorax
- **Type:** AttributeType.CHOICE
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 10. rib_fracture
- **Name:** rib_fracture
- **Type:** AttributeType.CHOICE
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 11. pulmonary_bleb
- **Name:** pulmonary_bleb
- **Type:** AttributeType.CHOICE
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

### New Attributes Added (11)

#### 1. presence
- **Type:** AttributeType.CHOICE
- **Values:** present, absent

#### 2. pneumothorax
- **Type:** AttributeType.CHOICE
- **Values:** present, absent

#### 3. pleural_effusion
- **Type:** AttributeType.CHOICE
- **Values:** present, absent

#### 4. hemothorax
- **Type:** AttributeType.CHOICE
- **Values:** present, absent

#### 5. rib_fracture
- **Type:** AttributeType.CHOICE
- **Values:** present, absent

#### 6. status
- **Type:** AttributeType.CHOICE
- **Values:** new, unchanged, complication, resolved, removed

#### 7. side Finding
- **Type:** AttributeType.CHOICE
- **Values:** right, left

#### 8. location
- **Type:** AttributeType.CHOICE
- **Values:** apical, basal, anterior, posterior, medial, lateral

#### 9. current_tip_position
- **Type:** AttributeType.CHOICE
- **Values:** pleural space, intraparenchymal, chest wall

#### 10. previous_tip_position
- **Type:** AttributeType.CHOICE
- **Values:** pleural space, intraparenchymal, chest wall

#### 11. pulmonary_bleb
- **Type:** AttributeType.CHOICE
- **Values:** present, absent

### Required Attributes Added
None

---

## Final Attributes (16)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 2. pneumothorax
- **Name:** pneumothorax
- **Type:** AttributeType.CHOICE
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 3. pleural_effusion
- **Name:** pleural_effusion
- **Type:** AttributeType.CHOICE
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 4. hemothorax
- **Name:** hemothorax
- **Type:** AttributeType.CHOICE
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 5. rib_fracture
- **Name:** rib_fracture
- **Type:** AttributeType.CHOICE
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 6. status
- **Name:** status
- **Type:** AttributeType.CHOICE
- **Values:** new, unchanged, complication, resolved, removed
- **Max selected:** 1
- **Required:** True

### 7. side Finding
- **Name:** side Finding
- **Type:** AttributeType.CHOICE
- **Values:** right, left
- **Max selected:** 1
- **Required:** True

### 8. location
- **Name:** location
- **Type:** AttributeType.CHOICE
- **Values:** apical, basal, anterior, posterior, medial, lateral
- **Max selected:** 1
- **Required:** True

### 9. current_tip_position
- **Name:** current_tip_position
- **Type:** AttributeType.CHOICE
- **Values:** pleural space, intraparenchymal, chest wall
- **Max selected:** 1
- **Required:** True

### 10. previous_tip_position
- **Name:** previous_tip_position
- **Type:** AttributeType.CHOICE
- **Values:** pleural space, intraparenchymal, chest wall
- **Max selected:** 1
- **Required:** True

### 11. pulmonary_bleb
- **Name:** pulmonary_bleb
- **Type:** AttributeType.CHOICE
- **Values:** present, absent
- **Max selected:** 1
- **Required:** True

### 12. Endotracheal tube
- **Name:** Endotracheal tube
- **Type:** AttributeType.CHOICE
- **Description:** Presence and position of endotracheal tube on XRAY
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

### 13. Central venous catheter
- **Name:** Central venous catheter
- **Type:** AttributeType.CHOICE
- **Description:** Presence and position of central venous catheter
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

### 14. Pulmonary artery catheter
- **Name:** Pulmonary artery catheter
- **Type:** AttributeType.CHOICE
- **Description:** Presence and position of pulmonary artery catheter
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

### 15. Nasogastric tube
- **Name:** Nasogastric tube
- **Type:** AttributeType.CHOICE
- **Description:** Presence and position of nasogastric tube
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

### 16. Airway stent
- **Name:** Airway stent
- **Type:** AttributeType.CHOICE
- **Description:** Presence and position of airway stent
- **Values:** absent, adequately positioned, malpositioned, indeterminate, suboptimally positioned
- **Max selected:** 1
- **Required:** False

---
