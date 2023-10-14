import sys

n, m = map(int, sys.stdin.readline().split())
l = []

def dfs(k):
    if len(l) == m:
        print(' '.join(map(str, l)))
        return
    
    for i in range(k, n + 1):
        l.append(i)
        dfs(i + 1)
        l.pop()

dfs(1)