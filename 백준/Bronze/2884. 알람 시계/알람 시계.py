import sys

input = sys.stdin.readline
h, m = map(int, input().split())
if m - 45 < 0:
    h -= 1
    m += 15
else:
    m -= 45
if h < 0:
    h = 23
    
print(h, m)