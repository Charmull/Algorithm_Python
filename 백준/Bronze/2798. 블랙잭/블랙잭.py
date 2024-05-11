import sys

input = sys.stdin.readline
n, m = map(int, input().split())
card = list(map(int, input().split()))
result = 0


for i in range(n):
    if m < card[i]:
        continue

    for j in range(i + 1, n):
        if m < card[i] + card[j]:
            continue

        for k in range(j + 1, n):
            if result < card[i] + card[j] + card[k] <= m:
                result = card[i] + card[j] + card[k]
            if result == m:
                print(result)
                sys.exit(0)
        
print(result)