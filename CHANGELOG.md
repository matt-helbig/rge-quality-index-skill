# Changelog

## Unreleased

Scores produced by this version are **not comparable** to scores produced before it. Anything stored from an earlier version should keep its originating rubric and calculator version rather than being reconciled against new output.

### Scoring changes

**Unobserved strategy is renormalized away rather than averaged in.** When P5 carries `observability_default`, the calculator now drops strategy from the weighted sum and rescales the four observed pillars to sum to 1.0. Previously the 3.0 default was blended in at full weight, which pulled every strong email down and every weak one up for the majority of gallery reviews, where journey context is simply unavailable. An email with 4.5 across the observed pillars used to land at 4.27. Observed strategy is unaffected and carries its full weight.

**Bands collapsed from seven to five,** now half a point wide, with labels re-mapped so their meaning tracks the numbers rather than sliding down:

| Before | After |
|---|---|
| 4.7+ Exceptional, 4.4–4.6 Elevated, 4.1–4.3 Teachable, 3.8–4.0 Strong, 3.5–3.7 Competent, 3.0–3.4 Below, <3.0 Reject | 4.5+ Exceptional, 4.0–4.4 Teachable, 3.5–3.9 Competent, 3.0–3.4 Below, <3.0 Reject |

The accessibility cap (3.4) still lands at the top of Below / Needs Work, so capped emails are labeled exactly as before. The CFO clamp (4.4) now sits at the top of Teachable / Strong, one band below Exceptional, so failing that gate visibly costs the top band.

**Deductions collapsed to three tiers** — −0.2 minor, −0.3 notable, −0.5 serious — so a new rule can be placed consistently. Two rules changed value as a result: *visual clutter with no focal path* and *verified clipping that hides essential content*, both −0.4 before, are now −0.5.

**Deductions within one pillar may now total no more than −1.2,** enforced by the calculator. Stacking past the floor means the anchor was set too high, which is a scoring error rather than a worse email.

**Two double-deduction rules were narrowed.** Both will lower scores on affected emails:

- *Mobile failures.* The rule was that a mobile failure always deducts in both P1 (layout) and P2 (usability), explicitly "do not soften one to compensate for the other." Both now apply only where there are two distinct observed consequences.
- *Brand jargon.* The rule was that jargon in place of customer language flags in both P3 (voice) and P5 (positioning). A P3 wording criticism no longer automatically becomes a P5 deduction; P5 needs separate evidence of audience or task mismatch.

**CFO gate inputs are enforced rather than merely documented.** Claiming `cfo_metric_impact` requires a `cfo_metric_hypothesis`, and `cfo_criteria_met` may not exceed the distinct criteria recorded in `cfo_criteria_evidence`, whose names must match the six in `scoring.md`. A stored object that claimed the gate without recording evidence now fails validation. Objects that never claimed it are unaffected.

**Pillar arithmetic must reconcile exactly.** Anchor plus deductions reproducing the pillar score moved from a warning to a validation error, and the old 0.05 tolerance is gone.

### Output changes

- New `--audience=sender` mode emits only `valid`, `tier`, and `pillar_labels`. `--external` still adds labels without redacting anything.
- New `weights_renormalized` boolean records whether strategy was dropped from the weighted sum.
- A Forward tier downgraded by the craft floor no longer keeps the justification written for Forward; `distinctiveness_justification` is cleared.
- `weighted_craft_score` is floored to two decimals, matching the final score, instead of rounding half-to-even.
- `passes_distinctiveness_gate` is the explicit name for the old `gallery_eligible` check, which remains as an alias. Both check distinctiveness only.

### Structure

`SKILL.md` is now a router. The rubric, scoring formula, output contract, worked examples, industry context, cross-pillar patterns, time-sensitive calibration, and implementation guidance live in `references/`. A loader that sends only `SKILL.md` to a model without file tools must also include `rubric.md`, `scoring.md`, and `output.md` for a full review.

Guidance that inferred AI authorship from surface features — emoji counts, bullet density, stock phrases — was removed throughout. Generic execution is still scored; it is scored as a reader problem rather than as evidence about how the copy was written.
