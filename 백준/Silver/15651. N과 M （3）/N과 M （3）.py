import sys

n, m = map(int, sys.stdin.readline().split())
l = []

def dfs():
    if len(l) == m:
        print(' '.join(map(str, l)))
        return
    
    for i in range(1, n + 1):
        l.append(i)
        dfs()
        l.pop()

dfs()