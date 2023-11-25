import sys

input = sys.stdin.readline
matrix = [[0] * 101 for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            matrix[i][j] = 1
            
result = 0
for i in range(101):
    for j in range(101):
        if matrix[i][j] == 1:
            result += 1
            
print(result)