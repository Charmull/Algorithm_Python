import sys

input = sys.stdin.readline
h, w = map(int, input().split())
board = [list(input().strip()) for _ in range(h)]
result = 0
for i in range(h):
    line = 0 # /이나 \이 등장한 개수
    for j in range(w):
        el = board[i][j]
        if el == '/' or el == '\\':
            line += 1
        if el == '.' and line % 2: # /이나 \이 홀수번 등장했고, 이번 값이 .이면 도형 내부의 .임
            result += 1
    result += line // 2
print(result)