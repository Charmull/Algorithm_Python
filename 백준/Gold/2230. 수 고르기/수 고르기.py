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
# m + nums[i]보다 크거나 같은 수를 nums에서 이분탐색
# 정렬이 깨지지 않는 타겟(m + nums[i])을 넣을 수 있는 위치이면서 가장 왼쪽
for i in range(n):
    idx = lower_idx(m + nums[i], i)
    if idx >= n:
        continue
    mn = min(mn, nums[idx] - nums[i])
    
print(mn)