import sys

input = sys.stdin.readline
n = int(input())
minus_nums = []
plus_nums = []
result = 0
for _ in range(n):
    tmp = int(input())
    if tmp > 1:
        plus_nums.append(tmp)
    elif tmp == 1:
        result += 1
    else:
        minus_nums.append(tmp)
        
minus_nums.sort()
plus_nums.sort()

for i in range(len(plus_nums) - 1, -1, -2):
    if i - 1 < 0:
        result += plus_nums[0]
        continue
    result += plus_nums[i] * plus_nums[i - 1]
for i in range(0, len(minus_nums), 2):
    if i + 1 >= len(minus_nums):
        result += minus_nums[i]
        continue
    result += minus_nums[i] * minus_nums[i + 1]
    
print(result)