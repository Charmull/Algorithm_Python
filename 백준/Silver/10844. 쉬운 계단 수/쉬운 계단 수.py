import sys

n = int(sys.stdin.readline())
d = [[0] * 10 for _ in range(n + 1)]
d[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            d[i][j] = d[i - 1][j + 1]
            continue
        elif j == 9:
            d[i][j] = d[i - 1][j - 1]
            continue
        d[i][j] = d[i - 1][j - 1] + d[i - 1][j + 1]
        
print(sum(d[n]) % 1000000000)