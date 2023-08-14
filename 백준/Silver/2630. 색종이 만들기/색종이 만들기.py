import sys

input = sys.stdin.readline
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
count_white = 0
count_blue = 0

def count(start_row, start_col, n):
    global count_white, count_blue
    
    prev = matrix[start_row][start_col]
    for y in range(start_row, start_row + n):
        for x in range(start_col, start_col + n):
            if prev != matrix[y][x]:
                for i in range(2):
                    for j in range(2):
                        count(start_row + i * n // 2, start_col + j * n // 2, n // 2)
                return 0
    if prev:
        count_blue += 1
    else:
        count_white += 1
        
count(0, 0, n)
print(count_white, count_blue, sep="\n")