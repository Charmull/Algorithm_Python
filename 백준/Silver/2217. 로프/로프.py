import sys

input = sys.stdin.readline
n = int(input())
ropes = [int(input()) for _ in range(n)]
ropes.sort(reverse=True)

mw = ropes[0]
for i in range(1, n + 1):
    mw = max(mw, ropes[i - 1] * i)
print(mw)