import sys

input = sys.stdin.readline
n = int(input())
ds = int(input())
nums = [int(input()) for _ in range(n - 1)]
nums.sort(reverse=True)
result = 0
if n == 1:
    print(0)
else:
    while nums[0] >= ds:
        nums[0] -= 1
        nums.sort(reverse=True)
        ds += 1
        result += 1
    print(result)