raw_input = open(0).readlines()
# print(f"{raw_input=}")


map: list[list[int]] = []

for input in raw_input:
    map.append(list(i for i in input.strip()))

# (row, column)
rows = len(map)
columns = len(map[0])

guard_symbols = [
    "^",
    ">",
    "v",
    "<",
]
directons_dict = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def traverse(map):
    def move_player(map, start_i, start_j, delta, new_player):
        delta_i, delta_j = delta
        i, j = start_i, start_j
        while True:
            seen.add((i, j, delta_i, delta_j))
            if (
                i + delta_i < 0
                or i + delta_i >= rows
                or j + delta_j < 0
                or j + delta_j >= columns
            ):
                return False
            if map[i + delta_i][j + delta_j] == "#":
                # map[i - delta_i][j - delta_j] = new_player
                delta_j, delta_i = -delta_i, delta_j
            else:
                i += delta_i
                j += delta_j
            if (i, j, delta_i, delta_j) in seen:
                return True
        return False

    while any(row for row in map if any(c in row for c in ["v", "<", ">", "^"])):
        for i in range(rows):
            for j in range(columns):
                current_pos = map[i][j]
                if current_pos in guard_symbols:
                    # Move the player, using the directions of the current position and the next symbol in the guard_symbols list
                    seen = set()
                    return move_player(
                        map,
                        i,
                        j,
                        directons_dict[current_pos],
                        guard_symbols[
                            (guard_symbols.index(current_pos) + 1) % len(guard_symbols)
                        ],
                    )


def print_map():
    print("------------")
    for row in map:
        print("".join(row))
    print("------------")


traverse(map)
# Check if the symbol > is in the map, loop until it is not
# traverse(map)
sum = 0
for i in range(rows):
    for j in range(columns):
        if map[i][j] != ".":
            continue
        map[i][j] = "#"
        if traverse(map):
            sum += 1
        map[i][j] = "."
print_map()

print(f"{sum=}")
