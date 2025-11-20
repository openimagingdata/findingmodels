# Merge Report: Hepatic Steatosis
**Timestamp:** 2025-11-19 22:36:43

**Existing Model:** fatty liver (ID: OIFM_GMTS_022461)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 11
  - Presence
  - Severity
  - Density (noncontrast exam)
  - Distribution
  - Pattern
  - Falciform ligament
  - Hepatomegaly
  - Focal Lesions
  - Portal Vein Thrombosis
  - Ascites
  - Biliary Dilatation
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 11
- **Total final attributes:** 13

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of fatty liver
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a fatty liver has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (11)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Description:** The presence or absence of hepatic steatosis.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Severity
- **Name:** Severity
- **Type:** AttributeType.CHOICE
- **Description:** The severity of hepatic steatosis.
- **Values:** Mild, Moderate, Severe
- **Max selected:** 1
- **Required:** True

### 3. Density (noncontrast exam)
- **Name:** Density (noncontrast exam)
- **Type:** AttributeType.NUMERIC
- **Description:** The density of hepatic steatosis on a noncontrast exam (in Hounsfield Units).
- **Unit:** HU
- **Required:** True

### 4. Distribution
- **Name:** Distribution
- **Type:** AttributeType.CHOICE
- **Description:** The distribution of hepatic steatosis.
- **Values:** Diffuse, Focal
- **Max selected:** 1
- **Required:** True

### 5. Pattern
- **Name:** Pattern
- **Type:** AttributeType.CHOICE
- **Description:** The pattern of hepatic steatosis.
- **Values:** Homogeneous, Heterogeneous, Patchy, Geographic
- **Max selected:** 1
- **Required:** True

### 6. Falciform ligament
- **Name:** Falciform ligament
- **Type:** AttributeType.CHOICE
- **Description:** The presence of focal fat infiltration or focal fat sparing in the falciform ligament.
- **Values:** Focal fat infiltration, Focal fat sparing
- **Max selected:** 1
- **Required:** True

### 7. Hepatomegaly
- **Name:** Hepatomegaly
- **Type:** AttributeType.CHOICE
- **Description:** The presence or absence of hepatomegaly.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 8. Focal Lesions
- **Name:** Focal Lesions
- **Type:** AttributeType.CHOICE
- **Description:** The presence or absence of focal lesions in the liver.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 9. Portal Vein Thrombosis
- **Name:** Portal Vein Thrombosis
- **Type:** AttributeType.CHOICE
- **Description:** The presence or absence of portal vein thrombosis.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 10. Ascites
- **Name:** Ascites
- **Type:** AttributeType.CHOICE
- **Description:** The presence or absence of ascites.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 11. Biliary Dilatation
- **Name:** Biliary Dilatation
- **Type:** AttributeType.CHOICE
- **Description:** The presence or absence of biliary dilatation.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

### New Attributes Added (11)

#### 1. Presence
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** The presence or absence of hepatic steatosis.

#### 2. Severity
- **Type:** AttributeType.CHOICE
- **Values:** Mild, Moderate, Severe
- **Description:** The severity of hepatic steatosis.

#### 3. Density (noncontrast exam)
- **Type:** AttributeType.NUMERIC
- **Unit:** HU
- **Description:** The density of hepatic steatosis on a noncontrast exam (in Hounsfield Units).

#### 4. Distribution
- **Type:** AttributeType.CHOICE
- **Values:** Diffuse, Focal
- **Description:** The distribution of hepatic steatosis.

#### 5. Pattern
- **Type:** AttributeType.CHOICE
- **Values:** Homogeneous, Heterogeneous, Patchy, Geographic
- **Description:** The pattern of hepatic steatosis.

#### 6. Falciform ligament
- **Type:** AttributeType.CHOICE
- **Values:** Focal fat infiltration, Focal fat sparing
- **Description:** The presence of focal fat infiltration or focal fat sparing in the falciform ligament.

#### 7. Hepatomegaly
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** The presence or absence of hepatomegaly.

#### 8. Focal Lesions
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** The presence or absence of focal lesions in the liver.

#### 9. Portal Vein Thrombosis
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** The presence or absence of portal vein thrombosis.

#### 10. Ascites
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** The presence or absence of ascites.

#### 11. Biliary Dilatation
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** The presence or absence of biliary dilatation.

### Required Attributes Added
None

---

## Final Attributes (13)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Description:** The presence or absence of hepatic steatosis.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Severity
- **Name:** Severity
- **Type:** AttributeType.CHOICE
- **Description:** The severity of hepatic steatosis.
- **Values:** Mild, Moderate, Severe
- **Max selected:** 1
- **Required:** True

### 3. Density (noncontrast exam)
- **Name:** Density (noncontrast exam)
- **Type:** AttributeType.NUMERIC
- **Description:** The density of hepatic steatosis on a noncontrast exam (in Hounsfield Units).
- **Unit:** HU
- **Required:** True

### 4. Distribution
- **Name:** Distribution
- **Type:** AttributeType.CHOICE
- **Description:** The distribution of hepatic steatosis.
- **Values:** Diffuse, Focal
- **Max selected:** 1
- **Required:** True

### 5. Pattern
- **Name:** Pattern
- **Type:** AttributeType.CHOICE
- **Description:** The pattern of hepatic steatosis.
- **Values:** Homogeneous, Heterogeneous, Patchy, Geographic
- **Max selected:** 1
- **Required:** True

### 6. Falciform ligament
- **Name:** Falciform ligament
- **Type:** AttributeType.CHOICE
- **Description:** The presence of focal fat infiltration or focal fat sparing in the falciform ligament.
- **Values:** Focal fat infiltration, Focal fat sparing
- **Max selected:** 1
- **Required:** True

### 7. Hepatomegaly
- **Name:** Hepatomegaly
- **Type:** AttributeType.CHOICE
- **Description:** The presence or absence of hepatomegaly.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 8. Focal Lesions
- **Name:** Focal Lesions
- **Type:** AttributeType.CHOICE
- **Description:** The presence or absence of focal lesions in the liver.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 9. Portal Vein Thrombosis
- **Name:** Portal Vein Thrombosis
- **Type:** AttributeType.CHOICE
- **Description:** The presence or absence of portal vein thrombosis.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 10. Ascites
- **Name:** Ascites
- **Type:** AttributeType.CHOICE
- **Description:** The presence or absence of ascites.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 11. Biliary Dilatation
- **Name:** Biliary Dilatation
- **Type:** AttributeType.CHOICE
- **Description:** The presence or absence of biliary dilatation.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 12. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of fatty liver
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 13. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a fatty liver has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
