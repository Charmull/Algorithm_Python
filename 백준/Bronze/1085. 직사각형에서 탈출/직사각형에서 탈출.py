import sys

input = sys.stdin.readline
x, y, w, h = map(int, input().split())
print(min(abs(w - x), abs(h - y), x, y))