import sys

input = sys.stdin.readline
n, m = map(int, input().split())
trees = list(map(int, input().split()))

h_st = 0
h_en = 1000000000 - 1


def total_len(h):
    total = 0
    for tree in trees:
        total += 0 if tree <= h else tree - h
    return total


while h_st < h_en:
    mid = (h_st + h_en + 1) // 2
    total = total_len(mid)
    if total < m:
        h_en = mid - 1
    else:
        h_st = mid

print(h_st)