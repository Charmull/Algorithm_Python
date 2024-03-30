import sys

input = sys.stdin.readline
a = input().strip()
b = input().strip()
len_a = len(a)
len_b = len(b)
dp = [[0] * len_b for _ in range(len_a)]
# [i, j, k] -> i행 j열의 lcs에 k 추가
prev = [[[-1, -1, ''] for _ in range(len_b)] for _ in range(len_a)]

flag = False
for i in range(len_b):
    if flag or a[0] == b[i]:
        dp[0][i] = 1
        prev[0][i][2] = a[0]
        flag = True

flag = False
for i in range(len_a):
    if flag or a[i] == b[0]:
        dp[i][0] = 1
        prev[i][0][2] = b[0]
        flag = True

for i in range(1, len_a):
    for j in range(1, len_b):
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            prev[i][j] = [i - 1, j - 1, a[i]]
            continue
        if dp[i - 1][j] >= dp[i][j - 1]:
            dp[i][j] = dp[i - 1][j]
            prev[i][j] = [i - 1, j, '']
            continue
        dp[i][j] = dp[i][j - 1]
        prev[i][j] = [i, j - 1, '']

cnt = dp[len_a - 1][len_b - 1]
print(cnt)
if cnt:
    result = ''
    i, j, k = prev[len_a - 1][len_b - 1]
    while True:
        if k:
            result = k + result
        if i == -1 or j == -1:
            break
        i, j, k = prev[i][j]
    print(result)