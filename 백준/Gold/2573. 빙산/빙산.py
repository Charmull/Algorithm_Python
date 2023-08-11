import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)
def melt(matrix):
    after = [[matrix[i][j] for j in range(m)] for i in range(n)]
    melt_count = 0
    for y in range(n):
        for x in range(m):
            if not after[y][x]:
                continue
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or nx < 0 or ny >= n or nx >= m:
                    continue
                if matrix[ny][nx] or not after[y][x]:
                    continue
                after[y][x] -= 1
                melt_count += 1
    return after, melt_count

def bfs(start_row, start_col, matrix, visited):
    deq = deque([[start_row, start_col]])
    visited[start_row][start_col] = 1
    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if not matrix[ny][nx] or visited[ny][nx]:
                continue
            deq.append([ny, nx])
            visited[ny][nx] = 1

year = 0
while True:
    after, melt_count = melt(matrix)
    if not melt_count:
        print(0)
        break
    if after == [[0] * m for _ in range(n)]:
        print(0)
        break
    year += 1

    matrix = after
    visited = [[0] * m for _ in range(n)]
    count = 0
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] and not visited[i][j]:
                count += 1
                if count >= 2:
                    print(year)
                    sys.exit(0)
                bfs(i, j, matrix, visited)