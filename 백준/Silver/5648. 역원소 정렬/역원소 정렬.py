import sys
from collections import deque

input = sys.stdin.readline
nums = deque(input().split())
n = int(nums.popleft())
count = len(nums)
while count < n:
    tmp = deque(input().split())
    count += len(tmp)
    nums += tmp
    
def rev(arr, n):
    for i in range(n):
        arr[i] = int(arr[i][::-1])

rev(nums, n)
print('\n'.join(map(str, sorted(nums))))