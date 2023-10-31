import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
l = [1] * n
for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            l[i] = max(l[i], l[j] + 1)
            
print(max(l))