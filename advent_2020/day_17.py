"""
infinite 3d grid. at every integer coordinate (x,y,z) there's an active or inactive cube

initially all cubes inactive apart from the region described by the puzzle input (# active, . inactive)

boot up 6 cycles

each cube only affects its 26 neighbours (where any coord differs by at most 1)

during cycle all cubes change simultaneously according to the following rules:
    - if active && 2 or 3 neighbors active then stay active else inactive
    - if inactive && 3 neighbors active then becomes active, else inactive

a) how many are active after the sixth cycle
"""
from typing import List, Optional


class Point:
    def __init__(self, x: int, y: int, z: int, active: Optional[bool] = None):
        self.x = x
        self.y = y
        self.z = z
        self.active = active

    def __eq__(self, other: 'Point'):
        return self.x == other.x and self.y == other.y and self.z == other.z and (
                other.active is None or self.active is None or self.active == other.active)

    def __hash__(self):
        return hash(f"{self.x},{self.y},{self.z},{self.active}")

    def is_same_position(self, other: 'Point'):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z}) - {'' if self.active else 'in'}active"

    def is_neighbour(self, other: 'Point'):
        return self != other and all(abs(getattr(self, attr) - getattr(other, attr)) <= 1 for attr in {'x', 'y', 'z'})

    def neighbours(self) -> List['Point']:
        neighs = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    new_point = Point(self.x + x, self.y + y, self.z + z)
                    if new_point != self:
                        neighs.append(new_point)
        return neighs


class Point4D:
    def __init__(self, x: int, y: int, z: int, w: int):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    @classmethod
    def from_point(cls, point: 'Point4D'):
        return Point4D(point.x, point.y, point.z, 0)

    def is_neighbour(self, other: 'Point4D'):
        return self != other and abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1 \
               and abs(self.z - other.z) <= 1 and abs(self.w - other.w) <= 1

    def __eq__(self, other: 'Point4D'):
        return self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w


def parse_input(input_txt: str) -> List[Point]:
    lines = input_txt.strip().split("\n")
    initial_points = []
    for i, line in enumerate(lines):
        y_pos = len(lines) - (i + 1)
        for j, c in enumerate(line):
            initial_points.append(Point(j, y_pos, 0, c == "#"))
    return initial_points


def run_for_n_cycles(initial_points: List[Point], n: int) -> List[Point]:
    x_range = [min(p.x for p in initial_points), max(p.x for p in initial_points) + 1]
    y_range = [min(p.y for p in initial_points), max(p.y for p in initial_points) + 1]
    z_range = [0, 1]

    active_points: List[Point] = [p for p in initial_points if p.active]

    for cycle in range(n):
        new_active_points = []
        # expand the space range
        x_range[0] -= 1
        x_range[1] += 1
        y_range[0] -= 1
        y_range[1] += 1
        z_range[0] -= 1
        z_range[1] += 1
        # check neighbors for each point in the new range
        for x in range(*x_range):
            for y in range(*y_range):
                for z in range(*z_range):
                    new_point = Point(x, y, z)

                    active_neighbour_count = 0
                    old_point = None
                    for point in active_points:
                        if point == new_point:
                            old_point = point
                        elif new_point.is_neighbour(point):
                            active_neighbour_count += 1

                    if old_point is not None and old_point.active:
                        if active_neighbour_count in (2, 3):
                            new_point.active = True
                            new_active_points.append(new_point)
                        continue
                    if active_neighbour_count == 3:
                        new_point.active = True
                        new_active_points.append(new_point)
        active_points = new_active_points
    return active_points


def run_for_n_cycles_4d(initial_points: List[Point], n: int) -> List[Point4D]:
    x_range = [min(p.x for p in initial_points), max(p.x for p in initial_points) + 1]
    y_range = [min(p.y for p in initial_points), max(p.y for p in initial_points) + 1]
    z_range = [0, 1]
    w_range = [0, 1]

    active_points: List[Point4D] = [Point4D.from_point(p) for p in initial_points if p.active]

    for cycle in range(n):
        new_active_points = []
        # expand the space range
        x_range[0] -= 1
        x_range[1] += 1
        y_range[0] -= 1
        y_range[1] += 1
        z_range[0] -= 1
        z_range[1] += 1
        w_range[0] -= 1
        w_range[1] += 1
        # check neighbors for each point in the new range
        for x in range(*x_range):
            for y in range(*y_range):
                for z in range(*z_range):
                    for w in range(*w_range):
                        new_point = Point4D(x, y, z, w)

                        active_neighbour_count = 0
                        old_point = None
                        for point in active_points:
                            if point == new_point:
                                old_point = point
                            elif new_point.is_neighbour(point):
                                active_neighbour_count += 1

                        if old_point is not None:
                            if active_neighbour_count in (2, 3):
                                new_active_points.append(new_point)
                            continue
                        if active_neighbour_count == 3:
                            new_active_points.append(new_point)

        active_points = new_active_points
    return active_points


def a(input_txt: str):
    initial_points = parse_input(input_txt)
    active_points = run_for_n_cycles(initial_points, 6)
    return len(active_points)


def b(input_txt: str):
    initial_points = parse_input(input_txt)
    all_points = run_for_n_cycles_4d(initial_points, 6)
    return len(all_points)


if __name__ == "__main__":
    with open("advent_2020/inputs/17") as f:
        input_text = f.read()
    print("a)", a(input_text))
    print("a bit slow but does the trick (1m40s) could")
    print("b)", b(input_text))
    print("could probably be quicker if we just looked at the neighbours of active points instead of all points in "
          "the maximal space")
