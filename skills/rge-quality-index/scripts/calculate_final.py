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
    python calculate_final.py input.json --audience=sender  # qualitative labels only

Input: the internal scoring object (see references/output.md). Fields computed by
this script (weighted_craft_score, calculated_final_score, caps_applied, band,
gallery_eligible) may be omitted or present; they are overwritten either way.
"""

import json
import sys
from decimal import Decimal, ROUND_FLOOR

WEIGHTS = {
    # seasonal intentionally maps to promotional (default) weights
    "promotional": {"design": 0.25, "accessibility": 0.20, "copy": 0.20, "behavioral": 0.20, "strategy": 0.15},
    "seasonal":    {"design": 0.25, "accessibility": 0.20, "copy": 0.20, "behavioral": 0.20, "strategy": 0.15},
    "newsletter":  {"design": 0.20, "accessibility": 0.15, "copy": 0.30, "behavioral": 0.15, "strategy": 0.20},
    "transactional": {"design": 0.20, "accessibility": 0.30, "copy": 0.20, "behavioral": 0.10, "strategy": 0.20},
    "lifecycle":   {"design": 0.20, "accessibility": 0.20, "copy": 0.20, "behavioral": 0.25, "strategy": 0.15},
}

DISTINCTIVENESS = {"interchangeable": 0.95, "ownable": 1.00, "forward": 1.05}

# Half-point bands. Finer slicing implied precision the rubric does not have.
BANDS = [
    (4.5, "Exceptional", "Gallery-Worthy"),
    (4.0, "Teachable", "Strong"),
    (3.5, "Competent", "Fair"),
    (3.0, "Below", "Needs Work"),
    (0.0, "Reject", "Not Ready"),
]

PILLAR_LABELS = [
    (4.5, "Excellent"), (4.0, "Strong"), (3.5, "Good"),
    (3.0, "Fair"), (2.0, "Needs Work"), (0.0, "Critical"),
]

PILLARS = ["design", "accessibility", "copy", "behavioral", "strategy"]

DEDUCTION_FLOOR = -1.2
FORWARD_CRAFT_FLOOR = 3.8
COURAGE_CRAFT_FLOOR = 3.8
ALL_IMAGE_A11Y_CEILING = 2.9
A11Y_CAP_TRIGGER = 3.0
A11Y_CAP_VALUE = 3.4
INTERCHANGEABLE_CAP_VALUE = 4.2
CFO_THRESHOLD = 4.5
CFO_CLAMP = 4.4

# The six excellence criteria named in references/scoring.md.
CFO_CRITERIA = (
    "Behavioral reframing",
    "Structural innovation",
    "Visual metaphor alignment",
    "Lifecycle intelligence",
    "High distinctiveness",
    "Strong conversion psychology",
)
CFO_CRITERIA_LOOKUP = {name.casefold(): name for name in CFO_CRITERIA}


def band_for(score):
    for floor, band, tier in BANDS:
        if decimal(score) >= decimal(floor):
            return band, tier
    return "Reject", "Not Ready"


def pillar_label(score):
    for floor, label in PILLAR_LABELS:
        if decimal(score) >= decimal(floor):
            return label
    return "Critical"


def decimal(value):
    return Decimal(str(value))


def nonblank(value):
    return isinstance(value, str) and bool(value.strip())


def number(value, low, high, *, tenths=False):
    if type(value) not in (int, float) or not low <= value <= high:
        return False
    return not tenths or decimal(value) % Decimal("0.1") == 0


def documented_criteria(evidence, errors):
    """Distinct canonical CFO criteria that are actually backed by evidence."""
    if not isinstance(evidence, list):
        errors.append("cfo_criteria_evidence must be a list")
        return None
    names = []
    for item in evidence:
        if not isinstance(item, dict) or not nonblank(item.get("criterion")) or not nonblank(item.get("evidence")):
            errors.append("each cfo_criteria_evidence entry needs a named criterion and its evidence")
            return None
        canonical = CFO_CRITERIA_LOOKUP.get(item["criterion"].strip().casefold())
        if canonical is None:
            errors.append(f"unknown CFO criterion: {item['criterion']}")
            return None
        if canonical in names:
            errors.append(f"CFO criterion counted twice: {canonical}")
            return None
        names.append(canonical)
    return names


def validate(obj, errors, warnings):
    if not isinstance(obj, dict):
        errors.append("input must be a JSON object")
        return
    email_type = obj.get("email_type", "promotional")
    if not isinstance(email_type, str) or email_type not in WEIGHTS:
        errors.append("unknown email_type")
    if "email_type" not in obj:
        warnings.append("email_type omitted; using promotional weights")

    scores = obj.get("pillar_scores")
    if not isinstance(scores, dict):
        errors.append("pillar_scores must be an object")
        return
    for p in PILLARS:
        if not number(scores.get(p), 1.0, 5.0, tenths=True):
            errors.append(f"pillar '{p}' must be a number from 1.0 to 5.0 in tenths")

    reasoning = obj.get("pillar_reasoning")
    if reasoning is None and "pillar_reasoning" not in obj:
        warnings.append("pillar_reasoning omitted: legacy score cannot be audited; new runs must include it")
    elif not isinstance(reasoning, dict):
        errors.append("pillar_reasoning must be an object")
    else:
        for p in PILLARS:
            r = reasoning.get(p)
            if not isinstance(r, dict):
                errors.append(f"missing or invalid reasoning for '{p}'")
                continue
            anchor, deductions = r.get("anchor"), r.get("deductions")
            if not number(anchor, 1.0, 5.0, tenths=True) or not isinstance(deductions, list):
                errors.append(f"invalid anchor or deductions for '{p}'")
                continue
            if any(not isinstance(d, dict) or not nonblank(d.get("rule")) or
                   not number(d.get("value"), -5.0, 0.0, tenths=True) or d["value"] >= 0
                   for d in deductions):
                errors.append(f"deductions for '{p}' require a named rule and negative numeric value in tenths")
                continue
            total = sum((decimal(d["value"]) for d in deductions), Decimal("0"))
            if total < decimal(DEDUCTION_FLOOR):
                # Stacking past the floor means the anchor was wrong, not that
                # the email is worse. Lower the anchor instead.
                errors.append(
                    f"deductions for '{p}' total {total}, past the {DEDUCTION_FLOOR} "
                    "per-pillar floor; lower the anchor rather than stacking"
                )
                continue
            computed = max(Decimal("1"), min(Decimal("5"), decimal(anchor) + total))
            reported = scores.get(p)
            if number(reported, 1.0, 5.0, tenths=True):
                # Accept a completed all-image object whose effective score was clamped.
                effective = min(computed, decimal(ALL_IMAGE_A11Y_CEILING)) if p == "accessibility" and obj.get("all_image") is True else computed
                if decimal(reported) not in (computed, effective):
                    errors.append(f"pillar '{p}' arithmetic mismatch: computed={computed}, reported={reported}")
            if "observability_default" in r and type(r["observability_default"]) is not bool:
                errors.append(f"observability_default for '{p}' must be boolean")
            if p == "strategy" and r.get("observability_default") is True and (anchor != 3.0 or deductions or reported != 3.0):
                errors.append("unobserved strategy must use anchor 3.0, no deductions, and score 3.0")

    m = obj.get("modifiers", {})
    if not isinstance(m, dict):
        errors.append("modifiers must be an object")
        return
    tier = m.get("distinctiveness_tier", "ownable")
    if not isinstance(tier, str) or tier not in DISTINCTIVENESS:
        errors.append("unknown distinctiveness_tier")
    checks = [
        (tier != "ownable", "distinctiveness_justification"),
        (m.get("lifecycle_coherence", 1.0) != 1.0, "lifecycle_justification"),
        (m.get("courage_bonus", 0.0) != 0.0, "courage_justification"),
        (m.get("screenshot_bonus", 0.0) != 0.0, "screenshot_justification"),
    ]
    for non_default, field in checks:
        if non_default and not nonblank(m.get(field)):
            errors.append(f"non-default modifier without justification: {field}")
    for field, default, low, high in [
        ("lifecycle_coherence", 1.0, 1.0, 1.05),
        ("courage_bonus", 0.0, 0.0, 0.3),
        ("screenshot_bonus", 0.0, 0.0, 0.2),
    ]:
        if not number(m.get(field, default), low, high):
            errors.append(f"{field} must be a number from {low} to {high}")

    if obj.get("all_image") is None:
        warnings.append("all_image unverified; no all-image ceiling inferred")
    elif type(obj["all_image"]) is not bool:
        errors.append("all_image must be boolean or null")
    # The CFO gate is the only route to 4.5+, so its inputs carry the same
    # evidence burden as a non-default modifier: claim it, document it.
    metric_impact = obj.get("cfo_metric_impact", False)
    if type(metric_impact) is not bool:
        errors.append("cfo_metric_impact must be boolean")
    elif metric_impact and not nonblank(obj.get("cfo_metric_hypothesis")):
        errors.append("cfo_metric_impact requires a testable cfo_metric_hypothesis")

    criteria = obj.get("cfo_criteria_met", 0)
    if type(criteria) is not int or not 0 <= criteria <= 6:
        errors.append("cfo_criteria_met must be an integer from 0 to 6")
        criteria = 0
    documented = documented_criteria(obj.get("cfo_criteria_evidence", []), errors)
    if criteria and documented is not None and len(documented) < criteria:
        errors.append(
            f"cfo_criteria_met={criteria} claims more than the {len(documented)} "
            "distinct criteria documented in cfo_criteria_evidence"
        )


def calculate(obj):
    errors, warnings, caps = [], [], []
    validate(obj, errors, warnings)
    if errors:
        return {"valid": False, "errors": errors, "warnings": warnings}

    email_type = obj.get("email_type", "promotional")
    scores = {p: decimal(obj["pillar_scores"][p]) for p in PILLARS}
    m = obj.get("modifiers", {})

    # all-image emails: accessibility pillar cannot exceed 2.9 (forces hard cap)
    if obj.get("all_image") and scores["accessibility"] > decimal(ALL_IMAGE_A11Y_CEILING):
        scores["accessibility"] = decimal(ALL_IMAGE_A11Y_CEILING)
        caps.append("All-Image A11y Ceiling (pillar clamped to 2.9)")

    # An unobservable P5 must not act as a constant that drags every score
    # toward 3.0. Drop it and rescale the observed pillars to sum to 1.0.
    weights = {p: decimal(w) for p, w in WEIGHTS[email_type].items()}
    renormalized = obj.get("pillar_reasoning", {}).get("strategy", {}).get("observability_default") is True
    scored = [p for p in PILLARS if not (renormalized and p == "strategy")]
    craft = sum(scores[p] * weights[p] for p in scored)
    if renormalized:
        # Divide once by the observed weight rather than rescaling each weight,
        # which would leave the parts summing to just under 1 and floor low.
        craft /= sum(weights[p] for p in scored)
        warnings.append(
            "Strategy unobserved: weights renormalized across the four observed pillars"
        )

    # distinctiveness with Forward craft floor
    tier = m.get("distinctiveness_tier", "ownable")
    downgraded = False
    if tier == "forward" and craft < decimal(FORWARD_CRAFT_FLOOR):
        tier = "ownable"
        downgraded = True
        warnings.append(
            f"Forward tier downgraded to Ownable: weighted craft {craft:.2f} below {FORWARD_CRAFT_FLOOR} floor"
        )
    dist_mult = decimal(DISTINCTIVENESS[tier])

    courage = decimal(m.get("courage_bonus", 0.0))
    if courage > 0 and craft < decimal(COURAGE_CRAFT_FLOOR):
        warnings.append(
            f"Courage bonus (+{courage}) applied with weighted craft {craft:.2f} below {COURAGE_CRAFT_FLOOR} — review"
        )

    modified = craft * dist_mult * decimal(m.get("lifecycle_coherence", 1.00))
    final = modified + courage + decimal(m.get("screenshot_bonus", 0.0))

    # caps, in order
    if scores["accessibility"] < decimal(A11Y_CAP_TRIGGER) and final > decimal(A11Y_CAP_VALUE):
        final = decimal(A11Y_CAP_VALUE)
        caps.append("Accessibility Hard Cap (final ≤3.4)")
    if tier == "interchangeable" and final > decimal(INTERCHANGEABLE_CAP_VALUE):
        final = decimal(INTERCHANGEABLE_CAP_VALUE)
        caps.append("Interchangeability Cap (final ≤4.2)")

    # CFO gate
    if final >= decimal(CFO_THRESHOLD):
        metric_ok = bool(obj.get("cfo_metric_impact"))
        criteria = int(obj.get("cfo_criteria_met", 0))
        if not (metric_ok and criteria >= 3):
            final = decimal(CFO_CLAMP)
            caps.append(
                f"CFO Gate (metric_impact={metric_ok}, criteria={criteria}/6 — clamped to 4.4)"
            )

    final = max(Decimal("1.0"), min(Decimal("5.0"), final))
    # Floor display precision after gates; do not round up into an unearned band.
    final = final.quantize(Decimal("0.01"), rounding=ROUND_FLOOR)
    band, tier_label = band_for(final)

    result = dict(obj)
    result["email_type"] = email_type
    result["pillar_scores"] = {p: float(v) for p, v in scores.items()}
    result["modifiers"] = {**m, "distinctiveness_tier": tier}
    if downgraded:
        # The Forward rationale no longer describes the applied tier.
        result["modifiers"]["distinctiveness_justification"] = None
    result["weights_renormalized"] = renormalized
    result["weighted_craft_score"] = float(craft.quantize(Decimal("0.01"), rounding=ROUND_FLOOR))
    result["calculated_final_score"] = float(final)
    result["caps_applied"] = caps
    result["band"] = band
    result["passes_distinctiveness_gate"] = tier != "interchangeable"
    # Compatibility alias, NOT a complete gallery recommendation.
    result["gallery_eligible"] = result["passes_distinctiveness_gate"]
    result["valid"] = True
    result["warnings"] = warnings
    result["_external"] = {
        "tier": tier_label,
        "pillar_labels": {p: pillar_label(scores[p]) for p in PILLARS},
    }
    if obj.get("pillar_reasoning", {}).get("strategy", {}).get("observability_default") is True:
        result["_external"]["pillar_labels"]["strategy"] = "Not verified"
    return result


def sender_view(result):
    """Only what a sender should see: qualitative labels, no internal math."""
    if not result.get("valid"):
        return {"valid": False, "errors": result.get("errors", [])}
    external = result.get("_external", {})
    return {
        "valid": True,
        "tier": external.get("tier"),
        "pillar_labels": external.get("pillar_labels", {}),
    }


def main():
    flags = [a for a in sys.argv[1:] if a.startswith("--")]
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    audience = "internal"
    for flag in flags:
        if flag.startswith("--audience="):
            audience = flag.split("=", 1)[1]
    if audience not in ("internal", "sender"):
        json.dump({"valid": False, "errors": [f"unknown audience: {audience}"]},
                  sys.stdout, indent=2)
        print()
        sys.exit(1)
    try:
        if args:
            with open(args[0], encoding="utf-8") as source:
                raw = source.read()
        else:
            raw = sys.stdin.read()
        def reject_constant(value):
            raise ValueError(f"invalid JSON number: {value}")
        obj = json.loads(raw, parse_constant=reject_constant)
        result = calculate(obj)
    except (OSError, ValueError) as exc:
        result = {"valid": False, "errors": [str(exc)], "warnings": []}
    if audience == "sender":
        result = sender_view(result)
    elif "--external" not in flags:
        result.pop("_external", None)
    json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
    print()
    sys.exit(0 if result.get("valid") else 1)


if __name__ == "__main__":
    main()
