import sys

input = sys.stdin.readline
n = int(input())
have = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

have.sort()


def find_idx(target):
    st = 0
    en = len(have) - 1
    while st <= en:
        mid = (st + en) // 2
        if have[mid] == target:
            return 1
        if have[mid] > target:
            en = mid - 1
        elif have[mid] < target:
            st = mid + 1
    return 0


result = []
for el in find:
    result.append(find_idx(el))
print(' '.join(map(str, result)))