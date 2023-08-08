import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)
def bfs(start_points):
    deq = deque(start_points)
    result = 0
    
    for point_y, point_x in start_points:
        dist[point_y][point_x] = 0
    
    while deq:
        y, x = deq.popleft()
        current_dist = dist[y][x]
        result = max(current_dist, result)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if dist[ny][nx] != -1 or matrix[ny][nx] == -1:
                continue
            deq.append([ny, nx])
            dist[ny][nx] = current_dist + 1
    
    return result

start_points= []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            start_points.append([i, j])
result = bfs(start_points)

for i in range(n):
    for j in range(m):
        if dist[i][j] == -1 and matrix[i][j] != -1:
            print(-1)
            sys.exit(0)
print(result)