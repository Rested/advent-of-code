import unittest
from advent_2020.day_14 import parse_input_to_steps, SET_MEM, SET_MASK, combine_num_with_mask, \
    get_memory_addresses_v2_mask, combine_num_with_mask_v2

example = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""


class TestParseInputToSteps(unittest.TestCase):
    def test_example(self):
        parsed = parse_input_to_steps(example)
        self.assertListEqual(parsed, [(SET_MASK, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"), (SET_MEM, (8, 11)),
                                      (SET_MEM, (7, 101)), (SET_MEM, (8, 0))])


class TestCombineNumWithMask(unittest.TestCase):
    def test_examples(self):
        mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
        cases = (
            (11, 73),
            (101, 101),
            (0, 64)
        )
        for input_decimal_number, result in cases:
            with self.subTest(input_decimal_number=input_decimal_number, result=result):
                self.assertEqual(result, combine_num_with_mask(mask, input_decimal_number))


class TestCombineWithMaskV2(unittest.TestCase):
    def test_example(self):
        mask = "000000000000000000000000000000X1001X"
        addr = 42
        self.assertEqual("000000000000000000000000000000X1101X", combine_num_with_mask_v2(mask, addr))


class TestGetMemoryAddressesV2Mask(unittest.TestCase):
    def test_first_example(self):
        mask = "000000000000000000000000000000X1001X"
        addr = 42

        self.assertListEqual([26, 27, 58, 59], get_memory_addresses_v2_mask(mask, addr))

    def test_second_example(self):
        mask = "00000000000000000000000000000000X0XX"
        addr = 26

        self.assertListEqual([16, 17, 18, 19, 24, 25, 26, 27], get_memory_addresses_v2_mask(mask, addr))


if __name__ == '__main__':
    unittest.main()
