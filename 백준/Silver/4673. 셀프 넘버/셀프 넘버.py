d = [True] * 10001
for i in range(1, 10001):
    total = i
    while i:
        total += i % 10
        i //= 10
    if total < 10001:
        d[total] = False
    
for i in range(1, 10001):
    if d[i]:
        print(i)