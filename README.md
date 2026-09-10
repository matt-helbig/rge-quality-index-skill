# RGE Quality Index

**Not just pretty. Persuasive.**

Most email feedback lands in one of two piles. "Looks great, ship it." Or a wall of nitpicks about a button nobody was going to click anyway.

This is what we use instead. Five pillars, real numbers, and one rule that keeps everybody honest: every review has to say what you'd actually learn from the email.

It's packaged as an agent skill, so you can point a model at an email and get the same review we'd give it.

## How we read an email

**Every review earns its lesson.**

What would another designer steal from this? Name it. Say how it works. "Looks great" is not a reason to feature something, and neither is "the brand is famous." No lesson, no feature. We'd rather say that out loud than invent one.

**Gallery merit and "should you send this" are different questions.**

Plenty of good email never makes the gallery. That's not an insult. It means the email did its job without teaching anybody anything new. We score those separately, so a decline never reads as "your email is broken."

**Every email gets judged on its own job.**

A receipt doesn't need an upsell. A newsletter can have a hundred links and be working perfectly. A password reset can be flawless and still teach nobody anything. Urgency, persuasion, and personalization are tools, not homework.

**We only deduct for what we can see.**

Findings get marked observed, inferred, or unverified. A screenshot can't tell you alt text is missing. An anchor tag can't prove the unsubscribe works. If we didn't see it, it doesn't cost you. Our blind spot is not your problem.

**Distinctiveness is about the work, not the logo.**

Cover the logo. If the voice, the imagery, and the structure still say who sent it, that's ownable. Not recognizing a brand doesn't make its email generic. Being famous doesn't make it good.

**Legibility and trust are the floor.**

A clever concept doesn't buy you unreadable body copy, buttons nobody can tap, or a subject line faking a security alert to steal an open. Cool idea. Still no.

**The model judges. The script does the math.**

Scores, evidence, and modifiers come from judgment. Every number after that comes from [`calculate_final.py`](skills/rge-quality-index/scripts/calculate_final.py), which enforces the caps and throws out arithmetic that doesn't add up. No model gets to write its own final score. They always round up.

## The five pillars

Each one scores 1.0 to 5.0 in tenths. Weights below are for promotional email and shift by type.

| Pillar | Weight | The question |
|---|---:|---|
| Design and hierarchy | 25% | Can someone follow this? |
| Accessibility and technical craft | 20% | Can everyone read it, and does it work? |
| Copy and message discipline | 20% | Do the words earn their space? |
| Behavioral leverage | 20% | Does it move anybody? |
| Strategy and monetization intelligence | 15% | Does it fit where the reader actually is? |

### 1. Design and hierarchy

Strong work gives you a focal path you can trace in about three seconds. Rhythm between the dense parts and the breathing room. One CTA you can't miss. Type somebody actually chose.

Depth, high contrast, editorial display type, illustration systems, and mobile reflows all earn credit when they serve the message.

It costs you when there's no focal path at all. When the primary button drowns in the footer next to the unsubscribe. When columns stack in an order nobody meant. When things get cut off at 320px.

Popular is not the same as distinctive. Rounded corners and a gradient as accents, fine. Rounded corners and a gradient as the whole idea is a template with better lighting.

Retail density is not a deduction. Forty products with a clear priority beats six with none.

### 2. Accessibility and technical craft

Contrast you can measure. Body text at 16px and up. Tap targets around 44px. Alt text matched to what the image is doing. Dark mode. Footer controls that work. A first GIF frame that says something. Merge tags that don't render "Hi ,". Gmail clipping at roughly 102KB.

Alt text gets read as a sequence, not one image at a time. Play it back in order alongside the live text. Does it sound like a person reading you the email, or a filing cabinet? If a description breaks the story, it's either decorative or badly written.

Two rules hit hard. Score below 3.0 and the whole email caps at 3.4. Build the entire message inside images with no live text and this pillar can't clear 2.9, which trips that same cap. A live legal footer doesn't count. Nice try.

### 3. Copy and message discipline

What the words say. What they make you do is pillar 4.

Subject line, preheader, and first sentence are one promise. Ask a question in the subject, answer it in the opener. Tease something, pay it off. Break that and the reader learns not to trust the next one.

Clichés cost. So does fake urgency, onboarding copy that's all about your mission, and a CTA that won't say where it goes.

Then there's the one that isn't a craft problem. Subject lines dressed as security alerts or shipping notices to steal an open. Maximum deduction, flagged for rejection. Tricking somebody into opening is not a win.

Generic copy gets scored as a reader problem. We don't guess how it got written, and counting emoji proves nothing.

### 4. Behavioral leverage

Precision beats volume.

Strong work names a tension the reader recognizes. Clears the path to one action. Answers the objection before it hardens. Sometimes it changes how you think about the decision entirely.

Personalization scores by depth. A first name is table stakes. Real behavioral signal is a lift. A recipient-specific data viz that lands as natural instead of creepy sits at the top.

Promotional email gets three link clusters before deductions start. Newsletters are exempt, because the links are the product. Product grids count as browsing, not competing asks.

None of this is leverage: more buttons, a bigger discount, more exclamation points, a countdown to a deadline that doesn't exist.

### 5. Strategy and monetization intelligence

Funnel fit. What happens after the click. Activation, retention, and whether the ask was worth making.

It's only 15% because you usually can't see it. When journey context isn't available, this pillar takes a 3.0 and then drops out of the math entirely, with the other four rescaled to cover it. Missing context can't help you or hurt you. Which means there's no reason to make something up, which is exactly why we built it that way.

"Because it's Tuesday" is not a strategy. Cadence sends with no angle cap at 3.5. Send frequency and campaign-to-flow balance are program questions, and one email can't answer them.

## The math

Weighted craft, times distinctiveness (0.95 interchangeable, 1.00 ownable, 1.05 forward), times lifecycle coherence. Then add bonuses for commercial courage and screenshot-worthy moments.

Every non-default modifier has to name the element that earned it. No justification, back to neutral. Bonuses are for things you can point at.

Deductions come in three sizes: 0.2 minor, 0.3 notable, 0.5 serious. No pillar drops more than 1.2 total. Stacking past that means the problem is your anchor, not the email.

| Score | Band | What the sender sees |
|---|---|---|
| 4.5+ | Exceptional | Gallery-Worthy |
| 4.0 to 4.4 | Teachable | Strong |
| 3.5 to 3.9 | Competent | Fair |
| 3.0 to 3.4 | Below | Needs Work |
| under 3.0 | Reject | Not Ready |

Clearing 4.5 takes a plausible metric impact plus three of six excellence criteria, each one documented. Interchangeable work caps at 4.2 and never reaches the gallery, no matter how clean the build.

Our editors still make the actual call. Nothing in here means an email got in.

## Try it

```bash
mkdir -p ~/.claude/skills
cp -R skills/rge-quality-index ~/.claude/skills/
```

Then just ask. "Grade this against the Quality Index." "What should I fix before I send it?"

```bash
python skills/rge-quality-index/scripts/calculate_final.py scored.json
python skills/rge-quality-index/scripts/calculate_final.py scored.json --audience=sender
python -m unittest discover -s skills/rge-quality-index/tests -v
```

Use `--audience=sender` for anything a sender reads. Labels only, no internal math. Nobody needs to see the anchor you started from.

The full rubric, scoring math, output contract, worked examples, industry notes, and pipeline guidance live in [`references/`](skills/rge-quality-index/references). [CHANGELOG.md](CHANGELOG.md) tracks anything that moves a score, and this version's numbers don't line up with older ones.

## What this doesn't do

QI reviews the email and whatever context you hand it. It won't tell you whether you're legally compliant, whether you'll land in the inbox, whether your ESP is configured right, or what you'll make. Real questions. Just not this tool's job.

## License

Framework and docs under [CC BY 4.0](LICENSE). `calculate_final.py` under MIT. Really Good Emails and "Gallery-Worthy" are trademarks, so the license covers the framework, not the brand.
