import sys

n = int(sys.stdin.readline())
for i in range(2, int(n ** (1/2)) + 1):
    while not n % i:
        print(i)
        n //= i
        
if n != 1:
    print(n)