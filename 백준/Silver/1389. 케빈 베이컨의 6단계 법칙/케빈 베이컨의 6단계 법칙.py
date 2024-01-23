import sys
from collections import defaultdict

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[int(1e9)] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

score = defaultdict(list)
for i in range(1, N + 1):
    tmp_score = 0
    for j in range(1, N + 1):
        if graph[i][j] != int(1e9):
            tmp_score += graph[i][j]
    score[tmp_score].append(i)

score_items = list(score.items())
score_items.sort()
result = sorted(score_items[0][1])
print(result[0])