import unittest

from advent_2020.day_12 import parse_input, follow_directions, manhattan_distance, follow_directions_waypoint

example = """F10
N3
F7
R90
F11"""


class TestExampleDirections(unittest.TestCase):
    def test_gives_correct_position(self):
        self.assertEqual(follow_directions(parse_input(example)), [17, -8])

    def test_gives_correct_manhattan_distance(self):
        self.assertEqual(manhattan_distance(follow_directions(parse_input(example))), 25)


class TestExampleDirectionsWaypoint(unittest.TestCase):
    def test_gives_correct_position(self):
        self.assertEqual(follow_directions_waypoint(parse_input(example)), [214, -72])

    def test_gives_correct_manhattan_distance(self):
        self.assertEqual(follow_directions_waypoint(follow_directions(parse_input(example))), 286)


if __name__ == '__main__':
    unittest.main()
