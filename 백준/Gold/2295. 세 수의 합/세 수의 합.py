import sys

input = sys.stdin.readline
n = int(input())
u = [int(input()) for _ in range(n)]
u.sort()

two = []
for i in range(n):
    for j in range(i, n):
        two.append(u[i] + u[j])
two.sort()

def binary_search(l, r, target):
    while l <= r:
        mid = (l + r) // 2
        if two[mid] == target:
            return mid
        elif two[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

for i in range(n - 1, 0, -1):
    for j in range(i):
        if binary_search(0, len(two) - 1, u[i] - u[j]) != -1:
            print(u[i])
            sys.exit(0)