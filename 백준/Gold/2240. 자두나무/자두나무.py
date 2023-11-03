import sys

input = sys.stdin.readline
t, w = map(int, input().split())
jadu = [0] + [int(input()) for _ in range(t)]
dp = [[0] * (w + 1) for _ in range(t + 1)]

for i in range(1, t + 1):
    if jadu[i] == 1:
        dp[i][0] = dp[i - 1][0] + 1
    else:
        dp[i][0] = dp[i - 1][0]
        
    for j in range(1, w + 1):
        if jadu[i] == 1 and not j % 2:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + 1
        elif jadu[i] == 2 and j % 2:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])
            
print(max(dp[t]))