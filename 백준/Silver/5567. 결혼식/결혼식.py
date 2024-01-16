import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = -1
visited = [0] * (n + 1)
q = deque([[0, 1, 0]])  # (현재, 친구, 1과의 촌)
while q:
    cur, frd, t = q.popleft()
    if t >= 3:
        break
    if visited[frd]:
        continue
    visited[frd] = 1
    cnt += 1
    for nxt_frd in graph[frd]:
        if visited[nxt_frd]:
            continue
        q.append([frd, nxt_frd, t + 1])

print(cnt)