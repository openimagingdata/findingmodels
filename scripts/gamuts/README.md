# Gamuts.net Processing Script

This script converts Gamuts.net pages into structured JSONL files containing categorized medical terms.

## Overview

The script performs the following workflow:

1. Scrapes a Gamuts.net URL to extract medical terms and their IDs
2. Uses OpenAI's API to categorize and structure the terms with metadata
3. Saves the results to a JSONL file with one categorized term per line

## Prerequisites

- [uv](https://docs.astral.sh/uv/) - Fast Python package manager and project manager
- Python 3.13+ (automatically managed by uv)

## Setup

1. Install uv if you haven't already:

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Set up your OpenAI API key:

   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

   Or create a `.env` file in the project root:

   ```bash
   OPENAI_API_KEY=your-api-key-here
   ```

The script uses uv's script dependency management, so no separate dependency installation is required.

## Usage

Basic usage:

```bash
uv run process_gamuts.py "https://www.gamuts.net/s/vi"
```

With custom output file:

```bash
uv run process_gamuts.py "https://www.gamuts.net/s/vi" --output chest_gamuts.jsonl
```

With custom chunk size (number of terms processed per API call):

```bash
uv run process_gamuts.py "https://www.gamuts.net/s/vi" --output chest_gamuts.jsonl --chunk-size 15
```

## Output Format

The script generates a JSONL file where each line contains one categorized term in JSON format:

```json
{"gamuts_id": "15619", "name": "thymic enlargement", "seen_on_modalities": ["XR", "CT", "MR"], "description": "Enlargement of the thymus gland, often seen in various conditions.", "synonyms": ["thymic hypertrophy", "large thymus"], "category": "finding", "subcategories": ["congenital anomaly", "mediastinum"], "radiologist_comments": true}
{"gamuts_id": "14124", "name": "superior vena cava syndrome", "seen_on_modalities": ["CT", "MR"], "description": "A condition caused by obstruction of the superior vena cava.", "synonyms": ["SVC syndrome"], "category": "diagnosis", "subcategories": ["vascular", "mediastinum"], "radiologist_comments": true}
```

Each line represents a single `CategorizedTerm` object with the following structure:

- `gamuts_id`: Original Gamuts.net ID
- `name`: Medical term name
- `seen_on_modalities`: Imaging modalities (CT, XR, MR, US)
- `description`: Brief description
- `synonyms`: Alternative names and abbreviations
- `category`: "finding" or "diagnosis"
- `subcategories`: Anatomical location and process type
- `radiologist_comments`: Whether typically mentioned in reports

## Common Gamuts.net URLs

- Chest: `https://www.gamuts.net/s/vi`
- GI: `https://www.gamuts.net/s/gi`
- GU: `https://www.gamuts.net/s/gu`
- Head & Neck: `https://www.gamuts.net/s/hn`

## Error Handling

The script includes error handling for:

- Failed HTTP requests
- Missing OpenAI API key
- API response errors
- Individual chunk processing failures (continues with remaining chunks)

If a chunk fails to process, the script will log the error and continue with the remaining terms.

## Notes

- The script processes terms in chunks (default: 20) to avoid overwhelming the OpenAI API
- Processing time depends on the number of terms and API response times
- Output files are created with UTF-8 encoding and proper JSON formatting
