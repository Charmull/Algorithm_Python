import sys
import heapq

input = sys.stdin.readline
N = int(input())
h = []
for _ in range(N):
    x = int(input())
    if not x:
        if h:
            print(heapq.heappop(h))
            continue
        print(0)
        continue
    heapq.heappush(h, x)