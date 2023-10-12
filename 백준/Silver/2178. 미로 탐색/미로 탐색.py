import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)
def bfs(start_row, start_col):
    deq = deque([[start_row, start_col]])
    
    visited[start_row][start_col] = 1
    
    while deq:
        y, x = deq.popleft()
        current_count = visited[y][x]
        if y == n - 1 and x == m - 1:
            return current_count
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if not maze[ny][nx] or visited[ny][nx]:
                continue
            deq.append([ny, nx])
            visited[ny][nx] = current_count + 1
            
print(bfs(0, 0))