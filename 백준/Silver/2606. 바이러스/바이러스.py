import sys
from collections import deque

input = sys.stdin.readline
V = int(input())
E = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (V + 1)
queue = deque([[0, 1]])
while queue:
    cur_v, target_v = queue.popleft()
    if visited[target_v]:
        continue
    visited[target_v] = 1
    for nxt_v in graph[target_v]:
        queue.append([target_v, nxt_v])

result = visited.count(1)
print(result - 1)