import sys

input = sys.stdin.readline

def dfs(k, nums, nums_len, l):
    if len(l) == 6:
        print(' '.join(map(str, l)))
        return
    
    for i in range(k, nums_len):
        l.append(nums[i])
        dfs(i + 1, nums, nums_len, l)
        l.pop()

while True:
    t = list(map(int, input().split()))
    if t[0] == 0:
        break
    k = t[0]
    nums = t[1:]
    l = []
    dfs(0, nums, k, l)
    print()