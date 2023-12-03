import sys

input = sys.stdin.readline
n = int(input())
matrix = [list(input().strip()) for _ in range(n)]

result = [0, 0]
for i in range(n):
    count = 0
    for j in range(n):
        if matrix[i][j] == '.':
            count += 1
            continue
        if count >= 2:
            result[0] += 1
        count = 0
    if count >= 2:
        result[0] += 1

for j in range(n):
    count = 0
    for i in range(n):
        if matrix[i][j] == '.':
            count += 1
            continue
        if count >= 2:
            result[1] += 1
        count = 0
    if count >= 2:
        result[1] += 1

print(result[0], result[1])