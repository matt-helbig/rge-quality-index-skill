---
name: rge-quality-index
description: Use when evaluating email design quality, scoring email submissions, grading marketing emails, reviewing email craft, or building email scoring systems. Also trigger on any mention of QI, QI score, QI framework, or Quality Index. Covers the RGE Quality Index Five-Pillar Hybrid Model — a structured framework for evaluating marketing emails across design, accessibility, copy, behavioral leverage, and strategy. Includes weighted scoring, benchmarks, deduction rules, modifiers, caps, score bands, email type/industry context, and LLM implementation guidance.
---

# RGE Quality Index — Five-Pillar Hybrid Model

**Not just pretty. Persuasive.**

A structured scoring framework for evaluating marketing email quality. Balances editorial excellence (65%) with performance intelligence (35%) through five weighted pillars, four modifiers, and four caps/gates.

---

## When To Use This Skill

- Scoring or grading any email submission (any type, any industry)
- Building or improving an email quality rubric
- Evaluating email design, copy, accessibility, or behavioral effectiveness
- Comparing emails or explaining why one is better
- Providing structured feedback on email campaigns
- Training reviewers on what "good" looks like in email

### What This Skill Does Not Rule On

**Verify mechanics, not sufficiency.** Where a requirement varies by country, industry, jurisdiction, or ESP — compliance wording, the applicable accessibility standard, consent language, the must-support client list — this framework does not rule on legal or regulatory *sufficiency*. It scores whether the element is **present, prominent, and functional**. A scored footer signal means the unsubscribe works and is findable, not that the email is CAN-SPAM, CASL, or GDPR compliant. Capture jurisdiction-specific requirements separately, up front, and keep the scoring pass generic.

Also outside the five pillars:

- **Deliverability** — SPF/DKIM/DMARC alignment, `List-Unsubscribe` headers, IP and domain reputation, spam scoring, inbox placement. QI scores the email as a designed artifact, not its authentication or routing.
- **ESP campaign configuration** — audience, segmentation, send time, A/B setup, automation logic.
- **Legal certification** — presence and function, never conformance.

When a review touches one of these, note it and route it to the right owner rather than folding it into a pillar score.

---

## The Model

### Two Lenses

**65% Editorial Excellence** (Pillars 1–3) — Is this email worth archiving, studying, or presenting on stage?
**35% Performance Intelligence** (Pillars 4–5) — Does this email intelligently drive behavior, revenue, or retention?

The split shifts with email type. Transactional weighting pushes editorial to 70% and performance to 30%, because the action is already done. Lifecycle pushes performance to 40%, because the email exists to move someone.

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

**Why these adjustments:**
- **Newsletters / Editorial** (curated content, digest, report, infographic): Live or die on voice and curation — Copy up, Behavioral down. Strategy increases because audience positioning and content sequencing define newsletter quality.
- **Transactional** (order confirmation, shipping, password reset, receipt, cancellation, alert, verification, GDPR): Must be clear, accessible, and structurally sound above all. Behavioral is nearly irrelevant — the action is done. Strategy rises because smart transactionals use their high open-rate moment. Note: transactionals rarely expose journey context, so P5 often lands at its 3.0 unobservable default — the raised weight then pulls unobservable transactionals toward the middle. This is intentional: it keeps a bare-but-clean receipt from scoring high on structure alone.
- **Lifecycle / Triggered** (welcome, onboarding, browse abandonment, re-engagement, winback, post-purchase, upsell): Behavioral instruments by design — Behavioral up. Every element should serve the moment.

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

**⚠️ Implementation note:** Caps and gates must be enforced server-side, not by model instruction. LLMs reliably describe caps in reasoning but fail to apply them in math. Always recalculate final scores server-side and clamp. Never trust a model's self-reported final score when pillar scores are available. See LLM Scoring Implementation Guidance.

---

## How Pillar Scores Are Produced

Each pillar uses the same three-step mechanic. This resolves the ambiguity between the rubric tables and the deduction lists — they are sequential, not alternative, scoring methods.

1. **Anchor** the pillar using its signal table and scoring guidance. Read the email against the Strong (4–5) and Weak (1–2) columns and set a starting score that reflects the overall quality of execution. Positive signals are anchoring evidence — they justify a higher anchor, they are never added on top of it.
2. **Deduct** using the pillar's listed deduction values for each specific violation present. Deductions stack. Do not deduct twice for the same root cause within a pillar (a ghost primary CTA is one −0.3, not also "CTA prominence" anchor damage plus −0.3 — pick the anchor first, then apply deductions for discrete violations the anchor didn't already price in).
3. **Clamp** to the 1.0–5.0 range. No pillar goes below 1.0 regardless of deduction count — if deductions would drive a pillar below 1.0, the email is a rejection case and the pillar floor communicates that adequately.

Report the anchor, each deduction, and the resulting pillar score in reasoning. A pillar score that can't show its arithmetic is not auditable.

---

## Editorial Principles

Apply as judgment overlays when scores feel ambiguous. Read before scoring, not after.

**Legibility is the floor.** If content cannot be read, nothing else qualifies the email. Thin text on colored backgrounds, tight line heights, or body text below 14px on mobile are disqualifying regardless of visual appeal.

**Accessibility is a philosophy, not a checklist.** Emails that pass WCAG checks but produce poor screen reader experiences, rely on image text for key offers, or use all-caps throughout miss the point. Credit emails where accessibility is a design value, not a compliance checkbox. Regulatory context lives in Current-Era Calibration.

**Email shouldn't look the same everywhere.** Designs that exploit rendering environments — dark mode, animation, hover states, live personalization — reward the medium. Treating email as a static image delivery system is a missed opportunity.

**Humanity beats polish.** The differentiator is genuine understanding of the subscriber's context — their specific problem, their behavioral moment, their relationship with the brand. An email that reads like it was written by someone who knows the reader beats a polished template every time. Production tooling is not the question; evidence of understanding is.

---

## Current-Era Calibration

**Last reviewed: July 2026.** Time-sensitive claims live here so they rot in one place. Review this section quarterly; the rest of the rubric is timeless.

- **WCAG 2.1 AA is a legal requirement for US public entities** (DOJ ruling, effective April 2026). For government, higher-ed, and public-institution senders, accessibility failures carry regulatory risk on top of the standard scoring impact — flag in P5.
- **Dark mode readiness is a baseline expectation, not an advanced skill.** Score negligence increasingly as a disqualifier, not a missed bonus.
- **Interactive email techniques are expanding.** CSS/HTML spec updates keep raising the bar — what was exceptional in 2023 is approaching expected. Calibrate interactivity credit downward over time.
- **All-image emails are on a trajectory toward automatic disqualification.** The mechanical rule (P2 ceiling of 2.9) reflects current strictness; expect it to tighten further.
- **Generative tooling is now common in email production.** AI-generated imagery or copy is not a deduction in itself — judge the output, not its origin. Flag for internal review only when legibility, cohesion, or the AI Slop Indicators in P3 are triggered. As volume rises, the scarce signal is evidence the sender understands the reader; weight that accordingly.
- **Visual trend inventory.** The trend elements currently common enough to be non-distinctive: rounded corners, wavy dividers, organic blob shapes, heavy gradients, oversized type. Repetition of any of these is scored in P1; which specific elements are ubiquitous is what changes — revisit this list, not the rule.

---

## Pillar Boundary Guidance

These boundaries prevent double-crediting and inconsistent scoring.

**Pillar 3 (Copy) vs. Pillar 4 (Behavioral):** Pillar 3 scores what the words say and how they sound. Pillar 4 scores what they make you do. A great subject line can score 4.5 in P3 (distinctive voice) and 2.5 in P4 (no behavioral tension). Or 3.0 in P3 (functional wording) and 4.5 in P4 (engineered urgency). Scores are independent.

**Mobile across Pillars 1 and 2:** Pillar 1 evaluates mobile as a layout/hierarchy problem (stacking, column logic, scroll pacing). Pillar 2 evaluates mobile as an accessibility/usability problem (tap targets, legibility, readability at arm's length). Both sets of deductions apply independently. Mobile failure is both a design failure and an accessibility failure — do not soften one to compensate for the other.

**Copy voice (P3) vs. Strategic positioning (P5):** When messaging uses brand jargon instead of customer language, flag in both pillars. P3 captures the copy-level failure (voice doesn't match reader). P5 captures the strategic failure (positioning written for the brand, not the audience). Not double-counting — two different failures sharing a root cause.

---

## Handling Incomplete Observability

Not every pillar can be fully evaluated from a single submission.

**Pillar 5 (Strategy):** Default to 3.0 when lifecycle stage, sequence position, or segmentation logic can't be inferred. Note the assumption explicitly. Score on what's observable; flag what's inferred.

**Lifecycle Coherence modifier:** Default to ×1.00 when no journey context is visible. Do not guess.

**General rule:** Score what you can see. Flag what you can't. A score with a noted caveat is more useful than one built on assumptions.

---

## Pillar 1: Design & Hierarchy (25%) — Editorial

Measures visual structure and scroll control. Design supports the idea — not decorative filler.

| Signal | Strong (4–5) | Weak (1–2) |
|--------|-------------|------------|
| **Hierarchy** | Clear focal path, scannable in 3 seconds | Wall of content, no entry point |
| **Scroll pacing** | Rhythm between dense and breathing sections | Monotonous blocks |
| **CTA prominence** | Primary CTA unmissable, secondary subordinate | CTAs buried or competing equally |
| **Typography** | Deliberate pairing, readable scale | System defaults, too many fonts |
| **Layout** | Intentional grid, purposeful structure | Cramped, misaligned, inconsistent padding |
| **Brand cohesion** | Immediately recognizable as this brand | Generic template energy |

**Concrete benchmarks:**
- Body text: ≥16px (baseline, not a bonus)
- Headings: 22–30px
- Font families: max 2–3
- CTA buttons: ≥44×44px
- Email width: 600–700px
- Total height: 1500–2000px ideal; flag >3000px
- File weight: ideally <800kb; flag >1.5MB
- Header: ≤100px (no nav) or ≤200px (with nav)
- Mobile: logical stacking top-to-bottom at all narrow viewports; no truncation or overlap at 320px

**Deductions:**
- Centered text >4 lines: −0.3
- Visual clutter / no focal path: −0.4
- Template with no nuance: −0.3
- Poor mobile stacking / illogical column order: −0.3
- Content truncated or overlapping at 320px: −0.3
- Promotional CTA in footer: −0.2
- >2 animations: −0.2
- Nav bar without metric justification: −0.2
- Inconsistent font sizes across sections: −0.2
- Auto-linked phone numbers, dates, or addresses rendering as blue underlined text: −0.2 (layout and palette break; the craft gap is scored in Pillar 2)
- Variable CTA sizes within same email: −0.2
- Ghost CTA as primary (no fill, no color): −0.3; unclear secondary ghost: −0.2
- Pill shapes used as non-clickable section labels: −0.2
- CTA placed too close to footer (criminal proximity): −0.2
- Single trend element repeated 3+ times throughout: −0.2 (which elements currently count as trend rather than choice is listed in Current-Era Calibration)
- All-caps as dominant typographic treatment: −0.2

**Positive design signals:**
- Visual depth / perspective / layering
- High-contrast color combinations
- Z-pattern layouts with intentional color blocking
- Live text with web fonts throughout
- Mobile reflows or different images for narrow viewports
- Dark mode with full outlining / border treatment
- In-email interactivity (checkbox hack, carousels, CSS card flips) — reward for: does it work, is the fallback acceptable, does it serve the content
- Data visualization (stats, charts, wrapped formats) — rare and high-value, credit generously
- Character-led / illustration-forward design — distinctiveness signal when applied with design discipline
- Editorial display typography (serif headlines, oversized display, type-as-concept)
- Earth / muted / natural tones as intentional brand system — "quiet luxury" crossing from fashion into SaaS
- Glassmorphism / frosted-layer depth — positive when used intentionally
- 3D floating / depth product photography
- Cinematic widescreen / letterbox hero treatments
- Varying structural rhythm within a single email
- B2B product screenshots / dashboard visuals as primary hero ("show the product")
- Hover effects on CTAs

**Trend elements — the general rule:** A widely-adopted visual treatment is not a distinctive positive on its own. What earns credit is how it combines with hierarchy and whitespace. A treatment used as an accent is positive; the same treatment used as the entire design strategy is neutral-to-negative. See Current-Era Calibration for which treatments are currently ubiquitous.

**Product photography as hero**: Positive when the image does conceptual work and copy is disciplined. Strong image + weak copy: don't compensate.

**The "cover the logo" test**: If brand can't be identified with the logo hidden, the email fails cohesion → Interchangeability Cap (×0.95, final ≤4.2).

**The "cover the hero" test**: If the email still communicates its core value without the hero, the hero may be dead weight — quieter heroes frequently outperform elaborate ones when the hero competes with the subject line's implied promise. If the email collapses without it, the hero is doing structural work — reward accordingly.

**Retail Density Safeguard**: High-SKU emails are NOT penalized for density alone. Evaluate on hierarchy control, CTA clarity, and prioritization logic.

**Contextual Brand Evaluation**: Luxury and high-fashion brands operate within tight creative constraints. Precise, blocky, restrained execution can be excellent in context — evaluate distinctiveness relative to their brand parameters.

---

## Pillar 2: Accessibility & Technical Craft (20%) — Editorial

Measures execution quality, usability, and inclusiveness. Craft is non-negotiable.

| Signal | Strong (4–5) | Weak (1–2) |
|--------|-------------|------------|
| **Color contrast** | Meets WCAG AA everywhere | Light gray on white, ghost buttons |
| **Mobile readability** | ≥16px body, comfortable at arm's length | Requires zooming, tiny text |
| **Tap targets** | ≥44×44px, generous spacing | Tiny links, adjacent overlapping taps |
| **Text discipline** | Left-aligned body, short paragraphs | Centered walls of text |
| **Alt text** | Appropriate by image type, empty on decorative | Missing or generic on everything |
| **Dark mode** | Backgrounds invert, text legible, element definition preserved | Invisible text, broken backgrounds |
| **Footer** | Unsub prominent and functional, postal address present | Unsub buried, wall of fine print |
| **Line height** | Consistent, readable spacing throughout | Overlap or inconsistency across clients |
| **Animation fallback** | First GIF frame is meaningful and legible | First frame blank or mid-transition |

**Footer scoring is mechanical, not legal.** Score whether the unsubscribe is present, findable, and functional and whether the postal address is there. Do not score compliance conformance — requirements differ by jurisdiction and are out of scope. See What This Skill Does Not Rule On.

**Mobile note:** Mobile readability and tap targets are scored here as usability concerns. Mobile layout and stacking are scored in Pillar 1. Both apply independently.

**Dark mode — ask this first:** Is dark mode targeted at all? Check `<head>` for both opt-in metas: `<meta name="color-scheme" content="light dark">` and `<meta name="supported-color-schemes" content="light dark">`. The answer changes the scoring:

- **Both present** — the email declares dark-mode support. Inversion failures are craft failures. Score them.
- **Both absent** — dark mode was never targeted; clients will auto-handle it, usually by force-inverting. Note the gap, but deduct only where legibility actually breaks. Absence is a maturity signal, not a defect in itself.
- **Only one present** — incomplete opt-in. The email is asking for behavior it hasn't fully declared. −0.1 as a craft-hygiene gap.

**Fixed-dark vs. adaptive elements:** Distinguish elements that are *already dark and must render identically* (fixed-dark — typically a gradient rendered as a solid with a blend-mode wrap) from elements that are *light by default and deliberately invert* (adaptive — driven by a dark-mode class). The techniques are mutually exclusive. Mixing them on the same element is a craft failure that produces unpredictable results across clients: −0.2.

**Dark mode — failure taxonomy:**
- Dark logo on transparent background → vanishes in forced dark mode. Apply −0.3.
- Forced color inversion (Gmail Android, Samsung native): No `prefer-color-scheme` handling = fully exposed. Note unless legibility is impacted.
- Samsung-specific rendering: Heuristic inversion not simulatable in Litmus/EoA — requires real-device testing. Note as craft gap.
- ESP `<head>` access: Drag-and-drop ESPs without `<head>` access can't implement dark mode overrides — relevant context when evaluating ambitious execution against tool constraints.

**Dark mode is a maturity marker, not a bonus** — see Current-Era Calibration.

**True black / true white as dark mode risk**: Pure #000000 and #FFFFFF often hinder dark mode rendering — email clients may not invert them predictably, or the harsh contrast creates legibility issues in forced dark mode. Near-black (#1a1a1a, #222222) and near-white (#f5f5f5, #fafafa) tend to produce more reliable results across clients. Flag true black/white in dark-mode-aware evaluations.

**Interactive email credit calibrates over time** — see Current-Era Calibration.

**Technical hygiene:**
- **Gmail clipping (~102 KB)**: Gmail truncates the message past roughly 102 KB of HTML and hides the remainder behind a "View entire message" link. What gets cut is the bottom of the email — footer, unsubscribe, postal address, and often the closing CTA — and tracking pixels below the cut never fire, so the send's own open data understates reality. Treat the budget as <90 KB.
  - Over ~102 KB → −0.4 and flag as a structural failure. If the unsubscribe falls below the cut, treat it as absent and score the footer signal accordingly — that combination will usually pull this pillar under 3.0, which triggers the Accessibility Hard Cap on its own.
  - 90–102 KB → −0.2, at risk. Any late-stage copy addition pushes it over.
  - Bloat is usually the cause, not content: reflexive Outlook ghost tables, deep table nesting, inline styles pasted in from a document, unused CSS.
- Single H1: Multiple H1s = structural confusion → −0.2
- Language attribute (`lang="en"`): Missing = minor gap; deduct only when compounding other a11y issues
- Mobile stacking order: CTA before value prop = structural failure
- Illegible text or unusable tap targets at 320px → −0.3 (layout truncation/overlap at 320px is a Pillar 1 deduction — score the usability consequence here, the layout failure there)
- **Character encoding**: Missing `<meta charset="utf-8">` risks mojibake — curly quotes, em dashes, accented characters, and emoji rendering as garbage after copy moves design → code → ESP. Missing declaration = −0.1; visible mojibake in the rendered email = −0.3.
- **Auto-link suppression**: iOS and Gmail auto-detect phone numbers, dates, and addresses and re-render them as blue underlined links, overriding the type color and breaking layout. Suppression (`x-apple-data-detectors`, `#MessageViewBody`, `format-detection`) is basic craft when the email contains any of those content types. Absent and visibly firing → −0.2 here, plus the Pillar 1 layout deduction.
- **Merge-tag fallbacks**: Every personalization token needs a default. "Hi ," or a raw `{{first_name}}` reaching the inbox is the most visible failure in email and it lands on the highest-attention line. Missing fallback on any token → −0.3. This is the mechanical counterpart to the personalization *strategy* scored in Pillar 5 — a well-targeted merge that renders empty still fails here.

**Alt text by image type:**

| Type | Correct approach |
|------|-----------------|
| Graphical text | Replicate the embedded text (never ALL CAPS) |
| Informative | Brief description of information |
| Decorative | Empty `alt=""` (NOT missing — empty) |
| Complex | Brief generalization or empty if surrounding text covers it |
| Groups | Descriptive on first, empty on rest |
| Dynamic | General description of the element |

**Alt text as narrative flow:** Alt text isn't just per-image accuracy — it's a sequential reading experience. When consumed via screen reader, the alt text across all images should create a coherent narrative in the context of surrounding live text, like an audiobook. If a description breaks the flow of the content's argument or story, it's either unnecessary (mark decorative) or poorly written. Evaluate: does the alt text sequence make sense read aloud in order? Unnecessary alt text wastes a screen reader user's time — one of the golden rules of email is never waste your audience's time.

**Alt text failure patterns:**
- Auto-generated filenames as alt ("IMG_3847.png"): Worse than missing. Apply −0.3.
- Generic alt everywhere ("image", "photo"): −0.2
- Missing entirely (no `alt` attribute): −0.2 per instance, max −0.5

**GIF scoring:**
- Fewer frames = better craft — technical discipline signal
- Key content (CTA, primary offer) must never be in the last frame — behavioral failure if it is
- >2 promotional GIFs or any GIF >500kb: flag for load impact
- Always check: is there a legible fallback for non-animating clients (Outlook)?

**All-image emails** (no live HTML text): Mechanical rule — Pillar 2 cannot exceed 2.9 for an all-image email, which forces the Accessibility Hard Cap (final ≤3.4). No screen reader path, no image-off fallback, and no progressive loading is not a style choice; it's a structural exclusion of readers. Enforce this ceiling in the pipeline, not just in reasoning. See Current-Era Calibration for trajectory.

**Live text recognition**: Call out explicitly as a foundational craft signal, especially in fashion and luxury where it remains rare.

**Promo codes as image text**: Cardinal sin — if images don't load, offer is inaccessible. Apply −0.3.

**⚠️ Accessibility Hard Cap**: If this pillar <3.0, final score cannot exceed 3.4. An email that fails accessibility does not belong in the "Competent" band. Enforced server-side only — models fail to self-apply this cap.

---

## Pillar 3: Copy & Message Discipline (20%) — Editorial

Scores what the words say and how they sound. What they make you do is Pillar 4.

| Signal | Strong (4–5) | Weak (1–2) |
|--------|-------------|------------|
| **Subject line** | Specific, compelling, earned urgency | Generic, spammy, misleading |
| **Preheader** | Extends subject, adds information or intrigue | Repeats subject, "View in browser", missing |
| **Headline / hook** | Immediately communicates value | Buried lede, unclear purpose |
| **Body copy** | Concise, scannable, benefit-focused | Verbose, jargon-heavy, feature-dumping |
| **CTA text** | Clear action, brand voice, specific | "Shop Now", "Click Here", vague |
| **Tone & voice** | Distinctive, recognizable without the logo | Generic corporate, tone-deaf |
| **Specificity** | Concrete details, real numbers, named outcomes | Vague promises, filler adjectives |
| **User-centricity** | Written from recipient's perspective | Company-focused ("we want to help you…") |

**Deductions:**
- Clichés / filler: −0.3
- Empty urgency without real scarcity: −0.2
- Overwritten paragraphs: −0.2
- Company-focused onboarding copy: −0.3
- Excessively long / multi-line CTAs: −0.2
- Generic CTA copy ("Shop Now", "Learn More", "Click Here"): −0.2
- Wasted preheader (repeats subject, "View in browser", truncated, missing): −0.2

**Sender name / from address**: Part of the inbox impression. "noreply@" on relationship-building emails (welcome, re-engagement, feedback requests) is a strategic contradiction — flag in P3 and P5. Human name vs. generic brand name affects trust.

**Subject line signals** (from RGE Awards research):
- Casual > formal: Subject lines that feel like a text from a friend outperform polished corporate phrasing.
- Curiosity with payoff: Intrigue only works if the email delivers. Flat hero after an intriguing subject line = behavioral failure.
- Softer urgency: Conversational nudges ("Almost gone…") outperform hard-sell pressure ("Buy now!").
- Specificity beats vagueness: "Friday = 50% off your drink" > "Don't miss our weekend sale."

**Subject → opener payoff contract**: The first visible sentence in the email should answer or deliver on the subject line's promise. A question in the subject line demands an answer in the opener. An intriguing tease demands a payoff. Evaluating this as a unit — subject line, preheader, and opening sentence as a three-part contract with the reader — is more useful than scoring each element in isolation.

**Preheader**: Should extend the subject line — add value, tease detail, complete the thought. A preheader that feels like a deliberate second sentence earns credit. One that defaults to body text fallback loses −0.2.

**AI Slop Indicators** (auto-rejection when multiple appear together):

*Formatting patterns:*
- Emojis at the start of every sentence, bullet, or paragraph
- Excessive bullet points replacing prose that should flow as sentences
- Every section ends with a question ("Ready to get started?")
- Headers for every short paragraph — over-structured, no narrative flow

*Copy patterns:*
- Excessively long CTAs ("Click here to discover how our revolutionary platform can transform your business")
- Generic mission-speak ("we want to help you", "we're on a mission to", "we believe that")
- Filler openers ("In today's fast-paced world…", "We're excited to share…", "We're thrilled to announce…")
- Vague benefit stacking ("powerful, intuitive, seamless, best-in-class")
- Copy that could belong to any brand in the category — no voice, no specificity, no point of view
- Overuse of "game-changer", "revolutionize", "transform", "unlock", "elevate", "unleash"
- Listicle copy that summarizes features without naming outcomes ("✅ Easy to use ✅ Saves time ✅ Grows your business")

*Structural patterns:*
- PS line that's longer than the email body
- Three separate CTAs all asking for different things at equal visual weight
- Social proof block with no specificity ("Loved by thousands of customers worldwide")
- Testimonial that could have been written by the brand ("This product changed my life!" — no name, no context)

Single signals → pillar deductions. Clusters of 3+ → strong rejection indicator.

**Onboarding copy**: Center the recipient's outcomes, not the company's mission. Front-loading too much information causes overwhelm and early churn. The strongest welcome emails: (1) show a progress indicator, (2) present max 3 steps, (3) include at least one in-product visual creating inbox-to-product continuity.

**Expert audience register**: Specialist audiences (B2B SaaS, medical, industrial, financial) are hostile to hype. Does the copy trust its reader? Subject lines that spark curiosity without dumbing down outperform generic value-prop openers.

**Voice of the customer**: Copy that mirrors how the audience actually talks — not how the brand talks — is a P3 positive. This includes vocabulary: customer-facing language ("deploy", "send", "ship") outperforms internal jargon externalized ("export", "push", "leverage"). When copy reads as written for the brand rather than the reader, flag in both P3 and P5.

**Fake interactivity**: Quiz-style patterns that simulate choices without delivering real personalization are manipulative. Apply −0.3 when interactive framing is used purely for click tracking with no genuine outcome differentiation.

**Deceptive subject lines — trust violation**: Subject lines that mimic transactional or security alerts for promotional purposes (e.g., "Fraud Alert" for a sale extension, "Your account needs attention" for a marketing email) are a severe trust violation. This isn't clever copywriting — it's exploiting anxiety for opens. Beyond the ethical failure, it carries legal risk in some jurisdictions. Apply −0.5 in P3 and flag as a rejection-level concern in P5 (strategic self-harm). Doubling down in the preheader (making both the subject and preheader alarming with no tonal relief) compounds the violation.

---

## Pillar 4: Behavioral Leverage (20%) — Performance

Scores what the email makes you do. How it sounds is Pillar 3. Psychological precision beats intensity.

| Signal | Strong (4–5) | Weak (1–2) |
|--------|-------------|------------|
| **Tension** | Names specific pain the reader recognizes | Generic feature announcement |
| **Friction removal** | One dominant CTA, simplified next step | Multiple equal asks, high cognitive load |
| **Objection handling** | Proactively addresses hesitation, risk reversal | Ignores why someone would say no |
| **Motivation** | Concrete outcome, logical urgency with real constraint | Vague value prop, artificial "HURRY!" |
| **Reframing** | Shifts how reader sees the category or decision | No perspective shift |
| **Focus** | One primary behavior, everything supports that action | Fragmented: newsletter + sale + survey + referral |

**Link economy**: Max 3 link clusters for promotional emails (one primary + two secondary). Apply −0.2 per additional cluster beyond 3 for promotional sends.

**Carve-outs:**
- **Newsletters**: Exempt from link economy limits.
- **Product grid emails**: Individual product links within a structured grid are navigation, not competing CTAs. Evaluate on hierarchy control and CTA clarity, not raw link count. Apply Retail Density Safeguard alongside.

**What Behavioral Leverage is NOT**: Button repetition, CTA volume, discount size, emotional exaggeration, aggressive countdowns.

**Scoring guidance** (most emails cluster 3.0–3.9; behavioral leverage is the second-most-common weak pillar at ~34% of emails):

- 5.0: Decision path engineered from subject line to CTA with no wasted steps.
- 4.5–4.9: Sophisticated psychology (anchoring, loss aversion, commitment/consistency) serving the reader's decision.
- 4.0–4.4: Strong primary action, minor dilution from one secondary element.
- 3.5–3.9: Clear value prop, surface-level strategy — generic urgency, generic social proof, CTA that asks without earning.
- 3.0–3.4: Informational but not motivational. CTA exists but is perfunctory.
- 2.0–2.9: Actively works against conversion — competing CTAs, high cognitive load, manipulative tactics.
- <2.0: Pure announcement with no action path.

**Personalization depth** (scoring tiers):
- First-name substitution: Table stakes — neither adds nor subtracts
- Behavioral personalization (specific viewed items, quiz results, usage data, consultation context): Meaningful lift
- Personalized data visualization (wrapped formats, progress summaries, account milestones): High-value — credit generously
- Personalized GIF / dynamic visual (recipient-specific animation using behavioral data): The most technically demanding tier. Evaluate on: (a) does the personalization feel natural vs. gimmicky, (b) is GIF weight acceptable, (c) is it genuinely delightful or merely mechanical

Gold standard: "Invisible personalization" — emails where personalization reads like a human colleague wrote it based on real knowledge of the recipient.

**Depth-choice CTA pattern**: Emails that offer a low-context CTA early (for readers who already know what they want) followed by deeper context and a second CTA further down (for readers who need more information) respect different decision speeds within the same audience. This is a behavioral sophistication signal — it acknowledges that not every reader needs the same amount of persuasion. Credit in P4 when the two CTAs serve the same action at different commitment levels, rather than competing asks.

---

## Pillar 5: Strategy & Monetization Intelligence (15%) — Performance

| Signal | Strong (4–5) | Weak (1–2) |
|--------|-------------|------------|
| **Funnel fit** | Appropriate for lifecycle stage | Wrong tone for the moment |
| **Next step** | Obvious post-CTA journey | Dead end, no journey sense |
| **Activation** | Drives first meaningful action | Feature dump, no action path |
| **Retention** | Reinforces habit, builds switching cost | One-and-done, no stickiness |
| **AOV / cross-sell** | Intelligent bundling, complementary recs | Random product grid |
| **Monetization** | High-leverage action encouraged | Low-value action presented as high-value |

**Split**: Funnel Fit (5%) + Monetization Leverage (10%).
**Default cap**: Cadence-driven sends with no strategic angle → max 3.5.

**Note on pillar weight**: 15% because strategy is often inferred rather than directly observable. Lower weight ≠ lower importance — strategic failure can still trigger caps and gates that suppress the final score significantly.

**Incomplete observability default**: 3.0 when lifecycle stage, sequence position, or segmentation logic can't be inferred. Note the assumption. Never fabricate strategic intent to fill a gap.

**Language-to-audience mismatch**: Brand-preferred terminology instead of customer language = strategic positioning failure (flag in P5) and copy voice failure (flag in P3).

**Trigger logic**: Does the triggered email make sense for the moment? An email that works equally well as batch-and-blast is strategically weak as a triggered send. Timing is often more impactful than copy perfection — a well-timed triggered email earns Strategy credit even with imperfect copy. An untimed blast with excellent copy still gets penalized.

**Campaign strategy benchmarks** (from observed scoring data):
- Educational / value-first (guides, research, behind-the-scenes): avg ~3.4
- Discount-led (discount as primary concept): avg ~3.0
- Authority-positioning (surveys, benchmarks, clinical proof, expert positioning): Positive signal when credibility is substantiated, not just asserted
- Founder / transparency campaigns: Score well on P3 (voice) and P5 (relational positioning) when voice is genuine
- Personalization / consultation flows: One of the few campaign types where strategy and design quality visibly reinforce each other
- Discount alone = table stakes. Discount earned through trigger logic (consultation abandonment, browse signal) = strategic positive

**Email as a cross-functional signal**: Messaging that resonates in email should inform landing pages, ads, and product copy. When an email demonstrates awareness of this loop — tight subject line → hero payoff → CTA → landing page alignment — score generously on Strategy.

**Seasonal hook**: Does the seasonal angle connect to the brand's actual purpose, or is it a theme applied to unrelated content? Macro-seasonal with no genuine brand angle = low Strategy.

**Preference management**: A preference center linked from the footer — topic, frequency, or format choice instead of binary subscribe/unsubscribe — is a lifecycle sophistication signal. Credit it when it's visible in the email.

**Program-level signals**: Campaign-to-flow revenue balance, onboarding sequence length, send cadence discipline, and seasonal calendar ownership are diagnostics for a *program*, not an email. They live in `references/program-maturity.md`. Load it only when you actually have that context — a program audit or multi-email teardown. Scoring a single email, apply the incomplete-observability default of 3.0 and note the assumption. Never infer program maturity from one send.

**Data-highlight formats** (year-in-review, usage recaps, progress summaries): Score high on personalization and behavioral leverage when the data earns its place. Key question: is the data genuinely surprising or useful to *this* recipient, or is it filler dressed up as personalization?

---

## Modifiers

| # | Modifier | Range | Trigger |
|---|----------|-------|---------|
| 1 | **Distinctiveness** | ×0.95 / ×1.00 / ×1.05 | Three tiers: Interchangeable, Ownable, Forward |
| 2 | **Lifecycle Coherence** | ×1.00 to ×1.05 | Personalization, segmentation intelligence, system thinking |
| 3 | **Commercial Courage** | +0.00 to +0.30 | Bold stance, category reframing, seasonal trope rejection |
| 4 | **Screenshot Worthy** | +0.00 to +0.20 | At least one moment worth saving to a swipe file |

**Justification requirement**: Every non-default modifier (anything other than ×1.00 / +0.00, plus the ×0.95 Interchangeable tier) must be accompanied by a one-sentence justification naming the specific element that triggered it — the quoted subject line, the described visual moment, the observed trigger logic. If you cannot point to the element, the modifier is the default. This is the enforcement mechanism for the frequency targets below: neutral must be the path of least resistance.

### Distinctiveness — Three Tiers

| Tier | Multiplier | Definition |
|------|-----------|------------|
| **Interchangeable** | ×0.95 | Swap the logo with a competitor's and the email still makes sense. Template energy. Triggers Interchangeability Cap (final ≤4.2) and Gallery Gate. |
| **Ownable** | ×1.00 | Recognizable brand identity — consistent palette, voice, structure — but not pushing the category forward. Neutral default. |
| **Forward** | ×1.05 | Genuinely un-swappable AND ahead of the category. The industry will study it. Not just distinctive for this brand — pointing toward where the category is going. |

Forward craft floor: Do not apply ×1.05 when weighted craft score is below 3.8. If concept is forward but craft isn't, score Ownable and note the concept positively.

Frequency targets: ~10–15% Forward, ~70–75% Ownable, ~10–15% Interchangeable. Scoring data showed ~22% Forward — that's too high. Recalibrate if consistently exceeding these ranges.

### Lifecycle Coherence (×1.00 to ×1.05)

Award when the email demonstrates awareness of where the recipient is in their journey. ×1.01–1.02 for light personalization; ×1.03–1.05 for genuine system thinking (triggered, segmented, sequenced). Default to ×1.00 when context is unobservable.

Scoring data showed ~48% receiving this modifier — implausible unless context was inferred. Cross-check against Handling Incomplete Observability.

### Commercial Courage (+0.00 to +0.30)

Reserve for emails that take a real creative or strategic risk: rejecting a seasonal convention, staking out a contrarian position, making a bold aesthetic choice most brands wouldn't. +0.10 for a notable moment; +0.20–0.30 when the risk is the concept. Do not award for merely being different — risk must be deliberate and legible.

Craft floor: Weighted craft below 3.8 → courage bonus should almost never apply. Frequency target: <10% of emails. Scoring data showed ~35% — that's a participation trophy. Recalibrate.

### Screenshot Worthy (+0.00 to +0.20)

Award when there's at least one element a marketer or designer would screenshot for their swipe file — a brilliant subject line, clever visual moment, unexpected structural move. +0.10 for one strong moment; +0.20 for multiple. Does not imply overall quality — a competent email can earn this; an ambitious email can miss it.

---

## Caps & Gates

| | Trigger | Effect |
|--|---------|--------|
| **Accessibility Hard Cap** | A11y pillar <3.0 | Final ≤3.4 |
| **Interchangeability Cap** | Distinctiveness ×0.95 | Final ≤4.2 |
| **Gallery Gate** | Distinctiveness ×0.95 | Not recommended for gallery/archive |
| **CFO Gate** | Score approaching 4.5+ | Must meet both conditions below |

### Gallery Gate

Ownable (×1.00) or Forward (×1.05) required for RGE gallery inclusion. Interchangeable emails are not gallery-worthy regardless of craft score — the gallery exists to showcase work worth studying, not competent templates.

Scoring data: The single biggest predictor of human approval vs. denial is distinctiveness (gap of +1.14 between approved and denied), far exceeding any individual pillar gap (~0.25–0.30 each). The Gallery Gate makes this implicit human filter explicit. It is an editorial filter, not a score modifier — it does not change the final score.

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

**Effective range**: 3.0–~4.8. That's a 1.7-point usable window — granularity matters.
- 0.1 difference: minor real gap (one additional deduction, one missing signal)
- 0.2 difference: meaningful, visible comparing two emails side by side
- 0.3 difference: crosses a band boundary — should be clearly articulable

**Calibration rule**: If two scorers disagree by >0.3, compare pillar scores to find the divergence. The disagreement will almost always be traceable to one or two pillars.

**Expected distribution** (based on ~460 emails): 5–7% Exceptional, 5–7% Elevated, 15–18% Teachable, 18–22% Strong, 16–19% Competent, 20–23% Below, 10–13% Reject. Top-heavy (>15% at 4.4+) = inflating. Bottom-heavy (>30% below 3.0) = too harsh.

**Actionability standard**: Every score below 4.0 should carry at least one concrete, specific improvement. Rubric-driven scoring is only better than generic AI feedback when the feedback is specific enough that a sender knows exactly what to change.

---

## Email Type & Category Scoring Context

The RGE taxonomy organizes emails into type categories and industries. Scoring should account for which type is being evaluated — the job of a Transactional email is fundamentally different from a Promotional one, and criteria for success differ accordingly.

### Type Categories

**Behavioral** (Abandoned Cart, Browse Abandonment, Engagement, Feedback/Survey, Follow-Up, Personalized, Product Recommendations, Referral, Review/Testimonial, Winback, etc.): Evaluate primarily on whether trigger logic is sound, personalization is genuine, and behavioral architecture is sophisticated. These emails are scored as Lifecycle/Triggered for weight adjustment purposes.

**Enhancement** (GIF, Interactive, CSS Animation, Gamification, Dark Mode, Video, Web Fonts, etc.): Enhancement categories are signals to look for within emails — not primary types for weight adjustment. When an email is tagged as "Interactive," reward technical execution generosity and evaluate: does the interaction work, is the fallback acceptable, does it serve the content?

**Informational** (Newsletter, Report, Infographic, Case Study, Webinar, Course, How-To, Educational Content, etc.): Use Newsletter/Editorial weight adjustments. The primary job is value delivery, not conversion. Lead with: is this genuinely useful, is the editorial curation distinctive, does the reader finish wanting the next one?

**Lifecycle** (Welcome, Onboarding, Post-Purchase, Retention, Upsell, Loyalty, Digest, Thank You, etc.): Use Lifecycle/Triggered weight adjustments. Evaluate each against its specific moment — a Welcome email's job is to set a relationship; a Post-Purchase email's job is to reduce buyer's remorse and plant the next action. Mismatch between email job and execution = P5 deduction.

**Promotional** (Announcement, Sale, Discount, Product Launch, Event, Coupon, Giveaway, Limited, etc.): Use default Promotional weights. The most common type in the corpus. Evaluate on both craft excellence and conversion architecture.

**Seasonal** (Holiday, Birthday, Anniversary, Black Friday, Valentine's Day, etc.): Use default Promotional weights. The primary differentiator is whether the seasonal hook is authentic to the brand or just a promotional banner. Cultural relevance beats seasonal opportunism: does the holiday hook have a real connection to the brand's purpose, or is it a theme with no content substance?

**Transactional** (Order Confirmation, Shipping, Password Reset, Cancellation, Receipt, Alert, Verification, GDPR, etc.): Use Transactional weight adjustments. Evaluate primarily on clarity, accessibility, and structural soundness. Flag when transactionals miss their strategic opportunity — the best transactionals use their guaranteed-open moment to plant a seed, deliver value, or set up the next action.

### Industry Context

Different industries carry different design norms, audience expectations, and content standards. When the industry is identifiable, load `references/industry-context.md` before finalizing pillar anchors. It covers SaaS/B2B, e-commerce/retail, fashion/luxury, beauty, health/medical, food/beverage, non-profit, and B2B content norms.

---

## Pattern Libraries

Two cross-pillar pattern sets live in `references/patterns.md` — load it on every scoring pass after setting pillar anchors:

- **Rejection patterns**: compound failure clusters that consistently produce sub-3.0 outcomes. Use to confirm low-band placement.
- **Patterns that push emails into 4.1+**: signals that separate good from great. An email hitting several is a strong 4.1–4.6 candidate. Use to justify high-band placement.

Patterns inform anchors and band sanity checks; they never replace pillar arithmetic.

---

## Output Structure: Internal vs. External

The scoring model produces two distinct outputs from a single evaluation pass. These serve different audiences with different jobs and should never be conflated.

---

### Internal Scoring Object

The internal object is the source of truth for curation, ranking, gallery decisions, and data analysis. It contains full precision and is never shown to senders.

**Schema** (the model emits everything except `calculated_final_score`, `caps_applied`, `band`, and `gallery_eligible`, which the pipeline computes — see scripts/calculate_final.py):

```json
{
  "email_type": "promotional | newsletter | transactional | lifecycle | seasonal",
  "industry": "string | null",
  "pillar_scores": {
    "design": 0.0,
    "accessibility": 0.0,
    "copy": 0.0,
    "behavioral": 0.0,
    "strategy": 0.0
  },
  "pillar_reasoning": {
    "design": {"anchor": 0.0, "deductions": [{"rule": "string", "value": -0.0}]},
    "accessibility": {"anchor": 0.0, "deductions": []},
    "copy": {"anchor": 0.0, "deductions": []},
    "behavioral": {"anchor": 0.0, "deductions": []},
    "strategy": {"anchor": 0.0, "deductions": [], "observability_default": false}
  },
  "modifiers": {
    "distinctiveness_tier": "interchangeable | ownable | forward",
    "distinctiveness_justification": "string | null",
    "lifecycle_coherence": 1.00,
    "lifecycle_justification": "string | null",
    "courage_bonus": 0.00,
    "courage_justification": "string | null",
    "screenshot_bonus": 0.00,
    "screenshot_justification": "string | null"
  },
  "all_image": false,
  "flags": ["string"],
  "weighted_craft_score": 0.0,
  "calculated_final_score": 0.0,
  "caps_applied": ["string"],
  "band": "string",
  "gallery_eligible": true
}
```

Pillar scores are 1.0–5.0 in 0.1 increments. Every non-default modifier requires its justification field populated; a null justification with a non-default value is a validation failure.

**Key rules:**
- Final score is always recalculated server-side from pillar scores + modifiers. Never use the model's self-reported final score.
- All caps and gates are server-side operations — the model produces pillar scores and reasoning; the pipeline calculates and clamps.
- Gallery eligibility is false when distinctiveness tier is Interchangeable, regardless of final score.
- Validate internal consistency: a pillar score below 1.0 alongside a final score above 4.0 is a hallucinated output — reject and re-score.

---

### External User-Facing Output

Structured around **what to do**, not what score was achieved. The overall tier label is present but subordinate — benchmarking context, not the headline.

**Four layers in order of user value:**

1. **Pre-flight list** — 2–4 specific, prioritized issues to fix before sending. Each item names the problem, explains the reader impact (not the rule violation), and offers a concrete fix. Sourced from the lowest-scoring pillar signals and highest-impact deductions.
2. **What's working** — 1–3 specific elements worth keeping or building on. Not generic praise — named.
3. **Pillar breakdown** — Five qualitative labels (not decimals), one per pillar, each with one sentence of explanation.
4. **Overall tier** — Single tier label + one sentence of framing. Appears last or as a secondary UI element.

### Writing the Pre-Flight List

**Specificity over category**: Not "Copy needs work" — "Your subject line could be from any brand in your category. It names no benefit, creates no curiosity, and earns no open."

**Reader impact, not rule violation**: Not "Your CTA is a ghost button" — "Ghost buttons don't register as clickable on mobile. Most of your subscribers will scroll past it without realizing it's an action."

**One concrete fix per issue**: Not "improve your CTA" — "Try 'Get my 20% off' or 'Start your free trial' instead of 'Learn More.'"

**Priority order = impact order**: Accessibility failures first (they suppress scores and block readers). Behavioral failures second (they reduce clicks). Copy and strategy failures third (they erode trust and positioning — compounding, rarely blocking). Design polish last.

**Cap at 4 items**: More than 4 signals the email needs a full redesign, not targeted fixes. If 6+ critical issues exist, say so directly.

---

### Mapping Internal Scores to External Pillar Labels

| Pillar score | External label |
|-------------|----------------|
| 4.5–5.0 | Excellent |
| 4.0–4.4 | Strong |
| 3.5–3.9 | Good |
| 3.0–3.4 | Fair |
| 2.0–2.9 | Needs Work |
| <2.0 | Critical |

### Mapping Final Score to External Tier

| Internal band | External tier label |
|---------------|---------------------|
| 4.7+ (Exceptional) | Gallery-Worthy |
| 4.4–4.6 (Elevated) | Excellent |
| 4.1–4.3 (Teachable) | Strong |
| 3.8–4.0 (Strong) | Good |
| 3.5–3.7 (Competent) | Fair |
| 3.0–3.4 (Below) | Needs Work |
| <3.0 (Reject) | Not Ready |

"Gallery-Worthy" is the aspirational ceiling only RGE can confer — it anchors the rating system to the gallery's credibility rather than a generic rubric. "Not Ready" is constructive rather than "Reject." Neither exposes the internal decimal score to the sender.

---

### What the External Output Should Never Include

- The raw decimal final score (3.48, 3.7, etc.)
- Pillar score decimals
- Modifier names or values (Distinctiveness, Lifecycle Coherence, etc.)
- Cap or gate language ("Accessibility Hard Cap applied")
- Band names from the internal system ("Competent", "Below Standard")
- Scoring formula or weighting references
- Comparisons to a 0–5 or 0–100 scale
- More than 4 pre-flight items
- Generic praise ("Great job on the design!")
- Generic criticism ("Copy could be stronger")



---

## Worked Example

End-to-end scoring of a hypothetical DTC skincare promotional email. Use this as the reference for arithmetic, output shape, and reasoning discipline. It doubles as a regression test: if an edit to this skill changes this example's result, the edit changed the model.

**The email**: Product launch for a vitamin C serum. Strong product photography with clear visual hierarchy and a recognizable brand palette. Distinctive, funny subject line ("Your face called. It wants this back."). Primary CTA is a ghost button; two secondary CTAs vary in size. Launch promo code is rendered inside the hero image. Dark logo on a transparent background. Alt text present but generic ("image") on all images. Preheader defaults to body text fallback. Four link clusters. No journey context observable.

**Step 1 — Type and weights**: Promotional → default weights (0.25 / 0.20 / 0.20 / 0.20 / 0.15).

**Step 2 — Pillars (anchor → deduct → clamp)**:

| Pillar | Anchor | Deductions | Score |
|--------|--------|-----------|-------|
| Design | 4.3 (clear focal path, intentional grid, cohesive palette) | Ghost primary CTA −0.3, variable CTA sizes −0.2 | **3.8** |
| Accessibility | 4.0 (live text, WCAG-passing contrast, ≥16px body) | Promo code as image text −0.3, dark logo on transparent −0.3, generic alt everywhere −0.2 | **3.2** |
| Copy | 4.5 (distinctive voice, specific subject line) | Generic CTA copy −0.2, wasted preheader −0.2 | **4.1** |
| Behavioral | 3.6 (clear value prop, surface-level strategy) | 4 link clusters, 1 over promotional max −0.2 | **3.4** |
| Strategy | 3.0 (observability default — no journey context; assumption noted) | — | **3.0** |

**Step 3 — Weighted craft**: (3.8×0.25) + (3.2×0.20) + (4.1×0.20) + (3.4×0.20) + (3.0×0.15) = 0.95 + 0.64 + 0.82 + 0.68 + 0.45 = **3.54**

**Step 4 — Modifiers (with justifications)**:
- Distinctiveness: **Ownable ×1.00** — palette and voice are recognizable, but nothing here pushes the category forward
- Lifecycle Coherence: **×1.00** — no journey context observable, default applies
- Commercial Courage: **+0.00** — competent execution, no deliberate risk
- Screenshot Worthy: **+0.10** — "Your face called. It wants this back." is swipe-file material

**Step 5 — Final**: 3.54 × 1.00 × 1.00 + 0.00 + 0.10 = **3.64**

**Step 6 — Caps and gates**: A11y 3.2 ≥ 3.0 → no hard cap. Ownable → no interchangeability cap, gallery gate passed. 3.64 < 4.5 → CFO gate not in play. No caps applied.

**Step 7 — Band**: 3.64 → **Competent** (internal) → **Fair** (external tier).

**Internal object** (as the pipeline stores it):

```json
{
  "email_type": "promotional",
  "industry": "beauty",
  "pillar_scores": {"design": 3.8, "accessibility": 3.2, "copy": 4.1, "behavioral": 3.4, "strategy": 3.0},
  "modifiers": {
    "distinctiveness_tier": "ownable",
    "distinctiveness_justification": null,
    "lifecycle_coherence": 1.00,
    "lifecycle_justification": null,
    "courage_bonus": 0.00,
    "courage_justification": null,
    "screenshot_bonus": 0.10,
    "screenshot_justification": "Subject line 'Your face called. It wants this back.' is swipe-file material"
  },
  "all_image": false,
  "weighted_craft_score": 3.54,
  "calculated_final_score": 3.64,
  "caps_applied": [],
  "band": "Competent",
  "gallery_eligible": true
}
```

**External output** (what the sender sees — no decimals, no internal band names):

> **Before you send:**
> 1. Your promo code lives inside the hero image. If images don't load, and for a chunk of your list they won't, the offer doesn't exist. Move the code to live text.
> 2. Your primary CTA is a ghost button. On mobile it won't register as clickable, and most subscribers will scroll past it. Give it a fill: "Get my serum" beats an outline.
> 3. Your preheader is body-text fallback. That's free inbox real estate doing nothing. Write a second sentence that extends the subject line's joke.
>
> **What's working:**
> - The subject line has real voice. Specific, funny, unmistakably yours. Keep writing like this.
> - Product photography hierarchy is doing genuine work: the eye lands where you want it, in order.
>
> **Pillar breakdown**: Design: Good (strong structure, undermined by CTA treatment). Accessibility: Fair (solid foundation with three fixable gaps). Copy: Strong (distinctive voice, generic CTA text). Behavioral: Fair (clear value prop, diluted by competing links). Strategy: Fair (scored on what's observable; no journey context visible).
>
> **Overall: Fair.** A good email with a great subject line, held back by fixable accessibility and CTA issues.

Note the external copy contains no em dashes. Rubric documentation uses them; sender-facing output follows RGE voice standards and does not.

---

## LLM Scoring Implementation Guidance

The division of labor is strict: **the model judges, the pipeline calculates.**

**What the model emits**: email type, industry, per-pillar anchor + itemized deductions + pillar score, modifier tiers/values with justifications, `all_image` flag, CFO gate inputs (`cfo_metric_impact`, `cfo_criteria_met`) when craft is trending high, and flags. Emit the internal object JSON per the schema above.

**What the pipeline computes**: weighted craft, modifier math, all caps and gates, final score, band, gallery eligibility, external labels. Run `scripts/calculate_final.py` on the model's output — it enforces every cap, applies the Forward craft floor, clamps the CFO gate, and maps bands. Never surface a model-written final score anywhere.

**Prompting order matters**: type first, then pillars (anchor before deductions), then modifiers, then emit JSON. Do not ask the model for a final score or band — models decide the band first and back-fill pillar scores to match. Pillar-first ordering is the defense.

**Validation (the script enforces these; know why they exist):**
- Pillar scores in 1.0–5.0. A pillar below 1.0 alongside a high final is a hallucinated output — reject and re-score.
- Arithmetic audit: anchor + deductions must reproduce the pillar score within 0.05. A pillar score that can't show its arithmetic is not auditable.
- Non-default modifiers without a populated justification field fail validation. This is the mechanical enforcement of the modifier frequency targets.
- Forward tier with weighted craft below 3.8 is auto-downgraded to Ownable.

**Known LLM failure modes this design defends against:**
- **Self-applied caps**: models describe caps correctly in reasoning, then fail to apply them in math. Hence server-side enforcement.
- **Modifier inflation**: without the justification requirement, courage bonuses hit ~35% of emails and lifecycle coherence ~48% — both implausible. Neutral must be the path of least resistance.
- **Distribution drift**: batch-check outputs against the expected distribution in Score Bands. Top-heavy (>15% at 4.4+) means inflation; recalibrate anchors, not deductions.
- **Fabricated strategy**: models invent journey context to avoid the 3.0 default. The `observability_default` field in pillar reasoning makes the assumption explicit and auditable.
