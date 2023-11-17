# 1. 인접한 두 칸이 색이 다르면 교환 -> 50*50
# 2. 가장 긴 색 같은 사탕 개수 확인 -> 50*50
# 총 6,250,000
import sys

input = sys.stdin.readline
n = int(input())
board = [list(input().strip()) for _ in range(n)]
matrix = [[el for el in row] for row in board]
result = 0

def find_long(matrix):
    mn = 0
    for i in range(n):
        tmp = 1
        prev = ''
        for j in range(n):
            if not j:
                prev = matrix[i][j]
                continue
            if prev == matrix[i][j]:
                tmp += 1
                if j == n - 1:
                    mn = max(mn, tmp)
            else:
                mn = max(mn, tmp)
                prev = matrix[i][j]
                tmp = 1
                
    for j in range(n):
        tmp = 1
        prev = ''
        for i in range(n):
            if not i:
                prev = matrix[i][j]
                continue
            if prev == matrix[i][j]:
                tmp += 1
                if i == n - 1:
                    mn = max(mn, tmp)
            else:
                mn = max(mn, tmp)
                prev = matrix[i][j]
                tmp = 1
                
    return mn

for i in range(n):
    if result == n:
        break
    for j in range(n - 1):
        if board[i][j] != board[i][j + 1]:
            matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]
            result = max(result, find_long(matrix))
            matrix = [[el for el in row] for row in board]
            if result == n:
                break

for j in range(n):
    if result == n:
        break
    for i in range(n - 1):
        if board[i][j] != board[i + 1][j]:
            matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
            result = max(result, find_long(matrix))
            matrix = [[el for el in row] for row in board]
            if result == n:
                break
                
print(result)