import sys

input = sys.stdin.readline
n, m = map(int, input().split())
matrix1 = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
matrix2 = [list(map(int, input().split())) for _ in range(m)]
result = [[0] * k for _ in range(n)]

for ii in range(n):
    for jj in range(k):
        for kk in range(m):
            result[ii][jj] += matrix1[ii][kk] * matrix2[kk][jj]

for row in result:
    for el in row:
        print(el, end=' ')
    print()