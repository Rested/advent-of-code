from typing import Dict
from urllib import request


def parse_bag_rules(rule_text: str):
    rule_lines = rule_text.split("\n")
    rules = {}
    for line in rule_lines:
        if not line:
            continue
        bags = line.split("bag")
        outer_bag = bags[0].strip()
        rules[outer_bag] = {}
        if "contain no other" in bags[1]:
            continue
        for inner_bag in bags[1:]:
            inner_bag = inner_bag.lstrip("s,.")
            if not inner_bag:
                continue
            count, *bag_name = inner_bag.split("contain")[-1].strip().split(" ")
            bag_name_str = " ".join(bag_name)
            rules[outer_bag][bag_name_str] = int(count)
    return rules


BagRules = Dict[str, Dict[str, int]]


def can_bag_be_in_outer_bag(bag_rules: BagRules, outer_bag: str, target_inner_bag: str):
    if len(bag_rules[outer_bag]) == 0:
        return False
    if target_inner_bag in bag_rules[outer_bag]:
        return True
    return any(can_bag_be_in_outer_bag(bag_rules, inner_bag, target_inner_bag) for inner_bag in bag_rules[outer_bag])


def bags_containing_bag_count(bag_rules: BagRules, bag_colour: str):
    return len([bag_col for bag_col in bag_rules.keys() if
                can_bag_be_in_outer_bag(bag_rules, bag_col, target_inner_bag=bag_colour)])


def number_of_bags_inside_bag(bag_rules: BagRules, bag_color: str):
    if len(bag_rules[bag_color]) == 0:
        return 0
    return sum((number_of_bags_inside_bag(bag_rules, inner_bag) * bag_rules[bag_color][inner_bag]) + bag_rules[bag_color][inner_bag] for inner_bag in bag_rules[bag_color])

if __name__ == '__main__':
    with open("advent_2020/inputs/7") as f:
        input_text = f.read()

    bag_rules = parse_bag_rules(input_text)
    print("a)", bags_containing_bag_count(bag_rules, "shiny gold"))
    print("b)", number_of_bags_inside_bag(bag_rules, "shiny gold"))