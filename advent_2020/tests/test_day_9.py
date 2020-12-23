import unittest

from advent_2020.day_9 import get_invalid_numbers, get_contiguous_sum_for_number

example = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576,
]


class TestGetInvalidNumbers(unittest.TestCase):
    def test_example(self):
        self.assertEqual(get_invalid_numbers(example, preamble_length=5), [127])


class TestGetContiguousSumForNumber(unittest.TestCase):
    def test_example(self):
        contiguous_numbers = get_contiguous_sum_for_number(example, target_number=127, min_length=2)
        self.assertEqual(15, min(contiguous_numbers))
        self.assertEqual(47, max(contiguous_numbers))


if __name__ == '__main__':
    unittest.main()
