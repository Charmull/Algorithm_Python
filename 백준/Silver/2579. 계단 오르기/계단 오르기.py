import sys

input = sys.stdin.readline
n = int(input())
stair = [0]
for _ in range(n):
    stair.append(int(input()))

if n <= 2:
    print(sum(stair))
    sys.exit(0)

d = [0] * (n + 1)
d[1] = stair[1]
d[2] = stair[1] + stair[2]
d[3] = max(stair[2] + stair[3], stair[1] + stair[3])
for i in range(4, n + 1):
    d[i] = max(d[i - 3] + stair[i - 1] + stair[i], d[i - 2] + stair[i])

print(d[n])