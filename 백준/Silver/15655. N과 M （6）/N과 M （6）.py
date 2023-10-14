import sys

input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
log = []

def dfs(k):
    if len(log) == m:
        print(' '.join(map(str, log)))
        
    for i in range(k, n):
        log.append(nums[i])
        dfs(i + 1)
        log.pop()
        
dfs(0)