import sys

input = sys.stdin.readline
n, m = map(int, input().split())
nums = [0] + list(map(int, input().split()))
d = [0] * (n + 1)
d[1] = nums[1]
for i in range(2, n + 1):
    d[i] = d[i - 1] + nums[i]
    
for _ in range(m):
    i, j = map(int, input().split())
    print(d[j] - d[i - 1])