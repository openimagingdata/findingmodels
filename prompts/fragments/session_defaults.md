# Session defaults

Every finding model is created with a **source code**, a set of **contributors**, and a set of **tags**. These values stay the same across most or all findings within a working session — once the user tells you which to use, reuse them for the rest of the conversation unless they override.

## Read the defaults file

Read `prompts/defaults.yml` at the start of any session that will create or modify findings. It contains:

- `contributors.people` — known person keys (e.g., `hoodcm`, `talkasab`) with their metadata
- `contributors.organizations` — known organization keys (e.g., `OIDM`, `MGB`) with their metadata
- `sources` — known source codes that can be used for OIFM IDs
- `tag_defaults` — suggested tag sets by project / modality context

Do not hard-code contributor lists in skill prose — always read them from `defaults.yml`.

## Confirm with the user once per session

On first invocation in a conversation, ask the user to confirm:

- **Source code** for OIFM IDs — e.g., `OIDM`. Most sessions use a single source throughout.
- **Contributors** — ideally both a person AND an organization. Most sessions use a single contributor pair throughout.
- **Tags** — the common tag set for every finding in this session (e.g., `["head", "CT", "finding"]` or `["knee", "MRI", "finding"]`).

Example prompt to the user:

> Before we start: what source, contributors, and tags should I use for this session?
> - Known sources: `OIDM`, `CDE`, `GMTS` (from `prompts/defaults.yml`).
> - Known contributors: people `hoodcm`, `HeatherChase`, `radngandhi`, `talkasab`; organizations `OIDM`, `GMTS`, `CDE`, `MGB`.
> - Suggested tag sets for this project: (list any entries from `tag_defaults` that look relevant).

Record the user's answer for the rest of the conversation. If they override on a specific finding ("use `talkasab` for this one, it's yours"), apply the override to that finding only and keep the session default for subsequent ones.

## Posture: show, then act

Before any step that writes to `defs/`, edits an existing model, invokes `create_model.py`, or runs `update_csv.py`, surface what you are about to do and its inputs to the user. Wait for confirmation (implicit or explicit) before running the action. This is especially important when the action changes multiple files at once or touches the tracking CSV. Never commit without explicit user permission.

## Don't drift from the defaults file

If the user mentions a contributor or source that isn't in `defaults.yml`, ask whether it's a typo or a new addition. If it's a new addition, add it to `defaults.yml` **and** to the `CONTRIBUTORS` dict in `scripts/finding_authoring/create_model.py` (and the matching dict in `fix_stub.py`) as a single atomic edit — the two must stay in sync.
