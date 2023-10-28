import sys

n = int(sys.stdin.readline())
d = [[0] * 2 for _ in range(n + 1)]

if n == 1:
    print(0)
    print(1)
    sys.exit(0)
elif n <= 3:
    print(1)
    print(n, 1)
    sys.exit(0)
d[1][0] = 0
d[1][1] = [1]
d[2][0] = 1
d[2][1] = [1, 2]
d[3][0] = 1
d[3][1] = [1, 3]
for i in range(4, n + 1):
    d[i][0] = d[i - 1][0] + 1
    is_three = False
    is_two = False
    if not i % 3:
        d[i][0] = min(d[i][0], d[i // 3][0] + 1)
        is_three = True
    if not i % 2:
        d[i][0] = min(d[i][0], d[i // 2][0] + 1)
        is_two = True
    
    one = len(d[i - 1][1])
    two = 10**6 if not is_two else len(d[i // 2][1])
    three = 10**6 if not is_three else len(d[i // 3][1])
    if one <= two and one <= three:
        d[i][1] = d[i - 1][1] + [i]
    elif two <= one and two <= three:
        d[i][1] = d[i // 2][1] + [i]
    elif three <= one and three <= two:
        d[i][1] = d[i // 3][1] + [i]

print(d[n][0])
print(' '.join(map(str, d[n][1][::-1])))