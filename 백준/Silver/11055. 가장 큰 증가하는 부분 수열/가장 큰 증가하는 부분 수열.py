import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
arr = [num for num in nums]

for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            arr[i] = max(arr[i], arr[j] + nums[i])
        
print(max(arr))