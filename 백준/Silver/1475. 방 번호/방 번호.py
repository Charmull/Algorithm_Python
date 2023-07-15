n = input().replace('9', '6')
count = [0 for _ in range(10)]
for v in n:
    count[int(v)] += 1
count[6] = count[6] // 2 if count[6] % 2 == 0 else count[6] // 2 + 1
print(max(count))