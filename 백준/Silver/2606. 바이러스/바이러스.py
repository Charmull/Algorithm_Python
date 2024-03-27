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

group = set([1])
deq = deque([1])
visited = [0] * (n + 1)
visited[1] = 1
while deq:
    x = deq.popleft()
    for nx in graph[x]:
        if nx == x:
            continue
        if visited[nx]:
            continue
        group.add(nx)
        visited[nx] = 1
        deq.append(nx)

print(len(list(group)) - 1)