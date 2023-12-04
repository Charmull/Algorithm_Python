import sys

input = sys.stdin.readline
n, p = map(int, input().split())
arr = [n]
idx = -1
while idx == -1:
    tmp = arr[-1]
    cur = 0
    while tmp:
        cur += (tmp % 10) ** p
        tmp //= 10

    for i in range(len(arr)):
        if arr[i] == cur:
            idx = i
            break
    arr.append(cur)
print(i)