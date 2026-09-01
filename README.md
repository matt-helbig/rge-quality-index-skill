# RGE Quality Index

**Not just pretty. Persuasive.**

A five-pillar framework for scoring marketing emails, developed by
[Really Good Emails](https://reallygoodemails.com). Packaged as a
[Claude Code](https://docs.claude.com/en/docs/claude-code/overview) skill.

Every pillar is scored **1.0–5.0**, then weighted. The pillars are the whole
framework — everything else exists to keep them honest.

| | Pillar | Weight | The question it answers |
|---|---|:---:|---|
| **1** | Design & Hierarchy | 25% | Can you read it? |
| **2** | Accessibility & Technical Craft | 20% | Can *everyone* read it? |
| **3** | Copy & Message Discipline | 20% | Is it worth reading? |
| **4** | Behavioral Leverage | 20% | Does it make you act? |
| **5** | Strategy & Monetization | 15% | Should it exist at all? |

Pillars 1–3 are the **editorial** lens (65%): is this email worth archiving,
studying, or presenting on stage? Pillars 4–5 are **performance** (35%): does it
intelligently drive behavior, revenue, or retention?

---

## Pillar 1 — Design & Hierarchy (25%)

Visual structure and scroll control. Design supports the idea; it isn't
decorative filler.

| Signal | Strong (4–5) | Weak (1–2) |
|---|---|---|
| Hierarchy | Clear focal path, scannable in 3 seconds | Wall of content, no entry point |
| Scroll pacing | Rhythm between dense and breathing sections | Monotonous blocks |
| CTA prominence | Primary unmissable, secondary subordinate | Buried or competing equally |
| Typography | Deliberate pairing, readable scale | System defaults, too many fonts |
| Layout | Intentional grid, purposeful structure | Cramped, misaligned padding |
| Brand cohesion | Recognizable as this brand | Generic template energy |

**Benchmarks:** body text ≥16px · headings 22–30px · max 2–3 font families ·
CTA buttons ≥44×44px · width 600–700px · height 1500–2000px ideal, flag >3000px ·
no truncation or overlap at 320px.

**Costs the most:** visual clutter with no focal path (−0.4), centered text over
four lines (−0.3), a template applied with no nuance (−0.3).

---

## Pillar 2 — Accessibility & Technical Craft (20%)

Execution quality, usability, and inclusiveness. Craft is non-negotiable, and
this is the only pillar that can cap the entire score.

| Signal | Strong (4–5) | Weak (1–2) |
|---|---|---|
| Color contrast | Meets WCAG AA everywhere | Light gray on white, ghost buttons |
| Mobile readability | ≥16px, comfortable at arm's length | Requires zooming |
| Tap targets | ≥44×44px, generous spacing | Tiny, overlapping |
| Alt text | Appropriate by image type, empty on decorative | Missing or generic |
| Dark mode | Backgrounds invert, text legible | Invisible text, broken backgrounds |
| Footer | Unsub prominent and functional | Buried in fine print |

**Dark mode asks its question first.** Check `<head>` for both opt-in metas
(`color-scheme` and `supported-color-schemes`). If they're present, the email
declared support and inversion failures are *craft failures*. If they're absent,
dark mode was never targeted and clients will force-invert — note it, but deduct
only where legibility actually breaks. Absence is a maturity signal, not a defect.

**Mechanical checks that catch real sends:** Gmail's ~102 KB clipping threshold
(over it, the footer and unsubscribe vanish and tracking pixels below the cut
never fire), merge-tag fallbacks (`Hi ,` is the most visible failure in email and
it lands on the highest-attention line), auto-link suppression, and character
encoding.

**Two hard rules:**
- An all-image email cannot score above **2.9** here. No screen reader path is a
  structural exclusion of readers, not a style choice.
- If this pillar falls below **3.0**, the final score is capped at **3.4** — an
  email that fails accessibility doesn't belong in the Competent band.

---

## Pillar 3 — Copy & Message Discipline (20%)

What the words say and how they sound. What they make you *do* is Pillar 4.

| Signal | Strong (4–5) | Weak (1–2) |
|---|---|---|
| Subject line | Specific, earned urgency | Generic, spammy, misleading |
| Preheader | Extends the subject | Repeats it, or "View in browser" |
| Headline | Immediately communicates value | Buried lede |
| Body copy | Concise, scannable, benefit-focused | Verbose, feature-dumping |
| CTA text | Clear action in brand voice | "Shop Now", "Click Here" |
| Tone & voice | Recognizable without the logo | Generic corporate |
| Specificity | Real numbers, named outcomes | Filler adjectives |
| User-centricity | Written from the recipient's view | "We want to help you…" |

**The three-part contract.** Subject line, preheader, and opening sentence are
scored as one unit, not three. A question in the subject demands an answer in the
opener. A tease demands a payoff. Evaluating the contract beats scoring the
pieces in isolation.

**Costs the most:** clichés and filler (−0.3), company-focused onboarding copy
(−0.3), empty urgency with no real scarcity (−0.2). Deceptive subject lines that
mimic transactional or security alerts are a trust violation, not clever
copywriting — −0.5 and a rejection-level flag.

---

## Pillar 4 — Behavioral Leverage (20%)

What the email makes you do. Psychological precision beats intensity.

| Signal | Strong (4–5) | Weak (1–2) |
|---|---|---|
| Tension | Names a pain the reader recognizes | Generic feature announcement |
| Friction removal | One dominant CTA, simplified next step | Multiple equal asks |
| Objection handling | Addresses hesitation, risk reversal | Ignores why someone says no |
| Motivation | Concrete outcome, real constraint | Vague value prop, artificial "HURRY!" |
| Reframing | Shifts how the reader sees the decision | No perspective shift |
| Focus | One primary behavior | Newsletter + sale + survey + referral |

**What this pillar is not:** button repetition, CTA volume, discount size,
emotional exaggeration, or countdown timers. Intensity is not leverage.

**Link economy:** max three link clusters for promotional sends — one primary,
two secondary. −0.2 per cluster beyond that. Newsletters are exempt; product
grids are judged on hierarchy control, since grid links are navigation rather
than competing CTAs.

**Personalization is tiered.** First-name substitution is table stakes and earns
nothing. Behavioral personalization earns real lift. The gold standard is
*invisible personalization* — an email that reads like a colleague wrote it
knowing something true about you.

---

## Pillar 5 — Strategy & Monetization (15%)

Whether the email should exist, in this moment, in this sequence.

| Signal | Strong (4–5) | Weak (1–2) |
|---|---|---|
| Funnel fit | Right for the lifecycle stage | Wrong tone for the moment |
| Next step | Obvious post-CTA journey | Dead end |
| Activation | Drives a first meaningful action | Feature dump |
| Retention | Reinforces habit | One-and-done |
| Monetization | High-leverage action encouraged | Low-value action dressed as high-value |

**Weighted lowest, but not least important.** Strategy is usually *inferred*
rather than directly observed, which is why it carries 15%. Strategic failure
still triggers caps and gates that suppress the final score.

**It refuses to guess.** When lifecycle stage, sequence position, or segmentation
can't be inferred, the pillar defaults to **3.0** and records the assumption.
Fabricating strategic intent to fill a gap is worse than admitting the gap.

**Timing beats polish.** A well-timed triggered email earns credit with imperfect
copy. An untimed blast with excellent copy is penalized. An email that would work
equally well as batch-and-blast is strategically weak as a triggered send.

---

## Weights Shift By Email Type

The pillars are fixed; their weights aren't. Behavioral and Strategy *invert*
depending on what the email is for.

| Pillar | Promotional | Newsletter | Transactional | Lifecycle |
|---|:---:|:---:|:---:|:---:|
| Design | 25% | 20% | 20% | 20% |
| Accessibility | 20% | 15% | **30%** | 20% |
| Copy | 20% | **30%** | 20% | 20% |
| Behavioral | 20% | 15% | **10%** | **25%** |
| Strategy | 15% | 20% | 20% | 15% |

A newsletter lives or dies on voice, so copy carries most. A transactional email
has already gotten its action — behavioral barely matters and accessibility
carries most. A lifecycle email exists to move someone, so behavioral peaks.
Seasonal emails use promotional weights.

## Caps and Gates

Four rules stop a strong average from hiding a fatal flaw:

- **Accessibility cap** — Pillar 2 below 3.0 caps the final at 3.4
- **Interchangeability cap** — a 0.95 distinctiveness modifier caps the final at 4.2
- **Gallery gate** — gallery inclusion requires distinctiveness of 1.00 or better
- **CFO gate** — above 4.5 requires plausible metric impact plus three of six
  excellence criteria

Caps are why the pillars stay separate. Merge accessibility into design and a
beautiful, unreadable email averages its way past the gate.

## Score Bands

| Score | Internal band | What a sender sees |
|---|---|---|
| 4.7+ | Exceptional | Gallery-Worthy |
| 4.4 – 4.6 | Elevated | Excellent |
| 4.1 – 4.3 | Teachable | Strong |
| 3.8 – 4.0 | Strong | Good |
| 3.5 – 3.7 | Competent | Fair |
| 3.0 – 3.4 | Below | Needs Work |
| Below 3.0 | Reject | Not Ready |

The usable range is roughly 3.0 to 4.8 — a 1.7-point window, which is why tenths
matter. A 0.1 gap is one real deduction. A 0.3 gap crosses a band and should be
easy to say out loud.

---

## Install

```bash
mkdir -p ~/.claude/skills
cp -R skills/rge-quality-index ~/.claude/skills/
```

Then: *"Grade this email against the Quality Index"* · *"Why did this score
a 3.4?"* · *"Is this Gallery-Worthy or just Good?"*

## What's In Here

```
skills/rge-quality-index/
├── SKILL.md                    the five pillars, modifiers, caps, bands
├── references/
│   ├── patterns.md             rejection patterns + what pushes past 4.1
│   ├── industry-context.md     design norms by vertical
│   └── program-maturity.md     program diagnostics (load only with context)
└── scripts/
    └── calculate_final.py      deterministic scorer
```

Models describe caps accurately in their reasoning and then fail to apply them in
the arithmetic. The model's job is pillar scores, deductions, and modifier tiers
with justifications. `calculate_final.py` does the math, enforces every cap in
order, and clamps — standard library only, no network.

```bash
python skills/rge-quality-index/scripts/calculate_final.py scored.json --external
```

## Scope

The framework verifies **mechanics, not sufficiency**. A scored footer means the
unsubscribe works and is findable — not that the email is CAN-SPAM, CASL, or GDPR
compliant. Deliverability and ESP configuration are outside the pillars by design.

## License

Framework and documentation: [CC BY 4.0](./LICENSE). `calculate_final.py`: MIT.
Really Good Emails and "Gallery-Worthy" are trademarks; the license covers the
framework, not the brand.
