import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
dist = [-1] * 100001

deq = deque([n])

dist[n] = 0

while deq:
    x = deq.popleft()
    current_mm = dist[x]
    if x == k:
        print(current_mm)
        break
    for nx in [x - 1, x + 1, 2 * x]:
        if nx < 0 or nx > 100000:
            continue
        if dist[nx] != -1:
            continue
        deq.append(nx)
        dist[nx] = current_mm + 1