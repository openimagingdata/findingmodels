# Optional enrichment

After a finding model has been created and passed mechanical + quality review, the user may want a richer description with citations. This step is **optional** and applies only to the single-finding authoring flow — batch flows skip it.

## make-info

```bash
uv run --env-file .env --with findingmodel-ai findingmodel-ai make-info "<finding name>" --detailed
```

This calls an AI-backed tool that drafts a more detailed description with citations. It does not touch the `.fm.json` file — it prints a draft to stdout for you to review.

Use it when:

- The user asks for a richer description
- The existing description is a one-line placeholder and you want a clinically-grounded starting point
- You want citation candidates the user can review and keep

Do not use it for:

- Every finding in a batch (too slow, and your own radiology-aware drafting is usually sufficient)
- Findings whose existing description is already good

## Applying the enriched content

Use `fix_stub.py` to write the enriched description (and optionally a revised synonym list) back into the model file:

```bash
uv run --env-file .env scripts/finding_authoring/fix_stub.py \
    defs/<filename>.fm.json \
    --description "<enriched description>" \
    --synonyms "existing1" "existing2" "new_synonym"
```

Flags:

- `--description` — replaces the description field.
- `--synonyms` — replaces the synonyms list. Pass the full intended list, not just additions.
- `--name` — renames the finding (rare; re-check the file path afterward).
- `--contributor <person> <org>` — ensure contributors are recorded.

## Review afterward

Any edit via `fix_stub.py` is still subject to the normal review flow — re-run `review_model.py` on the file after enrichment, and re-run the quality-review sub-agent if the description or synonyms changed substantively.

## Don't

- Don't use `findingmodel-ai make-stub-model`. It performs AI-based name normalization that can rename the finding unexpectedly. `create_model.py` (see `create_invocation.md`) is the correct creation path.
- Don't chain `make-info` into `fix_stub.py` blindly. Read the draft, confirm it's accurate, then apply.
