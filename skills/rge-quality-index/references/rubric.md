# Five-pillar rubric

Read during a full scoring pass. Apply the evidence rules and email-type success criteria in [SKILL.md](../SKILL.md) before selecting anchors. Listed deductions apply to the described failure in context, not merely the presence of a visual or copy treatment. Positive signals are examples, not a checklist or a source of additional points.

## Pillar 1: Design & Hierarchy (25%) — Editorial

Measures visual structure and scroll control. Design supports the idea — not decorative filler.

| Signal | Strong (4–5) | Weak (1–2) |
|--------|-------------|------------|
| **Hierarchy** | Clear focal path, scannable in 3 seconds | Wall of content, no entry point |
| **Scroll pacing** | Rhythm between dense and breathing sections | Monotonous blocks |
| **CTA prominence** | Primary CTA unmissable, secondary subordinate | CTAs buried or competing equally |
| **Typography** | Deliberate pairing, readable scale | Unreadable scale, inconsistent or distracting font choices |
| **Layout** | Intentional grid, purposeful structure | Cramped, misaligned, inconsistent padding |
| **Brand cohesion** | Immediately recognizable as this brand | Generic template energy |

**Review benchmarks:** These are starting points for evaluating rendered content, not automatic failures. Judge deviations by readability, hierarchy, purpose, and the target audience. Screenshots without a known viewport do not establish CSS pixel measurements.
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
- Centered body text >4 lines that makes sustained reading difficult: −0.3
- Visual clutter / no focal path: −0.4
- Generic template execution that fails to express the message or brand: −0.3
- Poor mobile stacking / illogical column order: −0.3
- Content truncated or overlapping at 320px: −0.3
- Primary promotional action buried in the footer and difficult to find: −0.2
- Multiple animations competing for attention or disrupting reading: −0.2
- Navigation competing with the email’s primary task: −0.2. Missing analytics is not a failure.
- Inconsistent font sizes that obscure the intended hierarchy: −0.2
- Auto-linked phone numbers, dates, or addresses rendering as blue underlined text: −0.2 (layout and palette break; the craft gap is scored in Pillar 2)
- Inconsistent CTA sizes that misrepresent action priority: −0.2
- Primary outline CTA that is difficult to distinguish from surrounding content: −0.3; unclear secondary outline CTA: −0.2. Do not penalize an outline treatment that is prominent and readable.
- Non-clickable labels that misleadingly appear interactive in context: −0.2
- Primary CTA visually lost among footer utilities: −0.2. Do not also deduct for a buried footer CTA with the same root cause.
- Repeated decoration that competes with the message or weakens hierarchy: −0.2. Repetition that establishes a coherent system is not a defect.
- Extensive all-caps text that impairs reading: −0.2. Short display headlines are contextual choices.

**Positive design signals:**
- Visual depth / perspective / layering
- High-contrast color combinations
- Z-pattern layouts with intentional color blocking
- Readable live text with deliberate typography and reliable font fallbacks
- Mobile reflows or different images for narrow viewports
- Dark mode with full outlining / border treatment
- In-email interactivity (checkbox hack, carousels, CSS card flips) — reward for: does it work, is the fallback acceptable, does it serve the content
- Data visualization that makes useful information easier to understand
- Character-led / illustration-forward design — distinctiveness signal when applied with design discipline
- Editorial display typography (serif headlines, oversized display, type-as-concept)
- Color choices that support the brand and message
- 3D floating / depth product photography
- Cinematic widescreen / letterbox hero treatments
- Varying structural rhythm within a single email
- B2B product screenshots / dashboard visuals as primary hero ("show the product")
- Interaction feedback that works as progressive enhancement

**Trend elements — the general rule:** A widely-adopted visual treatment is not a distinctive positive on its own. What earns credit is how it combines with hierarchy and whitespace. A treatment used as an accent is positive; the same treatment used as the entire design strategy is neutral-to-negative. Do not infer originality or staleness from a treatment’s name alone.

**Product photography as hero**: Positive when the image does conceptual work and copy is disciplined. Strong image + weak copy: don't compensate.

**The "cover the logo" test**: Ask whether the voice, imagery, and structure express a coherent identity beyond a pasted logo. Compare with supplied brand context where available. A reviewer’s unfamiliarity with a brand is not evidence of interchangeability. Assign the Interchangeable tier only when the execution itself is generic.

**The "cover the hero" test**: Identify what the image contributes: product understanding, mood, proof, or narrative. Redundancy with live text can improve resilience. Do not reward making the essential message inaccessible when images are off.

**Retail Density Safeguard**: High-SKU emails are NOT penalized for density alone. Evaluate on hierarchy control, CTA clarity, and prioritization logic.

**Contextual Brand Evaluation**: Luxury and high-fashion brands operate within tight creative constraints. Precise, blocky, restrained execution can be excellent in context — evaluate distinctiveness relative to their brand parameters.

---

## Pillar 2: Accessibility & Technical Craft (20%) — Editorial

Measures execution quality, usability, and inclusiveness. Craft is non-negotiable.

| Signal | Strong (4–5) | Weak (1–2) |
|--------|-------------|------------|
| **Color contrast** | Measured text contrast meets the applicable AA threshold | Verified low-contrast essential text or controls |
| **Mobile readability** | ≥16px body, comfortable at arm's length | Requires zooming, tiny text |
| **Tap targets** | ≥44×44px, generous spacing | Tiny links, adjacent overlapping taps |
| **Text discipline** | Left-aligned body, short paragraphs | Centered walls of text |
| **Alt text** | Appropriate by image type, empty on decorative | Missing or generic on everything |
| **Dark mode** | Backgrounds invert, text legible, element definition preserved | Invisible text, broken backgrounds |
| **Footer** | Unsub prominent and functional, postal address present | Unsub buried, wall of fine print |
| **Line height** | Consistent, readable spacing throughout | Overlap or inconsistency across clients |
| **Animation fallback** | First GIF frame is meaningful and legible | First frame blank or mid-transition |

**Footer scoring is mechanical, not legal.** Inspect the contact and preference controls appropriate to the message's purpose. Record presence, findability, and tested functionality separately. Do not impose promotional footer expectations on every service message or certify compliance. See the scope in [SKILL.md](../SKILL.md).

**Mobile note:** Readability and tap targets belong here; layout and stacking belong in P1. Apply both only for distinct observed consequences, following the pillar-boundary guidance in SKILL.md.

**Dark mode — inspect evidence first:** Is dark mode targeted at all? Check `<head>` for both opt-in metas: `<meta name="color-scheme" content="light dark">` and `<meta name="supported-color-schemes" content="light dark">`. The answer changes the scoring:

- **Both present** — the email declares dark-mode support. Inversion failures are craft failures. Score them.
- **Both absent** — do not infer the author's intent or a specific client transformation. Inspect the target render and deduct only for an observed failure.
- **Only one present** — note the declared support and test the relevant clients. Metadata alone does not establish a rendering failure.

**Fixed-dark vs. adaptive elements:** Determine whether an element is intended to keep its appearance or change with the theme. Judge the inspected result rather than treating a particular blend of CSS techniques as inherently defective. Conflicting treatments that produce an observed rendering failure: −0.2.

**Dark mode — failure taxonomy:**
- Dark logo on transparent background that becomes illegible in an inspected dark-mode render: −0.3. Without that render, record a risk to verify.
- Forced color inversion: inspect the relevant client render. CSS support varies by client; a `prefers-color-scheme` rule alone does not establish support.
- Client-specific rendering: use an actual client test where a preview cannot reproduce the behavior. An unavailable test is unverified, not a craft defect.
- ESP constraints: Consider the supplied authoring environment when suggesting repairs; do not assume a particular setting or technique is available.

**Dark-mode readiness:** Credit verified legibility and appropriate fallback behavior. Do not infer a failure from absent opt-in metadata or a color choice alone.

**Color choices in dark mode:** Test actual foreground/background pairs after client transformations. Pure black or white is not inherently a defect; changing colors without testing is not a reliable repair.

**Interactive email:** Credit usefulness, accessibility, and fallback quality rather than technical complexity alone.

**Technical hygiene:**
- **Gmail clipping (~102 KB)**: Message code over roughly 102 KB can hide content behind a “View entire message” link. Check the delivered message where available; authoring-source size alone may differ after ESP processing. See [Mailchimp's clipping guidance](https://mailchimp.com/help/gmail-is-clipping-my-email/).
  - Verified clipping that hides essential content → −0.4. Name what is hidden. Deduct for a separate lost control only if it creates a distinct consequence; do not manufacture enough deductions to force a cap.
  - A source near or above the threshold is a risk to verify. A <90 KB authoring budget is a useful buffer, not evidence that every larger email has already failed.
- Heading structure that obscures content relationships or navigation: −0.2. Judge semantics in context rather than counting H1 elements alone.
- Language attribute (`lang="en"`): Missing = minor gap; deduct only when compounding other a11y issues
- Mobile stacking order: Essential explanation must be available before a reader needs it. An early CTA for an already-informed reader can be appropriate.
- Illegible text or unusable tap targets at 320px → −0.3 (layout truncation/overlap at 320px is a Pillar 1 deduction — score the usability consequence here, the layout failure there)
- **Character encoding**: Inspect the available message encoding and rendered output. Missing HTML metadata alone does not prove missing MIME encoding. Visible mojibake in the rendered email: −0.3.
- **Auto-linking**: Client-generated links may alter styling. Deduct −0.2 here for an observed usability failure; apply a separate P1 deduction only for a distinct layout consequence. Helpful phone or address links are not inherently defects.
- **Merge-tag fallbacks**: "Hi ," or a raw `{{first_name}}` is a visible execution failure. A token that can render empty or raw without an appropriate fallback → −0.3. Required data guaranteed by the sending system does not need a redundant fallback; inspect that context before deducting. This is separate from personalization strategy.

**Alt text by image type:**

| Type | Correct approach |
|------|-----------------|
| Graphical text | Convey the same essential words, including meaningful acronyms |
| Informative | Brief description of information |
| Decorative | Empty `alt=""` (NOT missing — empty) |
| Complex | Short identification plus a complete equivalent for the essential information, in surrounding text or an accessible description |
| Groups | Describe the shared information once only when the images genuinely form one informational group |
| Functional / linked | Describe the action or destination; include essential text |
| Dynamic | Convey the essential information and provide a usable fallback |

**Alt text as narrative flow:** Alt text isn't just per-image accuracy — it's a sequential reading experience. When consumed via screen reader, the alt text across all images should create a coherent narrative in the context of surrounding live text, like an audiobook. If a description breaks the flow of the content's argument or story, it's either unnecessary (mark decorative) or poorly written. Evaluate: does the alt text sequence make sense read aloud in order? Unnecessary alt text wastes a screen reader user's time — one of the golden rules of email is never waste your audience's time.

**Alt text failure patterns:**
- Auto-generated filenames as alt ("IMG_3847.png"): Worse than missing. Apply −0.3.
- Generic alt everywhere ("image", "photo"): −0.2
- Missing entirely (no `alt` attribute): −0.2 per instance, max −0.5

**GIF scoring:**
- Balance animation smoothness, duration, motion sensitivity, and asset weight; frame count alone does not establish quality
- Essential content must not depend only on a later frame; provide a meaningful static fallback or equivalent live text
- >2 promotional GIFs or any GIF >500kb: flag for load impact
- Always check: is there a legible fallback for non-animating clients (Outlook)?

**All-image emails:** For this rubric, set `all_image=true` when the essential message and action depend entirely on images, with no equivalent live body text. A live legal footer or hidden preheader does not satisfy that requirement. Appropriate alt text can provide a screen-reader alternative, but does not remove RGE’s editorial preference for adaptable live text. Preserve the mechanical ceiling: P2 ≤2.9, which forces final ≤3.4. Verify from source and rendered content; do not infer all-image construction from a screenshot alone. See [W3C image guidance](https://www.w3.org/WAI/tutorials/images/) for alternative-text purposes.

**Live text recognition**: Call out as a foundational craft signal when it preserves essential content and adaptability.

**Promo codes as image text**: An essential code available only in an image: −0.3. Do not deduct when an equivalent live code is present.

**Accessibility Hard Cap**: If this pillar <3.0, final score cannot exceed 3.4. The calculator enforces this numeric constraint. Explain the observed failures separately from the numerical band.

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
- CTA wording that leaves the action or destination unclear in context: −0.2. “Shop Now” or “Learn More” can be appropriate when adjacent copy makes the action specific.
- Available preheader that wastes the inbox preview or obscures the message: −0.2. A preheader not supplied for review is unverified, not missing from the email.

**Sender name / from address**: Assess clear identity and consistency with the requested action. Inviting a reply to an address that does not accept replies is a specific contradiction. A brand sender or `noreply` address alone is not a defect; score distinct copy or task failures where supported.

**Subject line judgment:** Evaluate specificity, truthful expectations, audience fit, and the payoff in the email. Casual, formal, curious, and urgent approaches can all work. Do not claim one outperforms another without relevant performance evidence.

**Subject → opener payoff contract**: The first visible sentence in the email should answer or deliver on the subject line's promise. A question in the subject line demands an answer in the opener. An intriguing tease demands a payoff. Evaluating this as a unit — subject line, preheader, and opening sentence as a three-part contract with the reader — is more useful than scoring each element in isolation.

**Preheader**: Should complement the subject line. Body-text fallback can work when the opening line serves that purpose. Deduct −0.2 when the actual preview is unhelpful; do not also deduct for the same wasted preview above.

**Generic or undisciplined copy indicators:** These are prompts for judgment, not detectors of AI authorship or automatic rejection rules. Assess whether the wording wastes attention, lacks specificity, or fails the recipient’s task.

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

Apply an appropriate listed deduction only for an observed weakness. Several stylistic indicators do not automatically reject an email; explain the resulting reader or editorial problem. Do not infer how the copy was produced.

**Onboarding copy**: Center the recipient's outcomes, not the company's mission. Front-loading too much information causes overwhelm and early churn. Progress indicators, a short set of steps, or an in-product visual can help when they serve the actual onboarding task; they are not required ingredients.

**Expert audience register**: Specialist audiences (B2B SaaS, medical, industrial, financial) are hostile to hype. Does the copy trust its reader? Look for useful specificity and an appropriate level of assumed knowledge.

**Voice of the customer**: Use the terms the intended audience understands; technical terms such as “export” may be correct for that audience. Score unclear wording in P3. Apply a P5 consequence only when there is separate evidence of audience or task mismatch.

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

**Scoring guidance for promotional persuasion:** Use the email-type success criteria in SKILL.md for informational and transactional tasks.

- 5.0: Decision path engineered from subject line to CTA with no wasted steps.
- 4.5–4.9: Sophisticated psychology (anchoring, loss aversion, commitment/consistency) serving the reader's decision.
- 4.0–4.4: Strong primary action, minor dilution from one secondary element.
- 3.5–3.9: Clear value prop, surface-level strategy — generic urgency, generic social proof, CTA that asks without earning.
- 3.0–3.4: Informational but not motivational. CTA exists but is perfunctory.
- 2.0–2.9: Actively works against conversion — competing CTAs, high cognitive load, manipulative tactics.
- <2.0: The required next step is absent or unusable. An informational message whose task is completed by reading does not require a CTA.

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

Evaluate recipient/task fit and the value of the next step together. Do not require monetization for informational, service, or transactional messages.
**Default cap**: Cadence-driven sends with no strategic angle → max 3.5.

**Note on pillar weight**: 15% because strategy is often inferred rather than directly observable. Lower weight ≠ lower importance — strategic failure can still trigger caps and gates that suppress the final score significantly.

**Incomplete observability default**: 3.0 when lifecycle stage, sequence position, or segmentation logic can't be inferred. Note the assumption. Never fabricate strategic intent to fill a gap.

**Language-to-audience mismatch**: Distinguish confusing wording from evidence that the email targets the wrong need or audience. Do not automatically turn a P3 wording criticism into a P5 deduction.

**Trigger logic**: Does the triggered email make sense for the moment? An email that works equally well as batch-and-blast is strategically weak as a triggered send. Timing is often more impactful than copy perfection — a well-timed triggered email earns Strategy credit even with imperfect copy. A scheduled broadcast can be strategically appropriate. Deduct for a demonstrated mismatch with the recipient’s task, not merely the absence of a trigger.

**Campaign strategy:** Evaluate the purpose rather than favoring a format. Educational content needs useful substance; discounts need a relevant offer; authority claims need support. Founder stories, research, and personalization earn credit only when they serve the recipient’s situation.

**Email as a cross-functional signal**: Messaging that resonates in email should inform landing pages, ads, and product copy. When an email demonstrates awareness of this loop — tight subject line → hero payoff → CTA → landing page alignment — score generously on Strategy.

**Seasonal hook**: Does the seasonal angle connect to the brand's actual purpose, or is it a theme applied to unrelated content? Macro-seasonal with no genuine brand angle = low Strategy.

**Preference management**: A visible preference link supports only the claim that a choice is offered. Credit the scope or usefulness of topic, frequency, or format controls when those controls are actually available for inspection.

**Program-level signals**: Campaign-to-flow revenue balance, onboarding sequence length, send cadence discipline, and seasonal calendar ownership are diagnostics for a *program*, not an email. They live in [program-maturity.md](program-maturity.md). Load it only when you actually have that context — a program audit or multi-email teardown. Scoring a single email, fall through to the incomplete-observability default above. Never infer program maturity from one send.

**Data-highlight formats** (year-in-review, usage recaps, progress summaries): Score high on personalization and behavioral leverage when the data earns its place. Key question: is the data genuinely surprising or useful to *this* recipient, or is it filler dressed up as personalization?
