import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
dic = defaultdict(str)
for _ in range(n):
    name, condition = input().split()
    dic[name] = condition

lst = []
for name in dic.keys():
    if dic[name] == 'enter':
        lst.append(name)

print('\n'.join(sorted(lst, reverse=True)))