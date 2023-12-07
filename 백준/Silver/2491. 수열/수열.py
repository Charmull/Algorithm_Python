import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
if n == 1:
    print(1)
    sys.exit(0)

i = 0
result = 0
while i < n - 1:
    tmp = 1
    while i < n - 1 and nums[i] <= nums[i + 1]:
        i += 1
        tmp += 1
    i += 1
    result = max(result, tmp)

i = 0
while i < n - 1:
    tmp = 1
    while i < n - 1 and nums[i] >= nums[i + 1]:
        i += 1
        tmp += 1
    i += 1
    result = max(result, tmp)

print(result)