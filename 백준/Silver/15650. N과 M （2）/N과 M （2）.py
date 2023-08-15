import sys

n, m = map(int, sys.stdin.readline().split())
l = []
appended = [0] * (n + 1)

def dfs(k):
    if len(l) == m:
        print(' '.join(map(str, l)))
        return
    
    for i in range(k, n + 1):
        if appended[i]:
            continue
        l.append(i)
        appended[i] = 1
        dfs(i + 1)
        l.pop()
        appended[i] = 0

dfs(1)