import sys

input = sys.stdin.readline
nums = list(map(int, input().split()))
print(sum([el ** 2 for el in nums]) % 10)