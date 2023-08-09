import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
matrix = [list(map(int, list(input().strip()))) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)
def bfs(start_row, start_col):
    deq = deque([[start_row, start_col]])
    count = 1
    visited[start_row][start_col] = 1
    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            if not matrix[ny][nx] or visited[ny][nx]:
                continue
            deq.append([ny, nx])
            visited[ny][nx] = 1
            count += 1
    return count

total_complex = 0
house_nums = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] and not visited[i][j]:
            total_complex += 1
            house_nums.append(bfs(i, j))
house_nums.sort()
print(total_complex)
print('\n'.join(map(str, house_nums)))