YEARS_SAVED_XMAS = 5
STARS_REQUIRED_FOR_ROOM_DEPOSIT = 50


def a(expenses):
    # find two that add to 2020 and give their multiplication
    for x in expenses:
        for y in expenses:
            if x + y == 2020:
                return x * y


def b(expenses):
    # find three that add to 2020 and give their multiplication
    for x in expenses:
        for y in expenses:
            for z in expenses:
                if sum((x, y, z)) == 2020:
                    return x * y * z


if __name__ == '__main__':
    with open("inputs/1") as f:
        expenses = [int(v) for v in f.read().split("\n") if v]
    print("a)", a(expenses))
    print("b)", b(expenses))
