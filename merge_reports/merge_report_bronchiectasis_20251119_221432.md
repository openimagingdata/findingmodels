# Merge Report: Bronchiectasis
**Timestamp:** 2025-11-19 22:14:32

**Existing Model:** bronchiectasis (ID: OIFM_GMTS_013943)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 4
  - Predominant Type(s)
  - Severity
  - Regional predominance
  - Associated diagnoses
- **Required attributes added:** 0
- **Total existing attributes:** 2
- **Total incoming attributes:** 4
- **Total final attributes:** 6

---

## Existing Attributes (2)

### 1. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of bronchiectasis
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 2. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a bronchiectasis has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---

## Incoming Attributes (4)

### 1. Predominant Type(s)
- **Name:** Predominant Type(s)
- **Type:** AttributeType.CHOICE
- **Description:** The predominant type(s) of bronchiectasis present.
- **Values:** Cylindrical, Varicose, Cystic
- **Max selected:** 1
- **Required:** True

### 2. Severity
- **Name:** Severity
- **Type:** AttributeType.CHOICE
- **Description:** The severity of bronchiectasis.
- **Values:** Mild, Moderate, Severe
- **Max selected:** 1
- **Required:** True

### 3. Regional predominance
- **Name:** Regional predominance
- **Type:** AttributeType.CHOICE
- **Description:** The regional predominance of bronchiectasis.
- **Values:** Apices, Upper lung zone, Middle lung zone, Lower lung zone
- **Max selected:** 1
- **Required:** True

### 4. Associated diagnoses
- **Name:** Associated diagnoses
- **Type:** AttributeType.CHOICE
- **Description:** Associated diagnoses related to bronchiectasis.
- **Values:** Immunodeficiency, Postinfective, Allergic and autoimmune, Obstruction, Congenital, Others
- **Max selected:** 1
- **Required:** True

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

### New Attributes Added (4)

#### 1. Predominant Type(s)
- **Type:** AttributeType.CHOICE
- **Values:** Cylindrical, Varicose, Cystic
- **Description:** The predominant type(s) of bronchiectasis present.

#### 2. Severity
- **Type:** AttributeType.CHOICE
- **Values:** Mild, Moderate, Severe
- **Description:** The severity of bronchiectasis.

#### 3. Regional predominance
- **Type:** AttributeType.CHOICE
- **Values:** Apices, Upper lung zone, Middle lung zone, Lower lung zone
- **Description:** The regional predominance of bronchiectasis.

#### 4. Associated diagnoses
- **Type:** AttributeType.CHOICE
- **Values:** Immunodeficiency, Postinfective, Allergic and autoimmune, Obstruction, Congenital, Others
- **Description:** Associated diagnoses related to bronchiectasis.

### Required Attributes Added
None

---

## Final Attributes (6)

### 1. Predominant Type(s)
- **Name:** Predominant Type(s)
- **Type:** AttributeType.CHOICE
- **Description:** The predominant type(s) of bronchiectasis present.
- **Values:** Cylindrical, Varicose, Cystic
- **Max selected:** 1
- **Required:** True

### 2. Severity
- **Name:** Severity
- **Type:** AttributeType.CHOICE
- **Description:** The severity of bronchiectasis.
- **Values:** Mild, Moderate, Severe
- **Max selected:** 1
- **Required:** True

### 3. Regional predominance
- **Name:** Regional predominance
- **Type:** AttributeType.CHOICE
- **Description:** The regional predominance of bronchiectasis.
- **Values:** Apices, Upper lung zone, Middle lung zone, Lower lung zone
- **Max selected:** 1
- **Required:** True

### 4. Associated diagnoses
- **Name:** Associated diagnoses
- **Type:** AttributeType.CHOICE
- **Description:** Associated diagnoses related to bronchiectasis.
- **Values:** Immunodeficiency, Postinfective, Allergic and autoimmune, Obstruction, Congenital, Others
- **Max selected:** 1
- **Required:** True

### 5. presence
- **Name:** presence
- **Type:** AttributeType.CHOICE
- **Description:** Presence or absence of bronchiectasis
- **Values:** absent, present, indeterminate, unknown
- **Max selected:** 1
- **Required:** False

### 6. change from prior
- **Name:** change from prior
- **Type:** AttributeType.CHOICE
- **Description:** Whether and how a bronchiectasis has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
