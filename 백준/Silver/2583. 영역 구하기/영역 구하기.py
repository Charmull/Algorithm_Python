import sys
from collections import deque

input = sys.stdin.readline
m, n, k = map(int, input().split())
matrix = [[0] * n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            matrix[i][j] = -1

dist = [[-1] * n for _ in range(m)]
count = 0
widths = []

dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)
def bfs(start_row, start_col):
    deq = deque([[start_row, start_col]])
    dist[start_row][start_col] = 1
    width = 1
    while deq:
        y, x = deq.popleft()
        current_dist = dist[y][x]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= m or nx >= n:
                continue
            if matrix[ny][nx] or dist[ny][nx] != -1:
                continue
            deq.append([ny, nx])
            dist[ny][nx] = current_dist + 1
            width += 1
    return width
            
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0 and dist[i][j] == -1:
            count += 1
            widths.append(bfs(i, j))
print(count)
print(' '.join(map(str, sorted(widths))))