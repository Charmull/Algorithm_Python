import sys

input = sys.stdin.readline
n, m = map(int, input().split())
nums = set(map(int, input().split()))
nums = list(nums)
nums.sort()
log = []

def dfs():
    if len(log) == m:
        print(' '.join(map(str, log)))
        return
    
    for num in nums:
        log.append(num)
        dfs()
        log.pop()
        
dfs()