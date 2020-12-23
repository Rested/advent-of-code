from typing import Union, Dict, List, Tuple, Set
import copy

Instructions = List[Dict[str, Union[str, int]]]


def parse_instructions(instruction_text: str) -> Instructions:
    instructions = []
    for line in instruction_text.split("\n"):
        if line:
            instruction, num, *_ = line.split(" ")
            instructions.append({
                "operation": instruction,
                "argument": int(num)
            })
    return instructions


def execute_instructions_till_repeate_or_complete(instructions: Instructions) -> Tuple[bool, int, Instructions]:
    accumulator = 0
    executed_instruction_indices = []
    offset = 0
    next_instruction = instructions[0]
    finished = False
    while offset not in executed_instruction_indices:
        executed_instruction_indices.append(offset)
        if next_instruction["operation"] == "jmp":
            offset += next_instruction["argument"]
        else:
            offset += 1

        if next_instruction["operation"] == "acc":
            accumulator += next_instruction["argument"]
        try:
            next_instruction = instructions[offset]
        except IndexError:
            finished = True
            break

    return finished, accumulator, [instructions[x] for x in executed_instruction_indices]


def find_finishing_jmp_nop(instructions: Instructions):
    finishes, acc, _ = execute_instructions_till_repeate_or_complete(instructions)
    if finishes:
        return acc
    for i, instruction in enumerate(instructions):
        modified_instruction_set = copy.deepcopy(instructions)
        if instruction["operation"] == "jmp":
            modified_instruction_set[i]["operation"] = "nop"
        if instruction["operation"] == "nop":
            modified_instruction_set[i]["operation"] = "jmp"
        finishes, acc, _ = execute_instructions_till_repeate_or_complete(modified_instruction_set)
        if finishes:
            return acc


def a(instruction_text: str):
    instructions = parse_instructions(instruction_text)
    _, acc, _ = execute_instructions_till_repeate_or_complete(instructions)
    return acc


def b(instruction_text: str):
    instructions = parse_instructions(instruction_text)
    return find_finishing_jmp_nop(instructions)


if __name__ == "__main__":
    with open("advent_2020/inputs/8") as f:
        input_text = f.read()
    print("a)", a(input_text))
    print("b)", b(input_text))
