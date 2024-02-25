import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
if n == 1:
    print('A')
elif n == 2:
    if nums[0] == nums[1]:
        print(nums[0])
    else:
        print('A')
else:
    if nums[0] - nums[1] == 0:
        a = 1
    else:
        a = (nums[1] - nums[2]) // (nums[0] - nums[1])
    b = nums[1] - nums[0] * a
    result = nums[-1] * a + b

    for i in range(1, n - 1):
        if nums[i] * a + b != nums[i + 1]:
            result = 'B'
            break

    print(result)