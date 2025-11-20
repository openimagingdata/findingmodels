# Merge Report: Mediastinal Lymph Nodes
**Timestamp:** 2025-11-19 22:44:24

**Existing Model:** mediastinal and/or hilar lymph node enlargement (ID: OIFM_GMTS_015734)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 1
- **Review decisions made:** 1
  - Keep existing: 1
    - presence (kept, Evidence of Metastasis not added)
- **New attributes added:** 7
  - Presence of Enlarged Mediastinal Lymph Nodes
  - IASLC Lymph Node Stations
  - Station Involvement
  - Short-Axis Diameter
  - Shape
  - Density
  - Involvement of Adjacent Structures
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 8
- **Total final attributes:** 9

---

## ⚠️ Attributes Needing Review (1)

*These attributes were reviewed and decisions were made.*

### 1. presence vs Evidence of Metastasis
- **Relationship:** needs_review (confidence: 0.90)
- **Recommendation:** no_merge
- **Reason for review:** Attributes have shared values but each has unique values
- ✅ **Decision: Keep existing** (incoming attribute not added)
- **AI Reasoning:** The existing attribute 'presence' has values: ['absent', 'present', 'indeterminate', 'unknown']. The incoming attribute 'Evidence of Metastasis' has values: ['Present', 'Absent']. Comparing these values, there are shared values of 'Present' and 'Absent' (case insensitive). However, the existing attribute also includes 'indeterminate' and 'unknown', which are not present in the incoming attribute, indicating that both attributes have unique values not found in each other. Hence, we recognize the relationship as 'needs_review' since there are some shared values but each has unique values. All incoming values are in existing, and Incoming has no unique values: []

- **Shared values:** present, absent
- **Existing only values:** indeterminate, unknown

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of mediastinal and/or hilar lymph node enlargement
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a mediastinal and/or hilar lymph node enlargement has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (8)

### 1. Presence of Enlarged Mediastinal Lymph Nodes
- **Name:** Presence of Enlarged Mediastinal Lymph Nodes
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 2. IASLC Lymph Node Stations
- **Name:** IASLC Lymph Node Stations
- **Type:** AttributeType.CHOICE
- **Values:** 1: Low Cervical, Supraclavicular, and Stellate Lymph Nodes, 2R: Upper Paratracheal Right, 2L: Upper Paratracheal Left, 3A: Prevascular, 3P: Retrotracheal, 4R: Lower Paratracheal Right, 4L: Lower Paratracheal Left, 5: Subaortic (Aortopulmonary Window), 6: Para-Aortic (Ascending Aorta or Phrenic), 7: Subcarinal, 8: Paraesophageal (Below Carina), 9: Pulmonary Ligament, 10: Hilar
- **Max selected:** 1
- **Required:** False

### 3. Station Involvement
- **Name:** Station Involvement
- **Type:** AttributeType.CHOICE
- **Values:** Low Cervical, Supraclavicular, and Stellate Lymph Nodes, Upper Paratracheal Right, Upper Paratracheal Left, Prevascular, Retrotracheal, Lower Paratracheal Right, Lower Paratracheal Left, Subaortic (Aortopulmonary Window), Para-Aortic (Ascending Aorta or Phrenic), Subcarinal, Paraesophageal (Below Carina), Pulmonary Ligament, Hilar
- **Max selected:** 1
- **Required:** False

### 4. Short-Axis Diameter
- **Name:** Short-Axis Diameter
- **Type:** AttributeType.NUMERIC
- **Unit:** mm
- **Required:** False

### 5. Shape
- **Name:** Shape
- **Type:** AttributeType.CHOICE
- **Values:** Round, Oval
- **Max selected:** 1
- **Required:** False

### 6. Density
- **Name:** Density
- **Type:** AttributeType.CHOICE
- **Values:** Homogeneous, Heterogeneous
- **Max selected:** 1
- **Required:** False

### 7. Evidence of Metastasis
- **Name:** Evidence of Metastasis
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 8. Involvement of Adjacent Structures
- **Name:** Involvement of Adjacent Structures
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

### New Attributes Added (7)

#### 1. Presence of Enlarged Mediastinal Lymph Nodes
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No

#### 2. IASLC Lymph Node Stations
- **Type:** AttributeType.CHOICE
- **Values:** 1: Low Cervical, Supraclavicular, and Stellate Lymph Nodes, 2R: Upper Paratracheal Right, 2L: Upper Paratracheal Left, 3A: Prevascular, 3P: Retrotracheal, 4R: Lower Paratracheal Right, 4L: Lower Paratracheal Left, 5: Subaortic (Aortopulmonary Window), 6: Para-Aortic (Ascending Aorta or Phrenic), 7: Subcarinal, 8: Paraesophageal (Below Carina), 9: Pulmonary Ligament, 10: Hilar

#### 3. Station Involvement
- **Type:** AttributeType.CHOICE
- **Values:** Low Cervical, Supraclavicular, and Stellate Lymph Nodes, Upper Paratracheal Right, Upper Paratracheal Left, Prevascular, Retrotracheal, Lower Paratracheal Right, Lower Paratracheal Left, Subaortic (Aortopulmonary Window), Para-Aortic (Ascending Aorta or Phrenic), Subcarinal, Paraesophageal (Below Carina), Pulmonary Ligament, Hilar

#### 4. Short-Axis Diameter
- **Type:** AttributeType.NUMERIC
- **Unit:** mm

#### 5. Shape
- **Type:** AttributeType.CHOICE
- **Values:** Round, Oval

#### 6. Density
- **Type:** AttributeType.CHOICE
- **Values:** Homogeneous, Heterogeneous

#### 7. Involvement of Adjacent Structures
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent

### Required Attributes Added
None

---

## Final Attributes (9)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of mediastinal and/or hilar lymph node enlargement
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. Presence of Enlarged Mediastinal Lymph Nodes
- **Name:** Presence of Enlarged Mediastinal Lymph Nodes
- **Type:** AttributeType.CHOICE
- **Values:** Yes, No
- **Max selected:** 1
- **Required:** True

### 3. IASLC Lymph Node Stations
- **Name:** IASLC Lymph Node Stations
- **Type:** AttributeType.CHOICE
- **Values:** 1: Low Cervical, Supraclavicular, and Stellate Lymph Nodes, 2R: Upper Paratracheal Right, 2L: Upper Paratracheal Left, 3A: Prevascular, 3P: Retrotracheal, 4R: Lower Paratracheal Right, 4L: Lower Paratracheal Left, 5: Subaortic (Aortopulmonary Window), 6: Para-Aortic (Ascending Aorta or Phrenic), 7: Subcarinal, 8: Paraesophageal (Below Carina), 9: Pulmonary Ligament, 10: Hilar
- **Max selected:** 1
- **Required:** False

### 4. Station Involvement
- **Name:** Station Involvement
- **Type:** AttributeType.CHOICE
- **Values:** Low Cervical, Supraclavicular, and Stellate Lymph Nodes, Upper Paratracheal Right, Upper Paratracheal Left, Prevascular, Retrotracheal, Lower Paratracheal Right, Lower Paratracheal Left, Subaortic (Aortopulmonary Window), Para-Aortic (Ascending Aorta or Phrenic), Subcarinal, Paraesophageal (Below Carina), Pulmonary Ligament, Hilar
- **Max selected:** 1
- **Required:** False

### 5. Short-Axis Diameter
- **Name:** Short-Axis Diameter
- **Type:** AttributeType.NUMERIC
- **Unit:** mm
- **Required:** False

### 6. Shape
- **Name:** Shape
- **Type:** AttributeType.CHOICE
- **Values:** Round, Oval
- **Max selected:** 1
- **Required:** False

### 7. Density
- **Name:** Density
- **Type:** AttributeType.CHOICE
- **Values:** Homogeneous, Heterogeneous
- **Max selected:** 1
- **Required:** False

### 8. Involvement of Adjacent Structures
- **Name:** Involvement of Adjacent Structures
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** False

### 9. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a mediastinal and/or hilar lymph node enlargement has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
