# dp로 A의 부배열의 합, B의 부배열의 합 구하기
# 각 부 배열의 합 개수 딕셔너리에 저장
import sys

input = sys.stdin.readline
t = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
dp_A = [[0] * n for _ in range(n)]
dp_B = [[0] * m for _ in range(m)]
dict_A = dict()
dict_B = dict()


def initial_dp(dp, dic, nums, n):
    for i in range(n):
        if not i:
            dp[0][i] = nums[i]
            dic[dp[0][i]] = 1
            continue
        dp[0][i] = dp[0][i - 1] + nums[i]
        if dp[0][i] in dic:
            dic[dp[0][i]] += 1
        else:
            dic[dp[0][i]] = 1


def make_dp(dp, dic, nums, n):
    for i in range(1, n):
        for j in range(i, n):
            dp[i][j] = dp[i - 1][j] - dp[i - 1][i - 1]
            if dp[i][j] in dic:
                dic[dp[i][j]] += 1
            else:
                dic[dp[i][j]] = 1


initial_dp(dp_A, dict_A, A, n)
initial_dp(dp_B, dict_B, B, m)
make_dp(dp_A, dict_A, A, n)
make_dp(dp_B, dict_B, B, m)

result = 0
for k, v in dict_A.items():
    if t - k in dict_B:
        result += v * dict_B[t - k]

print(result)