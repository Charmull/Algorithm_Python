import sys

input = sys.stdin.readline
n, m = map(int, input().split())
card = list(map(int, input().split()))
result = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            tmp = card[i] + card[j] + card[k]
            if tmp <= m and tmp > result:
                result = tmp

print(result)