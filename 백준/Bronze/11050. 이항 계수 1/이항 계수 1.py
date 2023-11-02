import sys

n, k = map(int, sys.stdin.readline().split())

def re(n):
    if n == 0 or n == 1:
        return 1
    return n * re(n - 1)

print(re(n) // (re(k) * re(n - k)))