# DP
# dp[i][j] = i번째 수부터 j번째 수까지가 펠린드롬인가
# dp[i][j] = dp[i + 1][j - 1]이 True고, num[i] == num[j]면 True
# dp[i][j] = dp[i + 1][j - 1]이 False거나, num[i] != num[j]면 False

# dp[i][i] = True
# i = n부터 1씩 마이너스, j = i부터 1씩 플러스

import sys

input = sys.stdin.readline

N = int(input())
nums = [0] + list(map(int, input().split()))
M = int(input())
dp = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N, 0, -1):
    for j in range(i, N + 1, 1):
        if i == j:  # i부터 i까지 -> 한자리수 팰린드롬
            dp[i][j] = 1
            continue
        elif i + 1 > j - 1:  # i + 1 == j -> 두자리수
            dp[i][j] = 1 if nums[i] == nums[j] else 0
            continue
        if dp[i + 1][j - 1] and nums[i] == nums[j]:
            dp[i][j] = 1
            continue
for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S][E])