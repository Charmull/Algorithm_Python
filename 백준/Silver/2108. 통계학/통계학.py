import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()
result = [round(sum(nums) / n), nums[n // 2], 0, max(nums) - min(nums)]

count_nums = defaultdict(list)
max_count = 0
count = 1
prev = nums[0]
for i in range(1, n):
    if nums[i] == prev:
        count += 1
        continue
    if max_count <= count:
        count_nums[count].append(prev)
        max_count = count
    prev = nums[i]
    count = 1

if max_count <= count:
    count_nums[count].append(prev)
    max_count = count

count_nums[max_count].sort()
result[2] = count_nums[max_count][0] if len(
    count_nums[max_count]) == 1 else count_nums[max_count][1]

print('\n'.join(map(str, result)))