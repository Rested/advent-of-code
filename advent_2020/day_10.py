from typing import List


def jolt_difference_counts(adapters: List[int], valid_jumps=(1, 2, 3)):
    diff_counts = {
        j: 0 for j in valid_jumps
    }
    sorted_ratings = [0] + sorted(adapters) + [max(adapters) + 3]
    for i, adapter_rating in enumerate(sorted_ratings):
        if i == 0:
            continue
        diff = adapter_rating - sorted_ratings[i - 1]
        diff_counts[diff] += 1

    return diff_counts


def distinct_adapter_arrangements(adapters: List[int], valid_jumps=(1, 2, 3)):
    # brute forcing this wont work because of combinatorial explosion
    sorted_ratings = [0] + sorted(adapters) + [max(adapters) + 3]
    ways_to_reach_rating = {}
    for i, rating in enumerate(sorted_ratings):
        if i == 0:
            ways_to_reach_rating[rating] = 1
            continue
        ways_to_reach_rating[rating] = 0
        # since always distinct ratings we only need to go back a maximum of 3 prior elements - could be more efficient
        # by going from i - 1 backward but this is easier to read imo
        for prior_rating in sorted_ratings[max(0, i - 3):i]:
            if rating - prior_rating in valid_jumps:
                ways_to_reach_rating[rating] += ways_to_reach_rating[prior_rating]

    return ways_to_reach_rating[sorted_ratings[-1]]


def a(adapters: List[int]):
    diff_counts = jolt_difference_counts(adapters)
    return diff_counts[1] * diff_counts[3]


if __name__ == "__main__":
    with open("advent_2020/inputs/10") as f:
        numbers = [int(x.strip()) for x in f.read().split("\n") if x]

    print("a)", a(numbers))
    print("b)", distinct_adapter_arrangements(numbers))
