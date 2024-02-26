# num[0] * a + b = num[1]
# num[1] * a + b = num[2]
# a = (num[1] - num[2]) / (num[0] - num[1])
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
    if nums[0] == nums[1]:
        a = 0
    else:
        a = (nums[1] - nums[2]) // (nums[0] - nums[1])
    b = nums[1] - nums[0] * a
    isCorrect = True
    for i in range(2, n):
        if nums[i] != nums[i - 1] * a + b:
            isCorrect = False
            break
            
    print(nums[-1] * a + b if isCorrect else 'B')