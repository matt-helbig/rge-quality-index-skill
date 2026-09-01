# RGE Quality Index

**Not just pretty. Persuasive.**

A five-pillar framework for scoring marketing emails, developed by
[Really Good Emails](https://reallygoodemails.com). It balances editorial
craft against performance intelligence, and it's built to be run by a human
reviewer or an LLM without the two disagreeing.

This repo packages the framework as a [Claude Code](https://docs.claude.com/en/docs/claude-code/overview)
skill, plus the reference libraries and the deterministic scorer that does the
math the model shouldn't be trusted with.

---

## The Five Pillars

Each pillar is scored 1.0–5.0, then weighted. Weights shift by email type.

| Pillar | Promotional | Newsletter | Transactional | Lifecycle |
|--------|:-----------:|:----------:|:-------------:|:---------:|
| Design & Hierarchy | 25% | 20% | 20% | 20% |
| Accessibility & Technical | 20% | 15% | 30% | 20% |
| Copy & Message Discipline | 20% | 30% | 20% | 20% |
| Behavioral Leverage | 20% | 15% | 10% | 25% |
| Strategy & Monetization | 15% | 20% | 20% | 15% |

A newsletter lives or dies on voice, so copy carries more. A transactional
email has already gotten its action, so behavioral leverage barely matters and
accessibility carries the most. Seasonal emails use promotional weights.

## How a Score Is Built

```
Weighted Craft Score
  × Distinctiveness Modifier      (0.95 / 1.00 / 1.05)
  × Lifecycle Modifier            (1.00 – 1.05)
  + Courage Bonus                 (0.00 – 0.30)
  + Screenshot Bonus              (0.00 – 0.20)
  → caps and gates, applied in order
```

Four caps and gates keep the number honest:

- **Accessibility cap** — a pillar score below 3.0 caps the final at 3.4
- **Interchangeability cap** — a 0.95 distinctiveness modifier caps the final at 4.2
- **Gallery gate** — gallery inclusion requires distinctiveness of 1.00 or better
- **CFO gate** — anything above 4.5 needs plausible metric impact plus at least
  three of six excellence criteria

## Score Bands

The framework keeps two vocabularies: a precise internal band for curation and
analysis, and a plainer external tier for the person who made the email.

| Score | Internal band | What a sender sees |
|-------|---------------|--------------------|
| 4.7+ | Exceptional | Gallery-Worthy |
| 4.4 – 4.6 | Elevated | Excellent |
| 4.1 – 4.3 | Teachable | Strong |
| 3.8 – 4.0 | Strong | Good |
| 3.5 – 3.7 | Competent | Fair |
| 3.0 – 3.4 | Below | Needs Work |
| Below 3.0 | Reject | Not Ready |

The usable range is roughly 3.0 to 4.8 — a 1.7-point window, which is why the
framework cares about tenths. A 0.1 gap is one real deduction. A 0.3 gap
crosses a band and should be easy to articulate out loud.

## What It Doesn't Do

The framework verifies **mechanics, not sufficiency**. Where a requirement varies
by jurisdiction, industry, or ESP, it scores whether the element is present,
prominent, and functional — it does not certify conformance. A scored footer
means the unsubscribe works and is findable, not that the email is CAN-SPAM,
CASL, or GDPR compliant.

Deliverability (SPF/DKIM/DMARC, reputation, inbox placement) and ESP campaign
configuration are outside the five pillars by design.

---

## Install

```bash
mkdir -p ~/.claude/skills
cp -R skills/rge-quality-index ~/.claude/skills/
```

Then ask Claude to grade something:

- *"Grade this email against the Quality Index"*
- *"Is this Gallery-Worthy or just Good?"*
- *"Why did this score a 3.4?"*
- *"Rewrite this CTA to be outcome-driven"*

## What's In Here

```
skills/rge-quality-index/
├── SKILL.md                        the framework
├── references/
│   ├── patterns.md                 rejection patterns + what pushes an email past 4.1
│   ├── industry-context.md         design norms by vertical
│   └── program-maturity.md         program-level diagnostics (load only with context)
└── scripts/
    └── calculate_final.py          deterministic scorer
```

### On that scorer

LLMs describe caps accurately in their reasoning and then fail to apply them in
the arithmetic. The model's job is pillar scores, deductions, and modifier
tiers with justifications. The math is not its job.

```bash
python skills/rge-quality-index/scripts/calculate_final.py scored.json
python skills/rge-quality-index/scripts/calculate_final.py scored.json --external
```

It takes the model's scoring object, recomputes the weighted craft score,
applies every cap and gate in order, maps the band, and clamps. Standard
library only, no network calls. Never ship a model's self-reported final score.

---

## License

The framework, reference libraries, and documentation are licensed
[CC BY 4.0](./LICENSE) — use it, adapt it, build on it, with attribution to
Really Good Emails. `scripts/calculate_final.py` is MIT.

Really Good Emails and the RGE gallery are trademarks of Really Good Emails.
The license covers the framework, not the brand: score with it freely, but
"Gallery-Worthy" is a designation the gallery confers.
