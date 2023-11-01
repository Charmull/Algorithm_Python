import sys

m, n = map(int, sys.stdin.readline().split())
primes = []
state = [1] * (n + 1)
state[0] = 0
state[1] = 0
for i in range(2, int(n ** (1/2)) + 1):
    if not state[i]:
        continue
    for j in range(i * i, n + 1, i):
        state[j] = 0

for i in range(2, n + 1):
    if state[i] and i >= m:
        primes.append(i)
        
print('\n'.join(map(str, primes)))