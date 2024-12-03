raw_input = open(0).readlines()
left = []
right = []
for input in raw_input:
    a, b = map(int, input.split())
    left.append(a)
    right.append(b)   

total = 0
for l in left:
    occurences = right.count(l)
    total += occurences * l
print(total)