import sys

n, k = map(int, sys.stdin.readline().split())
arr = [1] * (n + 1)
count = 0
for i in range(2, n + 1):
    j = 1
    while i * j <= n:
        if arr[i * j]:
            arr[i * j] = 0
            count += 1
            if count == k:
                print(i * j)
                break
        j += 1