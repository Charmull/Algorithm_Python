import sys
from collections import defaultdict

input = sys.stdin.readline
r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]

visited = set()
result = [0]

dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)
def dfs(y, x, cnt):
    result[0] = max(result[0], cnt)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= r or nx >= c:
            continue
        if board[ny][nx] in visited:
            continue
        visited.add(board[ny][nx])
        dfs(ny, nx, cnt + 1)
        visited.remove(board[ny][nx])


visited.add(board[0][0])
dfs(0, 0, 1)
print(result[0])