import sys

input = sys.stdin.readline
n = int(input())
cost = [[0, 0, 0]]
for _ in range(n):
    cost.append(list(map(int, input().split())))
    
d = [[0] * 3 for _ in range(n + 1)]
d[1][0] = cost[1][0]
d[1][1] = cost[1][1]
d[1][2] = cost[1][2]
for i in range(2, n + 1):
    d[i][0] = min(d[i - 1][1], d[i - 1][2]) + cost[i][0]
    d[i][1] = min(d[i - 1][0], d[i - 1][2]) + cost[i][1]
    d[i][2] = min(d[i - 1][0], d[i - 1][1]) + cost[i][2]
    
print(min(d[n][0], d[n][1], d[n][2]))