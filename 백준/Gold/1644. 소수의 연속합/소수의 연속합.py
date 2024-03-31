import sys

input = sys.stdin.readline
N = int(input())
primes = []
is_prime = [1] * (N + 1)
for i in range(2, int(N ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * 2, N + 1, i):
            is_prime[j] = 0

for i in range(2, N + 1):
    if is_prime[i]:
        primes.append(i)

if not primes:
    print(0)
    sys.exit()

cnt = 0

# 처음 찾기
st, en = 0, 1
total = primes[0]
while st < en and en <= len(primes):
    if total == N:
        cnt += 1
        break
    elif total < N:
        if en == len(primes):
            break
        total += primes[en]
        en += 1
    elif total > N:
        total -= primes[st]
        st += 1

# 다음 찾기
if not cnt or st + 1 == en or en == len(primes):
    print(cnt)
    sys.exit()

total = total - primes[st]
st += 1
en -= 1
while st <= en and en < len(primes):
    if total == N:
        cnt += 1
        if en + 1 == len(primes):
            break
        total -= primes[st]
        st += 1
        en += 1
        total += primes[en]
    elif total > N:
        if en + 1 == len(primes):
            break
        total -= primes[en]
        en -= 1
    elif total < N:
        if en + 1 == len(primes):
            break
        total -= primes[st]
        st += 1
        en += 1
        total += primes[en]

print(cnt)