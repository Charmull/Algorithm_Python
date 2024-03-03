# 1. 벽 세우기
# 2. 바이러스 퍼뜨리기
# 3. 안전지대 세기
import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
origin = [list(map(int, input().split())) for _ in range(n)]
birus = []
result = [0]

for i in range(n):
    for j in range(m):
        if origin[i][j] == 2:
            birus.append([i, j])


yx_list = []
for i in range(n):
    for j in range(m):
        if origin[i][j]:
            continue
        yx_list.append((i, j))

yx_list_visited = [0] * len(yx_list)
def build(idx, cnt):
    if cnt == 3:
        result[0] = max(result[0], bfs())
        return

    for i in range(idx, len(yx_list)):
        cur = yx_list[i]
        if origin[cur[0]][cur[1]]:
            continue
        origin[cur[0]][cur[1]] = 1
        build(i + 1, cnt + 1)
        origin[cur[0]][cur[1]] = 0


dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)
def bfs():
    deq = deque(birus)
    dist = [[0] * m for _ in range(n)]
    for y, x in birus:
        dist[y][x] = 1

    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if origin[ny][nx] or dist[ny][nx]:
                continue
            deq.append([ny, nx])
            dist[ny][nx] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if not origin[i][j] and not dist[i][j]:
                cnt += 1
    return cnt

build(0, 0)
print(result[0])