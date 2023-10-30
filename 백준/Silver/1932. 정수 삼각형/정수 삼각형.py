import sys

input = sys.stdin.readline
n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))
    
d = [[0] * i for i in range(1, n + 1)]
if n == 1:
    print(triangle[0][0])
    sys.exit(0)
d[0][0] = triangle[0][0]
d[1][0] = d[0][0] + triangle[1][0]
d[1][1] = d[0][0] + triangle[1][1]
mn = 0
for k in range(2, n):
    for i in range(k + 1):
        if i == 0:
            d[k][i] = d[k - 1][i] + triangle[k][i]
        elif i == k:
            d[k][i] = d[k - 1][i - 1] + triangle[k][i]
        else:
            d[k][i] = max(d[k - 1][i - 1], d[k - 1][i]) + triangle[k][i]
        mn = max(mn, d[k][i])

print(mn)