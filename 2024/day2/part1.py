raw_input = open(0).readlines()

total = 0


for input in raw_input:
    levels = list(map(int, input.split()))
    print(levels)
    valid = True
    for l_idx in range(1, len(levels)):
        if (
            0 >= abs(levels[l_idx] - levels[l_idx - 1])
            or abs(levels[l_idx] - levels[l_idx - 1]) > 3
        ):
            valid = False
        if levels != sorted(levels, reverse=True) and levels != sorted(levels):
            valid = False
    if valid:
        print(levels)
        total += 1


print(total)
