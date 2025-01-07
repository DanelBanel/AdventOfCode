raw_input = open(0).readlines()
left = []
right = []
for input in raw_input:
    a, b = map(int, input.split())
    left.append(a)
    right.append(b)

total = 0
for element in left:
    occurences = right.count(element)
    total += occurences * element
print(total)
