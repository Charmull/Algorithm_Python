import sys

input = sys.stdin.readline
nums = list(input().split())
if nums == sorted(nums):
    print('ascending')
elif nums == sorted(nums, reverse=True):
    print('descending')
else:
    print('mixed')