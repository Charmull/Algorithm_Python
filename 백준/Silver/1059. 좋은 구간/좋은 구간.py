import sys

input = sys.stdin.readline
l = int(input())
s = [0] + list(map(int, input().split()))
s.sort()
n = int(input())
result = 0

for i in range(l):
    if s[i] == n or s[i + 1] == n:
        break
    if s[i] < n < s[i + 1]:
        result = (n - s[i]) * (s[i + 1] - n) - 1
print(result)