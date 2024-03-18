# 판 오른쪽으로 회전
# 흩날리기
import sys

input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
result = [0]

nxt_idx = [[(-1, 1), (1, 1)], [(-2, 0), (2, 0)],
           [(-1, 0), (1, 0)], [(-1, -1), (1, -1)], [(0, -2)]]
def wind(y, x, a):
    nxt_a = [int(a * (1 / 100)), int(a * (2 / 100)),
             int(a * (7 / 100)), int(a * (1 / 10)), int(a * (1 / 20))]
    for i in range(5):
        tmp_a = nxt_a[i]
        if not tmp_a:
            continue
        for dy, dx in nxt_idx[i]:
            ny = y + dy
            nx = x + dx
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                result[0] += tmp_a
                continue
            board[ny][nx] += tmp_a
    if 0 <= x - 1 < N:
        board[y][x - 1] += a - sum(nxt_a[:4]) * 2 - nxt_a[-1]
    else:
        result[0] += a - sum(nxt_a[:4]) * 2 - nxt_a[-1]
    board[y][x] = 0


def rotation():
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_board[j][N - i - 1] = board[i][j]
    return new_board


i = N // 2
j = N // 2
turn = N // 2  # 회전 횟수 (왼, 아, 오, 위 한 묶음)
time = 1  # 이동 횟수
d = 0  # 방향
while turn:
    for d_time in range(4):
        for _ in range(time):
            i += 0
            j += -1
            if not board[i][j]:
                continue
            wind(i, j, board[i][j])
        if d == 1 or d == 3:  # 아래, 위 이동 끝나면 이동 횟수 +1
            time += 1
        d = (d + 1) % 4
        board = rotation()  # 보드 오른쪽으로 회전
        i, j = j, N - i - 1
    turn -= 1

for _ in range(time):
    i += 0
    j += -1
    if not board[i][j]:
        continue
    wind(i, j, board[i][j])

print(result[0])