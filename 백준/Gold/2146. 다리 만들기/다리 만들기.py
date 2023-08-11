import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)
def count_ground(start_row, start_col, matrix, visited, count, build_start_points):
    deq = deque([[start_row, start_col]])
    visited[start_row][start_col] = 1
    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            if visited[ny][nx]:
                continue
            if not matrix[ny][nx]:
                if matrix[y][x] > 0: matrix[y][x] = -count
                build_start_points.add((y, x))
                continue
            deq.append([ny, nx])
            visited[ny][nx] = 1
            if matrix[y][x] == 1: matrix[y][x] = count
            
count = 1
visited = [[0] * n for _ in range(n)]
build_start_points = set()
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1 and not visited[i][j]:
            count_ground(i, j, matrix, visited, count, build_start_points)
            count += 1
            
def make_bridge(build_start_point, start_value):
    deq = deque([build_start_point])
    dist = [[-1] * n for _ in range(n)]
    dist[build_start_point[0]][build_start_point[1]] = 0
    while deq:
        y, x = deq.popleft()
        current_dist = dist[y][x]
        if matrix[y][x] < 0 and matrix[y][x] != start_value:
            return current_dist - 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            if dist[ny][nx] != -1:
                continue
            if matrix[ny][nx] > 0 or matrix[ny][nx] == start_value:
                continue
            deq.append([ny, nx])
            dist[ny][nx] = current_dist + 1
    return n * n

length = n * n
for start_point in build_start_points:
    current_len =  make_bridge(start_point, matrix[start_point[0]][start_point[1]])
    length = min(length, current_len)
print(length)