import sys

input = sys.stdin.readline
n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

dp_R = [[float('inf')] * 3 for _ in range(n)]
dp_G = [[float('inf')] * 3 for _ in range(n)]
dp_B = [[float('inf')] * 3 for _ in range(n)]

dp_R[0][0] = cost[0][0]
dp_G[0][1] = cost[0][1]
dp_B[0][2] = cost[0][2]

for i in range(1, n):
    dp_R[i][0] = min(dp_R[i - 1][1], dp_R[i - 1][2]) + cost[i][0]
    dp_R[i][1] = min(dp_R[i - 1][0], dp_R[i - 1][2]) + cost[i][1]
    dp_R[i][2] = min(dp_R[i - 1][0], dp_R[i - 1][1]) + cost[i][2]

    dp_G[i][0] = min(dp_G[i - 1][1], dp_G[i - 1][2]) + cost[i][0]
    dp_G[i][1] = min(dp_G[i - 1][0], dp_G[i - 1][2]) + cost[i][1]
    dp_G[i][2] = min(dp_G[i - 1][0], dp_G[i - 1][1]) + cost[i][2]

    dp_B[i][0] = min(dp_B[i - 1][1], dp_B[i - 1][2]) + cost[i][0]
    dp_B[i][1] = min(dp_B[i - 1][0], dp_B[i - 1][2]) + cost[i][1]
    dp_B[i][2] = min(dp_B[i - 1][0], dp_B[i - 1][1]) + cost[i][2]

result = min(dp_R[n - 1][1], dp_R[n - 1][2], dp_G[n - 1][0],
             dp_G[n - 1][2], dp_B[n - 1][0], dp_B[n - 1][1])

print(result)