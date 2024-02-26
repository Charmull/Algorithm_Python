# 1. dp[i][j] = 문자열A의 i번째 문자와 문자열B의 j번째 문자까지 고려했을 때 최대 길이
# 2. dp[i][j] = dp[i - 1][j - 1] + 1 (단, A[i] == B[j])
#    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) (단, A[i] != B[j])
import sys

input = sys.stdin.readline
A = input().strip()
B = input().strip()
dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            
print(dp[len(A)][len(B)])