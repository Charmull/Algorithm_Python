import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))
a.sort()

for el in target:
    l = 0
    r = n - 1

    while l <= r:
        mid = (l + r) // 2
        if a[mid] == el:
            print(1)
            break
        elif a[mid] < el:
            l = mid + 1
        elif a[mid] > el:
            r = mid - 1

    if l > r:
        print(0)