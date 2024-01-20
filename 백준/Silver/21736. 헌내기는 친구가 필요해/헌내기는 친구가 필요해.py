import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
I_idx = [-1, -1]
for i in range(N):
    for j in range(M):
        if board[i][j] == 'I':
            I_idx = [i, j]
            break
    if I_idx[0] != -1 and I_idx[1] != -1:
        break

dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)
def find_people():
    deq = deque([I_idx])
    visited = [[0] * M for _ in range(N)]
    visited[I_idx[0]][I_idx[1]] = 1
    cnt = 0

    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                continue
            if visited[ny][nx] or board[ny][nx] == "X":
                continue
            deq.append([ny, nx])
            visited[ny][nx] = 1
            if board[ny][nx] == "P":
                cnt += 1
    return cnt

result = find_people()
print(result if result else 'TT')