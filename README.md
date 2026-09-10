# RGE Quality Index

**Not just pretty. Persuasive.**

A five-pillar email review framework developed by [Really Good Emails](https://reallygoodemails.com), packaged as an agent skill. Its primary job is to recommend work worth studying for the RGE gallery. Its second job is to help senders understand and improve their emails.

Every gallery review answers: **What specifically should another email designer or marketer learn from this email?** A high score supplies context; a concrete editorial reason explains why the work is worth featuring.

## Five pillars

| Pillar | Promotional weight | Question |
|---|---:|---|
| Design & Hierarchy | 25% | Is the message organized and readable? |
| Accessibility & Technical Craft | 20% | Can recipients access the content and complete its task? |
| Copy & Message Discipline | 20% | Are the words clear, specific, and appropriate? |
| Behavioral Leverage | 20% | Does the email support its intended outcome? |
| Strategy & Monetization Intelligence | 15% | Does the email fit the recipient's situation and purpose? |

Pillars use 1.0–5.0 scores in tenths. Weights change for newsletters, transactionals, and lifecycle emails; success criteria change with their jobs too. A receipt does not need an upsell, a newsletter may have many useful links, and a conventional password reset can have excellent craft without a distinctive gallery lesson.

The existing weights, modifier ranges, and numeric caps are retained. See [the scoring reference](skills/rge-quality-index/references/scoring.md) for the formula and bands.

## Two separate assessments

**Gallery:** Recommend, Consider, Decline, or Needs evidence. A recommendation needs a specific teachable reason, Ownable or Forward distinctiveness, adequate evidence, and no critical accessibility, task-completion, or trust failures. An editor can consider one exceptional idea in otherwise competent work without raising the numerical score or waiving a blocker.

**Readiness:** No critical issues observed, Fix before sending, or Not verified. The assessment is limited to the evidence inspected. A gallery decline is not automatically a judgment that the email is unusable.

RGE editors make actual inclusion decisions. Neither an automated recommendation nor the numerical “Gallery-Worthy” tier means the email has been accepted.

## Evidence and feedback

The normal input is HTML plus subject and preheader, with renders for visual judgments. Distinguish observed findings, supported inferences, and unverified conditions. A screenshot does not establish missing alt text; an HTML link does not establish successful post-click behavior.

Apply style deductions to demonstrated weaknesses, not to isolated choices such as outline buttons, system fonts, or “Shop Now.” Feedback names the issue, explains the reader impact, and suggests a concrete change. Give only the fixes supported by the evidence; do not invent criticism to fill a quota.

## Install

For Claude Code, copy the skill folder:

```bash
mkdir -p ~/.claude/skills
cp -R skills/rge-quality-index ~/.claude/skills/
```

Start with: “Review this email for the RGE gallery,” “Grade this email against the Quality Index,” or “Explain what to improve before sending.”

## Files

```text
skills/rge-quality-index/
├── SKILL.md                 workflow, evidence, type-specific criteria, editorial decisions
├── references/
│   ├── rubric.md            detailed pillar signals and contextual deductions
│   ├── scoring.md           weights, modifiers, gates, calibration
│   ├── output.md            scoring input and curator/sender output contract
│   ├── examples.md          worked score and contrasting editorial cases
│   ├── industry-context.md  audience and category interpretation
│   ├── patterns.md          optional cross-pillar review prompts
│   └── program-maturity.md  program context when evidence exists
├── scripts/
│   └── calculate_final.py   deterministic score calculation
└── tests/
    ├── fixtures/skincare.json
    └── test_calculate_final.py
```

## Calculate and validate

The model supplies pillar judgments and evidence. The Python script validates numbers and arithmetic, applies the existing caps, and maps bands. It uses only the standard library and makes no network calls.

```bash
python skills/rge-quality-index/scripts/calculate_final.py scored.json --external
python -m unittest discover -s skills/rge-quality-index/tests -v
```

The [input contract](skills/rge-quality-index/references/output.md) includes CFO-gate inputs and a valid JSON example. The [worked fixture](skills/rge-quality-index/tests/fixtures/skincare.json) produces 3.64 / Competent / Fair.

Calculation details relevant to existing integrations:

- `SKILL.md` now routes to reference files. Agents need access to the whole skill folder. An application that sends only `SKILL.md` to a model without file tools must also include `rubric.md`, `scoring.md`, and `output.md` in a full-review prompt, plus relevant industry/program context. Do not deploy that loader unchanged after this restructuring.
- Numeric strings, booleans used as scores, out-of-range values, unknown modifier tiers, and inconsistent supplied pillar arithmetic fail validation.
- Legacy objects without pillar reasoning remain accepted with a warning. New skill runs include full reasoning.
- CFO-gate inputs are enforced, not merely documented. Claiming `cfo_metric_impact` requires a `cfo_metric_hypothesis`, and `cfo_criteria_met` may not exceed the distinct criteria documented in `cfo_criteria_evidence`, whose names must match the six in `scoring.md`. A stored object that claimed the gate without recording its evidence now fails validation; either document the claim or drop it. Objects that never claimed the gate are unaffected.
- Decimal arithmetic prevents floating-point errors at band boundaries. Gates run before display precision is reduced; the final score is floored to two decimals so display rounding does not cross a band or gate.
- `passes_distinctiveness_gate` is the explicit name for the old `gallery_eligible` check. The old field remains an alias for compatibility. Both check distinctiveness only; use the separate editorial assessment for the complete gallery recommendation.
- `--external` adds labels; it does not redact the internal object. Defaulted strategy is labeled “Not verified.” The presentation layer must select the intended audience's fields and disclose other material evidence gaps.
- The calculator does not validate the truth of editorial evidence or decide gallery inclusion. The skill's editorial review follows the calculation.

## Scope

QI reviews the email artifact and supplied strategic context. It does not certify legal compliance, inbox placement, ESP configuration, or performance lift. Keep actual human editorial decisions separate from model output when evaluating the framework.

## License

Framework and documentation: [CC BY 4.0](LICENSE). `calculate_final.py`: MIT.
Really Good Emails and “Gallery-Worthy” are trademarks; the license covers the framework, not the brand.
