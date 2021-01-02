# translations
from typing import Tuple, List

NORTH = "N"
SOUTH = "S"
EAST = "E"
WEST = "W"

# rotations
LEFT = "L"
RIGHT = "R"

# rotation dependent translations
FORWARD = "F"


def parse_input(input_text: str) -> List[Tuple[str, int]]:
    return [(x[0], int(x[1:])) for x in input_text.split("\n") if x]


# lets assume rotations are all divisible by 90

def manhattan_distance(position):
    return abs(position[0]) + abs(position[1])


def follow_directions(actions: List[Tuple[str, int]]):
    bearings = [NORTH, EAST, SOUTH, WEST]
    current_bearing = EAST
    current_bearing_index = 1
    position = [0, 0]
    for action, amount in actions:
        if action == LEFT:
            current_bearing_index = (current_bearing_index - int(amount / 90)) % 4
            current_bearing = bearings[current_bearing_index]
            continue
        if action == RIGHT:
            current_bearing_index = (current_bearing_index + int(amount / 90)) % 4
            current_bearing = bearings[current_bearing_index]
            continue
        if action == FORWARD:
            action = current_bearing
        if action == NORTH:
            position[1] += amount
            continue
        if action == EAST:
            position[0] += amount
            continue
        if action == SOUTH:
            position[1] -= amount
            continue
        if action == WEST:
            position[0] -= amount
            continue
    return position


if __name__ == "__main__":
    with open("advent_2020/inputs/12") as f:
        inputs = f.read()
    print("a)", manhattan_distance(follow_directions(parse_input(inputs))))