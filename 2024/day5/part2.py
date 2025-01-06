import functools


raw_input = open(0).readlines()

page_ordering_rules: list[tuple] = []
pages: list[int] = []

# Parse input
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

# Create a cache for the ordering rules
cache = {}
for x, y in page_ordering_rules:
    cache[(x, y)] = -1
    cache[(y, x)] = 1


def is_ordered(page: list[int]) -> bool:
    # Check if the page is ordered
    for i in range(len(page)):
        for j in range(i + 1, len(page)):
            if (page[i], page[j]) in cache and cache[(page[i], page[j])] == 1:
                return False
    return True


# Loop over pages and check if they are not ordered, sort them by the cache and add the middle element to sum
sum = 0
for page in pages:
    if is_ordered(page):
        continue
    page.sort(key=functools.cmp_to_key(lambda x, y: cache.get((x, y), 0)))
    sum += page[len(page) // 2]

print(f"{sum=}")
