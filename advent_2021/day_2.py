
from typing import Any, List, Tuple

def navigate_course(instructions: List[str]) -> Tuple[int, int]:
    horizontal = 0
    depth = 0
    for instruction in instructions:
        match instruction.split(" "):
            case ["forward", amount]:
                horizontal += int(amount)
            case ["down", amount]:
                depth += int(amount)
            case ["up", amount]:
                depth -= int(amount)
            case _:
                pass
    return horizontal, depth

def navigate_aim_course(instructions: List[str]) -> Tuple[int, int]:
    horizontal = 0
    depth = 0
    aim = 0
    for instruction in instructions:
        match instruction.split(" "):
            case ["forward", amount]:
                horizontal += int(amount)
                depth += aim * int(amount)
            case ["down", amount]:
                aim += int(amount)
            case ["up", amount]:
                aim -= int(amount)
            case _:
                pass
    return horizontal, depth


def run(input_text: str) -> Any:
    instructions = input_text.split("\n")
    h, d = navigate_course(instructions)
    h2, d2 = navigate_aim_course(instructions)
    return h * d, h2*d2        
