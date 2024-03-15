# left_dp[i] = 0 ~ i-1 위치의 num이 i 위치 num보다 작으면, left_dp[0 ~ i-1] + 1한 값 중 최대값이 left_dp[i]
# right_dp[i] = left_dp와 동일하게 작동, 다만 n-1번째 요소부터 진행

import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))


def make_dp(start, end, step):
    dp = [1] * n
    for i in range(start, end, step):
        for j in range(start, i, step):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    return dp


left_dp = make_dp(0, n, 1)
right_dp = make_dp(n - 1, -1, -1)

result = 0
for i in range(n):
    if result < left_dp[i] + right_dp[i] - 1:
        result = left_dp[i] + right_dp[i] - 1

print(result)