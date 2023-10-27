import sys

n = int(sys.stdin.readline())
if n == 1:
    print(1)
    sys.exit(0)

d = [0] * (n + 1)
d[1] = 1
d[2] = 2
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]
print(d[n] % 10007)