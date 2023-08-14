import sys

input = sys.stdin.readline
k = int(input())
stack = []
result = 0

for _ in range(k):
    num = int(input())
    if not num:
        result -= stack.pop(-1)
        continue
    stack.append(num)
    result += num
    
print(result)