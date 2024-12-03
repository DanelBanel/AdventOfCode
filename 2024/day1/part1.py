raw_input = open(0).readlines()
left = []
right = []
for input in raw_input:
    a, b = map(int, input.split())
    left.append(a)
    right.append(b)   
left.sort()
right.sort()
total = 0
for i in range(len(left)):
    total += abs(left[i] - right[i])
print(total)