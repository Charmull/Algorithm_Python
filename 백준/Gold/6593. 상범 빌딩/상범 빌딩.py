# 풀이 1
# import sys
# from collections import deque

# di = (1, -1, 0, 0, 0, 0)
# dj = (0, 0, -1, 0, 0, 1)
# dk = (0, 0, 0, -1, 1, 0)
# def bfs(l, r, c, matrix, start_floor, start_row, start_col):
#     deq = deque([[start_floor, start_row, start_col]])
#     dist = [[[-1] * c for _ in range(r)] for _ in range(l)]
#     dist[start_floor][start_row][start_col] = 0
#     is_escape = False
    
#     while deq:
#         i, j, k = deq.popleft()
#         current_dist = dist[i][j][k]
#         if matrix[i][j][k] == "E":
#             is_escape = True
#             print(f'Escaped in {current_dist} minute(s).')
#             break
#         for v in range(6):
#             ni = i + di[v]
#             nj = j + dj[v]
#             nk = k + dk[v]
#             if ni < 0 or nj < 0 or nk < 0 or ni >= l or nj >= r or nk >= c:
#                 continue
#             if matrix[ni][nj][nk] == "#" or dist[ni][nj][nk] != -1:
#                 continue
#             deq.append([ni, nj, nk])
#             dist[ni][nj][nk] = current_dist + 1
#     return is_escape
    
# input = sys.stdin.readline
# while True:
#     l, r, c = map(int, input().split())
#     if l == r == c == 0: break
        
#     matrix = []
#     for i in range(l):
#         temp = []
#         for j in range(r):
#             temp.append(list(input().strip()))
#         input()
#         matrix.append(temp)
    
#     for i in range(l):
#         for j in range(r):
#             for k in range(c):
#                 if matrix[i][j][k] == "S":
#                     if not bfs(l, r, c, matrix, i, j, k): print("Trapped!")

    
# 풀이 2
import sys
from collections import deque
input = sys.stdin.readline
dz = (1, -1, 0, 0, 0, 0)
dx = (0, 0, 1, -1, 0, 0)
dy = (0, 0, 0, 0, 1, -1)

while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    board = []
    visited = [[[False] * c for _ in range(r)] for _ in range(l)]
    for _ in range(l):
        board.append([list(input().strip()) for _ in range(r)])
        temp = input()

    q = deque()
    escaped = False

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if board[i][j][k] == 'S':
                    start = (i, j, k, 0)
                    visited[i][j][k] = True
                if board[i][j][k] == 'E':
                    goal = (i, j, k)

    q.append(start)
    while q:
        # print(f'cur q: {q}')
        z, x, y, d = q.popleft()
        if (z, x, y) == goal:
            escaped = True
            print(f'Escaped in {d} minute(s).')
            break
        nd = d + 1

        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nz < l and 0 <= nx < r and 0 <= ny < c and not visited[nz][nx][ny]:
                if board[nz][nx][ny] == '.' or board[nz][nx][ny] == 'E':
                    q.append((nz, nx, ny, nd))
                    visited[nz][nx][ny] = True

    if not escaped:
        print('Trapped!')