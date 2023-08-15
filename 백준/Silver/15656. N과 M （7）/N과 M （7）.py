import sys

input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
l = []

def dfs():
    if len(l) == m:
        print(' '.join(map(str, l)))
        return
    
    for i in range(n):
        l.append(nums[i])
        dfs()
        l.pop()
        
dfs()