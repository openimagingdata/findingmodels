# Search and triage

Before creating, editing synonyms, or reviewing, check whether a finding already exists in the library. The goal is to answer "does this exist?" *yourself* using multiple searches and strict semantic judgment — and only involve the user when there's genuine ambiguity.

## Generate 2-3 search targets

One search is not enough. The index uses hybrid full-text + semantic matching, but any single query can miss matches that use different terminology. For each incoming finding, form **2-3 complementary search targets** and run each one:

- **The canonical term you'd use** — e.g., `subdural hematoma`
- **A common alternate phrasing or synonym** — e.g., `subdural hemorrhage`
- **The key anatomic or descriptive term alone**, if the canonical term is compound — e.g., `hematoma` or `subdural collection`

Pick targets that cover the ways a radiologist might have named this finding when it was originally created. Acronym expansions, eponym-vs-descriptive pairs, and anatomic-vs-pathologic phrasings are good axes to vary on.

## Run the searches

```bash
uv run --env-file .env --with findingmodel --with openai findingmodel search "<target>" --limit 5
```

For bulk triage in a batch flow, use `--limit 1` or `--limit 2` per target to keep output compact. For single-finding authoring, `--limit 5` on each of 2-3 targets is fine.

## Evaluate — don't just forward the results to the user

Pool the results across your 2-3 queries. For each distinct candidate, make your own semantic judgment:

- **Exact match**: the candidate refers to the *same* finding at the *same* level of specificity as the incoming term. Same clinical entity, same scope, same level of abstraction. If you have an exact match, **use it** — don't ask the user to re-confirm what you already know.
- **Not a match**: the candidate is a different finding, a subtype, a supertype, a sign rather than a disease, or at a different level of specificity. Silently discard.
- **True maybe**: the candidate might be the same finding but you genuinely cannot tell — missing context, ambiguous naming, overlapping but not identical scope. These are the only ones to escalate to the user.

See the specificity traps below — most search hits look superficially related but fail an exact-match test.

## Specificity traps (these are NOT exact matches)

- **Too general** — existing `detectable hardware` vs incoming `tunneled catheter`: parent concept, not same finding.
- **Too specific** — existing `bullous emphysema` vs incoming `emphysema`: subtype, not same finding.
- **Different scope** — existing `aortic calcification` vs incoming `coronary artery calcification`: shares words, different findings.
- **Sign vs disease** — existing `Kerley B lines` vs incoming `interstitial pulmonary edema`: a sign points to a disease; they are not equivalent.
- **Consequence vs cause** — existing `aspiration pneumonia` vs incoming `aspiration`.
- **Different pathophysiology** — existing `right ventricular hypertrophy` vs incoming `right ventricular enlargement`: wall thickening vs chamber dilation.

See `synonym_rules.md` for the full list.

## What to tell the user

- **Exact match found** — state the outcome: "This already exists as `<name>` (`<OIFM ID>`). Would you like to add a synonym or view it?" No triage question.
- **Only non-matches found** — state the outcome: "Searched `<target1>`, `<target2>`, `<target3>` — no existing model for this finding. Shall I create one?" No candidate list dumped on the user unless they ask.
- **True maybe(s)** — surface only the ambiguous candidates with your reasoning: "`<candidate>` is close but appears to be a subtype of your finding — same observation or should we create a new model?" Keep the list short; don't pad with obvious non-matches.

## Determining the file path for an existing model

```bash
uv run --env-file .env --with findingmodel --with openai python -c "from findingmodel.common import model_file_name; print(model_file_name('<finding name>'))"
```

The function returns the snake-cased stem; the file is at `defs/<stem>.fm.json`. Confirm with `ls defs/<stem>.fm.json` before editing.
