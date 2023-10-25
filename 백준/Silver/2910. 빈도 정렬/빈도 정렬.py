import sys
from collections import OrderedDict

input = sys.stdin.readline
n, c = map(int, input().split())
nums = map(int, input().split())
dic = OrderedDict()
for num in nums:
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1
        
ord = sorted(dic.items(), key=lambda x:-x[1])
for num in ord:
    for _ in range(num[1]):
        print(num[0], end=' ')