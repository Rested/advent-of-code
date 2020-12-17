import unittest

from advent_2020.day_7 import parse_bag_rules, bags_containing_bag_count, number_of_bags_inside_bag

example = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

class TestBagRules(unittest.TestCase):


    def test_parse_bag_rules(self):
        self.assertEqual(parse_bag_rules("\n".join(example.split("\n")[:2])),
                         {"light red": {"bright white": 1, "muted yellow": 2},
                          "dark orange": {"bright white": 3, "muted yellow": 4}})


class TestGetBagsContainingBagCount(unittest.TestCase):
    def test_get_bags_containing_bag_count(self):
        self.assertEqual(4, bags_containing_bag_count(parse_bag_rules(example), "shiny gold"))

num_bags_example = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

class TestNumberOfBagsInsideBag(unittest.TestCase):
    def test_number_of_bags_inside_bag(self):
        self.assertEqual(0, number_of_bags_inside_bag(parse_bag_rules(num_bags_example), "dark violet"))
        self.assertEqual(2, number_of_bags_inside_bag(parse_bag_rules(num_bags_example), "dark blue"))
        self.assertEqual(126, number_of_bags_inside_bag(parse_bag_rules(num_bags_example), "shiny gold"))

if __name__ == '__main__':
    unittest.main()
