import sys

input = sys.stdin.readline
n = int(input())
matrix = [list(map(int, list(input().strip()))) for _ in range(n)]
result = []

def quad_tree(k, row, col):
    prev = matrix[row][col]
    for i in range(row, row + k):
        for j in range(col, col + k):
            if prev != matrix[i][j]:
                result.append('(')
                for nrow in (row, row + k // 2):
                    for ncol in (col, col + k // 2):
                        quad_tree(k // 2, nrow, ncol)
                result.append(')')
                return
                
    result.append(prev)
    
quad_tree(n, 0, 0)
print(''.join(map(str, result)))