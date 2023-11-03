import sys

input = sys.stdin.readline
n, s = map(int, input().split())
nums = list(map(int, input().split()))

count = 100001
en = 0
cur_sum = 0
for st in range(n):
    while en <= n - 1:
        if cur_sum < s:
            cur_sum += nums[en]
            en += 1
        else:
            count = min(count, en - st)
            break

    if en == n:
        if cur_sum < s:
            break
        else:
            count = min(count, en - st)
        
    cur_sum -= nums[st]

print(count if count != 100001 else 0)