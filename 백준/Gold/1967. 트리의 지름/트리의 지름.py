import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)

input = sys.stdin.readline
n = int(input())
graph = defaultdict(list)
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dfs(node, cost):
    for nxt, nxt_cost in graph[node]:
        if visited[nxt] != -1:
            continue
        visited[nxt] = cost + nxt_cost
        dfs(nxt, cost + nxt_cost)

visited = [-1] * (n + 1)
visited[1] = 0
dfs(1, 0)

a = visited.index(max(visited))
visited = [-1] * (n + 1)
visited[a] = 0
dfs(a, 0)
print(max(visited))