import sys

input = sys.stdin.readline
n = int(input())
lst = []
for _ in range(n):
    name, d, m, y = input().split()
    d = d if len(d) == 2 else '0' + d
    m = m if len(m) == 2 else '0' + m
    lst.append([int(y + m + d), name])
lst.sort()
print(lst[-1][1], lst[0][1], sep='\n')