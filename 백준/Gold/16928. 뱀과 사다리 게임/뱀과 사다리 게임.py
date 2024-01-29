# 1. 맵 만들기
#    1.1. 사다리, 뱀 딕셔너리 관리
# 2. BFS
import sys
from collections import deque, defaultdict

input = sys.stdin.readline
N, M = map(int, input().split())
event = defaultdict(int)
for _ in range(N):
    x, y = map(int, input().split())
    event[x] = y
for _ in range(M):
    u, v = map(int, input().split())
    event[u] = v

dx = (1, 2, 3, 4, 5, 6)
def bfs():
    deq = deque([1])
    dist = [-1] * 101
    dist[1] = 0

    while deq:
        x = deq.popleft()
        cur_cnt = dist[x]
        if x == 100:
            return cur_cnt

        for i in range(6):
            nx = x + dx[i]
            if event[nx]:
                nx = event[nx]

            if nx <= 0 or nx >= 101:
                continue
            if dist[nx] != -1:
                continue

            deq.append(nx)
            dist[nx] = cur_cnt + 1


result = bfs()
print(result)