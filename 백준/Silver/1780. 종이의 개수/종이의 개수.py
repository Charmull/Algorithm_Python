import sys

input = sys.stdin.readline
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
count_minus = 0
count_zero = 0
count_plus = 0

def count_paper(row, col, n):
    global count_minus, count_zero, count_plus

    prev = matrix[row][col]
    for y in range(row, row + n):
        for x in range(col, col + n):
            if prev != matrix[y][x]:
                for i in range(3):
                    for j in range(3):
                        count_paper(row + i * n // 3, col + j * n // 3, n // 3)
                return
            
    if prev == -1:
        count_minus += 1
    elif prev == 0:
        count_zero += 1
    else:
        count_plus += 1

count_paper(0, 0, n)
print(count_minus, count_zero, count_plus, sep="\n")