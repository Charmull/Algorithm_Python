import sys

input = sys.stdin.readline
num = int(input())
result = 0
for i in range(1, num + 1):
    tmp = i + sum(map(int, list(str(i))))
    if num == tmp:
        result = i
        break
        
print(result)