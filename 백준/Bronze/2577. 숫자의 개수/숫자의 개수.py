a = int(input())
b = int(input())
c = int(input())
mult = str(a * b * c)

count = [0 for _ in range(10)]
for v in mult:
    count[int(v)] += 1
print('\n'.join(map(str, count)))