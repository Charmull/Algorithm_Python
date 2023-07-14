n, x = map(int, input().split(' '))
l = map(int, input().split(' '))
result = []
for v in l:
    if v < x: result.append(v)
print(' '.join(map(str, result)))