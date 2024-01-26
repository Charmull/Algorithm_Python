import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
dic = defaultdict(int)
for _ in range(n):
    book = input().strip()
    dic[book] += 1

items = list(dic.items())
items.sort(key=lambda x: (-x[1], x[0]))
print(items[0][0])