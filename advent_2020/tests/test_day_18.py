import unittest

from advent_2020.day_18 import evaluate_expression


class TestEvaluateExpression(unittest.TestCase):
    def test_flat(self):
        self.assertEqual(71, evaluate_expression("1 + 2 * 3 + 4 * 5 + 6"))

    def test_simple(self):
        self.assertEqual(26, evaluate_expression("2 * 3 + (4 * 5)"))
        self.assertEqual(437, evaluate_expression("5 + (8 * 3 + 9 + 3 * 4 * 3)"))

    def test_complex(self):
        self.assertEqual(51, evaluate_expression("1 + (2 * 3) + (4 * (5 + 6))"))
        self.assertEqual(12240, evaluate_expression("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"))
        self.assertEqual(13632, evaluate_expression("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"))

    def test_v2(self):
        self.assertEqual(231, evaluate_expression("1 + 2 * 3 + 4 * 5 + 6", version=2))
        self.assertEqual(51, evaluate_expression("1 + (2 * 3) + (4 * (5 + 6))", version=2))
        self.assertEqual(46, evaluate_expression("2 * 3 + (4 * 5)", version=2))
        self.assertEqual(1445, evaluate_expression("5 + (8 * 3 + 9 + 3 * 4 * 3)", version=2))
        self.assertEqual(669060, evaluate_expression("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", version=2))
        self.assertEqual(23340, evaluate_expression("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", version=2))

if __name__ == '__main__':
    unittest.main()
