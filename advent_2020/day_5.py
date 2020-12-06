import dataclasses

ROWS = 128
COLUMNS = 8


@dataclasses.dataclass
class Seat:
    spec: str
    seat_id: int
    row: int
    col: int


def seat_id(row, col):
    return row * 8 + col


def do_halving_search(spec, range_size, lower_notation, upper_notation):
    row_range = [0, range_size - 1]
    rows_left = range_size
    for char in spec:
        rows_left /= 2
        if char == upper_notation:
            row_range[0] += rows_left
            continue
        if char == lower_notation:
            row_range[1] -= rows_left
            continue
    return row_range[0]


def decode_seat_spec(spec: str) -> Seat:
    row_spec = spec[:7]
    col_spec = spec[7:]

    row = do_halving_search(row_spec, ROWS, "F", "B")
    col = do_halving_search(col_spec, COLUMNS, "L", "R")
    return Seat(spec=spec, col=col, row=row, seat_id=seat_id(row, col))


def a(seat_specs):
    max_seat_id = 0
    for spec in seat_specs:
        max_seat_id = max(max_seat_id, decode_seat_spec(spec).seat_id)
    return max_seat_id


def b(seat_specs):
    filled_seats = [decode_seat_spec(spec) for spec in seat_specs]
    for i in range(1, ROWS - 1):  # can't be at the front or the back
        for j in range(COLUMNS):
            if any(s.row == i and s.col == j for s in filled_seats):  # is filled spot
                continue
            # get the seat id of this missing seat
            missing_seat_id = seat_id(i, j)
            if any(s.seat_id == missing_seat_id + 1 for s in filled_seats) and any(
                    s.seat_id == missing_seat_id - 1 for s in filled_seats):  # id + and - 1 are filled
                return missing_seat_id


if __name__ == "__main__":
    with open("advent_2020/inputs/5") as f:
        seat_specs = f.read().split("\n")

    print("a)", a(seat_specs))
    print("b)", b(seat_specs))
