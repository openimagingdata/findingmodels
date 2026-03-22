# Prompt Length and Instruction Complexity: Research and Recommendations

*2026-03-22 — Background research for prompt architecture decisions*

## The Question

Our three agent prompts (create, review, merge) reference shared documents (`conventions.md`, `overview_compact.md`) that define naming rules, synonym strictness, attribute standards, associated findings vs components, etc. We currently inline these documents (~19KB) into every agent's system prompt, producing ~25K chars of instructions per agent call. Is this helping or hurting?

## What the Research Says

### 1. Instruction-Following Degrades With Instruction Count

The most directly relevant finding: LLMs' ability to follow instructions deteriorates as the number of simultaneous instructions increases — and the degradation is steep.

- **"Curse of Instructions" (ICLR 2025):** With 10 simultaneous instructions, GPT-4o succeeded only 15% of the time; Claude 3.5 Sonnet managed 44%. Performance drops exponentially, not linearly.
- **"How Many Instructions Can LLMs Follow at Once?" (arXiv:2507.11538, Feb 2026):** Even the best frontier models achieved only 68% accuracy at maximum instruction density. Three degradation patterns observed: threshold decay (good until a cliff), linear decay, and exponential decay. Reasoning models (o3, Gemini 2.5 Pro) showed threshold decay — near-perfect until a critical density, then rapid collapse.
- **"The Instruction Gap" (arXiv:2601.03269, Jan 2026):** Characterized this as a "fundamental barrier to reliable LLM deployment in production systems."

**Implication for us:** Our review agent prompt has ~40 discrete checklist items. Conventions.md adds ~30 more rules. We're deep in degradation territory.

### 2. Lost in the Middle — It Applies to System Prompts Too

The "Lost in the Middle" effect (Liu et al., TACL 2024) isn't just about retrieval tasks. LLMs attend to the beginning and end of their input with 30%+ accuracy advantage over material in the middle. MIT research (2025) traced the cause to RoPE positional encoding decay.

**Practical finding from PromptLayer:** A 10,000-token prompt may effectively operate on just the last ~2,000 tokens due to recency bias.

**Implication for us:** When we append conventions.md after the agent-specific prompt, the agent's own task instructions (which it needs most) end up in the "lost" middle zone, with conventions content at the end getting more attention than the actual task rules.

### 3. Extraneous Context Hurts Structured Output

For tasks where the model fills a JSON schema (our exact use case), the research is particularly clear:

- **"Identification without exclusion" problem (MLOps Community):** LLMs can identify irrelevant information in a prompt but cannot ignore it during response generation. The irrelevant details still influence the output.
- **Semantically similar noise is the worst kind:** If the system prompt contains domain background that is related to but not directly relevant to the specific field being filled, the model confuses it with task requirements.
- **Reasoning degradation begins around 3,000 tokens of input** (Goldberg et al., ACL 2024), well below context window limits. Chain-of-thought does not mitigate this.

**Implication for us:** Conventions.md is all closely related domain content. The merge agent doesn't need compound finding detection rules (that's the review agent's job), but it sees them anyway, and they influence its output.

### 4. GPT-5.x Handles Long Prompts Better — But Not Enough

GPT-5.2+ achieves near-100% on 4-needle retrieval at 256K tokens. GPT-5.4 supports 1M context with "stronger instruction adherence in modular, block-structured prompts."

But OpenAI still recommends "force summarization and re-grounding" for long-context tasks. Their explicit GPT-5.4 guidance: **"Start with the smallest prompt that passes your evals, and add blocks only when they fix a measured failure mode."**

The improvements are real but don't eliminate the fundamental tradeoffs.

### 5. Vendor Best Practices Converge on Structure and Separation

**OpenAI (GPT-5.4 Prompt Guidance):**
- Use modular, block-structured prompts with XML-like tags (`<output_contract>`, `<grounding_rules>`)
- Start with the smallest prompt that passes evals
- GPT-5.x follows instructions so well that "contradictory or vague instructions are more damaging than for previous models"
- For smaller models (mini/nano): "critical rules first," numbered steps, no implicit understanding

**Anthropic (Claude Best Practices):**
- Structure with XML tags to separate instructions, context, examples, and inputs
- Long-form data at top, queries/instructions at end (up to 30% improvement)
- Dynamic loading ("Skills") rather than embedding reference material in every prompt

Both recommend separating **instructions the model must follow** from **reference material the model should consult**.

## Analysis: Our Current Prompts

### What We're Doing

Each agent receives:
1. Its task-specific prompt (~3-5KB) — role, task, rules, output format
2. `overview_compact.md` (~2KB) — what a finding model is
3. `conventions.md` (~17KB) — the full rulebook

Total: ~22-25KB per agent call.

### What's Good

- The task-specific prompts are well-structured with clear sections
- The rules are consistent across prompts (because they share a source)
- The conventions.md document is thorough and well-organized

### What's Concerning

1. **Instruction density is very high.** The review agent sees 40+ checklist items in its own prompt plus 30+ rules from conventions. At this density, research predicts each individual rule is followed with significantly reduced probability.

2. **Every agent sees every rule.** The create agent sees compound finding detection rules it doesn't need. The merge agent sees the full synonym strictness test it could apply but shouldn't (it's matching attributes, not writing synonym lists). The review agent sees the merge strategy. Irrelevant-but-related content is the worst kind of noise.

3. **Task instructions get "lost in the middle."** The agent's own rules sit between the role/task header (beginning) and conventions.md (end). The middle is the worst position for critical content.

4. **No structural separation.** Instructions, rules, reference material, and output format are all in the same markdown flow. No XML tags or explicit delimiters distinguish "you must do this" from "here is context."

5. **Rules that could be enforced programmatically aren't.** Lowercase names, underscore checking, presence-as-first-attribute — these are mechanically verifiable. Relying on the LLM to enforce them wastes instruction budget and adds failure modes.

## Recommendations

These are starting points for discussion, not a plan.

### R1: Don't inline conventions.md wholesale

Instead, treat conventions.md as the **source of truth for humans** — the authoritative reference that prompt authors consult when writing task prompts. Each task prompt should contain the specific rules that agent needs to act on, in the agent's own voice, using the agent's own terminology. The task prompts already mostly do this.

**Keep inlining overview_compact.md** (~2KB). It's short, gives essential framing, and every agent needs the "what is a finding" context.

### R2: Each agent should see only the rules it acts on

| Rule area | Create | Review | Merge |
|-----------|:------:|:------:|:-----:|
| Naming conventions | Yes | Yes | Yes (for attribute names) |
| Synonym strictness | Yes | Yes | Partial (for value canonicalization) |
| Presence / change from prior | Yes | Yes | Yes |
| Associated findings vs components | Yes | Yes | Yes |
| Compound finding detection | No | Yes | Yes (flag only) |
| Clinical appropriateness / specificity | No | Yes | No |
| Description grammar | Yes | Yes | No |
| Subtype decision framework | No | Yes | No |
| Near-duplicate detection | No | Yes | No |
| Collision detection (synonym search) | Yes | No | Yes |

Some rules belong in one or two agents, not all three.

### R3: Separate instructions from reference material with structural tags

If we do include shared context, use explicit delimiters:

```
<instructions>
Your task-specific rules here — what you MUST do.
</instructions>

<reference>
Background context — consult when relevant, don't memorize.
</reference>

<output_contract>
Exact output format and field descriptions.
</output_contract>
```

OpenAI and Anthropic both recommend this pattern for GPT-5.x.

### R4: Move mechanical checks to Python post-processing

Rules that are deterministically verifiable should be enforced in code, not prompts:

- Lowercase name/attribute/value enforcement
- No underscores in name fields
- Presence as first attribute, change from prior as second
- Minimum value counts for presence (4) and change from prior (5+)
- No duplicate presence/change from prior attributes
- Minimum field lengths (name ≥ 5, description ≥ 5)

This reduces the instruction count the LLM must follow while providing stronger guarantees.

### R5: Measure before optimizing

OpenAI's GPT-5.4 guidance is explicit: "Start with the smallest prompt that passes your evals, and add blocks only when they fix a measured failure mode."

Before trimming, we should:
1. Run the pipeline on a representative batch (~10 findings)
2. Score the output against the conventions
3. Identify which rules are actually being violated
4. Only then decide what to add/remove/restructure

The current prompts may work fine despite being long. Or they may fail on specific rules. We won't know without running them.

### R6: Consider dynamic/conditional prompt composition

Not every finding needs every rule. A device finding doesn't need the subtype decision framework. A simple finding with no sub-components doesn't need the full associated-findings guidance.

A more sophisticated `load_instructions()` could select prompt sections based on the finding category or the pipeline stage context. This is a larger architectural change but aligns with both vendors' recommendations for production systems.

## Sources

- OpenAI, "Prompt guidance for GPT-5.4" — https://developers.openai.com/api/docs/guides/prompt-guidance
- Anthropic, "Claude Prompting Best Practices" — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- "Curse of Instructions" (ICLR 2025) — https://openreview.net/forum?id=R6q67CDBCH
- "How Many Instructions Can LLMs Follow at Once?" (Feb 2026) — https://arxiv.org/abs/2507.11538
- "The Instruction Gap" (Jan 2026) — https://arxiv.org/html/2601.03269v1
- "Lost in the Middle" (TACL 2024) — https://aclanthology.org/2024.tacl-1.9/
- MIT position bias research (2025) — https://techxplore.com/news/2025-06-lost-middle-llm-architecture-ai.html
- MLOps Community, "Impact of Prompt Bloat on LLM Output Quality" — https://mlops.community/the-impact-of-prompt-bloat-on-llm-output-quality/
- PromptLayer, "Disadvantage of Long Prompt for LLM" — https://blog.promptlayer.com/disadvantage-of-long-prompt-for-llm/
- Effects of prompt length on domain-specific tasks (Feb 2025) — https://arxiv.org/abs/2502.14255
- Goldberg et al. (ACL 2024) on reasoning degradation with input length
