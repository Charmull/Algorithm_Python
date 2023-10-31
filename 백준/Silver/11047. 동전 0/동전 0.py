import sys

input = sys.stdin.readline
n, k = map(int, input().split())
kind = [int(input()) for _ in range(n)]

result = 0
for i in range(n - 1, -1, -1):
    result += k // kind[i]
    k %= kind[i]

print(result)