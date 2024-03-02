import sys

a, b = map(int, sys.stdin.readline().split())
tmp = []
for i in range(1, 401):
    tmp += [i] * i
print(sum(tmp[a - 1: b]))