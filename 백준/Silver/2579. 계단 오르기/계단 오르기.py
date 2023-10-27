import sys

input = sys.stdin.readline
n = int(input())
stair = [0]
for _ in range(n):
    stair.append(int(input()))

if n == 1:
    print(stair[1])
    sys.exit(0)
    
d = [[0] * 3 for _ in range(n + 1)]
d[1][1] = stair[1]
d[1][2] = 0
d[2][1] = stair[2]
d[2][2] = stair[1] + stair[2]
for i in range(3, n + 1):
    d[i][1] = max(d[i - 2][1], d[i - 2][2]) + stair[i]
    d[i][2] = d[i - 1][1] + stair[i]
    
print(max(d[n][1], d[n][2]))