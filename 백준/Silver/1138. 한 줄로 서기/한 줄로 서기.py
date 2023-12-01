import sys

input = sys.stdin.readline
n = int(input())
count = list(map(int, input().split()))

result = [0] * n

for i in range(n):
    num = i + 1
    where = count[i]
    cnt = 0
    for j in range(where):
        if not result[j] or num < result[j]:
            cnt += 1
    while result[where]:
        where += 1

    while cnt < count[i]:
        where += 1
        if not result[where] or num < result[where]:
            cnt += 1

    result[where] = num
print(' '.join(map(str, result)))