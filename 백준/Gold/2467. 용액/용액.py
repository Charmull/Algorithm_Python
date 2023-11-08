import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()


def lower_idx(target):
    st = 0
    en = len(arr)
    while st < en:
        mid = (st + en) // 2
        if arr[mid] >= target:
            en = mid
        else:
            st = mid + 1
    return st


def uppder_idx(target):
    st = 0
    en = len(arr)
    while st < en:
        mid = (st + en) // 2
        if arr[mid] > target:
            en = mid
        else:
            st = mid + 1
    return st


mn = 2000000000
candidate = [-1, -1]
for i in range(len(arr)):
    lower_i = lower_idx(-arr[i])    # -arr[i]과 같거나 큰 수 중 가장 작은 수
    upper_i = uppder_idx(-arr[i])   # -arr[i]보다 큰 수 중 가장 작은 수 or 마지막인덱스

    if lower_i == len(arr):
        lower_i -= 1
    if upper_i == len(arr):
        upper_i -= 1

    if lower_i > 0 and arr[lower_i] > -arr[i]:
        lower_i -= 1

    tmp1 = abs(arr[lower_i] + arr[i]) if lower_i != i else 2000000000
    tmp2 = abs(arr[upper_i] + arr[i]) if upper_i != i else 2000000000
    if tmp1 <= tmp2 and tmp1 < mn:
        mn = tmp1
        candidate[0] = i
        candidate[1] = lower_i
    elif tmp1 > tmp2 and tmp2 < mn:
        mn = tmp2
        candidate[0] = i
        candidate[1] = upper_i

candidate.sort()
print(arr[candidate[0]], arr[candidate[1]])
