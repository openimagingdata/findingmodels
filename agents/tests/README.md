# Attribute Classifier Tests

This directory contains comprehensive tests for the attribute classifier agents.

## Test Files

- `test_attribute_classifier.py` - Main test script for all three agents
- `test_results_summary.md` - Initial test results summary
- `test_results_with_real_data.md` - Test results using real hood_findings data
- `attribute_classifier_explanation.md` - Detailed explanation of the code structure

## Running Tests

From the project root directory:

```bash
python agents/tests/test_attribute_classifier.py
```

## Test Coverage

### Classification Agent
- ✅ Presence attributes (Present/Absent values)
- ✅ Change from prior attributes (Status with temporal values)
- ✅ Other attributes (Size, Location, Morphology, Numeric)
- ✅ Error handling for invalid inputs

### Comparison Agent
- ✅ Identical attribute detection
- ✅ Enhanced attribute detection
- ✅ Different attribute identification
- ✅ Medical context understanding

### Merger Agent
- ✅ Attribute merging with real OIFMA IDs
- ✅ Value combination and deduplication
- ✅ Description preservation and enhancement
- ✅ Schema validation

## Test Data

Tests use real medical attributes from the `hood_findings` dataset:
- Pneumothorax findings (Presence, Status, Size, Location)
- Pulmonary nodule findings (Morphology, numeric size)
- Real OIFMA IDs for proper validation

## Results

All tests pass with high confidence scores (90-100%) demonstrating excellent performance with real medical data.
