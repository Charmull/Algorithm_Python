# DP
import sys

input = sys.stdin.readline
N = int(input())
dp_min = list(map(int, input().split()))
dp_max = [el for el in dp_min]

for i in range(1, N):
    origin = list(map(int, input().split()))
    dp_min_0 = min(dp_min[0], dp_min[1]) + origin[0]
    dp_min_1 = min(dp_min[0], dp_min[1], dp_min[2]) + origin[1]
    dp_min_2 = min(dp_min[1], dp_min[2]) + origin[2]

    dp_max_0 = max(dp_max[0], dp_max[1]) + origin[0]
    dp_max_1 = max(dp_max[0], dp_max[1], dp_max[2]) + origin[1]
    dp_max_2 = max(dp_max[1], dp_max[2]) + origin[2]

    dp_min = [dp_min_0, dp_min_1, dp_min_2]
    dp_max = [dp_max_0, dp_max_1, dp_max_2]

print(max(dp_max), min(dp_min))