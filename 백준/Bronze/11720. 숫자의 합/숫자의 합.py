import sys

input = sys.stdin.readline
cnt = int(input())
nums = list(map(int, list(input().strip())))
print(sum(nums))