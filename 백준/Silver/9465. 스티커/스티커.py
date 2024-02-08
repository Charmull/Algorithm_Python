# 1. DP

import sys

input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0], dp[0][1] = board[0][0], board[1][0]
    if n >= 2:
        dp[1][0] = max(dp[0][1] + board[0][1], dp[0][0])
        dp[1][1] = max(dp[0][0] + board[1][1], dp[0][1])

    for i in range(2, n):
        dp[i][0] = max(dp[i - 1][1] + board[0][i], max(dp[i - 2]) + board[0][i])
        dp[i][1] = max(dp[i - 1][0] + board[1][i], max(dp[i - 2]) + board[1][i])

    print(max(dp[n - 1]))