# 3*3 9개, 가로 9개, 세로 9개 각각 등장하는 숫자 set 두기
# 브루트포스(재귀)
import sys

input = sys.stdin.readline
board = [list(map(int, input().strip())) for _ in range(9)]
square = [set() for _ in range(9)]
row = [set() for _ in range(9)]
col = [set() for _ in range(9)]

for i in range(9):
    for j in range(9):
        target_sq = (i // 3) * 3 + (j // 3)
        if board[i][j]:
            square[target_sq].add(board[i][j])
            row[i].add(board[i][j])
            col[j].add(board[i][j])


def find_square(i, j):
    if 0 <= i < 3:
        if 0 <= j < 3:
            return 0
        elif 3 <= j < 6:
            return 1
        elif 6 <= j < 9:
            return 2
    elif 3 <= i < 6:
        if 0 <= j < 3:
            return 3
        elif 3 <= j < 6:
            return 4
        elif 6 <= j < 9:
            return 5
    elif 6 <= i < 9:
        if 0 <= j < 3:
            return 6
        elif 3 <= j < 6:
            return 7
        elif 6 <= j < 9:
            return 8


def dfs(i, j):
    nxt_i = i if j < 8 else i + 1
    nxt_j = (j + 1) % 9

    if i == 9 and j == 0:  # 정답
        for r in board:
            print(''.join(map(str, r)))
        sys.exit(0)

    if board[i][j]:  # 원래 채워진 칸이면
        dfs(nxt_i, nxt_j)
        return

    target_sq = find_square(i, j)
    for num in range(1, 10):
        if num in square[target_sq] or num in row[i] or num in col[j]:
            continue
        board[i][j] = num
        square[target_sq].add(num)
        row[i].add(num)
        col[j].add(num)
        dfs(nxt_i, nxt_j)
        board[i][j] = 0
        square[target_sq].remove(num)
        row[i].remove(num)
        col[j].remove(num)

dfs(0, 0)