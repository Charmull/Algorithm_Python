import sys

n, k = map(int, input().split())
circle = [i for i in range(1, n + 1)]
result = []
i = k - 1

while circle:
    if i >= len(circle):
        i %= len(circle)
    result.append(circle.pop(i))
    i += k - 1
    
print('<', ', '.join(map(str, result)), '>', sep='')