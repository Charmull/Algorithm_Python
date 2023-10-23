import sys

input = sys.stdin.readline
n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
nums.sort()

prev = nums[0]
cur_cnt = 0
mx_val = -(2 ** 62) - 1
mx_cnt = 0
for num in nums:
    if prev == num:
        cur_cnt += 1
        continue
    if cur_cnt > mx_cnt:
        mx_cnt = cur_cnt
        mx_val = prev
    prev = num
    cur_cnt = 1

print(prev if cur_cnt > mx_cnt else mx_val)