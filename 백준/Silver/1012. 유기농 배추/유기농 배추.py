import sys
from collections import deque

input = sys.stdin.readline
t = int(input().strip())

dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)
def bfs(matrix, visited, start_row, start_col, n, m):
    deq = deque([[start_row, start_col]])
    
    visited[start_row][start_col] = 1
    
    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if not matrix[ny][nx] or visited[ny][nx]:
                continue
            deq.append([ny, nx])
            visited[ny][nx] = 1
            
for _ in range(t):
    m, n, k = map(int, input().split())
    matrix = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        matrix[y][x] = 1
    
    visited = [[0] * m for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and not visited[i][j]:
                bfs(matrix, visited, i, j, n, m)
                count += 1
    print(count)