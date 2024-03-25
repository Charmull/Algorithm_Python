# 1. /나 \가 홀수번 들어온 시점은 도형 내부
# 2. /나 \는 0.5, .는 1
import sys

input = sys.stdin.readline
h, w = map(int, input().split())
board = [list(input().strip()) for _ in range(h)]
result = 0
for i in range(h):
    flag = False  # /이나 \ 홀수번 들어왔나
    for j in range(w):
        el = board[i][j]
        if el == '/' or el == '\\':
            result += 0.5
            flag = not flag
            continue
        if flag and el == '.':
            result += 1
print(int(result) if int(result) == result else result)