import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
result = n * m

dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)
def bfs(start_row, start_col):
    deq = deque([[start_row, start_col]])
    dist[start_row][start_col] = 1
    
    while deq:
        y, x = deq.popleft()
        current_dist = dist[y][x]
        if x == m - 1 and y == n - 1:
            result = current_dist
            print(result)
            break
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if dist[ny][nx] != -1 or graph[ny][nx] == '0':
                continue
            deq.append([ny, nx])
            dist[ny][nx] = current_dist + 1

bfs(0, 0)