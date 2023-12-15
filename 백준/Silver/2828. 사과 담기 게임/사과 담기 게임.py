import sys

input = sys.stdin.readline
n, m = map(int, input().split())
j = int(input())
apples = [int(input()) for _ in range(j)]
bowl = [1, m]
result = 0
for i in range(j):
    if bowl[0] <= apples[i] <= bowl[1]:
        continue
    while bowl[0] > apples[i]:
        bowl[0] -= 1
        bowl[1] -= 1
        result += 1
    while bowl[1] < apples[i]:
        bowl[0] += 1
        bowl[1] += 1
        result += 1
print(result)