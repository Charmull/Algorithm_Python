import sys
from collections import deque

input = sys.stdin.readline
t = int(input())

dy = (1, 0, 0, -1)
dx = (0, -1, 1, 0)
def bfs(m, n, f_starts, s_start, maze):
    f_deq = deque(f_starts)
    f_dist = [[-1] * m for _ in range(n)]
    s_deq = deque([s_start])
    s_dist = [[-1] * m for _ in range(n)]
    is_escape = False
    
    for y, x in f_starts:
        f_dist[y][x] = 0
    while f_deq:
        y, x = f_deq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if maze[ny][nx] == "#" or f_dist[ny][nx] != -1:
                continue
            f_deq.append([ny, nx])
            f_dist[ny][nx] = f_dist[y][x] + 1
            
    s_dist[s_start[0]][s_start[1]] = 0
    while s_deq:
        y, x = s_deq.popleft()
        current_time = s_dist[y][x]
        if y == 0 or y == n -1 or x == 0 or x == m -1:
            print(current_time + 1)
            is_escape = True
            break
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if maze[ny][nx] != "." or s_dist[ny][nx] != -1:
                continue
            if f_dist[ny][nx] != -1 and f_dist[ny][nx] <= current_time + 1:
                continue
            s_deq.append([ny, nx])
            s_dist[ny][nx] = current_time + 1
            
    return is_escape

for _ in range(t):
    m, n = map(int, input().split())
    maze = [list(input().strip()) for _ in range(n)]
    f_start = []
    s_start = []
    for i in range(n):
        for j in range(m):
            if maze[i][j] == "*":
                f_start.append([i, j])
            if maze[i][j] == "@":
                s_start = [i, j]
    if not bfs(m, n, f_start, s_start, maze):
        print("IMPOSSIBLE")