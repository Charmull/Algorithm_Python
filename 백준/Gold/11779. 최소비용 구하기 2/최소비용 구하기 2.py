import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline
n = int(input())
m = int(input())
graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
st, en = map(int, input().split())

def dijkstra(start, end):
    h = [(0, start)]
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pre = [0] * (n + 1)

    while h:
        cost, city = heapq.heappop(h)
        if dist[city] < cost:
            continue
        for nxt_city, nxt_cost in graph[city]:
            total_cost = cost + nxt_cost
            if dist[nxt_city] <= total_cost:
                continue
            dist[nxt_city] = total_cost
            pre[nxt_city] = city
            heapq.heappush(h, (total_cost, nxt_city))

    route = []
    cur = end
    while cur != start:
        route.append(cur)
        cur = pre[cur]
    route.append(start)

    return dist[end], route[::-1]

min_cost, route = dijkstra(st, en)
print(min_cost)
print(len(route))
print(' '.join(map(str, route)))