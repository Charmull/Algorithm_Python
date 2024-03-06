import sys

n = int(sys.stdin.readline())
bin_n = bin(n)[2:]
result = 0
for i in range(len(bin_n)):
    result += int(bin_n[-(i + 1)]) * (3 ** i)

print(result)