import unittest

from advent_2020.day_11 import parse_to_2d_array, apply_rules_till_stability, total_occupied_in_state, RULESET_VISION

example = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""


class TestParseTo2dArray(unittest.TestCase):
    def test_parse(self):
        parsed = parse_to_2d_array(example)
        self.assertListEqual(["L", ".", "L"], parsed[0][:3])


class TestApplyRulesTillStability(unittest.TestCase):
    def test_example(self):
        parsed = parse_to_2d_array(example)
        stable = apply_rules_till_stability(parsed)
        occupied_count = total_occupied_in_state(stable)
        self.assertEqual(37, occupied_count)

    def test_example_with_vision_ruleset(self):
        parsed = parse_to_2d_array(example)
        stable = apply_rules_till_stability(parsed, ruleset=RULESET_VISION)
        occupied_count = total_occupied_in_state(stable)
        self.assertEqual(26, occupied_count)


if __name__ == '__main__':
    unittest.main()
