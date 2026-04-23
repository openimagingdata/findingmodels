# Findingmodel / findingmodel-ai — candidate upstream issues

Analysis of what should move upstream into `openimagingdata/findingmodel` based on patterns we've built into `findingmodels-headcts`. Each entry is sized to become one GitHub issue.

**Already filed:** [#42 — `add_ids_to_model` silently regenerates existing oifm_id when model is round-tripped through FindingModelBase](https://github.com/openimagingdata/findingmodel/issues/42).

**Evidence base:** 14-model head-CT test batch + 1 existing-model review pass + 3 session-long fragment refinements exercised every capability below.

---

## Section A — Bugs

### A1. `findingmodel-ai` → `findingmodel` runtime version mismatch (ImportError on DuckDBIndex)

**Priority:** high (blocks `findingmodel-ai` enrichment flows under plain `uv run --with`).

**Problem:** When `findingmodel-ai` is installed alongside `findingmodel` via `uv run --with findingmodel-ai --with findingmodel`, the combined environment fails with:

```
from findingmodel.index import DuckDBIndex
ImportError: cannot import name 'DuckDBIndex' from 'findingmodel.index'
```

Downstream scripts that try to call `findingmodel-ai make-info` break immediately. We hit this when exercising our `enrichment.md` fragment's invocation form, and reproduced independently against the published pair `findingmodel-ai 0.2.1` + `findingmodel 1.0.4`. The current local `findingmodel-ai` source already imports `FindingModelIndex` instead of `DuckDBIndex`, so this is a release-contract / version-pinning problem, not a design problem.

**Proposed fix:** align the `findingmodel-ai` package's minimum-version constraint on `findingmodel` so both halves of the workspace publish their compatible pair together. Add a test that imports the full `findingmodel-ai` CLI's dependency graph inside a clean venv pinning the latest `findingmodel` from PyPI.

**Out of scope for this issue:** the API rename itself (which presumably happened for a reason); just the workspace version contract.

---

## Section B — Library API enhancements (findingmodel)

### B1. `create_model_stub_from_info` should accept `cfp_pairs` and drop the leading article

**Priority:** high (fixes a review-overhead pattern that hit 12 of 14 models in our test batch).

**Problem:** `create_model_stub_from_info(finding_info, tags=...)` currently emits all 8 `change from prior` values (`unchanged/stable/new/resolved/increased/decreased/larger/smaller`) unconditionally, and generates the attribute description as `"Whether and how a <name> has changed over time"` — which reads awkwardly for mass nouns and for multi-word names starting with a vowel.

Every finding we created had its direction pairs winnowed by the review step (12/14), and every one had the article flagged as poor grammar. This is backwards: generate minimum, opt in to direction pairs explicitly.

**Proposed API change (minimal-impact):**

```python
def create_model_stub_from_info(
    finding_info: FindingInfo,
    tags: list[str] | None = None,
    cfp_pairs: list[str] | None = None,   # NEW
    cfp_description_article: bool = False,  # NEW; default False drops the "a "
) -> FindingModelBase:
    ...
```

`cfp_pairs` accepts the canonical pair names (`larger-smaller`, `increased-decreased`, `worsened-improved`). Default is empty → minimum set only. `worsened-improved` is new territory (upstream currently doesn't generate those values at all); the library builds the value entries with `None` index_codes to match the existing `resolved` pattern.

**Proposed CLI** (in `findingmodel-ai make-stub-model` — already exists, add flag):

```
findingmodel-ai make-stub-model "pneumothorax" --cfp-pairs larger-smaller,worsened-improved
```

**Evidence:** our `scripts/finding_authoring/create_model.py` now does this client-side via post-processing. Code at `scripts/finding_authoring/create_model.py` in this repo is the reference implementation.

### B2. Public `rename_model` helper in `findingmodel.tools`

**Priority:** medium.

**Problem:** Renaming an existing model requires (a) updating `name`, (b) updating every attribute/value `description` string that embeds the finding name in capitalized form, (c) renaming the file on disk via `model_file_name()`, all while preserving `oifm_id`, every `oifma_id`, and every `value_code`. There's no library helper, and the obvious naive approach (round-trip through `FindingModelBase`) hits the ID-stripping bug in #42.

**Proposed API:**

```python
from findingmodel.tools import rename_model

new_path, old_path = rename_model(
    path: Path,
    new_name: str,
    keep_filename: bool = False,
) -> tuple[Path, Path]:
    """Rename a finding model. Preserves oifm_id, oifma_ids, value_codes.
    Rewrites embedded finding-name references in descriptions. Moves the
    file on disk unless keep_filename=True."""
```

**Proposed CLI:**

```
findingmodel rename defs/parenchymal_hypoattenuation.fm.json --new-name "brain parenchymal hypoattenuation"
```

**Evidence:** `scripts/finding_authoring/rename_model.py` in this repo. We hit this need during the head-CT review pass.

### B3. Public `add_change_from_prior` and `modify_change_from_prior` helpers

**Priority:** medium.

**Problem:** Two distinct gaps:

- Some existing models in the corpus have only a `presence` attribute (missing `change from prior` entirely). Adding it requires hand-allocating exactly one new `oifma_id` and building value entries with the right `value_code` pattern. Naive approaches hit #42.
- After `create_model_stub_from_info` runs, reviewers often add or remove direction pairs. There's no safe helper — hand-edits break IDs or drop `index_codes` inconsistently.

**Proposed API (two functions):**

```python
from findingmodel.tools import add_change_from_prior_attribute, modify_change_from_prior

# For models missing the attribute entirely:
model = add_change_from_prior_attribute(
    model: FindingModelFull,
    pairs: list[str] | None = None,
) -> FindingModelFull  # returns new model with oifma_id allocated

# For models where the attribute exists but values need tweaking:
model = modify_change_from_prior(
    model: FindingModelFull,
    add_values: list[str] | None = None,
    remove_values: list[str] | None = None,
) -> FindingModelFull
```

Core values (`unchanged/stable/new/resolved`) are protected from removal.

**Proposed CLIs:**

```
findingmodel add-change-from-prior <file> --pairs larger-smaller,worsened-improved
findingmodel modify-change-from-prior <file> --add worsened,improved --remove larger,smaller
```

**Evidence:** `scripts/finding_authoring/add_change_from_prior.py` and `scripts/finding_authoring/modify_change_from_prior.py` in this repo.

### B4. Standard direction-of-change value constants in `findingmodel.tools`

**Priority:** medium (supports B1–B3 cleanly; otherwise duplicated across all three helpers).

**Problem:** Three downstream scripts (`create_model.py`, `add_change_from_prior.py`, `modify_change_from_prior.py`) each carry their own copy of:

- The standard direction-value name → (RADLEX, SNOMED) code tuples
- The standard pair keys (`larger-smaller`, `increased-decreased`, `worsened-improved`)
- The canonical value-description text template (`"{Finding_cap} is larger"`, `"{Finding_cap} has worsened"`)
- The value_code construction pattern (`{oifma_id}.{N}`)

`findingmodel.tools.index_codes.STANDARD_CODES` already has most of the codes — extending it to cover `worsened`/`improved` and exposing a small builder API would let downstream helpers (and the three proposed library functions above) all share one source of truth.

**Proposed additions:**

- Extend `STANDARD_CODES` to include explicit entries for `worsened` and `improved` (even if `None` for RADLEX/SNOMED — matches the existing `resolved` pattern).
- New public constants: `findingmodel.tools.CFP_CORE_VALUES`, `findingmodel.tools.CFP_VALID_PAIRS`, `findingmodel.tools.CFP_ALL_DIRECTIONS`.
- New public helper: `findingmodel.tools.build_cfp_value_entry(name, value_code, finding_cap) -> dict`.

**Evidence:** three downstream helpers with duplicated tables. Refactoring them was consciously deferred per session discussion — cleaner to factor upstream.

### B5. Project-local contributor loading helpers

**Priority:** low-medium (nice-to-have; works around but doesn't require).

**Problem:** `findingmodel.contributor` already exports `Person` and `Organization` with their own load/save helpers — no new registry model is needed. What's missing is a documented path from a project-local YAML file to hydrated `Person`/`Organization` instances. Consequence: every consumer repo hand-codes a `CONTRIBUTORS` dict to bridge the gap. Ours lives in two places (`scripts/finding_authoring/create_model.py` and `fix_stub.py`) plus a third copy in `prompts/defaults.yml` — drift risk we've already flagged.

**Proposed API (thin loader on top of existing registry types):**

```python
# Hydrate Person and Organization instances from a project-local YAML.
# Default path: ./contributors.yml (project root).
from findingmodel.contributor import load_contributors_from_yaml

people, orgs = load_contributors_from_yaml(path: Path | None = None)
# people: dict[str, Person]    keyed by github_username or other stable key
# orgs:   dict[str, Organization]   keyed by code (OIDM, MGB, …)
```

Ship a starter `contributors.yml` alongside the library with the public contributors already documented in `Person`/`Organization` defaults (OIDM, GMTS, CDE, MSFT, RSNA, MGB).

**Proposed CLI (optional):** `findingmodel contributors list` / `findingmodel contributors validate` — just inspect/validate the YAML against the existing models. No new registry type.

**Evidence:** `prompts/defaults.yml` + duplicated dicts in `create_model.py` + `fix_stub.py`. Every consumer that emits models rebuilds the same bridge.

---

## Section C — New CLI subcommands on `findingmodel`

### C1. Hoist library-seam authoring subcommands into the `findingmodel` CLI

**Priority:** high (the core-library subset of the original umbrella — the ones that wrap true primitives the library should own).

**Problem:** Consumer repos rebuild CLI wrappers around mechanical operations that belong in the core library. Each of these subcommands is a thin wrapper over a library primitive proposed in Section B; shipping them together turns `findingmodel` into a usable authoring CLI without LLM involvement.

**Proposed subcommands** (one umbrella issue; each bullet is a candidate subcommand):

- `findingmodel create <name> --description ... --cfp-pairs ... [--source ...] [--output ...] [--with-ids] [--with-codes]` — mechanical stub creation (current downstream `create_model.py`). `findingmodel-ai make-stub-model` already exists with LLM normalization; this would be the no-LLM counterpart. Wraps B1.
- `findingmodel rename <file> --new-name ...` — wraps B2.
- `findingmodel add-change-from-prior <file> --pairs ...` — wraps B3.
- `findingmodel modify-change-from-prior <file> --add ... --remove ...` — wraps B3.

**Evidence:** four downstream scripts in `scripts/finding_authoring/` (`create_model.py`, `rename_model.py`, `add_change_from_prior.py`, `modify_change_from_prior.py`) each wrap what should be a library primitive. Collectively ~400 lines; each consumer repo rebuilds them.

### C2. Consumer-workflow CLI adapters (deferred)

**Priority:** medium — revisit after C1 lands and we can see how much of the remaining surface is genuinely reusable across consumers vs. project-local.

**Problem:** A second group of downstream CLIs are workflow-tier adapters rather than library primitives. They are valuable to this consumer but may belong in a future `findingmodel.authoring` subpackage (see E4) rather than the core CLI.

**Candidate subcommands (filed only if need survives C1):**

- `findingmodel review <files>...` — mechanical lint: underscores, lowercase, standard-attribute structure, `associated findings` shape, contributor completeness, placeholder descriptions. Severity levels: ERROR (auto-fixable) / WARNING / REVIEW (LLM judgment). `--fix` flag. Current downstream `review_model.py`.
- `findingmodel fix-stub <file> [--name ...] [--description ...] [--synonyms ...] [--contributor ...]` — post-process an existing stub's editable fields. Current downstream `fix_stub.py`.
- `findingmodel update-csv <csv> --id-column N --oifm-column N --mapping-stdin` — write OIFM IDs back to a tracking CSV after batch creation. Current downstream `update_csv.py`.
- `findingmodel collision-check <term>` — prints where a term appears as name or synonym anywhere in the index (see also E2).

**Evidence:** same `scripts/finding_authoring/` folder; the remaining ~300 lines after C1's primitives are removed.

---

## Section D — findingmodel-ai enhancements

### D1. Prompt-template updates to match current convention thinking

**Priority:** high for correctness of AI-drafted models.

**Problem:** The four Jinja2 prompts in `findingmodel-ai/prompt_templates/` predate recent convention refinements (distilled in this repo's `prompts/fragments/*.md`). Specific divergences:

- **`get_finding_description.md.jinja`** — lacks the pre-emptive cross-body-region synonym collision check. Example traps the AI doesn't catch: `follicular cyst` (dental vs ovarian), `cavernous hemangioma` (orbit/liver vs CNS misnomer for cavernous malformation), `adenoma` (pituitary/adrenal/thyroid/colonic), `carcinoid`, `nodule`. Our `prompts/fragments/synonym_rules.md` has the explicit rule.

- **`get_finding_description.md.jinja`** — silent on the scope-anchor specificity rule. The AI will produce names like `parenchymal hypoattenuation` where `parenchymal` is ambiguous (lung/liver/renal/brain). Our `naming.md` requires anatomy-specific anchors (`brain parenchymal`, `pulmonary parenchymal`).

- **`get_finding_description.md.jinja`** — silent on the "unscoped short form as synonym" caveat. Current behavior likely keeps `hypoattenuation` as a synonym on `brain parenchymal hypoattenuation` — wrong; generic imaging descriptors (`hypoattenuation`, `hypodensity`, `enhancement`, `calcification`, `lucency`) that apply across body regions fail the same-specificity test. Our `naming.md` documents this.

- **`get_finding_model_from_outline.md.jinja`** — doesn't enforce `presence` + `change from prior` as mandatory first two attributes. Treats them as optional.

- **`get_finding_detail.md.jinja`** — conflates "associated findings" with component structures. Our `associated_vs_component.md` has a strict independence test: co-occurring-but-independent → single multichoice presence-level attribute; intrinsic-to-the-finding → extract to its own model.

- **None of the prompts** reflect the direction-pair rules: which pairs fit a given finding, when to exclude all pairs (congenital variants, fractures, devices, postsurgical states), when to allow pairs on a congenital variant because severity is post-traumatically or post-surgically variable (e.g., nasal septal deviation).

**Proposed fix:** a single refactor PR that aligns the four prompt templates with the current conventions. Consider centralizing the convention rules into a shared Jinja partial or a Python constants module so future edits touch one place. Downstream `prompts/fragments/*.md` in this repo can serve as the reference.

**Evidence:** 14-model test batch had consistent quality-review flags on all of the above points when AI-drafted; the fixes were manual winnowing/renaming post-hoc.

### D2. `findingmodel-ai make-stub-model --no-normalize`

**Priority:** medium.

**Problem:** `make-stub-model` runs the input finding name through an AI normalization step. It sometimes silently renames the finding in unexpected ways — a real failure mode that we explicitly worked around by building a non-AI `create_model.py` downstream.

**Proposed fix:** add `--no-normalize` flag that passes the name straight through. (This overlaps with C1's `findingmodel create` — either both paths work, or `findingmodel create` fully replaces the non-AI case.)

**Evidence:** the existence of our `create_model.py` exists because of this issue. Our fragment `enrichment.md` explicitly tells users not to use `make-stub-model`.

### D3. Drafting helper for batch workflows: `draft_finding_from_row` / `findingmodel-ai draft`

**Status:** deferred — validate need first. Before filing, try replacing the handwritten drafting loop in `finding-batch` with calls to `find_similar_models` + `findingmodel-ai make-stub-model --no-normalize` (per D2). If the combination covers the batch-drafting use case, D3 does not need to be filed; if a concrete gap remains, the residual gap is what to file.

**Priority:** medium (once validated).

**Problem:** Our `finding-batch` skill fans out one sub-agent per incoming row, each drafting `{name, description, synonyms}` from (a) a source data row (CSV-like), (b) convention rules, (c) optional category/context hints. This pattern is reimplemented every time a consumer writes a batch workflow. Lifting it into `findingmodel-ai` as a first-class function (and CLI) would let any harness call it:

**Proposed API:**

```python
from findingmodel_ai.authoring import draft_finding_from_context

info = await draft_finding_from_context(
    raw_name: str,
    source_synonyms: list[str] | None = None,
    category: str | None = None,
    finding_type: Literal["observation", "diagnosis"] | None = None,
    modality_context: str | None = None,  # "head CT", "chest radiograph", etc.
) -> FindingInfo
```

Returns a `FindingInfo` — name applies `naming.md` rules (scope-anchor, acronym expansion, brand removal), synonyms apply `synonym_rules.md` strictness incl. cross-body-region check.

**Proposed CLI:**

```
findingmodel-ai draft --raw-name "hypoxic_ischemic_encephalopathy" --finding-type diagnosis --context "head CT" [--source-synonyms HIE,anoxic brain injury]
```

Stdin mode for batch: JSONL of rows in, JSONL of FindingInfo out.

**Evidence:** `finding-batch/SKILL.md` step 3 (the drafting fan-out) in this repo. Every consumer writing a batch workflow will rebuild this.

### D4. Expose the "find similar models" agent as a higher-level triage primitive

**Priority:** low-medium.

**Problem:** `findingmodel_ai.search.find_similar_models` does exactly what our batch-triage step needs (semantic-agent search for existing models matching an incoming finding), but our fragment `search_and_triage.md` tells the consumer to run 2–3 targeted `findingmodel search` calls and evaluate results themselves. This is a case where we're under-using the existing library because the downstream prompt flow isn't aware of the agent.

**Proposed fix:** document `find_similar_models` prominently in the `findingmodel-ai` README with a short usage example matching the batch-triage pattern (one call per incoming finding, limit N candidates, output a `match/close/no-match` classification). No API change needed — just expose it as the recommended entry point and optionally provide a thin CLI wrapper `findingmodel-ai triage <name>`.

---

## Section E — Workflow / harness primitives

### E1. `findingmodel triage` — batched search+classify

**Status:** deferred — validate need first. Before filing, try replacing `finding-batch`'s handwritten triage loop with `find_similar_models` (documented in `findingmodel-ai/README.md` already). If per-row `find_similar_models` calls produce acceptable match/close/no-match classifications, E1 does not need to be filed; file only the residual gap (e.g., a lightweight CLI wrapper per D4) rather than a new `triage_batch` primitive.

**Priority:** medium (once validated).

**Problem:** For a batch of N incoming findings, the downstream workflow issues N × 2–3 search queries, evaluates each candidate for exact-match semantics, and produces a classification table. This is reimplemented in every batch harness. The raw capability exists (`Index.search_batch` for low-level; `find_similar_models` for agent-level); missing is the thin tying-together.

**Proposed CLI:**

```
findingmodel triage --input incoming.csv --name-column 1 [--synonyms-column 4] [--limit 3] --output triage.json
```

Output: per-row classification `{row_id, incoming_name, outcome: "match"|"maybe"|"no_match", candidates: [...], reasoning}`.

**Proposed API (if useful):**

```python
from findingmodel import triage_batch
results = await triage_batch(rows, index=idx)  # list of TriageResult
```

**Evidence:** `finding-batch/SKILL.md` step 2 + our handwritten Python loops over `Index.search_batch` during the 20-row CSV exercise.

### E2. `findingmodel collision-check <term>`

**Priority:** low.

**Problem:** Every synonym we add gets a manual collision check (`findingmodel search "<term>"` + mental classification of hits as self/noise/actual-collision). The pattern is consistent enough to be a named operation. Companion to the pre-emptive cross-body-region check in D1 — if the library ships with a static "ambiguous-terms" list (or scans the corpus for anatomic-region hints), this could flag both corpus collisions and pre-emptive ambiguity in one go.

**Proposed CLI:**

```
findingmodel collision-check "follicular cyst" [--for-model OIFM_OIDM_...]
```

Output: lists each model that has this term as name or synonym; flags cross-body-region warnings from the ambiguity list.

**Evidence:** we ran `findingmodel search` for collision-check 20+ times during the head-CT batch; every single add-synonym call pairs with a search.

### E3. Consumer repo quickstart doc

**Priority:** medium.

**Problem:** Our skill suite (three skills + 15 fragments + ~700 lines of authoring scripts) is effectively a reference implementation of "how to build an authoring workflow on top of findingmodel". No such reference exists in the findingmodel repo. A consumer doc — "setting up a project that authors finding models" — would let new users get to a working authoring pipeline much faster.

**Proposed content:**

1. Minimal consumer repo layout (where to put `defs/`, `text/`, a validator, a contributors file).
2. Common operations cookbook (create, rename, review, batch-import).
3. Pointer to downstream convention docs (our `prompts/fragments/` or whatever the maintainers settle on).
4. Starter templates: `contributors.yml`, pre-commit hook for validation, CI snippet.

**Evidence:** this repo is one data point; each new consumer repo (knee-MRI, chest-MRI, etc. the user mentioned) will rebuild similar scaffolding until there's a reference.

### E4. Optional: "authoring kit" subpackage (`findingmodel.authoring`)

**Priority:** low (speculative).

**Problem:** If the library accrues enough of the above CLI subcommands, they naturally cluster into an authoring-kit surface. Could be promoted to `findingmodel.authoring` as a dedicated subpackage holding create/review/rename/modify/fix-stub/update-csv + the shared helpers.

Defer; revisit after C1 lands and we see how the CLI evolves.

---

## Priority summary

| Priority | Issues |
|---|---|
| **High** | A1 (import bug), B1 (cfp_pairs in create_stub), C1 (library-seam CLI subcommands), D1 (prompt template updates) |
| **Medium** | B2 (rename_model), B3 (add/modify_cfp), B4 (shared constants), C2 (consumer-workflow CLI adapters), D2 (--no-normalize), E3 (consumer doc) |
| **Low** | B5 (contributor loader helpers), D4 (expose find_similar_models), E2 (collision-check CLI), E4 (authoring subpackage) |
| **Deferred — validate need first** | D3 (draft_from_row), E1 (triage) — try `find_similar_models` in the batch-triage flow before filing |

## Filing order recommendation

A1 leads because it is a runtime blocker on the current published pair, not a release-engineering footnote — until it is fixed, `findingmodel-ai` enrichment is broken for any plain `uv run --with` user. After that, the ordering is driven by **dependency**: library primitives before the CLI umbrella that wraps them.

**First wave (file together or in rapid succession):**

1. **A1** — runtime blocker for `findingmodel-ai` enrichment.
2. **B1 + B4** — `cfp_pairs` on `create_model_stub_from_info` + the shared CFP constants it depends on. Pair because B4 is the shared-constants substrate that keeps B1's implementation small.
3. **B2 + B3** — `rename_model` + `add_change_from_prior` / `modify_change_from_prior`. Pair because they're sibling helpers around the same attribute primitive; authoring flows want all three to land together.
4. **D1** — single PR updating all four prompt templates. Delivers AI-drafting quality jump.
5. **D2** — `make-stub-model --no-normalize` flag. Small follow-on to D1; unblocks non-AI name preservation in the AI CLI.
6. **E3 + D4** — docs/thin-wrapper items. Consumer quickstart doc + prominent `find_similar_models` documentation / optional thin CLI wrapper. No new primitives; mostly README.

**Second wave (after the first wave lands):**

7. **C1** — the library-seam CLI umbrella (`findingmodel create / rename / add-change-from-prior / modify-change-from-prior`). Deliberately after B1–B4 + D1 because C1 wraps what those ship; filing it earlier inverts the dependency.
8. **B5** — project-local contributor loader helpers.
9. **C2** — consumer-workflow CLI adapters (review / fix-stub / update-csv / collision-check). Revisit once C1 lands and we can see how much remains genuinely reusable across consumers.
10. **E2** — `collision-check` CLI, if not subsumed by C2.
11. **E4** — optional `findingmodel.authoring` subpackage, if C1/C2 warrant it.

**Deferred (validate need first):**

- **D3** and **E1** — before filing, try replacing the handwritten batch-triage and drafting loops in `finding-batch` with `find_similar_models` (per D4). If that covers the use case, neither needs to be filed; if it does not, the residual gap is what to file.
