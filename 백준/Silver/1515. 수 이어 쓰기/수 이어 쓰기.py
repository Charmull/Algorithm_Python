import sys

nums = sys.stdin.readline().strip()
n_lst = ''
n = 0
nums_ptr = 0
n_ptr = 0
while nums_ptr < len(nums):
    n += 1
    n_lst += str(n)
    while nums_ptr < len(nums) and n_ptr < len(n_lst):
        if nums[nums_ptr] == n_lst[n_ptr]:
            nums_ptr += 1
        n_ptr += 1

print(n)