n = int(input())
l = 0
i = 0
while i < len(str(n)):
    if not i:
        if n >= 9:
            l += 9
        else:
            l += n
        i += 1
        continue
    if n / (i * 10) >= 1:
        if n >= 10 ** (i + 1) - 1:
            l += (i + 1) * (10 ** (i + 1) - 1 - (10 ** i - 1))
        else:
            l += (i + 1) * (n - (10**i - 1))
        i += 1

print(l)