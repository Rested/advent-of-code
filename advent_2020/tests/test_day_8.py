import unittest

from advent_2020.day_8 import parse_instructions, execute_instructions_till_repeate_or_complete, find_finishing_jmp_nop


class TestInstructionParse(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual(parse_instructions("""nop +0
acc +1
jmp +4
"""), [{"operation": "nop", "argument": 0}, {"operation": "acc", "argument": 1}, {"operation": "jmp", "argument": 4}])


example = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


class TestExecuteTillRepetition(unittest.TestCase):
    def test_example(self):
        instructions = parse_instructions(example)
        finished, accumulator, _ = execute_instructions_till_repeate_or_complete(instructions)
        self.assertFalse(finished)
        self.assertEqual(accumulator, 5)


second_example = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


class TestFinishingJmpNop(unittest.TestCase):
    def test_example(self):
        result = find_finishing_jmp_nop(parse_instructions(second_example))
        self.assertEqual(8, result)

if __name__ == '__main__':
    unittest.main()
