# Pattern Libraries: Rejection Clusters and 4.1+ Signals

Load this file during any scoring pass once pillar anchors are set. Rejection patterns confirm low-band placement; 4.1+ patterns justify high-band placement. Neither replaces pillar arithmetic.

## Rejection Patterns

Compound patterns — individual issues trigger deductions; these combinations consistently produce rejection.

- **Density + layout confusion**: Overwhelming density compounded by weak hierarchy and unclear CTA priority
- **Legibility failures**: Thin text on colored backgrounds (pink, teal, navy, medium-gray) + tight line heights + inconsistent sizing — nothing else saves the email
- **AI slop cluster**: Long CTAs + emoji-heavy copy + company-focused mission-speak + no editorial voice
- **All-image with no live text**: No fallback, no screen reader path, no progressive loading
- **Structural Frankenstein**: Newsletter + sale + survey + referral with no hierarchy prioritizing any of them
- **Mobile-first failure**: Strong desktop, failed mobile execution — poor stacking, insufficient tap targets, illegible text
- **Onboarding overwhelm**: Front-loaded information, company-focused copy, cognitive overload before context exists
- **Interaction confusion**: Pill-shaped non-clickable labels, fake quiz patterns, affordances that set expectations the email doesn't fulfill
- **Header clutter**: Multiple fonts, weights, colors, treatments crammed into the header — no entry point
- **Heavy GIF load, no fallback**: Multiple large GIFs or any GIF >500kb with blank/mid-transition first frames
- **Bilingual without segmentation**: Both languages in one send without dynamic content — a workaround, not inclusive practice
- **Higher education bulletin board**: Every program, event, and notice at equal visual priority — nothing survives
- **Excessive centered text**: Walls of small centered copy + tight line heights — harms dyslexic readers

---

## Patterns That Push Emails Into 4.1+

Cross-pillar signals that consistently separate good from great. An email hitting several of these is a strong candidate for 4.1–4.6.

- **Works without images**: Core message communicates even if images don't load — live text, strong alt text, structural clarity all doing real work
- **Inbox impression fully crafted**: Subject line, preheader, and sender name work as a coherent unit — the open is earned before the email is seen
- **Smart CTA differentiation**: Color, size, and shape create unambiguous primary/secondary hierarchy
- **Storytelling with a payoff**: Real narrative (founder voice, partnership story, behind-the-scenes) that uses scrollable format to deliver, not just to show off
- **Authority content as the centerpiece**: Original research, benchmark data, or credible proof is the value proposition
- **Unmistakable brand without the logo**: Voice + palette + structure identify the brand without needing the logo
- **Mobile-first thinking visible**: Stacking, tap targets, and reflow clearly reflect mobile-first design — not afterthought adaptation
- **Personalization that earns trust**: Genuine first-party signal — quiz result, purchase history, usage data, consultation context — not just `{{first_name}}`
- **Dark mode excellence with element outlining**: Borders, outlines, and layered treatments preserve legibility — not just background inversion
- **Interactive CSS-based elements**: Functional, content-appropriate, with acceptable fallback
- **Data visualization**: Personalized or aggregate data presented visually — high-value when the data is genuinely useful to this recipient
- **Live text in fashion / luxury**: Genuinely rare in those categories — call it out explicitly
- **Character-driven design at scale**: Mascot systems applied with visual discipline — unmistakably brand-specific
- **Editorial typography as concept**: Type is the idea — oversized serifs, expressive display, deliberate pacing
