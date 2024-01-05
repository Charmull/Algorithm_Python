import sys
from collections import defaultdict, deque

input = sys.stdin.readline
n = int(input())
lc = defaultdict(str)
rc = defaultdict(str)
for _ in range(n):
    p, c1, c2 = input().split()
    if c1 != '.':
        lc[p] = c1
    if c2 != '.':
        rc[p] = c2

def pre(root):
    if root != '':
        print(root, end='')
        pre(lc[root])
        pre(rc[root])
    
def mid(root):
    if root != '':
        mid(lc[root])
        print(root, end='')
        mid(rc[root])

def last(root):
    if root != '':
        last(lc[root])
        last(rc[root])
        print(root, end='')
    
pre('A')
print()
mid('A')
print()
last('A')