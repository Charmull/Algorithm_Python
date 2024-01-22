# 1. 뱀의 위치를 deque로 관리
# 2. 뱀의 현재 방향, 현재 시간을 변수로 두기
import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1

snake = deque([(0, 0)])
time = 0
cur_dir = 0  # 0:우, 1:하, 2:좌, 3:상
snake_dir = deque([])
for _ in range(int(input())):
    X, C = input().split()
    snake_dir.append((int(X), C))


def get_nxt_head(cur_dir, cur_idx):
    if cur_dir == 0:
        nxt_idx = (cur_idx[0], cur_idx[1] + 1)
    elif cur_dir == 1:
        nxt_idx = (cur_idx[0] + 1, cur_idx[1])
    elif cur_dir == 2:
        nxt_idx = (cur_idx[0], cur_idx[1] - 1)
    elif cur_dir == 3:
        nxt_idx = (cur_idx[0] - 1, cur_idx[1])
    return nxt_idx


# 게임
while True:
    time += 1

    nxt_idx = get_nxt_head(cur_dir, snake[0])
    if nxt_idx[0] < 0 or nxt_idx[1] < 0 or nxt_idx[0] >= N or nxt_idx[1] >= N:
        break
    if nxt_idx in snake:
        break

    # 뱀 늘이기 및 이동
    snake.appendleft(nxt_idx)
    if not board[nxt_idx[0]][nxt_idx[1]]:
        snake.pop()
    else:
        board[nxt_idx[0]][nxt_idx[1]] = 0

    if snake_dir and snake_dir[0][0] == time:
        nxt_dir = snake_dir.popleft()
        if nxt_dir[1] == 'L':
            cur_dir = (cur_dir - 1) % 4
        elif nxt_dir[1] == 'D':
            cur_dir = (cur_dir + 1) % 4

print(time)