import sys
from collections import deque

input = sys.stdin.readline
t = int(input())

def set_init(m, n, k):
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        cabbage_point = list(map(int, input().split()))
        graph[cabbage_point[1]][cabbage_point[0]] = 1
    visited = [[0] * m for _ in range(n)]
    return graph, visited

def find_start_point(m, n, graph, visited):
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(m, n, i, j, graph, visited)
                count += 1
    return count
              
dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)
def bfs(m, n, start_row, start_col, graph, visited):
    deq = deque([[start_row, start_col]])
    visited[start_row][start_col] = 1
        
    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if graph[ny][nx] != 1 or visited[ny][nx]:
                continue
            deq.append([ny, nx])
            visited[ny][nx] = 1

for _ in range(t):
    m, n, k = map(int, input().split())
    graph, visited = set_init(m, n, k)
    print(find_start_point(m, n, graph, visited))