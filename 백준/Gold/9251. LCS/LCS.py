# if A[i] == B[i]:dp[i][j] = dp[i - 1][j - 1] + 1
# if A[i] != B[i]:dp[i][j] = max(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
import sys

input = sys.stdin.readline
A = input().strip()
B = input().strip()
dp = [[0] * len(A) for _ in range(len(B))]
if len(A) == 0 or len(B) == 0:
    print(0)
    sys.exit(0)

if A[0] == B[0]:
    dp[0][0] = 1
flag = dp[0][0]
for i in range(1, len(B)):
    if flag:
        dp[i][0] = 1
        continue
    if A[0] == B[i]:
        dp[i][0] = 1
        flag = True
flag = dp[0][0]
for i in range(1, len(A)):
    if flag:
        dp[0][i] = 1
        continue
    if A[i] == B[0]:
        dp[0][i] = 1
        flag = True

for i in range(1, len(B)):
    for j in range(1, len(A)):
        if A[j] == B[i]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

print(dp[len(B) - 1][len(A) - 1])