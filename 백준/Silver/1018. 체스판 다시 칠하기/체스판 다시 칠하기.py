import sys

input = sys.stdin.readline
n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]
result = [float('inf')]

def check(r, c):
    make_b = 0
    make_w = 0
    for i in range(r, r + 8):
        for j in range(c, c + 8):
            if i % 2 == j % 2:
                if board[i][j] == 'W':
                    make_b += 1
                elif board[i][j] == 'B':
                    make_w += 1
            elif i % 2 != j % 2:
                if board[i][j] == 'B':
                    make_b += 1
                elif board[i][j] == 'W':
                    make_w += 1
    result[0] = min(result[0], make_b, make_w)
    
for i in range(n - 7):
    for j in range(m - 7):
        check(i, j)
        
print(result[0])