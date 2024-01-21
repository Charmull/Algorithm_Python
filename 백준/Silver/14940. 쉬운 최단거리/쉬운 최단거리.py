import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
result = [[-1] * m for _ in range(n)]

def find_start():
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                return i, j

dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)
def bfs(start_row, start_col):
    deq = deque([[start_row, start_col]])
    result[start_row][start_col] = 0

    while deq:
        y, x = deq.popleft()
        cur_dist = result[y][x]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if board[ny][nx] == 0:
                result[ny][nx] = 0
                continue
            if result[ny][nx] != -1:
                continue
            result[ny][nx] = cur_dist + 1
            deq.append([ny, nx])

bfs(*find_start())

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            result[i][j] = 0

for row in result:
    print(' '.join(map(str, row)))