import sys

input = sys.stdin.readline
while True:
    a, b = map(int, input().split())
    if not a and not b:
        break
    print(a + b)