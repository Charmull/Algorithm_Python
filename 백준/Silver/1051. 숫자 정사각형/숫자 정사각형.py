import sys

input = sys.stdin.readline
n, m = map(int, input().split())
matrix = [list(map(int, list(input().strip()))) for _ in range(n)]
result = 0

for i1 in range(n):
    for j1 in range(m):
        rang = min(n - i1 - 1, m - j1 - 1)
        if result >= rang:
            continue
        for i2 in range(rang, result, -1):
            if matrix[i1][j1] == matrix[i1][j1 + i2] == matrix[i1 + i2][j1] == matrix[i1 + i2][j1 + i2]:
                result = i2
                break
                
print((result + 1) ** 2)