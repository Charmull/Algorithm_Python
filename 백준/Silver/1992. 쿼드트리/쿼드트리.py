import sys

input = sys.stdin.readline
n = int(input())
matrix = [list(map(int, list(input().strip()))) for _ in range(n)]
result = ""

def quad_tree(start_row, start_col, n):
    global result
    
    prev = matrix[start_row][start_col]
    for row in range(start_row, start_row + n):
        for col in range(start_col, start_col + n):
            if prev != matrix[row][col]:
                result += "("
                for i in range(2):
                    for j in range(2):
                        quad_tree(start_row + i * n // 2, start_col + j * n // 2, n // 2)
                result += ")"
                return 0
                
    if prev:
        result += "1"
    else:
        result += "0"
        
quad_tree(0, 0, n)
print(result)