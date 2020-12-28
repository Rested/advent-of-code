import unittest

from advent_2020.day_10 import jolt_difference_counts, distinct_adapter_arrangements

simple_example = [
    16,
    10,
    15,
    5,
    1,
    11,
    7,
    19,
    6,
    12,
    4,
]

larger_example = [
    28,
    33,
    18,
    42,
    31,
    14,
    46,
    20,
    48,
    47,
    24,
    23,
    49,
    45,
    19,
    38,
    39,
    11,
    1,
    32,
    25,
    35,
    8,
    17,
    7,
    9,
    4,
    2,
    34,
    10,
    3,
]


class TestJoltDifferenceCounts(unittest.TestCase):
    def test_simple_example(self):
        self.assertEqual(jolt_difference_counts(simple_example), {
            1: 7,
            2: 0,
            3: 5
        })

    def test_larger_example(self):
        self.assertEqual(jolt_difference_counts(larger_example), {
            1: 22,
            2: 0,
            3: 10
        })


class TestDistinctAdapterArrangements(unittest.TestCase):
    def test_simple_example(self):
        self.assertEqual(distinct_adapter_arrangements(simple_example), 8)

    def test_longer_example(self):
        self.assertEqual(distinct_adapter_arrangements(larger_example), 19208)


if __name__ == '__main__':
    unittest.main()
