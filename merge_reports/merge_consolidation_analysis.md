# Merge Consolidation Analysis

**Generated:** 2025-01-15

## Overview

This report identifies existing findings that received multiple incoming findings merged into them. This occurs when the similarity search algorithm (used to find the closest match in the database) matches multiple incoming findings to the same existing finding.

**Key Finding:** Multiple incoming findings were merged into the same existing findings, which explains why we have 44 processed findings but only 35 files in `merged_findings`.

---

## Existing Findings with Multiple Merges

### 1. Chest Radiograph Lines and Tubes (ID: OIFM_CDE_000237)

**Number of incoming findings merged:** 4

#### Incoming Findings Merged Into This Existing Finding:

| Incoming Finding Name | File |
|----------------------|------|
| Picc Finding | `picc_finding.fm.json` |
| Nontunneled Cvc | `nontunneled_cvc.fm.json` |
| Ecmo Cannula | `ecmo_cannula.fm.json` |
| Chest Tube | `chest_tube.fm.json` |

---

### 2. diaphragmatic hernia (ID: OIFM_GMTS_022456)

**Number of incoming findings merged:** 3

#### Incoming Findings Merged Into This Existing Finding:

| Incoming Finding Name | File |
|----------------------|------|
| Morgagni Hernia | `morgagni_hernia.fm.json` |
| Hiatal Hernia | `hiatal_hernia.fm.json` |
| Bochdalek Hernia | `bochdalek_hernia.fm.json` |

---

### 3. mucoid impaction (ID: OIFM_GMTS_015330)

**Number of incoming findings merged:** 2

#### Incoming Findings Merged Into This Existing Finding:

| Incoming Finding Name | File |
|----------------------|------|
| Bronchial Plug | `bronchial_plug.fm.json` |
| Airway Mucus Plugging | `airway_mucus_plugging.fm.json` |

---

### 4. soft-tissue mediastinal mass (ID: OIFM_GMTS_015538)

**Number of incoming findings merged:** 2

**Note:** This appears to be the same finding processed twice (appears in two reports from different dates).

#### Incoming Findings Merged Into This Existing Finding:

| Incoming Finding Name | File |
|----------------------|------|
| Mediastinal Mass | `mediastinal_mass.fm.json` |
| Mediastinal Mass | `mediastinal_mass.fm.json` (processed twice) |

---

## Summary Statistics

- **Existing findings with multiple merges:** 4
- **Total incoming findings in consolidations:** 11 (4 + 3 + 2 + 2)
- **File updates created:** 4 (not 11, since multiple incoming findings update the same file)
- **"Extra" processed findings:** 7 (11 incoming findings - 4 unique files = 7)

### Breakdown by Number of Merges:

- **4 incoming finding(s):** 1 existing finding(s) (Chest Radiograph Lines and Tubes)
- **3 incoming finding(s):** 1 existing finding(s) (diaphragmatic hernia)
- **2 incoming finding(s):** 2 existing finding(s) (mucoid impaction, soft-tissue mediastinal mass)

---

## Explanation of the Discrepancy

The batch merge summary shows:
- **44 successfully processed findings**
- **35 files in `merged_findings`**

**Math:**
- 44 processed findings
- 11 of these merged into 4 existing findings (consolidations)
- 11 - 4 = 7 "extra" processed findings that didn't create new files
- 44 - 7 = 37 expected files... but we have 35

The remaining discrepancy (37 - 35 = 2) may be due to:
- Additional consolidations not captured in this analysis
- Findings that were merged but the existing file already existed
- Other edge cases in the merge process

---

## Why This Happens

This consolidation occurs because the similarity search algorithm (`find_similar_models`) matches incoming findings to existing findings in the database based on:
- Finding name similarity
- Description similarity
- Synonym matching

When multiple incoming findings are semantically similar to the same existing finding, they all get merged into that one existing finding, resulting in multiple updates to the same file rather than creating separate files.

