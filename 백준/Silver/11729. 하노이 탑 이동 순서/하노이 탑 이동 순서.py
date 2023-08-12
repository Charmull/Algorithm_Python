import sys

input = sys.stdin.readline
k = int(input())

def func(a, b, n):
    if n == 1:
        print(a, b)
        return 0
    func(a, 6 - a - b, n - 1)
    print(a, b)
    func(6 - a - b, b, n - 1)

print((1 << k) - 1)
func(1, 3, k)