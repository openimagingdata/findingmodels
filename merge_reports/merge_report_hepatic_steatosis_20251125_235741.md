# Merge Report: Hepatic Steatosis
**Timestamp:** 2025-11-25 23:57:41

**Existing Model:** fatty liver (ID: OIFM_GMTS_022461)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 7
  - Severity
  - Density (noncontrast exam)
  - Distribution
  - Pattern
  - Falciform ligament
  - Portal Vein Thrombosis
  - Biliary Dilatation
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 11
- **Total final attributes:** 9

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** Presence or absence of fatty liver
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Classification:** change_from_prior
- **Description:** Whether and how a fatty liver has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (11)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** The presence or absence of hepatic steatosis.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Hepatomegaly
- **Name:** Hepatomegaly
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** The presence or absence of hepatomegaly.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 3. Focal Lesions
- **Name:** Focal Lesions
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** The presence or absence of focal lesions in the liver.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 4. Ascites
- **Name:** Ascites
- **Type:** AttributeType.CHOICE
- **Classification:** presence
- **Description:** The presence or absence of ascites.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 5. Severity
- **Name:** Severity
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The severity of hepatic steatosis.
- **Values:** Mild, Moderate, Severe
- **Max selected:** 1
- **Required:** True

### 6. Density (noncontrast exam)
- **Name:** Density (noncontrast exam)
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Description:** The density of hepatic steatosis on a noncontrast exam (in Hounsfield Units).
- **Unit:** HU
- **Required:** True

### 7. Distribution
- **Name:** Distribution
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The distribution of hepatic steatosis.
- **Values:** Diffuse, Focal
- **Max selected:** 1
- **Required:** True

### 8. Pattern
- **Name:** Pattern
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The pattern of hepatic steatosis.
- **Values:** Homogeneous, Heterogeneous, Patchy, Geographic
- **Max selected:** 1
- **Required:** True

### 9. Falciform ligament
- **Name:** Falciform ligament
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The presence of focal fat infiltration or focal fat sparing in the falciform ligament.
- **Values:** Focal fat infiltration, Focal fat sparing
- **Max selected:** 1
- **Required:** True

### 10. Portal Vein Thrombosis
- **Name:** Portal Vein Thrombosis
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The presence or absence of portal vein thrombosis.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 11. Biliary Dilatation
- **Name:** Biliary Dilatation
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The presence or absence of biliary dilatation.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged) (4)

*These attributes were compared but not merged. Review to verify they should remain separate.*

#### 1. presence vs Presence
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Presence' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

#### 2. presence vs Hepatomegaly
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Hepatomegaly' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

#### 3. presence vs Focal Lesions
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Focal Lesions' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

#### 4. presence vs Ascites
- **Relationship:** subset (confidence: 1.00)
- **Recommendation:** no_merge
- **AI Reasoning:** Existing attribute has standard presence values. Incoming attribute 'Ascites' will be discarded.

- **Existing only values:** absent, present, indeterminate, unknown
- **Incoming only values:** Present, Absent

### New Attributes Added (7)

#### 1. Severity
- **Type:** AttributeType.CHOICE
- **Values:** Mild, Moderate, Severe
- **Description:** The severity of hepatic steatosis.

#### 2. Density (noncontrast exam)
- **Type:** AttributeType.NUMERIC
- **Unit:** HU
- **Description:** The density of hepatic steatosis on a noncontrast exam (in Hounsfield Units).

#### 3. Distribution
- **Type:** AttributeType.CHOICE
- **Values:** Diffuse, Focal
- **Description:** The distribution of hepatic steatosis.

#### 4. Pattern
- **Type:** AttributeType.CHOICE
- **Values:** Homogeneous, Heterogeneous, Patchy, Geographic
- **Description:** The pattern of hepatic steatosis.

#### 5. Falciform ligament
- **Type:** AttributeType.CHOICE
- **Values:** Focal fat infiltration, Focal fat sparing
- **Description:** The presence of focal fat infiltration or focal fat sparing in the falciform ligament.

#### 6. Portal Vein Thrombosis
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** The presence or absence of portal vein thrombosis.

#### 7. Biliary Dilatation
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** The presence or absence of biliary dilatation.

### Required Attributes Added
None

---

## Final Attributes (9)

### 1. Severity
- **Name:** Severity
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The severity of hepatic steatosis.
- **Values:** Mild, Moderate, Severe
- **Max selected:** 1
- **Required:** True

### 2. Density (noncontrast exam)
- **Name:** Density (noncontrast exam)
- **Type:** AttributeType.NUMERIC
- **Classification:** other
- **Description:** The density of hepatic steatosis on a noncontrast exam (in Hounsfield Units).
- **Unit:** HU
- **Required:** True

### 3. Distribution
- **Name:** Distribution
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The distribution of hepatic steatosis.
- **Values:** Diffuse, Focal
- **Max selected:** 1
- **Required:** True

### 4. Pattern
- **Name:** Pattern
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The pattern of hepatic steatosis.
- **Values:** Homogeneous, Heterogeneous, Patchy, Geographic
- **Max selected:** 1
- **Required:** True

### 5. Falciform ligament
- **Name:** Falciform ligament
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The presence of focal fat infiltration or focal fat sparing in the falciform ligament.
- **Values:** Focal fat infiltration, Focal fat sparing
- **Max selected:** 1
- **Required:** True

### 6. Portal Vein Thrombosis
- **Name:** Portal Vein Thrombosis
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The presence or absence of portal vein thrombosis.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 7. Biliary Dilatation
- **Name:** Biliary Dilatation
- **Type:** AttributeType.CHOICE
- **Classification:** other
- **Description:** The presence or absence of biliary dilatation.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 8. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of fatty liver
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 9. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a fatty liver has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
