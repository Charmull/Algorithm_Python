import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))

def is_prime(n):
    if n == 1:
        return 0
    for i in range(2, int(n ** (1/2)) + 1):
        if not n % i:
            return 0
    return 1

result = 0
for num in nums:
    result += is_prime(num)
    
print(result)