import sys
from copy import deepcopy

input = sys.stdin.readline
n, m, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
result_time = n * m * 256 * 2
result_level = 0

for i in range(257):
    use_num = 0
    get_num = 0
    for j in range(n):
        for k in range(m):
            if matrix[j][k] > i:
                get_num += matrix[j][k] - i
            else:
                use_num += i - matrix[j][k]
    if use_num > get_num + b:
        break
    time = use_num + get_num * 2
    if result_time >= time:
        result_time = time
        result_level = i

print(result_time, result_level)