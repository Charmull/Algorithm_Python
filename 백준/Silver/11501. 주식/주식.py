import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    mn = lst[n - 1]
    result = 0

    for i in range(n - 2, -1, -1):
        if mn < lst[i]:
            mn = lst[i]
            continue
        result += (mn - lst[i])
    print(result)