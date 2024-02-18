# 1. 다익스트라 -> O(ElogE), n명이니 O(NElogE)
import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline
n, m, x = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
result = [0]

def dijkstra(start, n):
    dist = [int(1e9)] * (n + 1)
    dist[start] = 0
    h = [(0, start)]
    while h:
        t, v = heapq.heappop(h)
        if dist[v] < t:
            continue
        for nxt_v, nxt_t in graph[v]:
            nxt_total_t = nxt_t + t
            if dist[nxt_v] <= nxt_total_t:
                continue
            dist[nxt_v] = nxt_total_t
            heapq.heappush(h, (nxt_total_t, nxt_v))
    return dist

# 돌아오는 길에 대해 계산 (x -> 다른 정점)
back_t = dijkstra(x, n)

# 가는 길에 대해 계산 (다른 정점 -> x)
for i in range(1, n + 1):
    if i == x:
        continue
    dist = dijkstra(i, n)
    if result[0] < dist[x] + back_t[i]:
        result[0] = dist[x] + back_t[i]
print(result[0])