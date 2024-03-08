import sys
import math
        
input = sys.stdin.readline
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
        
result = [a1 * b2 + b1 * a2, a2 * b2]
gcd = math.gcd(result[0], result[1])

print(result[0] // gcd, result[1] // gcd)