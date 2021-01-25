import unittest

from advent_2020.day_17 import Point, parse_input, run_for_n_cycles, run_for_n_cycles_4d

example = """.#.
..#
###"""


class TestParseInput(unittest.TestCase):
    def test_example(self):
        self.assertListEqual([
            Point(0, 2, 0, False),
            Point(1, 2, 0, True),
            Point(2, 2, 0, False),
            Point(0, 1, 0, False),
            Point(1, 1, 0, False),
            Point(2, 1, 0, True),
            Point(0, 0, 0, True),
            Point(1, 0, 0, True),
            Point(2, 0, 0, True),
        ], parse_input(example))


class TestPoint(unittest.TestCase):
    def test_neighbours(self):
        p = Point(1, 2, 3)
        neighbours = p.neighbours()
        self.assertEqual(26, len(neighbours))
        self.assertSetEqual({
            # 1 item changes
            Point(0, 2, 3),
            Point(2, 2, 3),
            Point(1, 1, 3),
            Point(1, 3, 3),
            Point(1, 2, 2),
            Point(1, 2, 4),
            # 2 items change
            # 1 and 2
            Point(0, 1, 3),
            Point(2, 1, 3),
            Point(0, 3, 3),
            Point(2, 3, 3),
            # 1 and 3
            Point(0, 2, 2),
            Point(2, 2, 2),
            Point(0, 2, 4),
            Point(2, 2, 4),
            # 2 and 3
            Point(1, 1, 2),
            Point(1, 3, 2),
            Point(1, 1, 4),
            Point(1, 3, 4),
            # 3 items change
            Point(0, 1, 2),
            Point(2, 1, 2),
            Point(0, 3, 2),
            Point(2, 3, 2),
            Point(0, 1, 4),
            Point(2, 1, 4),
            Point(0, 3, 4),
            Point(2, 3, 4)
        }, set(neighbours))


class TestRunForNCycles(unittest.TestCase):
    def test_example_1_cycle(self):
        final_points = run_for_n_cycles(parse_input(example), 1)
        active_count = len([x for x in final_points if x.active])
        self.assertEqual(active_count, 11)
        self.assertIn(Point(0, 1, 0, True), final_points)

    def test_example_6_cycle(self):
        final_points = run_for_n_cycles(parse_input(example), 6)
        active_count = len([x for x in final_points if x.active])
        self.assertEqual(active_count, 112)


class TestRunForNCycles4d(unittest.TestCase):
    def test_example_6_cycle(self):
        final_points = run_for_n_cycles_4d(parse_input(example), 6)
        active_count = len(final_points)
        self.assertEqual(active_count, 848)


if __name__ == '__main__':
    unittest.main()
