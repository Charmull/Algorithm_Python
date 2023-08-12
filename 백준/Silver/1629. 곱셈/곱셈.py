import sys

input = sys.stdin.readline
a, b, c = map(int, input().split())

def pow(a, b, c):
    if b == 1: return a % c
    val = pow(a, b // 2, c)
    val = val * val % c
    if not b % 2: return val
    return val * a % c

print(pow(a, b, c))