import sys

input = sys.stdin.readline
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
count = [0, 0, 0]

def find_num(k, row, col):
    prev = matrix[row][col]
    flag = False
    for i in range(k):
        for j in range(k):
            if prev != matrix[row + i][col + j]:
                flag = True
                break
        if flag:
            break
    
    if flag:
        point = k // 3
        for i in (0, point, point * 2):
            for j in (0, point, point * 2):
                find_num(point, row + i, col + j)
    else:
        if prev == -1:
            count[0] += 1
        elif prev == 0:
            count[1] += 1
        elif prev == 1:
            count[2] += 1
            
find_num(n, 0, 0)
print('\n'.join(map(str, count)))