# Redundancy Analysis - How Categorization Works

## Overview
This analysis uses AI-powered similarity detection to categorize new finding models based on their similarity to existing models.

## Categorization by Confidence Interval

### Unique Models
- **Confidence: 0.0**
- **Recommendation: "create_new"**
- **Meaning:** No similar models found in existing data
- **Action:** Safe to add as-is to the collection

### Exact Duplicates
- **Confidence: 0.9-1.0**
- **Recommendation: "edit_existing"**
- **Meaning:** Perfect or very close matches found
- **Action:** Merge new attributes into existing models

### Similar Models
- **Confidence: 0.5-0.8**
- **Recommendation: "edit_existing"**
- **Meaning:** Partial matches requiring manual review
- **Action:** Develop merge strategy

### Errors
- **Error Type:** Empty/malformed JSON files
- **Action:** Fix file format or skip

## How Confidence Scoring Works
- **1.0 (100%)** = Exact name match found
- **0.9 (90%)** = Very similar models found
- **0.5-0.8 (50-80%)** = Partial similarity, needs review
- **0.0 (0%)** = No similar models found (unique)

## Files Generated
- `unique_models.json` - Models safe to add as-is
- `exact_duplicate_models.json` - Models that need merging
- `similar_models.json` - Models needing manual review
- `error_models.json` - Files with processing errors
- `redundancy_analysis.json` - Complete analysis data
