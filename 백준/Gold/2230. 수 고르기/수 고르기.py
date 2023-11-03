import sys

input = sys.stdin.readline
n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]
nums.sort()

def lower_idx(target, j):
    l = j
    r = len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] >= target:
            r = mid
        else:
            l = mid + 1
    return l
    
mn = 2000000001

en = 0
for st in range(n):
    while en <= n - 1:
        if nums[en] - nums[st] >= m:
            mn = min(mn, nums[en] - nums[st])
            break
        en += 1
    if en == n:
        break
    
print(mn)