import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline
n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dirs = deque()
def make_dirs():
    for i in range(4 ** 5):
        tmp = deque()
        for _ in range(5):
            tmp.appendleft(i % 4)
            i //= 4
        dirs.append(tmp)

def upd(dir, board, max_num):
    if dir == 0:
        prev_num = -1
        next_row = 0
        for i in range(n):    # col
            for j in range(0, n):    # row
                if board[j][i]:
                    if prev_num == board[j][i]:
                        board[next_row - 1][i] *= 2
                        max_num = max(max_num, board[j][i] * 2)
                        prev_num = -1
                        board[j][i] = 0
                    else:
                        if not board[next_row][i]:
                            board[next_row][i] = board[j][i]
                        prev_num = board[j][i]
                        max_num = max(max_num, board[j][i])
                        if next_row != j:
                            board[j][i] = 0
                        next_row += 1
            prev_num = -1
            next_row = 0
    elif dir == 1:
        prev_num = -1
        next_row = n - 1
        for i in range(n):    # col
            for j in range(n - 1, -1, -1):    # row
                if board[j][i]:
                    if prev_num == board[j][i]:
                        board[next_row + 1][i] *= 2
                        max_num = max(max_num, board[j][i] * 2)
                        prev_num = -1
                        board[j][i] = 0
                    else:
                        if not board[next_row][i]:
                            board[next_row][i] = board[j][i]
                        prev_num = board[j][i]
                        max_num = max(max_num, board[j][i])
                        if next_row != j:
                            board[j][i] = 0
                        next_row -= 1
            prev_num = -1
            next_row = n - 1
    elif dir == 2:
        prev_num = -1
        next_col = 0
        for i in range(n):    # row
            for j in range(0, n):    # col
                if board[i][j]:
                    if prev_num == board[i][j]:
                        board[i][next_col - 1] *= 2
                        max_num = max(max_num, board[i][j] * 2)
                        prev_num = -1
                        board[i][j] = 0
                    else:
                        if not board[i][next_col]:
                            board[i][next_col] = board[i][j]
                        prev_num = board[i][j]
                        max_num = max(max_num, board[i][j])
                        if next_col != j:
                            board[i][j] = 0
                        next_col += 1
            prev_num = -1
            next_col = 0
    elif dir == 3:
        prev_num = -1
        next_col = n - 1
        for i in range(n):    # row
            for j in range(n - 1, -1, -1):    # col
                if board[i][j]:
                    if prev_num == board[i][j]:
                        board[i][next_col + 1] *= 2
                        max_num = max(max_num, board[i][j] * 2)
                        prev_num = -1
                        board[i][j] = 0
                    else:
                        if not board[i][next_col]:
                            board[i][next_col] = board[i][j]
                        prev_num = board[i][j]
                        max_num = max(max_num, board[i][j])
                        if next_col != j:
                            board[i][j] = 0
                        next_col -= 1
            next_col = n - 1
            prev_num = -1
    return max_num
                        
make_dirs()
max_num = 0
for dir in dirs:
    tmp_board = deepcopy(board)
    for el in dir:
        max_num = upd(el, tmp_board, max_num)
print(max_num)