# 1. 경계 허물기, 인구 이동시키기 - BFS
# 2. 변화 없을 때까지 반복
import sys
from collections import deque

input = sys.stdin.readline
N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
day = 0

dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)
def bfs(start_row, start_col, L, R):
    deq = deque([[start_row, start_col]])
    visited[start_row][start_col] = 1

    idxs = [(start_row, start_col)]
    total = board[start_row][start_col]
    cnt = 1

    while deq:
        y, x = deq.popleft()
        cur = board[y][x]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue
            if visited[ny][nx]:
                continue
            if L <= abs(board[ny][nx] - cur) <= R:
                deq.append([ny, nx])
                visited[ny][nx] = 1
                idxs.append((ny, nx))
                total += board[ny][nx]
                cnt += 1

    result = total // cnt
    for y, x in idxs:
        board[y][x] = result

    return True if cnt > 1 else False  # 인구 이동 있었을 시 True

while True:
    visited = [[0] * N for _ in range(N)]
    isContinue = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs(i, j, L, R):
                    isContinue = True
    if not isContinue:
        break
    else:
        day += 1
        
print(day)