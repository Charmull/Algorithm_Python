# 1. 다익스트라
import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline
n, e = map(int, input().split())
graph = defaultdict(list)
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

def dijkstra(start, n):
    dist = [sys.maxsize] * (n + 1)
    dist[start] = 0
    h = [(0, start)]

    while h:
        c, v = heapq.heappop(h)
        if dist[v] != c:
            continue
        for nxt_v, nxt_c in graph[v]:
            nxt_tc = c + nxt_c
            if dist[nxt_v] <= nxt_tc:
                continue
            dist[nxt_v] = nxt_tc
            heapq.heappush(h, (nxt_tc, nxt_v))

    return dist

one_to = dijkstra(1, n)
v1_to = dijkstra(v1, n)
v2_to = dijkstra(v2, n)
result = min(one_to[v1] + v1_to[v2] + v2_to[n],
             one_to[v2] + v2_to[v1] + v1_to[n])
print(result if result < sys.maxsize else -1)