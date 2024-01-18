import sys
import heapq

input = sys.stdin.readline
N = int(input())
h = []
cnt = 0
for _ in range(N):
    row = list(map(int, input().split()))
    for el in row:
        if cnt >= N:
            if h[0] > el:
                continue
            heapq.heappop(h)
            heapq.heappush(h, el)
            continue
        heapq.heappush(h, el)
        cnt += 1
print(h[0])