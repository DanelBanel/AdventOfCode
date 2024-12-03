raw_input = open(0).readlines()

total = 0


for input in raw_input:
    levels = list(map(int, input.split()))
    valid = False
    # Test all possible mutations of levels
    for l_i in range(len(levels)):
        levels_mut = levels[0:l_i] + levels[l_i+1:]
        if all(0 < abs(levels_mut[l_idx] - levels_mut[l_idx - 1]) and abs(levels_mut[l_idx] - levels_mut[l_idx - 1]) <= 3 for l_idx in range(1, len(levels_mut))) and (levels_mut == sorted(levels_mut, reverse=True) or levels_mut == sorted(levels_mut)):
            valid = True
    # Test default levels
    if all(0 < abs(levels[l_idx] - levels[l_idx - 1]) and abs(levels[l_idx] - levels[l_idx - 1]) <= 3 for l_idx in range(1, len(levels))) and (levels == sorted(levels, reverse=True) or levels == sorted(levels)):
        valid = True
    if valid:
        total += 1


print(total)