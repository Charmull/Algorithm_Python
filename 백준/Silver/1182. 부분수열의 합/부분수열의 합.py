import sys

input = sys.stdin.readline
n, s = map(int, input().split())
nums = list(map(int, input().split()))
log = []
count = [0]

def dfs(k):
    if log and sum(log) == s:
        count[0] += 1
    for i in range(k, n):
        log.append(nums[i])
        dfs(i + 1)
        log.pop()
        
dfs(0)
print(count[0])