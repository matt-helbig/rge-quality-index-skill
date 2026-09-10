# Scoring objects and feedback

Read when producing a score or presenting the review. Preserve the user's requested level of detail. Sender output defaults to qualitative labels; an explicit request to inspect scores or methodology can receive the internal detail.

## Input to the calculator

Emit inputs only, not a model-written final score or band. This valid neutral example shows the input shape; replace its illustrative scores and evidence with the reviewed email's evidence.

```json
{
  "email_type": "promotional",
  "industry": null,
  "pillar_scores": {"design": 3.0, "accessibility": 3.0, "copy": 3.0, "behavioral": 3.0, "strategy": 3.0},
  "pillar_reasoning": {
    "design": {"anchor": 3.0, "evidence": "Readable hierarchy; conventional execution.", "deductions": []},
    "accessibility": {"anchor": 3.0, "evidence": "Core content readable in the supplied render; other client conditions unverified.", "deductions": []},
    "copy": {"anchor": 3.0, "evidence": "Specific offer; functional but undistinguished wording.", "deductions": []},
    "behavioral": {"anchor": 3.0, "evidence": "Clear action with limited decision support.", "deductions": []},
    "strategy": {"anchor": 3.0, "evidence": "Journey context not supplied.", "deductions": [], "observability_default": true}
  },
  "modifiers": {
    "distinctiveness_tier": "ownable",
    "distinctiveness_justification": null,
    "lifecycle_coherence": 1.00,
    "lifecycle_justification": null,
    "courage_bonus": 0.00,
    "courage_justification": null,
    "screenshot_bonus": 0.00,
    "screenshot_justification": null
  },
  "all_image": false,
  "cfo_metric_impact": false,
  "cfo_metric_hypothesis": null,
  "cfo_criteria_met": 0,
  "cfo_criteria_evidence": [],
  "flags": [],
  "evidence_summary": {
    "observed": ["HTML and supplied desktop render inspected"],
    "inferred": [],
    "unverified": ["Other client renders", "Journey context"]
  }
}
```

- `email_type`: `promotional`, `newsletter`, `transactional`, `lifecycle`, or `seasonal`.
- A deduction has `rule`, negative numeric `value`, and a specific `evidence` explanation. Every new pillar reasoning object includes `anchor`, `evidence`, and `deductions`.
- `all_image`: true or false when verified, null when unknown. The calculator cannot infer image dependence from prose; null produces a warning and cannot be used as evidence of a pass.
- Non-default modifiers require nonblank justifications. Unsupported modifiers remain neutral.
- `cfo_metric_impact` is a boolean, not a text hypothesis or the string `"false"`. When true, a testable `cfo_metric_hypothesis` is required; the calculator rejects the object without one.
- `cfo_criteria_met` is an integer from 0 to 6, and it may not exceed the criteria you actually document. Record each met criterion in `cfo_criteria_evidence` using `criterion` and `evidence`. Criterion names must match the six in [scoring.md](scoring.md) (matched case-insensitively) and each may be counted once, so a repeated or renamed criterion cannot pad the total. The calculator enforces these inputs because the CFO gate is the only route above 4.4; it still cannot judge whether the evidence you supply is true, which remains the reviewer's job.
- Set P5's `observability_default` only when using its unknown-context default. Do not claim observed poor strategy merely because the default is 3.0.

The calculator adds `weighted_craft_score`, `calculated_final_score`, `caps_applied`, `band`, `passes_distinctiveness_gate`, legacy `gallery_eligible`, `valid`, and `warnings`. With `--external` it also adds `_external` labels; that flag does **not** remove the internal fields. An application must select the fields appropriate for its audience.

## Complete the editorial assessment after calculation

Keep this assessment alongside the calculated object; it is not an input to the score formula and is not generated or enforced by the numerical calculator.

| Field | Values / meaning |
|---|---|
| `gallery_recommendation` | `recommend`, `consider`, `decline`, or `needs-evidence` |
| `reason_to_feature` | Specific teachable element, mechanism, and lesson; null when none is supported |
| `gallery_reason` | Why this recommendation follows from the evidence, lesson, and limitations |
| `readiness` | `no-critical-issues-observed`, `fix-before-sending`, or `not-verified` |
| `critical_issues` | Supported accessibility, task-completion, or trust failures with evidence |
| `verification_needed` | Missing evidence material to the recommendation or readiness |

**Recommend:** A clear lesson supported by coherent execution, Ownable/Forward distinctiveness, and adequate evidence, with no critical failures. This is a recommendation to RGE editors, not an acceptance action.

**Consider:** A narrow, exceptional lesson in otherwise competent work merits an editor's judgment. Name what is worth studying and what limits broader endorsement. No critical failures; no score adjustment or cap override.

**Decline:** There is no sufficient editorial reason, the execution is Interchangeable, or a critical failure prevents recommendation. State the actual reason. If the email is functional but conventional, say so without inventing readiness problems.

**Needs evidence:** A material unknown prevents deciding. Ask for the specific missing evidence. Missing journey details alone need not hold a gallery review when the proposed lesson is independently observable; an unsupported claim of lifecycle sophistication cannot be its basis.

If accessibility is below 3.0, `all_image` is true, or there is a critical trust/task failure, do not use Recommend or Consider. Preserve a worthwhile idea in the feedback while stating what prevents recommendation. Do not override these constraints because of a high average. Missing evidence does not erase a known blocker.

## Curator-facing output

1. **Gallery recommendation and reason to feature** (or reason to decline / evidence needed).
2. **Readiness and critical issues**, with material unverified conditions.
3. **What to retain and improve**, prioritized by effect on the reader and editorial value.
4. **Score context**, when useful or requested; use the calculator's result, never a model-written total.

## Sender-facing output

Lead with the most useful changes. Give up to four specific improvements when warranted, fewer when fewer exist, and none when no supported fix is needed. Each names the observed issue, its reader impact, and a concrete suggestion. Distinguish fixes before sending from optional editorial enhancements and verification requests. If many critical failures exist, explain the need for a broader rework rather than pretending four tweaks will resolve everything.

Then identify specific elements worth retaining. Give qualitative pillar labels and an optional overall tier as context. Show **Not verified** for defaulted strategy and mark partially observed pillars **Provisional** with the missing evidence. Do not disguise unavailable evidence as a mediocre grade.

If the sender asked about gallery inclusion, explain the recommendation in plain language. An email can work well without being selected. “Gallery-Worthy” is the numerical system's highest tier label, not a claim that RGE has accepted the email. “Not Ready,” when displaying the low numeric tier, is not a substitute for the separate readiness assessment.

**Feedback example:** “The outlined primary button has little visual separation from the adjacent cards. Try a filled treatment or more spacing to make the next step easier to find.” Avoid unsupported predictions such as “most subscribers will scroll past.”

Use RGE's direct, specific voice. Avoid generic praise, claimed conversion lift without evidence, formula jargon in default sender feedback, and forced criticism. Sender-facing prose should avoid em dashes; this is a voice convention, not a scoring rule.

## Integration notes

Store the full evidence and scoring inputs if reproducible grading is needed. Preserve input identity and rubric/model/calculator versions. Do not treat timestamps or model-written verdicts as human editorial decisions. Keep actual editor acceptance separate from model recommendations.
