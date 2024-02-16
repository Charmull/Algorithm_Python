import sys

input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
lp = 0
rp = 0
cur = 0
cnt = 0
while lp <= rp and rp < n:
    if cur < m:
        cur += nums[rp]
        rp += 1
    elif cur >= m:
        cur -= nums[lp]
        lp += 1
    if cur == m:
        cnt += 1

if cur - nums[lp] == m:
    cnt += 1

print(cnt)