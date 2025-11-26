# Merge Report: Mediastinal Lymph Nodes
**Timestamp:** 2025-11-26 00:05:30

**Existing Model:** mediastinal and/or hilar lymph node enlargement (ID: OIFM_GMTS_015734)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 6
  - IASLC Lymph Node Stations
  - Station Involvement
  - Short-Axis Diameter
  - Shape
  - Density
  - Involvement of Adjacent Structures
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 8
- **Total final attributes:** 8

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence or absence of mediastinal and/or hilar lymph node enlargement
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Whether and how a mediastinal and/or hilar lymph node enlargement has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (8)

### 1. Presence of Enlarged Mediastinal Lymph Nodes
- **Name:** Presence of Enlarged Mediastinal Lymph Nodes
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 2. Evidence of Metastasis
- **Name:** Evidence of Metastasis
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 3. IASLC Lymph Node Stations
- **Name:** IASLC Lymph Node Stations
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** 1: Low Cervical, Supraclavicular, and Stellate Lymph Nodes, 2R: Upper Paratracheal Right, 2L: Upper Paratracheal Left, 3A: Prevascular, 3P: Retrotracheal, 4R: Lower Paratracheal Right, 4L: Lower Paratracheal Left, 5: Subaortic (Aortopulmonary Window), 6: Para-Aortic (Ascending Aorta or Phrenic), 7: Subcarinal, 8: Paraesophageal (Below Carina), 9: Pulmonary Ligament, 10: Hilar
- **Max selected:** 1
- **Required:** False

### 4. Station Involvement
- **Name:** Station Involvement
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Low Cervical, Supraclavicular, and Stellate Lymph Nodes, Upper Paratracheal Right, Upper Paratracheal Left, Prevascular, Retrotracheal, Lower Paratracheal Right, Lower Paratracheal Left, Subaortic (Aortopulmonary Window), Para-Aortic (Ascending Aorta or Phrenic), Subcarinal, Paraesophageal (Below Carina), Pulmonary Ligament, Hilar
- **Max selected:** 1
- **Required:** False

### 5. Short-Axis Diameter
- **Name:** Short-Axis Diameter
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Unit:** mm
- **Required:** False

### 6. Shape
- **Name:** Shape
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Round, Oval
- **Max selected:** 1
- **Required:** False

### 7. Density
- **Name:** Density
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Homogeneous, Heterogeneous
- **Max selected:** 1
- **Required:** False

### 8. Involvement of Adjacent Structures
- **Name:** Involvement of Adjacent Structures
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (2)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. presence vs Presence of Enlarged Mediastinal Lymph Nodes
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Presence of Enlarged Mediastinal Lymph Nodes' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Yes, No

#### 2. presence vs Evidence of Metastasis
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Evidence of Metastasis' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

### New Attributes Added (6)

#### 1. IASLC Lymph Node Stations
- **Type:** AttributeType.CHOICE
- **Values:** 1: Low Cervical, Supraclavicular, and Stellate Lymph Nodes, 2R: Upper Paratracheal Right, 2L: Upper Paratracheal Left, 3A: Prevascular, 3P: Retrotracheal, 4R: Lower Paratracheal Right, 4L: Lower Paratracheal Left, 5: Subaortic (Aortopulmonary Window), 6: Para-Aortic (Ascending Aorta or Phrenic), 7: Subcarinal, 8: Paraesophageal (Below Carina), 9: Pulmonary Ligament, 10: Hilar

#### 2. Station Involvement
- **Type:** AttributeType.CHOICE
- **Values:** Low Cervical, Supraclavicular, and Stellate Lymph Nodes, Upper Paratracheal Right, Upper Paratracheal Left, Prevascular, Retrotracheal, Lower Paratracheal Right, Lower Paratracheal Left, Subaortic (Aortopulmonary Window), Para-Aortic (Ascending Aorta or Phrenic), Subcarinal, Paraesophageal (Below Carina), Pulmonary Ligament, Hilar

#### 3. Short-Axis Diameter
- **Type:** AttributeType.NUMERIC
- **Unit:** mm

#### 4. Shape
- **Type:** AttributeType.CHOICE
- **Values:** Round, Oval

#### 5. Density
- **Type:** AttributeType.CHOICE
- **Values:** Homogeneous, Heterogeneous

#### 6. Involvement of Adjacent Structures
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

### Required Attributes Added
None

---

## Final Attributes (8)

### 1. IASLC Lymph Node Stations
- **Name:** IASLC Lymph Node Stations
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** 1: Low Cervical, Supraclavicular, and Stellate Lymph Nodes, 2R: Upper Paratracheal Right, 2L: Upper Paratracheal Left, 3A: Prevascular, 3P: Retrotracheal, 4R: Lower Paratracheal Right, 4L: Lower Paratracheal Left, 5: Subaortic (Aortopulmonary Window), 6: Para-Aortic (Ascending Aorta or Phrenic), 7: Subcarinal, 8: Paraesophageal (Below Carina), 9: Pulmonary Ligament, 10: Hilar
- **Max selected:** 1
- **Required:** False

### 2. Station Involvement
- **Name:** Station Involvement
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Low Cervical, Supraclavicular, and Stellate Lymph Nodes, Upper Paratracheal Right, Upper Paratracheal Left, Prevascular, Retrotracheal, Lower Paratracheal Right, Lower Paratracheal Left, Subaortic (Aortopulmonary Window), Para-Aortic (Ascending Aorta or Phrenic), Subcarinal, Paraesophageal (Below Carina), Pulmonary Ligament, Hilar
- **Max selected:** 1
- **Required:** False

### 3. Short-Axis Diameter
- **Name:** Short-Axis Diameter
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Unit:** mm
- **Required:** False

### 4. Shape
- **Name:** Shape
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Round, Oval
- **Max selected:** 1
- **Required:** False

### 5. Density
- **Name:** Density
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Homogeneous, Heterogeneous
- **Max selected:** 1
- **Required:** False

### 6. Involvement of Adjacent Structures
- **Name:** Involvement of Adjacent Structures
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 7. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of mediastinal and/or hilar lymph node enlargement
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 8. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a mediastinal and/or hilar lymph node enlargement has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
