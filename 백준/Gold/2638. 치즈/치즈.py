# bfs
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
total_cheeze = 0
for i in range(n):
    for j in range(m):
        if board[i][j]:
            total_cheeze += 1

dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)
def bfs(start):
    deq = deque([start])
    visited = [[0] * m for _ in range(n)]
    visited[start[0]][start[1]] = 1
    cnt_meet_cheeze = [[0] * m for _ in range(n)]

    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if visited[ny][nx]:
                continue
            if board[ny][nx] == 1:
                cnt_meet_cheeze[ny][nx] += 1
                continue
            deq.append([ny, nx])
            visited[ny][nx] = 1

    return cnt_meet_cheeze

def upd(cur_cheeze, cnt_meet_cheeze, total_cheeze):
    for i in range(n):
        for j in range(m):
            if cnt_meet_cheeze[i][j] >= 2:
                cur_cheeze[i][j] = 0
                total_cheeze -= 1
    return cur_cheeze, total_cheeze

time = 1
while True:
    cnt_meet_cheeze = bfs([0, 0])
    board, total_cheeze = upd(board, cnt_meet_cheeze, total_cheeze)
    if not total_cheeze:
        print(time)
        break
    time += 1