# 1. i번째 배열의 숫자 크기에 따른 등수를 배열에 저장(이분탐색) - (NlogN) * M
# 2. i번째 배열과 j번째 배열에 대해 - (M^2)
#     둘이 같은지 비교 - (N)
# 시간복잡도 : O(100*10000*100 + 10000*10000) = 100,000,000

import sys

input = sys.stdin.readline
m, n = map(int, input().split())
rank = []

def lower_idx(arr, target, size):
    st = 0
    en = size
    while st < en:
        mid = (st + en) // 2
        if arr[mid] >= target:
            en = mid
        else:
            st = mid + 1
    return st

for _ in range(m):
    arr = list(map(int, input().split()))
    l = [el for el in arr]
    l.sort()

    tmp = []
    for el in arr:
        tmp.append(lower_idx(l, el, len(l)) + 1)
    rank.append(tmp)

count = 0
for i in range(m):
    for j in range(i + 1, m):
        count += 1 if rank[i] == rank[j] else 0
print(count)