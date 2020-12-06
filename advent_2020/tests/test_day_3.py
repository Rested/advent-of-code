import unittest

"""
Trees grow on exact integer coordinates on the grid.
. -> open square
# -> Tree
"""

from advent_2020.day_3 import parse_map, a, b


class TestMapParse(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        example_map = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
        cls.tree_map = parse_map(example_map)

    def test_parses_correctly(self):
        self.assertEqual(".", self.tree_map[0, 0])
        self.assertEqual("#", self.tree_map[1, 2])

    def test_parses_len(self):
        self.assertEqual(len("..##......."), self.tree_map.line_length, 11)

    def test_loops(self):
        self.assertEqual("#", self.tree_map[14, 0], self.tree_map[15, 0])


example = """
..##.........##.........##.........##.........##.........##.......
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#"""


class TestA(unittest.TestCase):
    def test_gets_correct_number_of_trees(self):
        tree_map = parse_map(example)
        self.assertEqual(7, a(tree_map))


class TestB(unittest.TestCase):
    def test_gets_correct_answer_for_example(self):
        tree_map = parse_map(example)
        self.assertEqual(336, b(tree_map))


if __name__ == '__main__':
    unittest.main()
