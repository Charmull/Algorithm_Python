import sys

input = sys.stdin.readline
t = int(input())

def binary_search(target, arr):
    l, r = 0, len(arr) - 1
    res = -1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] < target:
            res = mid
            l = mid + 1
        else:
            r = mid - 1
    return res

for _ in range(t):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    count = 0
    
    for a in A:
        count += binary_search(a, B) + 1
    print(count)