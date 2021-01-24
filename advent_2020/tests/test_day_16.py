import unittest

from advent_2020.day_16 import parse_ticket_notes, split_valid_and_invalid_tickets, determine_field_positions_in_ticket

example = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

second_example = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""


class TestParseTicket(unittest.TestCase):
    def test_example(self):
        rules, my_ticket, nearby_tickets = parse_ticket_notes(example)
        self.assertListEqual([
            ("class", {1, 2, 3, 5, 6, 7}),
            ("row", {6, 7, 8, 9, 10, 11, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44}),
            ("seat", set(range(13, 41)).union({45, 46, 47, 48, 49, 50}))
        ], rules)
        self.assertListEqual([7, 1, 14], my_ticket)
        self.assertListEqual([
            [7, 3, 47],
            [40, 4, 50],
            [55, 2, 20],
            [38, 6, 12],
        ], nearby_tickets)


class TestSplitValidAndInvalidTickets(unittest.TestCase):
    def test_example(self):
        rules, _, nearby_tickets = parse_ticket_notes(example)
        valid_tickets, invalid_tickets, invalid_values = split_valid_and_invalid_tickets(rules, nearby_tickets)
        self.assertListEqual([[7, 3, 47]], valid_tickets)
        self.assertListEqual([
            [40, 4, 50],
            [55, 2, 20],
            [38, 6, 12],
        ], invalid_tickets)
        self.assertListEqual([4, 55, 12], invalid_values)

    def test_second_example(self):
        rules, _, nearby_tickets = parse_ticket_notes(second_example)
        valid_tickets, invalid_tickets, invalid_values = split_valid_and_invalid_tickets(rules, nearby_tickets)
        self.assertListEqual([
            [3, 9, 18],
            [15, 1, 5],
            [5, 14, 9],
        ], valid_tickets)
        self.assertListEqual([], invalid_tickets)
        self.assertListEqual([], invalid_values)


class TestDetermineFieldPositionsInTicket(unittest.TestCase):
    def test_second_example(self):
        rules, _, nearby_tickets = parse_ticket_notes(second_example)
        valid_tickets, _, _ = split_valid_and_invalid_tickets(rules, nearby_tickets)

        self.assertListEqual(["row", "class", "seat"], determine_field_positions_in_ticket(rules, valid_tickets))


if __name__ == '__main__':
    unittest.main()
