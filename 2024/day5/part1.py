raw_input = open(0).readlines()

page_ordering_rules: list[tuple] = []
pages: list[int] = []
for input in raw_input:
    print(f"{input=}")
    if "|" in input:
        a, b = map(int, input.split("|"))
        page_ordering_rules.append((a, b))
    elif input == "\n":
        continue
    else:
        print(f"{input.split(",")=}")
        page = list(map(int, input.split(",")))
        pages.append(page)

print(f"{page_ordering_rules=}")
print(f"{pages=}")
cache = {}
for x,y in page_ordering_rules:
    cache[(x,y)]   = True
    cache[(y,x)] = False

def is_ordered(page: list[int]) -> bool:
    for i in range(len(page)):
        for j in range(i + 1, len(page)):
            if (page[i], page[j]) in cache and not cache[(page[i], page[j])]:
                print("NO")
                return False
    print("YES")
    print(f"{page[len(page) // 2]}")
    return True
sum = 0
for page in pages:
    print(f"{page=}")
    if is_ordered(page):
        sum += page[len(page) // 2]

print(f"{sum=}")