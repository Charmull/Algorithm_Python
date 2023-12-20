import sys

n = int(sys.stdin.readline())
board = [[' '] * (4 * n - 3) for _ in range(4 * n - 3)]

def make_pattern(n, start_row, start_col):
    for i in range(start_row, start_row + (4 * n - 3)):
        for j in range(start_col, start_col + (4 * n - 3)):
            if i == start_row or i == start_row + (4 * n - 3) - 1:
                board[i][j] = '*'
            if j == start_col or j == start_col + (4 * n - 3) - 1:
                board[i][j] = '*'

for i in range(n, 0, -1):
    make_pattern(i, (n - i) * 2, (n - i) * 2)

for row in board:
    print(''.join(row))