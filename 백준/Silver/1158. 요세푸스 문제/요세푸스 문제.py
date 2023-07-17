n, k = map(int, input().split())
circle = [i for i in range(1, n + 1)]
pointer = k - 1
result = []

while circle:
    if pointer >= len(circle): pointer %= len(circle)
    result.append(circle[pointer])
    del circle[pointer]
    pointer += k - 1

print('<', ', '.join(map(str, result)), '>', sep='')