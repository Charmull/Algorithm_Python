import sys

input = sys.stdin.readline
n = int(input())
schj = [list(map(int, input().split())) for _ in range(n)]
arr = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    if schj[i][0] + i > n:
        arr[i] = arr[i + 1]
        continue
    arr[i] = max(arr[i + schj[i][0]] + schj[i][1], arr[i + 1])
    
print(max(arr))