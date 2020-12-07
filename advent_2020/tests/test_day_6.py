import unittest
from advent_2020.day_6 import parse_responses, unique_answer_counts

"""
26 yes-no questions (a-z)
identify qs where anyone in the group answers yes
part b switches to everyone
"""


class TestParseGroupAnswers(unittest.TestCase):
    def test_parses_groups_correctly(self):
        example = """
abc
dd

aa
bb
"""
        self.assertEqual([["abc", "dd"], ["aa", "bb"]], parse_responses(example))

    def test_parses_correctly(self):
        group_answers = ["abc", "a", "caf", "ef"]
        self.assertEqual(unique_answer_counts(group_answers), {"a": 3, "b": 1, "c": 2, "e": 1, "f": 2})


if __name__ == '__main__':
    unittest.main()
