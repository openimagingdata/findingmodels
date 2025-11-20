# Finding Model Merge Process

## Overview

When merging finding models, each incoming attribute is compared with all existing attributes of the same type. The system uses relationship type prioritization to determine the best match and action.

## Relationship Types

### 1. **Enhanced** → MERGE
- Incoming has ALL existing values + additional values
- **Example:** Existing: `["present", "absent"]` → Incoming: `["present", "absent", "unknown"]`
- **Action:** Merged automatically (if confidence ≥ 0.7)
- **If confidence < 0.7:** Flagged as "needs_review"

### 2. **Subset** → KEEP EXISTING
- Existing has ALL incoming values + additional values
- **Example:** Existing: `["left", "right", "unknown"]` → Incoming: `["left", "right"]`
- **Action:** Keep existing (no merge needed)

### 3. **Identical** → KEEP EXISTING
- Both have exactly the same values
- **Action:** Keep existing (no merge needed)

### 4. **Needs Review** → FLAG FOR REVIEW
- Shared values but each has unique values (ambiguous)
- **Example:** Existing: `["present", "absent", "unknown"]` → Incoming: `["present", "absent", "indeterminate"]`
- **Also:** Enhanced relationships with confidence < 0.7
- **Action:** Requires human decision

### 5. **No Similarities** → ADD AS NEW
- Completely different value sets (no overlap)
- **Action:** Added as new attribute (only if ALL comparisons are "no_similarities")

## Relationship Type Prioritization

The system prioritizes relationship types (not just confidence) to ensure the best match:

**Priority Order:**
1. **Enhanced** (confidence ≥ 0.7) → MERGE
2. **Subset/Identical** → KEEP EXISTING
3. **Needs Review** → FLAG FOR REVIEW
4. **No Similarities** → ADD AS NEW (only if all comparisons are no_similarities)

**Why it matters:** If an incoming attribute has "enhanced" with one existing (confidence 0.75) and "no_similarities" with others (confidence 0.95), the "enhanced" relationship takes priority and the attribute is merged, not added as new.

## Comparison Process

1. **Classify** attributes into: `presence`, `change_from_prior`, or `other`
2. **Compare** each incoming attribute with ALL existing attributes of the same type
3. **Prioritize** relationships using the priority order above
4. **Execute** actions: merge, keep existing, flag for review, or add as new

## Confidence Threshold

- **Enhanced relationships:** Require confidence ≥ 0.7 to auto-merge
- **Below 0.7:** Flagged as "needs_review" for safety

## Merge Reports

Reports include:
- **Summary** - Statistics
- **⚠️ Attributes Needing Review** - At the top for visibility
- **Merged Attributes** - Successfully merged
- **New Attributes Added** - Added as new
- **Final Attributes** - Complete list

## Key Points

- All attributes of the same type are compared (no pre-filtering)
- An attribute is only "new" if ALL comparisons are "no_similarities"
- Enhanced relationships need ≥ 0.7 confidence to auto-merge
- When in doubt, flag for review rather than auto-merge
