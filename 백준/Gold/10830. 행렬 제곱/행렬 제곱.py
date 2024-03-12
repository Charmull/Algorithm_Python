import sys
from collections import deque

input = sys.stdin.readline
N, B = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


def matrix_mult(board1, board2):
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                new_board[i][j] += (board1[i][k] * board2[k][j])
            new_board[i][j] %= 1000
    return new_board


result = [[int(i == j) for j in range(N)] for i in range(N)]
while B:
    if B % 2:
        result = matrix_mult(result, board)
    B //= 2
    board = matrix_mult(board, board)

for row in result:
    print(*row)