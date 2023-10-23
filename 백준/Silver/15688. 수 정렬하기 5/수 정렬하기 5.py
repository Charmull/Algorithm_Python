import sys

input = sys.stdin.readline
n = int(input())
nums = [0] * 2000001
for _ in range(n):
    num = int(input())
    nums[num + 1000000] += 1

for i in range(2000001):
    while nums[i]:
        print(i - 1000000)
        nums[i] -= 1