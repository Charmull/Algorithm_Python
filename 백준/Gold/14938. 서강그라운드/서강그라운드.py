# 플로이드 와샬
import sys

input = sys.stdin.readline
n, m, r = map(int, input().split())
item_num = list(map(int, input().split()))
graph = [[int(1e9)] * n for _ in range(n)]
for i in range(n):
    graph[i][i] = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    if graph[a - 1][b - 1] < l:
        continue
    graph[a - 1][b - 1] = l
    graph[b - 1][a - 1] = l

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

result = 0
for i in range(n):
    tmp = 0
    for j in range(n):
        if graph[i][j] <= m:
            tmp += item_num[j]
    result = max(result, tmp)

print(result)