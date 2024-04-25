import sys

input = sys.stdin.readline

n, m = map(int, input().split(':'))

def gcd(a, b):
    while b > 0:
        tmp = a
        a = b
        b = tmp % b
    return a

a = gcd(n, m)

print(n // a, ':', m // a, sep='')