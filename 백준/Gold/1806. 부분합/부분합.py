import sys

input = sys.stdin.readline
n, s = map(int, input().split())
nums = list(map(int, input().split()))

count = 100001
en = 0
cur_sum = nums[0]
for st in range(n):
    while en <= n - 1 and cur_sum < s:
        en += 1
        if en != n:
            cur_sum += nums[en]

    if en == n:
        break
    
    count = min(count, en - st + 1)
    cur_sum -= nums[st]

print(count if count != 100001 else 0)