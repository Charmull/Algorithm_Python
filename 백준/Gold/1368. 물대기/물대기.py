import sys
import heapq

# 최소 신장 그래프
input = sys.stdin.readline
n = int(input())
self_cost = [int(input()) for _ in range(n)]
cost = [list(map(int, input().split())) for _ in range(n)]
tmp = [int(1e9), 0]  # 처음 팔 우물의 (비용, 정점)
heap = [(self_cost[i], i) for i in range(n)]
heapq.heapify(heap)

visited = [0] * n
cnt = 0
result = 0
while heap:
    if cnt == n:
        break
    c, v = heapq.heappop(heap)
    if visited[v]:
        continue
    visited[v] = 1
    cnt += 1
    result += min(self_cost[v], c)
    for i in range(n):
        heapq.heappush(heap, (cost[v][i], i))

print(result)