import sys

input = sys.stdin.readline
INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
nxt = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)   # 노선이 하나가 아닐 수 있음
    nxt[a][b] = b if graph[a][b] == c else nxt[a][b]

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                nxt[i][j] = nxt[i][k]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print(0, end=' ')
            continue
        print(graph[i][j], end=' ')
    print()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if nxt[i][j]:
            path = []
            st = i
            while st != j:
                path.append(st)
                st = nxt[st][j]
            path.append(j)
            print(len(path), ' '.join(map(str, path)))
        else:
            print(0)