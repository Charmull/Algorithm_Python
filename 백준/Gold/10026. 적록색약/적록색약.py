import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = [list(input().strip()) for _ in range(n)]
normal_visited = [[0] * n for _ in range(n)]
abnormal_visited = [[0] * n for _ in range(n)]

dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)
def bfs(start_row, start_col, visited, who):
    deq = deque([[start_row, start_col]])
    visited[start_row][start_col] = 1
    while deq:
        y, x = deq.popleft()
        current_color = graph[y][x]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            if who == "normal":
                if graph[ny][nx] != current_color or visited[ny][nx]:
                    continue
            else:
                if visited[ny][nx]:
                    continue
                if current_color in ("R", "G") and graph[ny][nx] == "B":
                    continue
                if current_color == "B" and graph[ny][nx] != "B":
                    continue
            deq.append([ny, nx])
            visited[ny][nx] = 1
            
result = [0, 0]
for i in range(n):
    for j in range(n):
        if not normal_visited[i][j]:
            bfs(i, j, normal_visited, "normal")
            result[0] += 1
        if not abnormal_visited[i][j]:
            bfs(i, j, abnormal_visited, "abnormal")
            result[1] += 1
print(result[0], result[1])