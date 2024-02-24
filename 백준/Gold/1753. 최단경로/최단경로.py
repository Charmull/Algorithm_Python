# 1. 다익스트라
import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline
v, e = map(int, input().split())
k = int(input())
graph = defaultdict(list)
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start, v):
    dist = [float('inf')] * (v + 1)
    dist[start] = 0
    h = [(0, start)]
    while h:
        c, cur = heapq.heappop(h)
        if dist[cur] != c:
            continue
        for nxt, nxt_c in graph[cur]:
            nxt_tc = c + nxt_c
            if dist[nxt] <= nxt_tc:
                continue
            dist[nxt] = nxt_tc
            heapq.heappush(h, (nxt_tc, nxt))
    return dist

dist = dijkstra(k, v)
for i in range(1, v + 1):
    if i == k:
        print(0)
        continue
    print(dist[i] if dist[i] != float('inf') else 'INF')