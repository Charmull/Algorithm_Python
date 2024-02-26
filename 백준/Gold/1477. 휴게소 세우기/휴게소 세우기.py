import sys
from math import ceil
from collections import defaultdict

input = sys.stdin.readline
n, m, l = map(int, input().split())
store = [0] + list(map(int, input().split())) + [l]
store.sort()
diff = [store[i + 1] - store[i] for i in range(n + 1)]

dp = [[i] * (n + m + 1) for i in range(l + 1)]
for i in range(l + 1):
    for j in range(1, n + m + 1):
        dp[i][j] = ceil(i / (j + 1))

result = [float('inf')]

memo = [[0] * (m + 1) for _ in range(n + 2)]
def dfs(m, idx):
    if idx >= n + 1:
        return 0
    if not m:
        return max(diff[idx:])
    if not memo[idx][m]:
        result = float('inf')
        for i in range(m + 1):
            result = min(result, max(dfs(m - i, idx + 1), dp[diff[idx]][i]))
        memo[idx][m] = result
    else:
        result = memo[idx][m]

    return result

print(dfs(m, 0))