import unittest
from advent_2020.day_5 import Seat, decode_seat_spec

"""
find seat,
binary space partitioning used to seat people

FBLR - front back left right
first 7 chars either F or B - specify which row it is in
each letter tells you which half of the rows left it is in
same with the last 3 but with the columns
"""


class TestDecodeSeatSepc(unittest.TestCase):
    def test_correctly_decodes(self):
        self.assertEqual(Seat(spec="FBFBBFFRLR", col=5, row=44, seat_id=357), decode_seat_spec("FBFBBFFRLR"))


if __name__ == '__main__':
    unittest.main()
