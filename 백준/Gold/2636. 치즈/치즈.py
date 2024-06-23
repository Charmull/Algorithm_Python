import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
origin = [list(map(int, input().split())) for _ in range(n)]
next_board = [[el for el in row] for row in origin]

dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)
def bfs(st_n, st_m, dist):
    deq = deque([[st_n, st_m]])
    dist[st_n][st_m] = 1
    
    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if dist[ny][nx] == 1:
                continue
            if origin[ny][nx] == 1:
                next_board[ny][nx] = 0
                continue
            dist[ny][nx] = 1
            deq.append([ny, nx])

def isEnd(board):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                cnt += 1
    return cnt

time = 0
prev_cnt = isEnd(origin)

while prev_cnt > 0:
    dist = [[0] * m for _ in range(n)]
    bfs(0, 0, dist)
    
    time += 1
    cnt = isEnd(next_board)
    if cnt == 0:
        print(time, prev_cnt, sep='\n')
        break
    prev_cnt = cnt
    origin = next_board
    next_board = [[el for el in row] for row in origin]