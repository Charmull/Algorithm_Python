import sys

input = sys.stdin.readline
k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

def solve(x):
    global k, n
    cur = 0
    for i  in range(k):
        cur += arr[i] // x
    return cur >= n

st = 0
en = 2 ** 31 - 1
while st < en:
    mid = (st + en + 1) // 2
    if solve(mid):
        st = mid
    else:
        en = mid - 1

print(st)