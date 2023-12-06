import sys

input = sys.stdin.readline
n = int(input())
num = int(input())
matrix = [[0] * n for _ in range(n)]

def upd(start, n, num):
    for i in range(n):
        matrix[start + i][start] = num
        num -= 1
    for i in range(1, n):
        matrix[start + n - 1][start + i] = num
        num -= 1
    for i in range(1, n):
        matrix[start + n - 1 - i][start + n - 1] = num
        num -= 1
    for i in range(1, n - 1):
        matrix[start][start + n - 1 - i] = num
        num -= 1

for i in range(n // 2 + 1):
    upd(i, n - i * 2, (n - i * 2) ** 2)

result = []
for i in range(n):
    print(' '.join(map(str, matrix[i])))
    for j in range(n):
        if matrix[i][j] == num:
            result = [i, j]

print(result[0] + 1, result[1] + 1)