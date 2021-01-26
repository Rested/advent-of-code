from math import prod


def evaluate_expression(expression: str, version=1) -> int:
    # print("evaluating expr: ", expression)
    if "(" in expression:
        inner_count = 0
        parenthetic_slice = []
        for i, c in enumerate(expression):
            if c == "(":
                if len(parenthetic_slice) == 0:
                    parenthetic_slice.append(i)
                else:
                    inner_count += 1
            elif c == ")":
                if inner_count == 0:
                    parenthetic_slice.append(i)
                    break
                inner_count -= 1
        evaluated_inner = evaluate_expression(expression[parenthetic_slice[0] + 1:parenthetic_slice[1]],
                                              version=version)
        return evaluate_expression(
            f"{expression[:parenthetic_slice[0]]}{evaluated_inner}{expression[parenthetic_slice[1] + 1:]}",
            version=version)

    if version == 2:
        return prod(eval(sum_expr.strip()) for sum_expr in expression.split(" * "))

    current_value = None
    last_operator = None
    for value in expression.split(" "):
        if value.strip():
            if value.isnumeric():
                if current_value is None:
                    current_value = int(value)
                    continue
                if last_operator == "*":
                    current_value *= int(value)
                else:
                    current_value += int(value)
            else:
                last_operator = value

    return current_value


def a(input_txt: str):
    return sum(evaluate_expression(line) for line in input_txt.split("\n") if line)


def b(input_txt: str):
    return sum(evaluate_expression(line, version=2) for line in input_txt.split("\n") if line)


if __name__ == "__main__":
    with open("advent_2020/inputs/18") as f:
        input_text = f.read()
    print("a)", a(input_text))
    print("b)", b(input_text))
