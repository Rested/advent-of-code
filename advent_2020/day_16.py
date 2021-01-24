"""
known fields, known valid value ranges
have numbers (values) on my ticket, numbers on nearby tickets

e.g.
class: 1-3 or 5-7
ticket is represented as single csv line
"""
from typing import List, Set, Tuple
from math import prod

FieldValidValues = Tuple[str, Set[int]]
Ticket = List[int]


def parse_ticket_notes(ticket_text: str) -> Tuple[List[FieldValidValues], Ticket, List[Ticket]]:
    rules_raw, my_ticket_raw, nearby = ticket_text.split("\n\n")
    rule_list = []

    for rule in rules_raw.split("\n"):
        rule_name, rule_content = rule.split(":")
        rule_values = set()
        for value_range in rule_content.split(" or "):
            lower, upper = value_range.split("-")
            rule_values.update(set(range(int(lower.strip()), int(upper.strip()) + 1)))
        rule_list.append((rule_name, rule_values))

    my_ticket = [int(x) for x in my_ticket_raw.split(":")[-1].strip().split(",")]
    nearby_tickets = [[int(x) for x in ticket.split(",")] for ticket in nearby.split(":")[-1].strip().split("\n")]

    return rule_list, my_ticket, nearby_tickets


def split_valid_and_invalid_tickets(rules: List[FieldValidValues],
                                    tickets: List[Ticket]) -> Tuple[List[Ticket], List[Ticket], List[int]]:
    """Invalid if it has any value which is invalid for all possible fields"""
    valid_tickets = []
    invalid_tickets = []
    invalid_values = []

    all_valid_values = set()
    for _, valid_values in rules:
        all_valid_values.update(valid_values)

    for ticket in tickets:
        invalid_values_in_ticket = set(ticket).difference(all_valid_values)
        if invalid_values_in_ticket:
            invalid_tickets.append(ticket)
            invalid_values += list(invalid_values_in_ticket)
            continue
        valid_tickets.append(ticket)

    return valid_tickets, invalid_tickets, invalid_values


def determine_field_positions_in_ticket(rules: List[FieldValidValues], valid_tickets: List[Ticket]) -> List[str]:
    num_fields = len(rules)
    possible_values_in_position: List[Set[str]] = [{rule[0] for rule in rules} for _ in range(num_fields)]
    # get all possible field names for each position
    for ticket in valid_tickets:
        for pos, value in enumerate(ticket):
            for rule_name, valid_values in rules:
                if value not in valid_values:
                    possible_values_in_position[pos].remove(rule_name)
    # confirmed items are those who only have one possible field name, we assume there is at least one of these and
    # that multiple configurations are not possible
    confirmed_items = set()
    for pos_set in possible_values_in_position:
        if len(pos_set) == 1:
            confirmed_items.update(pos_set)
    # we can use the confirmed items to eliminate duplicate items which have already had their position confirmed
    # until each position is assigned exactly 1 field name
    while len(confirmed_items) != num_fields:
        for pos_set in possible_values_in_position:
            if len(pos_set) == 1:
                continue
            for conf_item in confirmed_items:
                try:
                    pos_set.remove(conf_item)
                except KeyError:
                    pass
            if len(pos_set) == 1:
                confirmed_items.update(pos_set)
    return [list(x)[0] for x in possible_values_in_position]


def a(input_txt: str):
    rules, _, tickets = parse_ticket_notes(input_txt)
    _, _, invalid_values = split_valid_and_invalid_tickets(rules, tickets)
    return sum(invalid_values)


def b(input_txt: str):
    rules, my_ticket, tickets = parse_ticket_notes(input_txt)
    valid_tickets, _, _ = split_valid_and_invalid_tickets(rules, tickets)
    field_name_positions = determine_field_positions_in_ticket(rules, valid_tickets)
    return prod((my_ticket[indx] for indx in
                 (i for i, field_name in enumerate(field_name_positions) if field_name.startswith("departure"))))


if __name__ == "__main__":
    with open("advent_2020/inputs/16") as f:
        input_str = f.read()
    print("a)", a(input_str))
    print("b)", b(input_str))
