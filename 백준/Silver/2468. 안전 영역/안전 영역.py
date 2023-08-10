import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
max_mark = 0
for i in range(n):
    for j in range(n):
        max_mark = max(matrix[i][j], max_mark)


deq6 = deque([])
visited6 = [[0] * n for _ in range(n)]

dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)
def bfs(start_row, start_col, mark, deq, visited):
    deq.append([start_row, start_col])
    visited[start_row][start_col] = 1
    
    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            if matrix[ny][nx] <= mark or visited[ny][nx]:
                continue
            deq.append([ny, nx])
            visited[ny][nx] = 1

result = 0
for mark in range(0, max_mark + 1):
    deq = deque([])
    visited = [[0] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > mark and not visited[i][j]:
                count += 1
                bfs(i, j, mark, deq, visited)
    result = max(result, count)
print(result)