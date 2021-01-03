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


Actions = List[Tuple[str, int]]


def follow_directions(actions: Actions):
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


def follow_directions_waypoint(actions: Actions):
    bearings = [NORTH, EAST, SOUTH, WEST]
    current_bearing = EAST
    current_bearing_index = 1
    way_point_position = [10, 1]
    ship_position = [0, 0]
    for action, amount in actions:
        if action == LEFT:
            # rotate way point around ship 90

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
            ship_position[1] += amount
            continue
        if action == EAST:
            ship_position[0] += amount
            continue
        if action == SOUTH:
            ship_position[1] -= amount
            continue
        if action == WEST:
            ship_position[0] -= amount
            continue
    return ship_position


if __name__ == "__main__":
    with open("advent_2020/inputs/12") as f:
        inputs = f.read()
    print("a)", manhattan_distance(follow_directions(parse_input(inputs))))
