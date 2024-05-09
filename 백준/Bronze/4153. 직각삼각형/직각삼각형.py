import sys

input = sys.stdin.readline
while True:
    nums = list(map(int, input().split()))
    if not nums[0] and not nums[1] and not nums[2]:
        break
    nums.sort()
    if nums[0] ** 2 + nums[1] ** 2 == nums[2] ** 2:
        print('right')
    else:
        print('wrong')