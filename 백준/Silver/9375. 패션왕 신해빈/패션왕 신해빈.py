import sys
from collections import defaultdict

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    kind = defaultdict(int)
    for _ in range(n):
        name, kind_name = input().split()
        kind[kind_name] += 1
        
    result = 1
    for key in kind.keys():
        result *= kind[key] + 1
    print(result - 1)