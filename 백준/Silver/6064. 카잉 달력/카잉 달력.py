import sys

input = sys.stdin.readline
t = int(input())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

for _ in range(t):
    m, n, x, y = map(int, input().split())
    
    k = -1
    gcd_num = gcd(max(m, n), min(m, n))
    end = m * n // gcd_num
    for i in range(x, end + 1, m):
        if i % n == y % n:
            k = i
            break
    print(k)