#!/usr/bin/env python3
"""
RGE Quality Index — deterministic final score calculator.

The model emits pillar scores, modifiers, and reasoning. This script does all
math, cap/gate enforcement, band mapping, and validation. Never trust a
model's self-reported final score — recalculate here and clamp.

Usage:
    python calculate_final.py input.json            # completed object to stdout
    cat input.json | python calculate_final.py      # same, via stdin
    python calculate_final.py input.json --external # also emit external labels

Input: the internal scoring object (see SKILL.md schema). Fields computed by
this script (weighted_craft_score, calculated_final_score, caps_applied, band,
gallery_eligible) may be omitted or present; they are overwritten either way.
"""

import json
import sys

WEIGHTS = {
    # seasonal intentionally maps to promotional (default) weights
    "promotional": {"design": 0.25, "accessibility": 0.20, "copy": 0.20, "behavioral": 0.20, "strategy": 0.15},
    "seasonal":    {"design": 0.25, "accessibility": 0.20, "copy": 0.20, "behavioral": 0.20, "strategy": 0.15},
    "newsletter":  {"design": 0.20, "accessibility": 0.15, "copy": 0.30, "behavioral": 0.15, "strategy": 0.20},
    "transactional": {"design": 0.20, "accessibility": 0.30, "copy": 0.20, "behavioral": 0.10, "strategy": 0.20},
    "lifecycle":   {"design": 0.20, "accessibility": 0.20, "copy": 0.20, "behavioral": 0.25, "strategy": 0.15},
}

DISTINCTIVENESS = {"interchangeable": 0.95, "ownable": 1.00, "forward": 1.05}

BANDS = [
    (4.7, "Exceptional", "Gallery-Worthy"),
    (4.4, "Elevated", "Excellent"),
    (4.1, "Teachable", "Strong"),
    (3.8, "Strong", "Good"),
    (3.5, "Competent", "Fair"),
    (3.0, "Below", "Needs Work"),
    (0.0, "Reject", "Not Ready"),
]

PILLAR_LABELS = [
    (4.5, "Excellent"), (4.0, "Strong"), (3.5, "Good"),
    (3.0, "Fair"), (2.0, "Needs Work"), (0.0, "Critical"),
]

PILLARS = ["design", "accessibility", "copy", "behavioral", "strategy"]

FORWARD_CRAFT_FLOOR = 3.8
COURAGE_CRAFT_FLOOR = 3.8
ALL_IMAGE_A11Y_CEILING = 2.9
A11Y_CAP_TRIGGER = 3.0
A11Y_CAP_VALUE = 3.4
INTERCHANGEABLE_CAP_VALUE = 4.2
CFO_THRESHOLD = 4.5
CFO_CLAMP = 4.4


def band_for(score):
    for floor, band, tier in BANDS:
        if score >= floor:
            return band, tier
    return "Reject", "Not Ready"


def pillar_label(score):
    for floor, label in PILLAR_LABELS:
        if score >= floor:
            return label
    return "Critical"


def validate(obj, errors, warnings):
    email_type = obj.get("email_type", "promotional")
    if email_type not in WEIGHTS:
        errors.append(f"unknown email_type '{email_type}'")

    scores = obj.get("pillar_scores", {})
    for p in PILLARS:
        v = scores.get(p)
        if v is None:
            errors.append(f"missing pillar score: {p}")
        elif not (1.0 <= v <= 5.0):
            errors.append(f"pillar '{p}' out of range: {v}")

    # arithmetic audit: anchor + deductions should reproduce the pillar score
    reasoning = obj.get("pillar_reasoning", {})
    for p, r in reasoning.items():
        if p not in PILLARS or "anchor" not in r:
            continue
        computed = r["anchor"] + sum(d.get("value", 0) for d in r.get("deductions", []))
        computed = max(1.0, min(5.0, computed))
        reported = scores.get(p)
        if reported is not None and abs(computed - reported) > 0.05:
            warnings.append(
                f"pillar '{p}' arithmetic mismatch: anchor+deductions={computed:.2f}, reported={reported:.2f}"
            )

    # non-default modifiers require justification
    m = obj.get("modifiers", {})
    checks = [
        (m.get("distinctiveness_tier", "ownable") != "ownable", "distinctiveness_justification"),
        (m.get("lifecycle_coherence", 1.00) != 1.00, "lifecycle_justification"),
        (m.get("courage_bonus", 0.0) != 0.0, "courage_justification"),
        (m.get("screenshot_bonus", 0.0) != 0.0, "screenshot_justification"),
    ]
    for non_default, field in checks:
        if non_default and not m.get(field):
            errors.append(f"non-default modifier without justification: {field}")

    # modifier range checks
    if not (1.00 <= m.get("lifecycle_coherence", 1.00) <= 1.05):
        errors.append("lifecycle_coherence out of range (1.00–1.05)")
    if not (0.0 <= m.get("courage_bonus", 0.0) <= 0.30):
        errors.append("courage_bonus out of range (0.00–0.30)")
    if not (0.0 <= m.get("screenshot_bonus", 0.0) <= 0.20):
        errors.append("screenshot_bonus out of range (0.00–0.20)")


def calculate(obj):
    errors, warnings, caps = [], [], []
    validate(obj, errors, warnings)
    if errors:
        return {"valid": False, "errors": errors, "warnings": warnings}

    email_type = obj["email_type"]
    scores = dict(obj["pillar_scores"])
    m = obj.get("modifiers", {})

    # all-image emails: accessibility pillar cannot exceed 2.9 (forces hard cap)
    if obj.get("all_image") and scores["accessibility"] > ALL_IMAGE_A11Y_CEILING:
        scores["accessibility"] = ALL_IMAGE_A11Y_CEILING
        caps.append("All-Image A11y Ceiling (pillar clamped to 2.9)")

    weights = WEIGHTS[email_type]
    craft = sum(scores[p] * weights[p] for p in PILLARS)

    # distinctiveness with Forward craft floor
    tier = m.get("distinctiveness_tier", "ownable")
    if tier == "forward" and craft < FORWARD_CRAFT_FLOOR:
        tier = "ownable"
        warnings.append(
            f"Forward tier downgraded to Ownable: weighted craft {craft:.2f} below {FORWARD_CRAFT_FLOOR} floor"
        )
    dist_mult = DISTINCTIVENESS[tier]

    courage = m.get("courage_bonus", 0.0)
    if courage > 0 and craft < COURAGE_CRAFT_FLOOR:
        warnings.append(
            f"Courage bonus (+{courage}) applied with weighted craft {craft:.2f} below {COURAGE_CRAFT_FLOOR} — review"
        )

    modified = craft * dist_mult * m.get("lifecycle_coherence", 1.00)
    final = modified + courage + m.get("screenshot_bonus", 0.0)

    # caps, in order
    if scores["accessibility"] < A11Y_CAP_TRIGGER and final > A11Y_CAP_VALUE:
        final = A11Y_CAP_VALUE
        caps.append("Accessibility Hard Cap (final ≤3.4)")
    if tier == "interchangeable" and final > INTERCHANGEABLE_CAP_VALUE:
        final = INTERCHANGEABLE_CAP_VALUE
        caps.append("Interchangeability Cap (final ≤4.2)")

    # CFO gate
    if final >= CFO_THRESHOLD:
        metric_ok = bool(obj.get("cfo_metric_impact"))
        criteria = int(obj.get("cfo_criteria_met", 0))
        if not (metric_ok and criteria >= 3):
            final = CFO_CLAMP
            caps.append(
                f"CFO Gate (metric_impact={metric_ok}, criteria={criteria}/6 — clamped to 4.4)"
            )

    final = max(1.0, min(5.0, final))
    band, tier_label = band_for(final)

    result = dict(obj)
    result["pillar_scores"] = scores
    result["modifiers"] = {**m, "distinctiveness_tier": tier}
    result["weighted_craft_score"] = round(craft, 2)
    result["calculated_final_score"] = round(final, 2)
    result["caps_applied"] = caps
    result["band"] = band
    result["gallery_eligible"] = tier != "interchangeable"
    result["valid"] = True
    result["warnings"] = warnings
    result["_external"] = {
        "tier": tier_label,
        "pillar_labels": {p: pillar_label(scores[p]) for p in PILLARS},
    }
    return result


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    raw = open(args[0]).read() if args else sys.stdin.read()
    obj = json.loads(raw)
    result = calculate(obj)
    if "--external" not in sys.argv:
        result.pop("_external", None)
    json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
    print()
    sys.exit(0 if result.get("valid") else 1)


if __name__ == "__main__":
    main()
