import sys

input = sys.stdin.readline
c, r = map(int, input().split())
k = int(input())
matrix = [[0] * c for _ in range(r)]
num = 1
y, x = r, 0
mode = 0

while num < c * r + 1:
    if mode == 0:
        ny, nx = y - 1, x
    elif mode == 1:
        ny, nx = y, x + 1
    elif mode == 2:
        ny, nx = y + 1, x
    elif mode == 3:
        ny, nx = y, x - 1

    if ny < 0 or nx < 0 or ny >= r or nx >= c:
        mode = (mode + 1) % 4
        continue
    if matrix[ny][nx]:
        mode = (mode + 1) % 4
        continue
    matrix[ny][nx] = num
    if num == k:
        print(nx + 1, r - ny)
        sys.exit(0)
    num += 1
    y, x = ny, nx

print(0)