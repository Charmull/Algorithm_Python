import sys

input = sys.stdin.readline

n = int(input())
origin = [list(map(int, input().split())) for _ in range(n)]
result = [0, 0]

def re(n, r, c):
    if n == 1:
        if origin[r][c] == 0:
            result[0] += 1
        else:
            result[1] += 1
        return
    color = origin[r][c]
    isBreak = 0
    for i in range(r, r + n):
        for j in range(c, c + n):
            if color != origin[i][j]:
                isBreak = 1
                break
        if isBreak:
            break

    if not isBreak:
        if color == 0:
            result[0] += 1
        else:
            result[1] += 1
        return

    re(n // 2, r, c)
    re(n // 2, r, n // 2 + c)
    re(n // 2, n // 2 + r, c)
    re(n // 2, n // 2 + r, n // 2 + c)

re(n, 0, 0)
print(result[0])
print(result[1])