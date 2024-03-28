# 최소 연결 트리 구하기, 그 중 가장 비용 큰 연결 경로 하나 삭제하기
# 최소 연결 트리 구하기 -> 프림
import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def prim(start):
    visited = [0] * (n + 1)
    h = [(0, start)]
    cost = []

    while h:
        if len(cost) == n:
            break
        c, cur = heapq.heappop(h)
        if visited[cur]:
            continue
        visited[cur] = 1
        cost.append(c)
        for nxt, nxt_cost in graph[cur]:
            if visited[nxt]:
                continue
            heapq.heappush(h, (nxt_cost, nxt))

    return sum(cost) - max(cost)


print(prim(1))