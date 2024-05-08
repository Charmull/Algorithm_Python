import sys
from collections import defaultdict

input = sys.stdin.readline
dic = defaultdict(int)
for _ in range(10):
    num = int(input())
    dic[num % 42] += 1
    
print(len(dic.items()))