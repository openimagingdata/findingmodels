# Merge Report: Emphysema
**Timestamp:** 2025-11-19 22:28:03

**Existing Model:** Emphysema (ID: OIFM_CDE_000286)

---

## Summary

- **Attributes merged:** 0
- **Attributes needing review:** 0
- **New attributes added:** 6
  - Presence
  - Type Finding
  - Severity
  - Location
  - Laterality
  - Associated Findings
- **Required attributes added:** 1
- **Total existing attributes:** 5
- **Total incoming attributes:** 6
- **Total final attributes:** 12

---

## Existing Attributes (5)

### 1. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Values:** right upper lobe (RUL), right middle lobe (RML), right upper lobe and right middle lobe (RUL + RML), right lower lobe (RLL), left upper lobe (LUL), left lower lobe (LLL)
- **Max selected:** 1
- **Required:** False

### 2. Emphysema scale (% - 920HU)
- **Name:** Emphysema scale (% - 920HU)
- **Type:** AttributeType.NUMERIC
- **Unit:** %
- **Range:** 0 - 100
- **Required:** False

### 3. Emphysema scale (% - 950HU)
- **Name:** Emphysema scale (% - 950HU)
- **Type:** AttributeType.NUMERIC
- **Unit:** %
- **Range:** 0 - 100
- **Required:** False

### 4. Fissure completeness scale
- **Name:** Fissure completeness scale
- **Type:** AttributeType.NUMERIC
- **Unit:** %
- **Range:** 0 - 100
- **Required:** False

### 5. Volume
- **Name:** Volume
- **Type:** AttributeType.NUMERIC
- **Unit:** ml
- **Range:** 0 - 3000
- **Required:** False

---

## Incoming Attributes (6)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Description:** The presence or absence of emphysema.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Type Finding
- **Name:** Type Finding
- **Type:** AttributeType.CHOICE
- **Description:** The type of emphysema.
- **Values:** Centrilobular, Panlobular, Paraseptal, Bullous, Irregular, Subpleural
- **Max selected:** 1
- **Required:** True

### 3. Severity
- **Name:** Severity
- **Type:** AttributeType.CHOICE
- **Description:** The severity of emphysema.
- **Values:** Mild, Moderate, Severe, Very Severe, Extensive
- **Max selected:** 1
- **Required:** True

### 4. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Description:** The location of emphysema in the lungs.
- **Values:** Upper Lobes, Lower Lobes, Diffuse, Peribronchovascular, Apex to Base
- **Max selected:** 1
- **Required:** True

### 5. Laterality
- **Name:** Laterality
- **Type:** AttributeType.CHOICE
- **Description:** The laterality of emphysema.
- **Values:** Right, Left, Bilateral, Predominant Side
- **Max selected:** 1
- **Required:** True

### 6. Associated Findings
- **Name:** Associated Findings
- **Type:** AttributeType.CHOICE
- **Description:** The associated findings with emphysema.
- **Values:** Air trapping, Pulmonary nodules, Fibrosis, Pleural abnormalities, Bronchiectasis
- **Max selected:** 1
- **Required:** False

---

### Merged Attributes
None

### Comparisons Made (Not Merged)
None

### New Attributes Added (6)

#### 1. Presence
- **Type:** AttributeType.CHOICE
- **Values:** Present, Absent
- **Description:** The presence or absence of emphysema.

#### 2. Type Finding
- **Type:** AttributeType.CHOICE
- **Values:** Centrilobular, Panlobular, Paraseptal, Bullous, Irregular, Subpleural
- **Description:** The type of emphysema.

#### 3. Severity
- **Type:** AttributeType.CHOICE
- **Values:** Mild, Moderate, Severe, Very Severe, Extensive
- **Description:** The severity of emphysema.

#### 4. Location
- **Type:** AttributeType.CHOICE
- **Values:** Upper Lobes, Lower Lobes, Diffuse, Peribronchovascular, Apex to Base
- **Description:** The location of emphysema in the lungs.

#### 5. Laterality
- **Type:** AttributeType.CHOICE
- **Values:** Right, Left, Bilateral, Predominant Side
- **Description:** The laterality of emphysema.

#### 6. Associated Findings
- **Type:** AttributeType.CHOICE
- **Values:** Air trapping, Pulmonary nodules, Fibrosis, Pleural abnormalities, Bronchiectasis
- **Description:** The associated findings with emphysema.

### Required Attributes Added (1)

#### change from prior
- **Type:** choice
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller

---

## Final Attributes (12)

### 1. Presence
- **Name:** Presence
- **Type:** AttributeType.CHOICE
- **Description:** The presence or absence of emphysema.
- **Values:** Present, Absent
- **Max selected:** 1
- **Required:** True

### 2. Type Finding
- **Name:** Type Finding
- **Type:** AttributeType.CHOICE
- **Description:** The type of emphysema.
- **Values:** Centrilobular, Panlobular, Paraseptal, Bullous, Irregular, Subpleural
- **Max selected:** 1
- **Required:** True

### 3. Severity
- **Name:** Severity
- **Type:** AttributeType.CHOICE
- **Description:** The severity of emphysema.
- **Values:** Mild, Moderate, Severe, Very Severe, Extensive
- **Max selected:** 1
- **Required:** True

### 4. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Description:** The location of emphysema in the lungs.
- **Values:** Upper Lobes, Lower Lobes, Diffuse, Peribronchovascular, Apex to Base
- **Max selected:** 1
- **Required:** True

### 5. Laterality
- **Name:** Laterality
- **Type:** AttributeType.CHOICE
- **Description:** The laterality of emphysema.
- **Values:** Right, Left, Bilateral, Predominant Side
- **Max selected:** 1
- **Required:** True

### 6. Associated Findings
- **Name:** Associated Findings
- **Type:** AttributeType.CHOICE
- **Description:** The associated findings with emphysema.
- **Values:** Air trapping, Pulmonary nodules, Fibrosis, Pleural abnormalities, Bronchiectasis
- **Max selected:** 1
- **Required:** False

### 7. Location
- **Name:** Location
- **Type:** AttributeType.CHOICE
- **Values:** right upper lobe (RUL), right middle lobe (RML), right upper lobe and right middle lobe (RUL + RML), right lower lobe (RLL), left upper lobe (LUL), left lower lobe (LLL)
- **Max selected:** 1
- **Required:** False

### 8. Emphysema scale (% - 920HU)
- **Name:** Emphysema scale (% - 920HU)
- **Type:** AttributeType.NUMERIC
- **Unit:** %
- **Range:** 0 - 100
- **Required:** False

### 9. Emphysema scale (% - 950HU)
- **Name:** Emphysema scale (% - 950HU)
- **Type:** AttributeType.NUMERIC
- **Unit:** %
- **Range:** 0 - 100
- **Required:** False

### 10. Fissure completeness scale
- **Name:** Fissure completeness scale
- **Type:** AttributeType.NUMERIC
- **Unit:** %
- **Range:** 0 - 100
- **Required:** False

### 11. Volume
- **Name:** Volume
- **Type:** AttributeType.NUMERIC
- **Unit:** ml
- **Range:** 0 - 3000
- **Required:** False

### 12. change from prior
- **Name:** change from prior
- **Type:** choice
- **Description:** Whether and how a Emphysema has changed over time
- **Values:** unchanged, stable, new, resolved, increased, decreased, larger, smaller
- **Max selected:** 1
- **Required:** False

---
