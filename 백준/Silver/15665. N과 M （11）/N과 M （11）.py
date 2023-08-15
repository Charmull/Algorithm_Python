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
    
    prev = 0
    for i in range(n):
        if prev == nums[i]:
            continue
        l.append(nums[i])
        prev = nums[i]
        dfs()
        l.pop()
        
dfs()