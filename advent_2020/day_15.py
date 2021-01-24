"""
memory game,
take turns saying numbers
start with list of starting numbers
then each turn:
    if first time number has been spoken current player says 0
    other wise current player says how many turns apart the number is from when it was last spoken

"""
from typing import List


def get_nth_number_spoken(starting_numbers: List[int], n: int) -> int:
    turn_last_spoken_tracker = {}
    last_number_spoken = None
    prev_number = None
    for i in range(n):
        if prev_number is not None:
            turn_last_spoken_tracker[prev_number] = i
        prev_number = last_number_spoken
        turn = i + 1
        if i < len(starting_numbers):
            last_number_spoken = starting_numbers[i]
        else:
            try:
                last_number_spoken = turn - turn_last_spoken_tracker[last_number_spoken]
            except KeyError:
                last_number_spoken = 0
    return last_number_spoken


if __name__ == "__main__":
    with open("advent_2020/inputs/15") as f:
        nums = [int(x) for x in f.read().strip().split(",")]
    print("a)", get_nth_number_spoken(starting_numbers=nums, n=2020))
    print("b)", get_nth_number_spoken(starting_numbers=nums, n=30000000))
