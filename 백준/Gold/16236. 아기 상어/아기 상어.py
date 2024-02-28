# 1. BFS (위, 왼, 오, 아)순
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
shark = []
for i in range(n):
    if shark:
        break
    for j in range(n):
        if board[i][j] == 9:
            shark = [i, j]
            board[i][j] = 0
            break

dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)
def eat_fish(shark, size):
    deq = deque([shark])
    visited = [[-1] * n for _ in range(n)]
    visited[shark[0]][shark[1]] = 0
    result = []  # 먹은 시간, 이동한 아기상어 위치

    while deq:
        y, x = deq.popleft()
        t = visited[y][x]
        if result and result[0] < t + 1:
            break
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            if visited[ny][nx] != -1 or board[ny][nx] > size:
                continue
            if not board[ny][nx] or board[ny][nx] == size:
                deq.append([ny, nx])
                visited[ny][nx] = t + 1
                continue
            if board[ny][nx] and board[ny][nx] < size:  # 작은 물고기 발견
                if not result:
                    result = [t + 1, [ny, nx]]
                else:
                    if result[1][0] < ny:
                        continue
                    elif result[1][0] > ny:
                        result = [t + 1, [ny, nx]]
                        continue
                    elif result[1][0] == ny:
                        if result[1][1] > nx:
                            result = [t + 1, [ny, nx]]

    if result:
        board[result[1][0]][result[1][1]] = 0
        return result  # 먹은 시간, 이동한 아기상어 위치
    else:
        return False

shark_sz = 2
time = 0
cnt = 0
while True:
    tmp = eat_fish(shark, shark_sz)
    if not tmp:
        break
    time += tmp[0]
    shark = tmp[1]
    cnt += 1
    if shark_sz == cnt:
        shark_sz += 1
        cnt = 0
        
print(time)