import sys

input = sys.stdin.readline
n = int(input())
nums = []
for _ in range(n):
    nums.append(input().strip())

for i in range(n):
    tmp = 0
    for j in range(len(nums[i])):
        try:
            tmp += int(nums[i][j])
        except:
            continue
    nums[i] = [nums[i], len(nums[i]), tmp]
    
nums.sort(key = lambda x:(x[1], x[2], x[0]))

for num, _, _ in nums:
    print(num)