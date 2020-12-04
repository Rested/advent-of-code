import unittest

from day_2 import PasswordEntry, parse_entry


class TestParsing(unittest.TestCase):
    def test_parses_correctly(self):
        self.assertEqual(parse_entry("1-3 a: abcde"),
                         PasswordEntry(password="abcde", char_low=1, char_high=3, character="a"))


class Test2B(unittest.TestCase):

    def test_valid_examples(self):
        entry_1 = PasswordEntry(char_low=1, char_high=3, character="a", password="abcde")
        self.assertTrue(entry_1.is_valid("b"))

    def test_invalid_examples(self):
        entry_1 = PasswordEntry(char_low=1, char_high=3, character="b", password="cdefg")
        entry_2 = PasswordEntry(char_low=2, char_high=9, character="c", password="ccccccccc")

        self.assertFalse(entry_1.is_valid("b"))
        self.assertFalse(entry_2.is_valid("b"))


if __name__ == '__main__':
    unittest.main()
