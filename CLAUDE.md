# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the **Open Imaging Finding Models** repository, a collection of standardized, machine-readable definitions for radiology findings. Finding models are updatable data models that define semantic tags for imaging findings and their properties, enabling structured reporting in radiology.

The repository contains:
- **2000+ finding model definitions** in JSON format (`defs/*.fm.json`)
- **Auto-generated markdown documentation** for each finding (`text/*.md`)
- **Schema definitions** (`schema/finding_model.schema.json`)
- **Lists and gamut collections** (`lists/`)

## Key Concepts

### Finding Models
Each finding model (`.fm.json`) defines a radiology finding with:
- Unique OIFM ID (pattern: `OIFM_[A-Z]{3,4}_[0-9]{6}`)
- Name and description
- Attributes (choice or numeric) that radiologists use to characterize the finding
- Each attribute has unique OIFMA ID (pattern: `OIFMA_[A-Z]{3,4}_[0-9]{6}`)
- Links to standard ontologies (SNOMED, RadLex, GAMUTS)

### File Organization
- `defs/`: Source JSON finding model definitions
- `text/`: Auto-generated markdown documentation (never edit manually)
- `index.md`: Auto-generated index of all findings (never edit manually)
- `ids.json`: Auto-generated ID tracking file (never edit manually)
- `schema/`: JSON schema and documentation
- `scripts/`: Validation and processing scripts
- `lists/`: Gamuts collections and other curated lists

## Development Commands

### Validation and Code Generation
```bash
# Validate all finding models, generate markdown files, and update indices
uv run scripts/validator.py

# Validate with git staging (used by pre-commit hook)
uv run scripts/validator.py --with-git-adds
```

The validator script:
1. Validates all `.fm.json` files against the schema
2. Checks for duplicate OIFM IDs and OIFMA IDs across all files
3. Auto-formats JSON files (rewrites them with consistent formatting)
4. Generates markdown files in `text/`
5. Updates `index.md` with all findings
6. Updates `ids.json` with ID tracking


### Pre-commit Hook
A pre-commit hook automatically runs validation on every commit:
```bash
# The hook runs automatically, but you can also run it manually:
pre-commit run --all-files
```

## Important Constraints

### Never Edit Generated Files
The following files are **auto-generated** and should **never be edited manually**:
- `text/*.md` (markdown documentation)
- `index.md` (finding index)
- `ids.json` (ID tracking)

These are regenerated from `defs/*.fm.json` by `scripts/validator.py`.

### ID Uniqueness
- Each finding model must have a unique `oifm_id`
- Each attribute must have a unique `oifma_id` across ALL finding models
- The validator enforces this and will fail if duplicates are found

### File Naming
Finding model JSON files must:
- Be in `defs/` directory
- End with `.fm.json` extension
- Use snake_case naming derived from the finding name

## Schema Structure

See schema/finding_model_schema.json.

## Python Environment

All Python scripts use **uv** for dependency management with inline script metadata (PEP 723):
- Scripts specify dependencies in header comments
- Run with: `uv run script_name.py`
- No separate virtual environment or requirements.txt needed
- Requires Python 3.13+ for main scripts

The main Python package used is `findingmodel`, which provides:
- `FindingModelFull` - Pydantic model for finding definitions
- `model_file_name()` - Generate proper filename from finding name
- `normalize_name()` - Convert finding name to snake_case
- `as_markdown()` - Generate markdown documentation

## Workflow for Adding/Editing Findings

1. **Edit or create** a `.fm.json` file in `defs/`
2. **Run validation**: `uv run scripts/validator.py`
   - This auto-formats JSON, generates markdown, and updates indices
3. **Review changes** to generated files (text/, index.md, ids.json)
4. **Commit** (pre-commit hook will run validation automatically)

## Workflow for Git Operations

The validator can automatically stage generated files when used with `--with-git-adds` flag (used by pre-commit hook). When committing changes:

1. Edit `.fm.json` files in `defs/`
2. Stage your changes: `git add defs/your_file.fm.json`
3. Commit (pre-commit hook runs validation and stages generated files)
4. The hook ensures all generated files are in sync

## Branch Strategy

- Main branch: `main`
- Current branch: `load_cde_fms` (migrating CDE-based definitions)
- Create pull requests to merge into `main`

## Common Ontologies

Finding models link to standard medical ontologies:
- **SNOMED**: Systematized Nomenclature of Medicine
- **RadLex**: Radiology Lexicon
- **GAMUTS**: Radiology Gamuts Ontology (gamuts.net)

Index codes are specified in `index_codes` arrays with `system`, `code`, and optional `display` fields.
