"""Behavioral checks for the scoring contract; no network or external packages."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "calculate_final.py"
spec = importlib.util.spec_from_file_location("calculator", SCRIPT)
calculator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(calculator)


def sample(score=4.0):
    return {
        "email_type": "promotional",
        "pillar_scores": dict.fromkeys(calculator.PILLARS, score),
        "pillar_reasoning": {
            p: {"anchor": score, "evidence": "Test fixture", "deductions": []}
            for p in calculator.PILLARS
        },
        "all_image": False,
        "modifiers": {},
    }


class CalculatorTests(unittest.TestCase):
    def test_documented_example(self):
        obj = json.loads((ROOT / "tests/fixtures/skincare.json").read_text())
        r = calculator.calculate(obj)
        self.assertTrue(r["valid"], r)
        self.assertEqual(r["weighted_craft_score"], 3.54)
        self.assertEqual(r["calculated_final_score"], 3.64)
        self.assertEqual(r["band"], "Competent")
        self.assertEqual(r["_external"]["pillar_labels"]["strategy"], "Not verified")

    def test_each_email_type_uses_normalized_weights(self):
        for kind in calculator.WEIGHTS:
            with self.subTest(kind=kind):
                obj = sample()
                obj["email_type"] = kind
                self.assertEqual(calculator.calculate(obj)["calculated_final_score"], 4.0)

    def test_invalid_input_types_return_errors(self):
        objects = [None, [], "text", {}, {"pillar_scores": None}]
        for field, value in [
            ("email_type", []), ("email_type", "unknown"),
            ("modifiers", None), ("pillar_reasoning", None),
            ("all_image", "false"), ("cfo_metric_impact", "false"),
            ("cfo_criteria_met", 999), ("cfo_criteria_met", 3.5),
            ("cfo_criteria_met", True), ("cfo_criteria_met", -1),
        ]:
            obj = sample()
            obj[field] = value
            objects.append(obj)
        for obj in objects:
            with self.subTest(obj=obj):
                result = calculator.calculate(obj)
                self.assertFalse(result["valid"])
                self.assertTrue(result["errors"])

    def test_pillars_require_numbers_in_range_in_tenths(self):
        for v in [True, "4", None, [], 0.5, 5.1, 4.123, float("nan"), float("inf"), 10**400]:
            with self.subTest(value=v):
                obj = sample()
                obj["pillar_scores"]["design"] = v
                self.assertFalse(calculator.calculate(obj)["valid"])

    def test_reasoning_must_reproduce_scores(self):
        obj = sample()
        obj["pillar_reasoning"]["design"]["anchor"] = 2.0
        self.assertFalse(calculator.calculate(obj)["valid"])
        for value in [True, 0, 0.2, "-0.2", float("nan")]:
            obj = sample()
            obj["pillar_reasoning"]["design"]["deductions"] = [{"rule": "issue", "value": value}]
            self.assertFalse(calculator.calculate(obj)["valid"])
        obj = sample()
        del obj["pillar_reasoning"]["copy"]
        self.assertFalse(calculator.calculate(obj)["valid"])

    def test_deductions_clamp_at_pillar_floor(self):
        obj = sample()
        obj["pillar_scores"]["design"] = 1.0
        obj["pillar_reasoning"]["design"] = {"anchor": 2.0, "deductions": [{"rule": "severe issue", "value": -2.0}]}
        self.assertTrue(calculator.calculate(obj)["valid"])

    def test_modifiers_validate_types_tiers_and_justifications(self):
        for modifiers in [
            {"distinctiveness_tier": "bogus", "distinctiveness_justification": "evidence"},
            {"distinctiveness_tier": []},
            {"screenshot_bonus": 0.1, "screenshot_justification": "   "},
            {"courage_bonus": True, "courage_justification": "evidence"},
            {"lifecycle_coherence": 1.1, "lifecycle_justification": "evidence"},
            {"screenshot_bonus": float("nan"), "screenshot_justification": "evidence"},
        ]:
            obj = sample()
            obj["modifiers"] = modifiers
            self.assertFalse(calculator.calculate(obj)["valid"])

    def test_accessibility_gate_and_all_image_ceiling(self):
        for a11y, expected in [(2.9, 3.4), (3.0, 3.8)]:
            obj = sample()
            obj["pillar_scores"]["accessibility"] = a11y
            obj["pillar_reasoning"]["accessibility"]["anchor"] = a11y
            self.assertEqual(calculator.calculate(obj)["calculated_final_score"], expected)
        obj = sample()
        obj["all_image"] = True
        r = calculator.calculate(obj)
        self.assertEqual(r["pillar_scores"]["accessibility"], 2.9)
        self.assertEqual(r["calculated_final_score"], 3.4)
        self.assertTrue(calculator.calculate(r)["valid"])
        self.assertEqual(obj["pillar_scores"]["accessibility"], 4.0)

    def test_interchangeability_and_legacy_gate_alias(self):
        obj = sample(5.0)
        obj["modifiers"] = {"distinctiveness_tier": "interchangeable", "distinctiveness_justification": "Generic execution"}
        r = calculator.calculate(obj)
        self.assertEqual(r["calculated_final_score"], 4.2)
        self.assertFalse(r["passes_distinctiveness_gate"])
        self.assertEqual(r["gallery_eligible"], r["passes_distinctiveness_gate"])

    def test_forward_floor(self):
        for craft, expected in [(3.7, "ownable"), (3.8, "forward")]:
            obj = sample(craft)
            obj["modifiers"] = {"distinctiveness_tier": "forward", "distinctiveness_justification": "Novel structure"}
            self.assertEqual(calculator.calculate(obj)["modifiers"]["distinctiveness_tier"], expected)

    def test_cfo_gate(self):
        for score, impact, criteria, expected in [
            (4.4, False, 0, 4.4), (4.5, False, 0, 4.4),
            (4.8, True, 2, 4.4), (4.8, True, 3, 4.8),
        ]:
            obj = sample(score)
            obj.update(cfo_metric_impact=impact, cfo_criteria_met=criteria)
            self.assertEqual(calculator.calculate(obj)["calculated_final_score"], expected)

    def test_exact_band_boundary(self):
        obj = sample()
        obj["email_type"] = "newsletter"
        for p, v in zip(calculator.PILLARS, [3.0, 3.1, 4.1, 4.3, 2.8]):
            obj["pillar_scores"][p] = v
            obj["pillar_reasoning"][p]["anchor"] = v
        r = calculator.calculate(obj)
        self.assertEqual(r["calculated_final_score"], 3.5)
        self.assertEqual(r["band"], "Competent")
        self.assertEqual(r["_external"]["tier"], "Fair")

    def test_display_does_not_round_up_across_a_gate(self):
        obj = sample(4.4)
        obj["modifiers"] = {"courage_bonus": 0.099, "courage_justification": "Fixture for precision boundary"}
        r = calculator.calculate(obj)
        self.assertEqual(r["calculated_final_score"], 4.49)
        self.assertFalse(r["caps_applied"])

    def test_unknown_strategy_is_not_labeled_fair(self):
        obj = sample(3.0)
        obj["pillar_reasoning"]["strategy"]["observability_default"] = True
        self.assertEqual(calculator.calculate(obj)["_external"]["pillar_labels"]["strategy"], "Not verified")
        obj["pillar_scores"]["strategy"] = 4.0
        self.assertFalse(calculator.calculate(obj)["valid"])

    def test_legacy_input_defaults_and_unknown_images_are_explicit(self):
        obj = sample()
        for field in ["email_type", "pillar_reasoning", "all_image"]:
            del obj[field]
        r = calculator.calculate(obj)
        self.assertTrue(r["valid"])
        self.assertEqual(r["email_type"], "promotional")
        self.assertEqual(len(r["warnings"]), 3)

    def test_cli_reports_bad_json_and_reads_utf8(self):
        for raw in ['{', '{"bad":NaN}', '[]']:
            run = subprocess.run([sys.executable, str(SCRIPT)], input=raw, text=True, capture_output=True)
            self.assertEqual(run.returncode, 1)
            self.assertFalse(json.loads(run.stdout)["valid"])
            self.assertNotIn("Traceback", run.stderr)
        run = subprocess.run([sys.executable, str(SCRIPT), str(ROOT / "tests/fixtures/skincare.json"), "--external"], text=True, capture_output=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(json.loads(run.stdout)["_external"]["tier"], "Fair")


if __name__ == "__main__":
    unittest.main()
