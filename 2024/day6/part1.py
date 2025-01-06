raw_input = open(0).readlines()
# print(f"{raw_input=}")


map: list[list[int]] = []

for input in raw_input:
    map.append(list(i for i in input.strip()))

# (row, column)

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
        while 0 <= i < len(map) and 0 <= j < len(map[0]):
            if map[i][j] == "#":
                map[i - delta_i][j - delta_j] = new_player
                return
            map[i][j] = "X"
            i += delta_i
            j += delta_j

    for i in range(len(map)):
        for j in range(len(map[i])):
            current_pos = map[i][j]
            if map[i][j] in guard_symbols:
                # Move the player, using the directions of the current position and the next symbol in the guard_symbols list
                move_player(
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


# Check if the symbol > is in the map, loop until it is not
while any(row for row in map if any(c in row for c in ["v", "<", ">", "^"])):
    traverse(map)
    # print_map()

# Loop over map and count the number of X
sum = 0
for row in map:
    sum += row.count("X")
print(f"{sum=}")
