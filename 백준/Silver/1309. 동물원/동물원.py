import sys
input = sys.stdin.readline
n = int(input())
if n == 1:
    print(3)
    sys.exit(0)
dp = [0] * n
dp[0] = 1
dp[1] = 2
for i in range(2, n):
    dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % 9901
print((sum(dp) * 2 + 1) % 9901)