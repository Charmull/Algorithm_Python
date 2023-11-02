import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
sort_nums = list(set([i for i in nums]))
sort_nums.sort()

# 정렬이 깨지지 않고 target이 들어갈 수 있는 가장 왼쪽 위치
def lower_idx(target, size):
    l = 0
    r = size
    while l < r:
        mid = (l + r) // 2
        if sort_nums[mid] >= target:
            r = mid
        else:
            l = mid + 1
    return l

result = []
for num in nums:
    result.append(lower_idx(num, (len(sort_nums))))

print(' '.join(map(str, result)))