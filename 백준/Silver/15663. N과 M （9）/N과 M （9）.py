import sys

input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
log = []
appended = [0] * n

def dfs():
    if len(log) == m:
        print(' '.join(map(str, log)))
        return
    
    prev = 0
    for i in range(n):
        if appended[i] or prev == nums[i]:
            continue
        log.append(nums[i])
        appended[i] = 1
        prev = nums[i]
        dfs()
        log.pop()
        appended[i] = 0
        
dfs()