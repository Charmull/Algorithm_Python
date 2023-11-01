import sys

input = sys.stdin.readline
n = int(input())
required = list(map(int, input().split()))
required.sort()
result = 0
for i in range(n):
    result += sum(required[:i + 1])
    
print(result)