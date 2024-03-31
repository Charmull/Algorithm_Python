# 1,000,000 * 54 = 54,000,000
import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
if M:
    broken = set(map(int, input().split()))
else:
    broken = set()
if N == 100:
    print(0)
    sys.exit()

result = abs(N - 100)
if M == 10:
    print(result)
    sys.exit()


def check(num):
    num_set = set() if num else set([0])
    num_len = 0 if num else 1
    tmp = num
    while tmp:
        num_set.add(tmp % 10)
        tmp //= 10
        num_len += 1

    if (num_set & broken) != set():
        return False, 0
    return True, num_len


for i in range(0, 1000001):
    isCanPush, num_len = check(i)
    if isCanPush:
        result = min(result, abs(N - i) + num_len)

print(result)