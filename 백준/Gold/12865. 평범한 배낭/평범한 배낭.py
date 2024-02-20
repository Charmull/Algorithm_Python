# 1. dp[i][w] = i번째 물건을 고려해 w 무게까지 담는 최대 가치
# 2. 배낭에 i번째 물건 넣을 수 있음 -> max(dp[i-1][w], dp[i-1][w-물건i무게] + 물건i무게)
# 3. 배낭에 i번째 물건 넣을 수 없음 -> dp[i-1][w]
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
obj = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(K + 1):
    dp[0][i] = 0
for i in range(N + 1):
    dp[i][0] = 0

for i in range(1, N + 1):
    for w in range(1, K + 1):
        if obj[i][0] <= w:
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - obj[i][0]] + obj[i][1])
        else:
            dp[i][w] = dp[i - 1][w]
            
print(dp[N][K])