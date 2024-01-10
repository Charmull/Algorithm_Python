import sys
import heapq

input = sys.stdin.readline
V, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append([w, v])

dist = [int(1e9)] * (V + 1)
dist[k] = 0
h = [[0, k]]

while h:
    cur_c, cur_v = heapq.heappop(h)
    if cur_c > dist[cur_v]:
        continue

    for nxt_c, nxt_v in graph[cur_v]:
        if cur_c + nxt_c < dist[nxt_v]:
            dist[nxt_v] = cur_c + nxt_c
            heapq.heappush(h, [cur_c + nxt_c, nxt_v])

for i in range(1, V + 1):
    print(dist[i] if dist[i] != int(1e9) else 'INF')