import sys
from collections import deque

input = sys.stdin.readline
m, n, h = map(int, input().split())
matrix = []
dist = []
for _ in range(h):
    tmp = []
    tmp2 = []
    for _ in range(n):
        tmp.append(list(map(int, input().split())))
        tmp2.append([0] * m)
    matrix.append(tmp)
    dist.append(tmp2)
tomatos = []
count = 0

di = (1, -1, 0, 0, 0, 0)
dj = (0, 0, 1, -1, 0, 0)
dk = (0, 0, 0, 0, -1, 1)
def bfs(start_idxs):
    deq = deque(start_idxs)
    max_day = 0
    
    for i, j, k in start_idxs:
        dist[i][j][k] = 1
    
    while deq:
        i, j, k = deq.popleft()
        current_day = dist[i][j][k]
        max_day = max(max_day, current_day)
        for order in range(6):
            ni = i + di[order]
            nj = j + dj[order]
            nk = k + dk[order]
            if ni < 0 or nj < 0 or nk < 0 or ni >= h or nj >= n or nk >= m:
                continue
            if matrix[ni][nj][nk] or dist[ni][nj][nk]:
                continue
            deq.append([ni, nj, nk])
            dist[ni][nj][nk] = current_day + 1
    return max_day - 1
            
for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k] == 1:
                tomatos.append([i, j, k])

count = bfs(tomatos)
for i in range(h):
    for j in range(n):
        for k in range(m):
            if not matrix[i][j][k] and not dist[i][j][k]:
                print(-1)
                sys.exit(0)
print(count)