import sys
from collections import deque

input = sys.stdin.readline
m, n, h = map(int, input().split())
graph = []
dist = []
for i in range(h):
    temp_g = []
    temp_d = []
    for j in range(n):
        temp_g.append(list(map(int, input().split())))
        temp_d.append([-2] * m)
    graph.append(temp_g)
    dist.append(temp_d)
    
start_points = []
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                start_points.append([i, j, k])
                
di = (1, -1, 0, 0, 0, 0)
dj = (0, 0, 1, 0, 0, -1)
dk = (0, 0, 0, 1, -1, 0)
def bfs(start_points):
    deq = deque(start_points)
    for i, j, k in start_points:
        dist[i][j][k] = 0
    day = 0
    
    while deq:
        i, j, k = deq.popleft()
        current_day = dist[i][j][k]
        day = max(day, current_day)
        for num in range(6):
            ni = i + di[num]
            nj = j + dj[num]
            nk = k + dk[num]
            if ni < 0 or nj < 0 or nk < 0 or ni >= h or nj >= n or nk >= m:
                continue
            if graph[ni][nj][nk] == -1:
                dist[ni][nj][nk] = -1
                continue
            if graph[ni][nj][nk] != 0 or dist[ni][nj][nk] != -2:
                continue
            deq.append([ni, nj, nk])
            dist[ni][nj][nk] = current_day + 1
    return day

result = bfs(start_points)
for i in range(h):
    for j in range(n):
        for k in range(m):
            if dist[i][j][k] == -2 and graph[i][j][k] == 0:
                print(-1)
                sys.exit(0)
print(result)