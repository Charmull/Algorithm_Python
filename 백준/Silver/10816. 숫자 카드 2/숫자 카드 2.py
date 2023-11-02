import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))
dic = defaultdict(int)

for num in a:
    if dic[num]:
        dic[num] += 1
    else:
        dic[num] = 1

result = []
for num in target:
    if dic[num]:
        result.append(dic[num])
    else:
        result.append(0)

print(' '.join(map(str, result)))