# Scoring, modifiers, and gates

Read when calculating or auditing numerical scores.

## The Model

### Two Lenses

**65% Editorial Excellence** (Pillars 1–3) — Is this email worth archiving, studying, or presenting on stage?
**35% Performance Intelligence** (Pillars 4–5) — Does this email intelligently drive behavior, revenue, or retention?

The split shifts with email type. Transactional weighting pushes editorial to 70% and performance to 30%, because task clarity and reliable access take priority. Lifecycle pushes performance to 40%, because the email exists to move someone.

### Five Pillars (scored 1.0–5.0, weighted)

Default weights (Promotional):

```
Weighted Craft Score =
  (Design × 0.25) + (Accessibility × 0.20) + (Copy × 0.20) + (Behavioral × 0.20) + (Strategy × 0.15)
```

### Email Type Weight Adjustments

Apply adjusted weights when the email type is clearly not promotional. Default to Promotional when ambiguous. When an email is a hybrid (a newsletter that's really a product launch), use the weights matching primary intent.

| Pillar | Promotional (default) | Newsletter / Editorial | Transactional | Lifecycle / Triggered |
|--------|----------------------|----------------------|---------------|----------------------|
| Design | 0.25 | 0.20 | 0.20 | 0.20 |
| Accessibility | 0.20 | 0.15 | 0.30 | 0.20 |
| Copy | 0.20 | 0.30 | 0.20 | 0.20 |
| Behavioral | 0.20 | 0.15 | 0.10 | 0.25 |
| Strategy | 0.15 | 0.20 | 0.20 | 0.15 |

**Seasonal emails use default Promotional weights.** Visual concept execution and conversion both stay primary, so no adjustment is needed. Seasonal-specific judgment (authentic hook vs. promotional banner) lives in the Email Type scoring context, not the weights.

The criteria change with the job as well as the weights; use the type table in [SKILL.md](../SKILL.md). For a receipt, reassurance and comprehension may complete the task. For a password reset, a clear next action remains essential. Neither needs an upsell to earn a strong score.

### Final Score Formula

```
Step 1: Modified Craft Score
  = Weighted Craft Score × Distinctiveness Modifier × Lifecycle Modifier

Step 2: Bonus Application
  = Modified Craft Score + Courage Bonus + Screenshot Bonus

Step 3: Cap & Gate Enforcement (applied in order)
  → Accessibility Cap: A11y pillar <3.0 → final ≤3.4
  → Interchangeability Cap: Distinctiveness ×0.95 → final ≤4.2
  → Gallery Gate: Distinctiveness must be ×1.00+ for gallery inclusion
  → CFO Gate: 4.5+ requires plausible metric impact + ≥3 of 6 excellence criteria
```

**Modifier math:** Distinctiveness multiplies by 0.95 / 1.00 / 1.05. Lifecycle multiplies by 1.00–1.05. Courage and Screenshot are raw additions (+0.00–0.30 and +0.00–0.20).

**Implementation note:** Use the deterministic calculator for arithmetic and numeric caps. Local execution is sufficient; no server is required. The model supplies judgments and evidence, then makes the separate editorial assessment described in [output.md](output.md).

## Modifiers

| # | Modifier | Range | Trigger |
|---|----------|-------|---------|
| 1 | **Distinctiveness** | ×0.95 / ×1.00 / ×1.05 | Three tiers: Interchangeable, Ownable, Forward |
| 2 | **Lifecycle Coherence** | ×1.00 to ×1.05 | Personalization, segmentation intelligence, system thinking |
| 3 | **Commercial Courage** | +0.00 to +0.30 | Bold stance, category reframing, seasonal trope rejection |
| 4 | **Screenshot Worthy** | +0.00 to +0.20 | At least one moment worth saving to a swipe file |

**Justification requirement**: Every non-default modifier (anything other than ×1.00 / +0.00, plus the ×0.95 Interchangeable tier) must be accompanied by a one-sentence justification naming the specific element that triggered it — the quoted subject line, the described visual moment, the observed trigger logic. If you cannot point to the element, the modifier is the default. Neutral is the default. A persuasive-sounding justification is not evidence unless it names an observable element and explains the criterion it satisfies.

### Distinctiveness — Three Tiers

| Tier | Multiplier | Definition |
|------|-----------|------------|
| **Interchangeable** | ×0.95 | Swap the logo with a competitor's and the email still makes sense. Template energy. Triggers Interchangeability Cap (final ≤4.2) and Gallery Gate. |
| **Ownable** | ×1.00 | Recognizable brand identity — consistent palette, voice, structure — but not pushing the category forward. Neutral default. |
| **Forward** | ×1.05 | Genuinely un-swappable AND ahead of the category. The industry will study it. Not just distinctive for this brand — pointing toward where the category is going. |

Forward craft floor: Do not apply ×1.05 when weighted craft score is below 3.8. If concept is forward but craft isn't, score Ownable and note the concept positively.

### Lifecycle Coherence (×1.00 to ×1.05)

Award when the email demonstrates awareness of where the recipient is in their journey. ×1.01–1.02 for a small but evidenced adaptation beyond first-name substitution; ×1.03–1.05 for genuine system thinking (triggered, segmented, sequenced). Default to ×1.00 when context is unobservable.

### Commercial Courage (+0.00 to +0.30)

Reserve for emails that take a real creative or strategic risk: rejecting a seasonal convention, staking out a contrarian position, making a bold aesthetic choice most brands wouldn't. +0.10 for a notable moment; +0.20–0.30 when the risk is the concept. Do not award for merely being different — risk must be deliberate and legible.

Craft guidance: Below weighted craft 3.8, normally leave courage at zero. An unusual exception needs a specific explanation; the calculator flags it for review rather than treating this guidance as a hard cap.

### Screenshot Worthy (+0.00 to +0.20)

Award when there's at least one element a marketer or designer would screenshot for their swipe file — a brilliant subject line, clever visual moment, unexpected structural move. +0.10 for one strong moment; +0.20 for multiple. Does not imply overall quality — a competent email can earn this; an ambitious email can miss it.

---

## Caps & Gates

| | Trigger | Effect |
|--|---------|--------|
| **Accessibility Hard Cap** | A11y pillar <3.0 | Final ≤3.4 |
| **Interchangeability Cap** | Distinctiveness ×0.95 | Final ≤4.2 |
| **Gallery Gate** | Distinctiveness ×0.95 | Not recommended for gallery/archive |
| **CFO Gate** | Pre-gate score ≥4.5 | Must meet both conditions below; otherwise final is clamped to 4.4 |

### Gallery Gate

Ownable (×1.00) or Forward (×1.05) required for RGE gallery inclusion. Interchangeable emails are not gallery-worthy regardless of craft score — the gallery exists to showcase work worth studying, not competent templates.

### CFO Gate — Criteria for 4.5+

**Condition 1: Plausible metric impact.** The email must credibly move at least one business metric: conversion rate, revenue per email, activation rate, retention, AOV, or engagement lift. Requires a testable hypothesis, not proof.

**Condition 2: At least 3 of these 6 excellence criteria:**

| Criterion | What it means | Example |
|-----------|---------------|---------|
| **Behavioral reframing** | Changes how the reader thinks about a decision, not just what they know | "Sleep as a performance tool" not "comfortable mattress" |
| **Structural innovation** | Layout or format the reader hasn't seen before in the category | Interactive configurator in-email; timeline scroll instead of hero-body-CTA |
| **Visual metaphor alignment** | Visual and conceptual layers reinforce each other — design is meaningful, not decorative | Blueprint aesthetics for financial "building wealth"; decaying/regenerating visuals for sustainability story |
| **Lifecycle intelligence** | Awareness of where the recipient is, adapted accordingly — beyond basic personalization | Browse-abandonment referencing the specific product, addressing the likely objection, offering a relevant incentive |
| **High distinctiveness** | Scored ×1.05 (Forward tier) | See Distinctiveness guidance |
| **Strong conversion psychology** | Sophisticated use of anchoring, loss aversion, social proof, commitment/consistency — serving the reader's decision, not just the brand's goal | Pricing anchored on annual before monthly revealed; testimonial placed to answer the objection just raised |

---

## Score Bands

| Score | Label | Meaning |
|-------|-------|---------|
| 4.7+ | Exceptional | Category-shifting, structurally innovative. Rare. |
| 4.4–4.6 | Elevated | Distinctive, psychologically sharp, ownable |
| 4.1–4.3 | Teachable | Disciplined, strategically sound, worth studying |
| 3.8–4.0 | Strong | Good execution, limited conceptual lift |
| 3.5–3.7 | Competent | Competent but diluted or generic |
| 3.0–3.4 | Below | Functional, cluttered, or strategically weak |
| <3.0 | Reject | Significant problems across multiple pillars |

Use lower-inclusive bands: 3.0 ≤ score <3.5, 3.5 ≤ score <3.8, and so on. A small decimal difference is not evidence of a meaningful editorial difference by itself. Explain the specific gap when comparing emails.

**Calibration rule**: If two scorers disagree by >0.3, compare pillar scores to find the divergence. Compare evidence, anchors, deductions, type selection, and modifiers before changing weights.

**Actionability standard**: Where a fixable weakness exists, give a concrete improvement. A provisional score caused by unavailable evidence calls for a verification step, not an invented defect. Rubric-driven scoring is only better than generic AI feedback when the feedback is specific enough that a sender knows exactly what to change.

## Avoid repeated creative credit

The existing formula and modifier ranges are retained. A strong idea may support a pillar anchor and an editorial observation, but do not automatically turn every compliment into every bonus. Distinctiveness asks whether the execution is ownable; courage asks whether a deliberate risk adds value; screenshot-worthy asks what specific element merits saving. When one element supports multiple numerical rewards, explain the distinct contribution of each; otherwise keep the additional modifiers neutral. These attributes can always be mentioned without awarding points.

## Calculation and compatibility

Use `scripts/calculate_final.py` relative to the skill folder; local execution is sufficient. Use the input contract in [output.md](output.md). The calculator uses decimal arithmetic, applies gates before rounding, then floors the final result to two decimal places so display rounding cannot move a result across a gate or band. Pillar values stay in tenths; do not round them to halves. Intermediate rounding is for display only.

`gallery_eligible` is retained for existing consumers but means **passes the distinctiveness gate only**. The clearer alias `passes_distinctiveness_gate` has the same value. Neither is a complete gallery recommendation. Read the separate editorial assessment; a score or numeric tier never records actual RGE acceptance.

For older stored objects, missing pillar reasoning generates a warning; supplied reasoning must be complete and reproduce the supplied scores. New skill runs must emit full reasoning. Malformed values and inconsistent arithmetic fail validation. Historical scores should retain their originating rubric/calculator version rather than being silently overwritten.

## Calibration

Use a stable set of emails with independent human editorial decisions and the same available evidence. Compare recommendations and specific disagreements across rubric versions. A sample’s score distribution is diagnostic, not a quota. Do not force a fixed proportion into high or low bands, or mistake the model’s own earlier grades for human labels.
