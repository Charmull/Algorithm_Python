import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline
n = int(input())
m = int(input())
graph = defaultdict(list)
for _ in range(m):
    a, b, v = map(int, input().split())
    graph[a].append((b, v))
st, en = map(int, input().split())

dist = [int(1e9)] * (n + 1)
h = [(0, st)] # (비용, 출발점)
dist[st] = 0
while h:
    c, s = heapq.heappop(h)
    if dist[s] != c:
        continue
    for nxt_s, nxt_c in graph[s]:
        nxt_tc = nxt_c + c
        if dist[nxt_s] <= nxt_tc:
            continue
        dist[nxt_s] = nxt_tc
        heapq.heappush(h, (nxt_tc, nxt_s))

print(dist[en])        