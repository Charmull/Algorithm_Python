import sys
import heapq

input = sys.stdin.readline
n = int(input())
h = []
for _ in range(n):
    num = int(input())
    if not num:
        if not h:
            print(0)
            continue
        print(-heapq.heappop(h))
    heapq.heappush(h, -num)