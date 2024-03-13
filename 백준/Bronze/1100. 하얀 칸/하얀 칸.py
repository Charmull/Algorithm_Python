import sys

input = sys.stdin.readline
cnt = 0
board = [list(input().strip()) for _ in range(8)]
for i in range(8):
    for j in range(8):
        if not i % 2 and not j % 2 and board[i][j] == 'F':
            cnt += 1
        elif i % 2 and j % 2 and board[i][j] == 'F':
            cnt += 1

print(cnt)