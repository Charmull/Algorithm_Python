import sys

n = int(sys.stdin.readline())
k = -1
tmp = n // 3
while tmp:
    tmp //= 2
    k += 1
board = [[' '] * (3 * (2 ** (k + 1)) - 1) for _ in range(n)]

# 재귀
# 1. 위 삼각형 재귀
# 2. 왼쪽 삼각형 재귀
# 3. 오른쪽 삼각형 재귀
def star(start_col, start_row, k):
    if k == 0:
        board[start_row][start_col + 2] = '*'
        board[start_row + 1][start_col + 1:start_col + 4] = ['*', ' ', '*']
        board[start_row + 2][start_col:start_col + 5] = ['*'] * 5
        return

    half = 3 * (2 ** (k - 1))
    pull = 3 * (2 ** k)
    star(start_col + half, start_row, k - 1)
    star(start_col, start_row + half, k - 1)
    star(start_col + pull, start_row + half, k - 1)

star(0, 0, k)

for row in board:
    print(''.join(row))