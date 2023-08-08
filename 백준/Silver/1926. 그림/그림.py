import sys
from collections import deque

def bfs(start_row, start_col):
    deq = deque([[start_row, start_col]])
    local_width = 0
    
    visited[start_row][start_col] = True
    
    while deq:
        y, x = deq.popleft()
        local_width += 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if visited[ny][nx] or matrix[ny][nx] == 0:
                continue
            deq.append([ny, nx])
            visited[ny][nx] = True
            
    return local_width

n, m = map(int, sys.stdin.readline().split())
count = 0
width = 0

visited = [[False] * m for _ in range(n)]
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dy = (-1, 0, 1, 0)
dx = (0, -1, 0, 1)
            
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1 and not visited[i][j]:
            count += 1
            width = max(bfs(i, j), width)

print(count)
print(width)