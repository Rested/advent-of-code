class TreeMap:
    # origin is the top left
    def __init__(self, rows, line_length):
        self.rows = rows
        self.line_length = line_length

    def __getitem__(self, item):
        return self.rows[item[1]][item[0] % self.line_length]


def parse_map(map_text: str):
    rows = []
    line_length = None
    for line in map_text.split("\n"):
        if line:
            if line_length is None:
                line_length = len(line)
            rows.append(line)
    return TreeMap(rows=rows, line_length=line_length)


def a(tree_map: TreeMap, direction_vector=(3, 1)):
    current_position = [0, 0]

    tree_count = 0
    while True:
        try:
            if tree_map[current_position] == "#":
                tree_count += 1
            current_position[0] += direction_vector[0]
            current_position[1] += direction_vector[1]
        except IndexError:
            return tree_count


def b(tree_map: TreeMap):
    cases = (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    )
    answer = None
    for case in cases:
        trees_hit = a(tree_map, case)
        print(f"with direction vector {case} we hit {trees_hit} trees")
        if answer is None:
            answer = trees_hit
        else:
            answer *= trees_hit
    return answer


if __name__ == '__main__':
    with open("advent_2020/inputs/3") as f:
        real_tree_map = parse_map(f.read())

    print("a)", a(real_tree_map))
    print("b)", b(real_tree_map))
