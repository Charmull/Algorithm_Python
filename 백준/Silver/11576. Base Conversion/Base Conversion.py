import sys
from collections import deque

input = sys.stdin.readline
a, b = map(int, input().split())
m = int(input())
nums = list(map(int, input().split()))


def make_ten(a, m):
    result = 0
    for i in range(m):
        result += (a ** i) * (nums[m - 1 - i])
    return result

def make_b(b, num):
    result = deque()
    while num:
        result.appendleft(num % b)
        num //= b
    return list(result)

n = make_ten(a, m)
result = make_b(b, n)

print(' '.join(map(str, result)))