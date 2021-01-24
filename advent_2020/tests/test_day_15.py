import unittest

from advent_2020.day_15 import get_nth_number_spoken


class TestGetNthNumberSpoken(unittest.TestCase):
    def test_for_example(self):
        starting_numbers = [0, 3, 6]
        expected_numbers = [0, 3, 6, 0, 3, 3, 1, 0, 4, 0]
        for i in range(len(expected_numbers)):
            expected_number_spoken = expected_numbers[i]
            with self.subTest(turn=i + 1, expected_number=expected_number_spoken):
                self.assertEqual(expected_number_spoken, get_nth_number_spoken(starting_numbers, n=i + 1))


if __name__ == '__main__':
    unittest.main()
