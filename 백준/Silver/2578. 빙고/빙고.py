import sys

input = sys.stdin.readline
matrix = [list(map(int, input().split())) for _ in range(5)]
call = [list(map(int, input().split())) for _ in range(5)]

def upd(num):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == num:
                matrix[i][j] = 'x'
                
def check():
    cnt = 0
    dig1 = 0
    dig2 = 0
    for i in range(5):
        tmp1 = 0
        tmp2 = 0
        for j in range(5):
            if matrix[i][j] == 'x':
                tmp1 += 1
            if matrix[j][i] == 'x':
                tmp2 += 1
            if i == j and matrix[i][j] == 'x':
                dig1 += 1
            if i + j == 4 and matrix[i][j] == 'x':
                dig2 += 1
        if tmp1 == 5:
            cnt += 1
        if tmp2 == 5:
            cnt += 1
    if dig1 == 5:
        cnt += 1
    if dig2 == 5:
        cnt += 1
    return True if cnt >= 3 else False
            
            

for i in range(5):
    for j in range(5):
        num = call[i][j]
        upd(num)
        if check():
            print(i * 5 + j + 1)
            sys.exit(0)