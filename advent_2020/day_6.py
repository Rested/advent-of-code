from typing import List, Dict


def parse_responses(text: str) -> List[List[str]]:
    return [group.strip().split("\n") for group in text.split("\n\n") if group]


def unique_answer_counts(group_response: List[str]) -> Dict[str, int]:
    unique_answer_cnts = {}
    for response in group_response:
        for answer_label in response:
            try:
                unique_answer_cnts[answer_label] += 1
            except KeyError:
                unique_answer_cnts[answer_label] = 1
    return unique_answer_cnts


def a(input_text: str):
    group_responses = parse_responses(input_text)
    return sum(len(unique_answer_counts(group_response)) for group_response in group_responses)


def b(input_text: str):
    group_responses = parse_responses(input_text)
    total = 0
    for group_response in group_responses:
        unique_answer_cnts = unique_answer_counts(group_response)
        for ans in unique_answer_cnts:
            if unique_answer_cnts[ans] == len(group_response):
                total += 1
    return total


if __name__ == "__main__":
    with open("advent_2020/inputs/6") as f:
        input_txt = f.read()

    print("a)", a(input_txt))
    print("b)", b(input_txt))
