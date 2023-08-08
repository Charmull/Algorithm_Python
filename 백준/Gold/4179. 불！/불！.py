import sys
from collections import deque

input = sys.stdin.readline
r, c = map(int, input().split())
matrix = [list(input().strip()) for _ in range(r)]
fire_dist = [[r * c] * c for _ in range(r)]
jihun_dist = [[r * c] * c for _ in range(r)]
time = 0

dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)
def bfs(start_points, who):
    if who == "fire":
        deq = deque(start_points)
        for point_y, point_x in start_points:
            fire_dist[point_y][point_x] = 0
    else:
        deq = deque(start_points)
        for point_y, point_x in start_points:
            jihun_dist[point_y][point_x] = 0
    
    while deq:
        y, x = deq.popleft()
        current_dist = fire_dist[y][x] if who == "fire" else jihun_dist[y][x]
        if who != "fire" and (y == 0 or x == 0 or y == r - 1 or x == c - 1):
            print(current_dist + 1)
            sys.exit(0)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= r or nx >= c:
                continue
            if who == "fire":
                if fire_dist[ny][nx] != r * c or matrix[ny][nx] != ".":
                    continue
                fire_dist[ny][nx] = current_dist + 1
            else:
                if jihun_dist[ny][nx] != r * c or matrix[ny][nx] != "." or fire_dist[ny][nx] <= current_dist + 1:
                    continue
                jihun_dist[ny][nx] = current_dist + 1
            deq.append([ny, nx])
jihun_points = []
fire_points = []
flag = False
for i in range(r):
    for j in range(c):
        if matrix[i][j] == "J":
            jihun_points.append([i, j])
        elif matrix[i][j] == "F":
            fire_points.append([i, j])
bfs(fire_points, "fire")
bfs(jihun_points, "jihun")
print("IMPOSSIBLE")