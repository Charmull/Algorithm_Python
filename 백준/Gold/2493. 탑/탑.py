import sys

input = sys.stdin.readline
n = int(input())
heights = list(map(int, input().split()))
group = []
result = []

for idx, height in enumerate(heights):
    is_meet = False
    while group:
        if group[-1][1] < height:
            group.pop()
            continue
        result.append(group[-1][0])
        group.append((idx + 1, height))
        is_meet = True
        break
    if not is_meet:
        result.append(0)
        group.append((idx + 1, height))

print(' '.join(map(str, result)))