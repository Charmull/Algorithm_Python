import sys
import heapq

input = sys.stdin.readline
n = int(input())
h = []
for _ in range(n):
    num = int(input())
    if not num:
        if h:
            print(-heapq.heappop(h))
            continue
        print(0)
        continue
    heapq.heappush(h, -num)