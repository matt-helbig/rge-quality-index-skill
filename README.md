# RGE Quality Index

**Not just pretty. Persuasive.**

A five-pillar review framework from [Really Good Emails](https://reallygoodemails.com), packaged as an agent skill. It decides whether an email is worth featuring in the gallery, and tells a sender what to fix.

## How RGE reads an email

**Every review names the lesson.** What should another designer or marketer learn from this email? Name the element, say how it works, say why it repays study. "Beautiful", "on-brand" and "high-converting" are not reasons to feature anything. If there is no defensible lesson, say so instead of inventing one.

**Gallery merit and readiness are separate questions.** An email can be well built and still too ordinary for the gallery. A decline says nothing about whether it should ship. The framework answers both questions on their own terms and never lets one substitute for the other.

**The email is judged against its own job.** A receipt does not need an upsell. A newsletter with forty links may be doing exactly what it should. A password reset can be flawless and still teach nobody anything. Persuasion, urgency and personalization are tools, not requirements.

**Evidence comes first.** Findings are marked observed, inferred, or unverified. A screenshot cannot prove alt text is missing. An anchor tag cannot prove the unsubscribe works. Deductions attach to failures you can point at, so a reviewer's blind spot never becomes the sender's problem.

**Distinctiveness belongs to the work, not the brand.** Cover the logo. If the voice, imagery and structure still identify the sender, the execution is ownable. Not recognizing a brand is not evidence that its email is generic, and fame is not evidence that it isn't.

**Legibility and trust are floors.** A clever concept does not buy out unreadable body copy, buttons nobody can tap, or a subject line that fakes a security alert to get opened.

**The model judges, the script calculates.** Pillar scores, evidence and modifiers come from judgment. Every number after that comes from [`calculate_final.py`](skills/rge-quality-index/scripts/calculate_final.py), which enforces the caps and rejects arithmetic that does not reconcile. A model-written final score never reaches the reader.

## The five pillars

Each pillar scores 1.0 to 5.0 in tenths. Weights shown are for promotional email and shift by type.

| Pillar | Weight | The question |
|---|---:|---|
| Design and hierarchy | 25% | Is the message organized and readable? |
| Accessibility and technical craft | 20% | Can recipients reach the content and finish the task? |
| Copy and message discipline | 20% | Are the words clear, specific and appropriate? |
| Behavioral leverage | 20% | Does the email support its intended outcome? |
| Strategy and monetization intelligence | 15% | Does it fit the recipient's situation? |

### 1. Design and hierarchy

Visual structure and scroll control. Design carries the idea rather than decorating it.

Strong work has a focal path you can follow in about three seconds, rhythm between dense and open sections, a primary CTA nobody has to hunt for, and type chosen on purpose. Depth, high-contrast color, editorial display typography, illustration systems and mobile-specific reflows all earn credit when they serve the message.

It costs you when there is no focal path at all, when a primary button disappears among footer utilities, when columns stack in an illogical order, or when content truncates at 320px. Popular treatments are not distinctive by themselves. Rounded corners and heavy gradients used as accents can work; used as the entire design idea they are neutral at best.

High-SKU retail density is not a deduction. Judge prioritization, not product count.

### 2. Accessibility and technical craft

Execution quality, usability, and whether everyone can actually read the thing. This pillar is where craft becomes non-negotiable.

It covers measured contrast, body text at 16px and up, tap targets around 44px, alt text matched to image type, dark mode behavior, footer controls, animation fallbacks, merge-tag fallbacks, and Gmail clipping near 102KB.

Alt text is judged as a reading experience, not per image. Read in order alongside the live text, it should make sense out loud. Descriptions that break the argument are either unnecessary, so mark them decorative, or badly written.

Two rules bite hard. An accessibility score below 3.0 caps the final score at 3.4. An email whose essential message and action exist only inside images cannot score above 2.9 here, which forces that same cap. A legal footer in live text does not exempt it.

### 3. Copy and message discipline

What the words say and how they sound. What they make you do is pillar 4.

Subject line, preheader and opening sentence work as one contract with the reader. A question in the subject needs an answer in the opener. A tease needs a payoff. Strong copy is specific, written from the recipient's side, and recognizable as this brand without the logo.

Clichés, empty urgency, company-focused onboarding and CTAs that hide the destination all cost. Subject lines that imitate transactional or security alerts to lift opens are a trust violation, worth the maximum deduction and a rejection-level flag.

Generic copy is scored as a reader problem. Nothing here infers how the copy was produced, and emoji counts prove nothing.

### 4. Behavioral leverage

What the email makes you do. Precision beats intensity.

Strong work names a tension the reader recognizes, removes friction toward one dominant action, answers the objection before it hardens, and sometimes reframes the decision itself. Personalization earns credit by depth: a first name is table stakes, behavioral signal is a real lift, and a recipient-specific data visualization is the top tier when it feels natural rather than clever.

Promotional email gets three link clusters before deductions start. Newsletters are exempt, and product grids count as navigation rather than competing asks.

Button repetition, discount size, emotional exaggeration and countdown timers are not leverage.

### 5. Strategy and monetization intelligence

Whether the email fits where the recipient actually is. Funnel fit, the next step after the click, activation, retention, and whether the ask is worth making.

The weight is 15% because strategy is usually inferred rather than seen. When journey context is genuinely unavailable, this pillar takes a 3.0 default and drops out of the weighted sum entirely, with the remaining four pillars rescaled. Missing context neither helps nor hurts the score, so there is no reason to invent it.

Cadence-driven sends with no angle cap at 3.5. Program-level questions like send frequency and campaign-to-flow balance are diagnostics for a program, never for one email.

## Scoring

Weighted craft is multiplied by distinctiveness (0.95 interchangeable, 1.00 ownable, 1.05 forward) and lifecycle coherence, then bonuses for commercial courage and screenshot-worthy moments are added. Every non-default modifier needs a justification naming the element that earned it, or it reverts to neutral.

Deductions come in three sizes. Minor is 0.2, notable is 0.3, serious is 0.5. No pillar can lose more than 1.2 in total, because stacking past that means the anchor was set too high.

| Score | Band | Sender-facing tier |
|---|---|---|
| 4.5+ | Exceptional | Gallery-Worthy |
| 4.0 to 4.4 | Teachable | Strong |
| 3.5 to 3.9 | Competent | Fair |
| 3.0 to 3.4 | Below | Needs Work |
| under 3.0 | Reject | Not Ready |

Reaching 4.5 requires a plausible metric impact plus three of six excellence criteria, each documented. Interchangeable work caps at 4.2 and never reaches the gallery, however clean the craft.

RGE editors make the real inclusion decisions. Nothing the framework outputs means an email has been accepted.

## Using it

```bash
mkdir -p ~/.claude/skills
cp -R skills/rge-quality-index ~/.claude/skills/
```

Then ask for a review: "Grade this email against the Quality Index", or "What should I fix before sending?"

```bash
python skills/rge-quality-index/scripts/calculate_final.py scored.json           # internal object
python skills/rge-quality-index/scripts/calculate_final.py scored.json --audience=sender
python -m unittest discover -s skills/rge-quality-index/tests -v
```

Use `--audience=sender` for anything a sender sees. It emits qualitative labels only, with no scores or internal reasoning.

Detail lives in [`skills/rge-quality-index/references/`](skills/rge-quality-index/references): the full rubric, scoring math, output contract, worked examples, industry context, cross-pillar patterns, and pipeline guidance. [CHANGELOG.md](CHANGELOG.md) records score-affecting changes, and this version's scores are not comparable to earlier ones.

## Scope

QI reviews the email and whatever strategic context you supply. It does not certify legal compliance, inbox placement, ESP configuration, or revenue.

## License

Framework and documentation under [CC BY 4.0](LICENSE). `calculate_final.py` under MIT. Really Good Emails and "Gallery-Worthy" are trademarks; the license covers the framework, not the brand.
