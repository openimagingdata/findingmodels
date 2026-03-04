# Refactor: Agent Pipeline with Python Orchestration

## Context

The current `agents/hood_agent.py` is a single monolithic pydantic-ai agent with 7 tools and a ~50-line system prompt. Problems:

1. **Pydantic-AI anti-patterns**: `system_prompt=` instead of `instructions=`, factory function instead of module-level singleton, `tools=[]` list instead of `@agent.tool` decorators, JSON string returns from tools, blanket `try/except` instead of `ModelRetry`
2. **Re-implements library functions**: The `findingmodel_ai` library already provides `find_similar_models()`, `find_anatomic_locations()`, `create_info_from_name()` — but the agent uses raw index search + its own logic
3. **Single agent does too much**: Search, match, merge, create, format, add IDs, add codes, find locations — all in one agent call with one prompt
4. **No structured branching**: The agent decides merge vs. create internally with no Python-level control flow

**Goal**: Replace with a Python-orchestrated pipeline using 3 focused agents (merge, create, review) and library functions for search/enrichment, with clear data flow between steps.

---

## Architecture

```
1. Parse Input (extract finding name, description, content)
       |
       +------------ PARALLEL (asyncio.gather) -----------+
       |                                                   |
       v                                                   v
2a. find_similar_models()                           2b. find_anatomic_locations()
    (findingmodel_ai library)                           (findingmodel_ai library)
       |                                                   |
       v                                                   | (saved for step 4+5)
   SimilarModelAnalysis                                    |
       |                                                   |
   BRANCH on recommendation + confidence                   |
   |                           |                           |
   v                           v                           |
3a. Merge Agent             3b. Create Agent               |
   (gpt-5.2, high)            (gpt-5.2, medium)           |
       |                           |                       |
       +-------------+------------+                       |
                     |                                     |
                     v                                     |
4. Review Agent (gpt-5.2, none)    <----- locations ------+
       |
       v
5. Post-processing (deterministic Python)
   - add_ids_to_model()
   - add_standard_codes_to_model()
   - set anatomic_locations from step 2b
   - normalize_for_validation()
       |
       v
6. Validate (FindingModelFull.model_validate) + Save
```

---

## Implementation Chunks

Each chunk below is atomic and can be implemented and tested independently. Chunks have dependencies noted.

---

### Chunk 1: Create `agents/merge_agent.py`

**Depends on**: Nothing (new file)

**File**: `agents/merge_agent.py`

**What to build**:
- `MergeResult` pydantic model (structured output)
- `MergeContext` dataclass (deps with Index)
- Module-level `merge_agent = Agent(...)` singleton
- `@merge_agent.tool` for `get_full_model` (returns `dict`, raises `ModelRetry` on error)
- Instructions loaded from `prompts/merge_agent.md`

**Output model**:
```python
class MergeResult(BaseModel):
    merged_model: dict[str, Any]     # FindingModelFull as dict (with oifm_id from target)
    target_oifm_id: str              # which existing model was merged into
    changes_made: list[str]          # summary of merge decisions
    sub_findings: list[str]          # attributes that should be separate findings
```

**Deps dataclass**:
```python
@dataclass
class MergeContext:
    index: Index
```

**Tool — `get_full_model`**:
```python
@merge_agent.tool
async def get_full_model(ctx: RunContext[MergeContext], oifm_id: str) -> dict[str, Any]:
    """Retrieve a full finding model by OIFM ID to inspect before merging."""
    try:
        model = await ctx.deps.index.get_full(oifm_id)
        return model.model_dump(exclude_none=False)
    except Exception as e:
        raise ModelRetry(f"Failed to retrieve model {oifm_id}: {e}")
```

**Agent definition**:
```python
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel, OpenAIChatModelSettings

MODEL = OpenAIChatModel("gpt-5.2")

merge_agent = Agent(
    model=MODEL,
    deps_type=MergeContext,
    output_type=MergeResult,
    instructions=Path("prompts/merge_agent.md").read_text(),
    model_settings=OpenAIChatModelSettings(openai_reasoning_effort='high'),
    retries=3,
)
```

**Prompt**: See `prompts/merge_agent.md`

**Expected output**: A Python module that can be imported. Agent is not runnable standalone without the pipeline feeding it a user message.

**Verification**: `python -c "from agents.merge_agent import merge_agent, MergeResult; print('OK')"` should import without error.

---

### Chunk 2: Create `agents/create_agent.py`

**Depends on**: Nothing (new file)

**File**: `agents/create_agent.py`

**What to build**:
- `CreateResult` pydantic model (structured output)
- Module-level `create_agent = Agent(...)` singleton
- No tools (pure text-in, structured-out)
- Instructions loaded from `prompts/create_agent.md`

**Output model**:
```python
class CreateResult(BaseModel):
    model: dict[str, Any]            # FindingModelBase as dict (no IDs yet)
    sub_findings: list[str]          # potential separate finding models
    naming_decisions: list[str]      # acronyms expanded, eponyms replaced, etc.
```

**Agent definition**:
```python
from pydantic_ai.models.openai import OpenAIChatModelSettings

create_agent = Agent(
    model=MODEL,
    output_type=CreateResult,
    instructions=Path("prompts/create_agent.md").read_text(),
    model_settings=OpenAIChatModelSettings(openai_reasoning_effort='medium'),
    retries=3,
)
```

**Prompt**: See `prompts/create_agent.md`

**Verification**: `python -c "from agents.create_agent import create_agent, CreateResult; print('OK')"`

---

### Chunk 3: Create `agents/review_agent.py`

**Depends on**: Nothing (new file)

**File**: `agents/review_agent.py`

**What to build**:
- `ReviewResult` pydantic model (structured output)
- Module-level `review_agent = Agent(...)` singleton
- No tools (pure text-in, structured-out)
- Instructions loaded from `prompts/review_agent.md`

**Output model**:
```python
class ReviewResult(BaseModel):
    reviewed_model: dict[str, Any]   # The model dict after review corrections
    changes_made: list[str]          # What was changed and why
    quality_warnings: list[str]      # Issues that couldn't be auto-fixed
    sub_findings: list[str]          # Additional sub-finding candidates found during review
```

**Agent definition** (no model_settings needed — `none` is GPT-5.2 default):
```python
review_agent = Agent(
    model=MODEL,
    output_type=ReviewResult,
    instructions=Path("prompts/review_agent.md").read_text(),
    retries=3,
    # reasoning_effort defaults to 'none' for gpt-5.2 — checklist-based review doesn't need reasoning
)
```

**Prompt**: See `prompts/review_agent.md`

**Verification**: `python -c "from agents.review_agent import review_agent, ReviewResult; print('OK')"`

---

### Chunk 4: Create `findingmodels/pipeline.py` — the orchestrator

**Depends on**: Chunks 1, 2, 3

**File**: `findingmodels/pipeline.py`

**What to build**:

#### 4a. Data models

```python
@dataclass
class FindingInput:
    """Parsed input from a definition file."""
    name: str
    description: str
    synonyms: list[str] | None
    content: str          # raw content (JSON string or markdown text)
    file_type: str        # "json" or "md"
    filename: str

class ProcessingResult(BaseModel):
    """Complete result from processing one finding."""
    final_model: dict[str, Any]
    match_used: str | None           # oifm_id if merged, None if created new
    merge_summary: str
    sub_findings: list[str]
    changes_made: list[str]
    quality_warnings: list[str]
```

#### 4b. Helper: `parse_input(file_path) -> FindingInput`

Uses existing `load_definition()` from `findingmodels.hood.loaders`.

For JSON files:
- If file has `finding_name` key (Hood JSON from CDEStaging): use that as name
- If file has `name` key (already a FindingModel): use that
- Call `create_info_from_name()` to get description + synonyms

For MD files:
- Extract name from filename (stem, replace `-`/`_` with space)
- Call `create_info_from_name()` to get description + synonyms

```python
async def parse_input(file_path: Path) -> FindingInput:
    data, markdown_content, file_type = await load_definition(file_path)

    if file_type == "json":
        raw_name = data.get("finding_name") or data.get("name", "")
        content = json.dumps(data, indent=2, ensure_ascii=False)
    else:
        raw_name = file_path.stem.replace("-", " ").replace("_", " ")
        content = markdown_content or ""

    info = await create_info_from_name(raw_name)

    return FindingInput(
        name=info.name,
        description=info.description,
        synonyms=info.synonyms,
        content=content,
        file_type=file_type,
        filename=file_path.name,
    )
```

#### 4c. Prompt formatters

```python
def format_merge_prompt(finding: FindingInput, similar_models: list[dict]) -> str:
    """Format user message for merge agent."""
    # Includes: finding info, raw content, list of similar model summaries

def format_create_prompt(finding: FindingInput) -> str:
    """Format user message for create agent."""
    # Includes: finding info (name, description, synonyms), raw content, file type

def format_review_prompt(model_dict: dict, locations: list[dict] | None) -> str:
    """Format user message for review agent."""
    # Includes: model JSON, anatomic locations for reference
```

#### 4d. Post-processing: `finalize_model()`

Deterministic Python — no LLM calls:

```python
def finalize_model(
    model_dict: dict[str, Any],
    locations: list[dict] | None,
    source: str = "MGB",
) -> FindingModelFull:
    """Add IDs, standard codes, locations, normalize, validate."""
    # 1. Set anatomic_locations from locations
    model_dict["anatomic_locations"] = locations

    # 2. Set contributors (MGB)
    if not model_dict.get("contributors"):
        model_dict["contributors"] = [
            {"name": "Massachusetts General Brigham", "code": "MGB"}
        ]

    # 3. Normalize (fix MGB format, validate locations shape)
    model_dict = normalize_for_validation(model_dict)

    # 4. If model has oifm_id already (merge case), validate as FindingModelFull directly
    #    If no oifm_id (create case), add IDs first
    if "oifm_id" not in model_dict or not model_dict.get("oifm_id"):
        base = FindingModelBase.model_validate(model_dict)
        full = add_ids_to_model(base, source=source)
    else:
        full = FindingModelFull.model_validate(model_dict)

    # 5. Add standard codes
    add_standard_codes_to_model(full)

    return full
```

#### 4e. Main function: `process_finding()`

```python
async def process_finding(
    file_path: Path,
    index: Index,
    output_dir: Path,
) -> ProcessingResult:
    with logfire.span("process_finding", file=file_path.name):
        # 1. Parse
        with logfire.span("parse_input"):
            finding = await parse_input(file_path)

        # 2. Parallel: similar models + anatomic locations
        with logfire.span("search_parallel"):
            similar, location_result = await asyncio.gather(
                find_similar_models(
                    finding.name, finding.description,
                    finding.synonyms, index=index,
                ),
                find_anatomic_locations(finding.name, finding.description),
            )

        # Convert locations to IndexCode dicts
        locations = []
        for loc in [location_result.primary_location] + location_result.alternate_locations:
            if loc.concept_id != "NO_RESULTS":
                locations.append(loc.as_index_code().model_dump())
        locations = locations or None

        # 3. Branch: merge or create
        with logfire.span("agent_run", branch=similar.recommendation):
            if similar.recommendation == "edit_existing" and similar.confidence >= 0.7:
                result = await merge_agent.run(
                    format_merge_prompt(finding, similar.similar_models),
                    deps=MergeContext(index=index),
                )
                model_dict = result.output.merged_model
                match_used = result.output.target_oifm_id
                sub_findings = result.output.sub_findings
                changes = result.output.changes_made
            else:
                result = await create_agent.run(
                    format_create_prompt(finding),
                )
                model_dict = result.output.model
                match_used = None
                sub_findings = result.output.sub_findings
                changes = result.output.naming_decisions

        # 4. Review
        with logfire.span("review"):
            review = await review_agent.run(
                format_review_prompt(model_dict, locations),
            )
            model_dict = review.output.reviewed_model
            sub_findings.extend(review.output.sub_findings)
            changes.extend(review.output.changes_made)

        # 5. Post-process (deterministic)
        with logfire.span("finalize"):
            final = finalize_model(model_dict, locations, source="MGB")

        # 6. Save
        output_file = output_dir / model_file_name(final.name)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(
            final.model_dump_json(indent=2, exclude_none=True),
            encoding="utf-8",
        )

        return ProcessingResult(
            final_model=final.model_dump(exclude_none=True),
            match_used=match_used,
            merge_summary="; ".join(changes),
            sub_findings=sub_findings,
            changes_made=changes,
            quality_warnings=review.output.quality_warnings,
        )
```

**Imports needed**:
```python
import asyncio
import json
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import logfire
from findingmodel import FindingModelBase, FindingModelFull, Index
from findingmodel.common import model_file_name
from findingmodel.tools import add_ids_to_model, add_standard_codes_to_model
from findingmodel_ai.authoring import create_info_from_name
from findingmodel_ai.search import find_similar_models, find_anatomic_locations
from pydantic import BaseModel

from agents.merge_agent import merge_agent, MergeContext
from agents.create_agent import create_agent
from agents.review_agent import review_agent
from findingmodels.hood import load_definition
from findingmodels.hood.normalize_output import normalize_for_validation

import findingmodels.compat  # noqa: F401 - patch for findingmodel-ai
```

**Verification**: Not independently runnable yet — needs the script update (Chunk 5).

---

### Chunk 5: Update `scripts/hood_to_final_finding.py`

**Depends on**: Chunk 4

**File**: `scripts/hood_to_final_finding.py` (modify in place)

**Changes**:
1. Replace `from agents.hood_agent import create_hood_agent, AgentContext` with `from findingmodels.pipeline import process_finding, ProcessingResult`
2. Remove `_hood_agent` global and `_get_agent()` function
3. Rewrite `process_single_file()` to call `pipeline.process_finding()` and adapt the return tuple
4. Keep `generate_attribute_report()` and `generate_sub_finding_report()` as-is (they consume tracking dicts)
5. Adapt tracking dict construction in `process_hood_directory()` to match new `ProcessingResult` fields

**New `process_single_file()`**:
```python
async def process_single_file(
    file_path: Path,
    index: Index,
    output_dir: Path,
) -> Tuple[bool, str, Optional[Dict], Optional[Dict], Optional[Dict], Optional[List[str]]]:
    try:
        result = await process_finding(file_path, index, output_dir)

        finding_name = result.final_model.get("name", "unknown")

        tracking_info = {
            "finding_name": finding_name,
            "presence": {"finding_name": finding_name},
            "change_from_prior": {"finding_name": finding_name},
        }
        sub_finding_tracking_info = {"finding_name": finding_name}
        merge_tracking_info = {
            "finding_name": finding_name,
            "match_found": result.match_used is not None,
            "result": "merged" if result.match_used else "created_new",
            "existing_match": {"oifm_id": result.match_used} if result.match_used else None,
            "merge_details": result.merge_summary,
        }

        return True, f"Successfully processed {file_path.name}", tracking_info, sub_finding_tracking_info, merge_tracking_info, []
    except Exception as e:
        logger.error(f"Error processing {file_path.name}: {e}")
        import traceback
        traceback.print_exc()
        return False, f"Error processing {file_path.name}: {e}", None, None, None, None
```

**Verification**: `uv run python scripts/hood_to_final_finding.py --limit 1` should process one file end-to-end.

---

### Chunk 6: Delete `agents/hood_agent.py`

**Depends on**: Chunk 5 verified working

**File**: Delete `agents/hood_agent.py`

**Verification**: `uv run python scripts/hood_to_final_finding.py --limit 1` still works after deletion.

---

## Library Functions Reused vs Custom

| Function | Source | Import Path | Notes |
|---|---|---|---|
| `find_similar_models()` | **library** | `findingmodel_ai.search.find_similar_models` | Returns `SimilarModelAnalysis` with `.recommendation`, `.confidence`, `.similar_models` |
| `find_anatomic_locations()` | **library** | `findingmodel_ai.search.find_anatomic_locations` | Returns `LocationSearchResponse` with `.primary_location`, `.alternate_locations` |
| `create_info_from_name()` | **library** | `findingmodel_ai.authoring.create_info_from_name` | Returns `FindingInfo` with `.name`, `.description`, `.synonyms` |
| `add_ids_to_model()` | **library** | `findingmodel.tools.add_ids_to_model` | `(FindingModelBase, source) -> FindingModelFull` |
| `add_standard_codes_to_model()` | **library** | `findingmodel.tools.add_standard_codes_to_model` | `(FindingModelFull) -> None` (mutates in place) |
| `load_definition()` | **local** | `findingmodels.hood.loaders.load_definition` | `(Path) -> (dict|None, str|None, str)` |
| `should_process_file()` | **local** | `findingmodels.hood.loaders.should_process_file` | Filters .cde.json, handles MD/JSON priority |
| `normalize_for_validation()` | **local** | `findingmodels.hood.normalize_output` | Fixes anatomic_locations shape, MGB contributor format |
| `model_file_name()` | **library** | `findingmodel.common.model_file_name` | Generates `*.fm.json` filename from model name |
| `compat` patch | **local** | `findingmodels.compat` | Must be imported before findingmodel_ai usage |

## Key Library Type Signatures

```python
# find_similar_models
async def find_similar_models(
    finding_name: str,
    description: str | None = None,
    synonyms: list[str] | None = None,
    index: Index | None = None,
) -> SimilarModelAnalysis

class SimilarModelAnalysis(BaseModel):
    similar_models: list[SearchResult]  # max 3
    recommendation: Literal["edit_existing", "create_new"]
    confidence: float  # 0.0 to 1.0

class SearchResult(TypedDict):
    oifm_id: str
    name: str
    description: NotRequired[str]
    synonyms: NotRequired[list[str]]

# find_anatomic_locations
async def find_anatomic_locations(
    finding_name: str,
    description: str | None = None,
) -> LocationSearchResponse

class LocationSearchResponse(BaseModel):
    primary_location: OntologySearchResult
    alternate_locations: list[OntologySearchResult]  # max 3
    reasoning: str

class OntologySearchResult(BaseModel):
    concept_id: str
    concept_text: str
    score: float
    table_name: str
    # has method: as_index_code() -> IndexCode

# create_info_from_name
async def create_info_from_name(finding_name: str) -> FindingInfo

class FindingInfo(BaseModel):
    name: str
    synonyms: list[str] | None
    description: str
    detail: str | None
    citations: list[str] | None
```

## Model & Reasoning Effort Summary

| Agent | Model | Reasoning Effort | Rationale |
|---|---|---|---|
| Merge Agent | gpt-5.2 | **high** | Multi-step attribute comparison, relationship classification, specificity judgment, deduplication logic |
| Create Agent | gpt-5.2 | **medium** | Structured transformation with clinical judgment for descriptions, naming, sub-finding detection |
| Review Agent | gpt-5.2 | **none** (default) | Checklist-based verification — lowercase check, standard values check, pattern matching |
| Library: `find_similar_models` | Controlled by library | `search_model_tier="small"`, `analysis_model_tier="base"` | Library defaults |
| Library: `find_anatomic_locations` | Controlled by library | `model_tier="small"` | Library defaults |
| Library: `create_info_from_name` | Controlled by library | `model_tier="small"` | Library defaults |

GPT-5.2 defaults to reasoning effort `none`. We must explicitly set `high` for merge and `medium` for create via `OpenAIChatModelSettings(openai_reasoning_effort=...)`.

## Pydantic-AI Best Practices Applied

| Anti-pattern in old code | Fix in new code |
|---|---|
| `system_prompt=SYSTEM_PROMPT` | `instructions=Path("prompts/X.md").read_text()` |
| `tools=[fn1, fn2, ...]` list | `@agent.tool` decorator |
| Tools return `json.dumps(...)` strings | Tools return `dict` / structured data |
| Blanket `try/except → json.dumps({"error": ...})` | `raise ModelRetry(...)` for recoverable errors |
| Factory function `create_hood_agent()` | Module-level `agent = Agent(...)` singleton |
| One 50-line prompt for everything | ~20-line focused prompt per agent |

## Verification Plan

1. **Smoke test**: `uv run python scripts/hood_to_final_finding.py --limit 1`
2. **Compare output**: Diff `defs/single_agent_output/aberrant_subclavian_artery.fm.json` before/after — should have same structure (oifm_id, name, attributes with presence+change_from_prior first, anatomic_locations, contributors)
3. **Logfire traces**: Verify spans: `process_finding` > `parse_input`, `search_parallel`, `agent_run`, `review`, `finalize`
4. **Validate output**: `uv run python scripts/validator.py defs/single_agent_output/`
5. **Batch test**: `uv run python scripts/hood_to_final_finding.py --limit 5` — check processing report
6. **Sub-findings**: Verify sub_findings lists in ProcessingResult are populated where appropriate
