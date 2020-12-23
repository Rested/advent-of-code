from typing import List
from itertools import combinations


def get_invalid_numbers(number_sequence: List[int], preamble_length=25):
    invalid_nums = []

    for i in range(preamble_length, len(number_sequence)):
        sub_sequence = number_sequence[i - preamble_length:i]
        valid = False
        for combo in combinations(sub_sequence, 2):

            if number_sequence[i] == sum(combo):
                valid = True
                break
        if not valid:
            invalid_nums.append(number_sequence[i])

    return invalid_nums


def get_contiguous_sum_for_number(number_sequence: List[int], target_number: int, min_length=2):
    for length in range(min_length, len(number_sequence)):
        for offset in range(len(number_sequence) - length):
            window = number_sequence[offset:offset + length]
            if sum(window) == target_number:
                return window
    return None


if __name__ == "__main__":
    with open("advent_2020/inputs/9") as f:
        numbers = [int(x.strip()) for x in f.read().split("\n") if x]

    invalid_num = get_invalid_numbers(numbers)[0]
    print("a)", invalid_num)
    contiguous_sequence = get_contiguous_sum_for_number(numbers, invalid_num)
    print("b)", min(contiguous_sequence) + max(contiguous_sequence))
