import sys

input = sys.stdin.readline
cnt = int(input())
nums = list(map(int, input().split()))
print(min(nums), max(nums))