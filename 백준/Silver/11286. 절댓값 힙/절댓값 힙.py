import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
h = []
dic = defaultdict(list)

for _ in range(n):
    num = int(input())
    if not num:
        if not h:
            print(0)
            continue
        target = heapq.heappop(h)    # logN
        print(dic[target].pop())    # 1
    else:
        heapq.heappush(h, abs(num))    # logN
        dic[abs(num)].append(num)    # 1
        dic[abs(num)].sort(reverse=True)    # NlogN