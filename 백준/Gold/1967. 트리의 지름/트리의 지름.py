import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
graph = defaultdict(list)
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dfs(node, cost):
    stack = [(node, cost)]
    while stack:
        cur, cur_cost = stack.pop()
        for nxt, nxt_cost in graph[cur]:
            if visited[nxt] != -1:
                continue
            visited[nxt] = cur_cost + nxt_cost
            stack.append((nxt, cur_cost + nxt_cost))

visited = [-1] * (n + 1)
visited[1] = 0
dfs(1, 0)

a = visited.index(max(visited))
visited = [-1] * (n + 1)
visited[a] = 0
dfs(a, 0)
print(max(visited))