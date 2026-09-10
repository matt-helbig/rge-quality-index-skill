# Implementation guidance

Read when building or maintaining a pipeline on this skill.

The division of labor is strict: **the model judges, the script calculates.**

## What each side produces

**The model emits:** email type, industry, per-pillar anchor plus itemized deductions plus the resulting pillar score, modifier tiers and values with justifications, the `all_image` flag, CFO gate inputs with their evidence when craft is trending high, and flags. It emits the object in [output.md](output.md) and nothing more.

**The script computes:** weighted craft, renormalization when strategy is unobserved, modifier math, every cap and gate, the final score, the band, and external labels. Never surface a model-written final score anywhere.

## Prompting order matters

Type first, then pillars — anchor before deductions — then modifiers, then emit JSON.

Do not ask a model for a final score or a band. Models pick the band first and back-fill pillar scores to justify it, which produces arithmetic that reconciles and judgment that does not. Pillar-first ordering is the defense, and the arithmetic audit is the check that it held.

## Why each guardrail exists

Removing one of these because it looks redundant is how the failure it prevents comes back.

- **Pillar scores in 1.0–5.0, in tenths.** A pillar below 1.0 next to a high final is a hallucinated output. Reject and re-score rather than repairing it.
- **The arithmetic audit.** Anchor plus deductions must reproduce the pillar score exactly. A score that cannot show its arithmetic is not auditable, and unauditable scores are the ones that drift.
- **Justification required on every non-default modifier.** This is not paperwork. Without it, courage bonuses land on roughly a third of emails and lifecycle coherence on nearly half — both wildly implausible. Neutral has to be the path of least resistance, or every modifier becomes a compliment.
- **The per-pillar deduction floor (−1.2).** Models stack small deductions rather than revising an anchor they already committed to. The floor forces the anchor to absorb a genuinely weak pillar.
- **CFO gate inputs require documented evidence.** The gate is the only route above 4.4. Left as bare booleans and counts, it is the cheapest thing in the object to overstate.
- **The Forward craft floor.** A forward concept on weak craft is still weak craft; the script downgrades the tier and drops the justification written for it.
- **`observability_default` on strategy.** Models invent journey context to escape the default. Making the assumption explicit keeps it auditable, and renormalization removes the incentive by ensuring the default no longer drags the score.

## Watching a batch

Check the distribution of a batch against the score bands. Top-heaviness is a symptom of anchor inflation, and the fix is to recalibrate anchors, not to add deductions until the numbers look right.

This is diagnostic, not a quota. Do not force a fixed proportion of emails into any band, do not tune a batch toward a target shape, and do not treat the model's own earlier grades as ground truth. A genuinely strong batch is allowed to look like one.
