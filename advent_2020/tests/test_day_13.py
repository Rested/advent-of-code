import unittest

from advent_2020.day_13 import parse_bus_times, get_earliest_bus, get_earliest_timestamp_for_sequential_departures

example = """939
7,13,x,x,59,x,31,19
"""


class TestParseNotes(unittest.TestCase):
    def test_parses_example(self):
        earliest_depart_timestamp, bus_ids = parse_bus_times(example)
        self.assertEqual(939, earliest_depart_timestamp)
        self.assertListEqual([7, 13, None, None, 59, None, 31, 19], bus_ids)


class TestFindEarliestBus(unittest.TestCase):
    def test_earliest_bus(self):
        self.assertEqual((59, 5), get_earliest_bus(*parse_bus_times(example)))


class TestEarliestTimestamp(unittest.TestCase):
    def test_get_earliest_timestamp_for_sequential_departures_with_example(self):
        self.assertEqual(1068781, get_earliest_timestamp_for_sequential_departures(parse_bus_times(example)[1]))
