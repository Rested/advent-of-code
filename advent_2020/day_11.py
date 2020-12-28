"""
L = empty
. = floor
# = occupied

if seat empty and no occupied seats adjacent, it becomes occupied
if seat occupied and >=4 seats adjacent are occupied it becomes emmpty
else stays same
"""
import copy
from typing import List
from itertools import product

EMPTY = "L"
OCCUPIED = "#"
FLOOR = "."

RULESET_ADJACENT = "adjacent"
RULESET_VISION = "vision"


def parse_to_2d_array(input_text: str) -> List[List[str]]:
    return [list(l.strip()) for l in input_text.split("\n") if l]


def get_surrounding_occupied_count(seat_grid: List[List[str]], row_index: int, seat_index: int,
                                   ruleset: (RULESET_ADJACENT, RULESET_VISION)):
    occupied_count = 0
    # print("at", row_index, seat_index)

    if RULESET_ADJACENT == ruleset:
        for k in range(row_index - 1, row_index + 2):
            for l in range(seat_index - 1, seat_index + 2):
                if k < 0 or l < 0:
                    continue
                if k == row_index and l == seat_index:
                    continue
                try:
                    if seat_grid[k][l] == OCCUPIED:
                        # print("occ", k, l)
                        occupied_count += 1
                except IndexError:
                    continue
    if RULESET_VISION == ruleset:
        directions = product((-1, 0, 1), repeat=2)
        for direction in directions:
            cursor = [row_index, seat_index]
            if direction == (0, 0):
                continue
            while True:
                cursor = [cursor[0] + direction[0], cursor[1] + direction[1]]
                # off the start
                if min(cursor) < 0:
                    break

                try:
                    seat = seat_grid[cursor[0]][cursor[1]]
                except IndexError:
                    # off the end
                    break

                if seat == OCCUPIED:
                    occupied_count += 1
                    break
                if seat == EMPTY:
                    break

    return occupied_count


def apply_rules_till_stability(seat_grid: List[List[str]], ruleset=RULESET_ADJACENT):
    state = copy.deepcopy(seat_grid)
    state_transitions = 0
    while True:
        state_changes = 0
        new_state = copy.deepcopy(state)
        for i, row in enumerate(state):
            for j, seat in enumerate(row):
                if seat == EMPTY and get_surrounding_occupied_count(state, i, j, ruleset) == 0:
                    new_state[i][j] = OCCUPIED
                    state_changes += 1
                elif seat == OCCUPIED and get_surrounding_occupied_count(state, i, j, ruleset) >= (
                        4 if ruleset == RULESET_ADJACENT else 5):
                    new_state[i][j] = EMPTY
                    state_changes += 1

        if state_changes == 0:
            return new_state
        state = copy.deepcopy(new_state)
        state_transitions += 1


def total_occupied_in_state(seat_grid: List[List[str]]):
    total = 0
    for x in seat_grid:
        for y in x:
            if y == OCCUPIED:
                total += 1
    return total


if __name__ == "__main__":
    with open("advent_2020/inputs/11") as f:
        input_data = f.read()
    print("a)", total_occupied_in_state(apply_rules_till_stability(parse_to_2d_array(input_data))))
    print("b)", total_occupied_in_state(apply_rules_till_stability(parse_to_2d_array(input_data), ruleset=RULESET_VISION)))
