import sys

input = sys.stdin.readline
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
count = [0, 0]

def count_num(k, row, col):
    prev = matrix[row][col]
    flag = False
    for i in range(row, row + k):
        for j in range(col, col + k):
            if prev != matrix[i][j]:
                flag = True
                break
        if flag:
            break
            
    if flag:
        half = k // 2
        for i in (row, row + half):
            for j in (col, col + half):
                count_num(half, i, j)
    else:
        if prev:
            count[1] += 1
        else:
            count[0] += 1
            
count_num(n, 0, 0)
print(count[0], count[1], sep='\n')