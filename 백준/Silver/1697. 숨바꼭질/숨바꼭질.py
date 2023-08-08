import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
dist = [-1] * 100001
deq = deque([n])
dist[n] = 0

while deq:
    current_point = deq.popleft()
    current_time = dist[current_point]
    if current_point == k:
        print(current_time)
        sys.exit(0)
    for v in [current_point - 1, current_point + 1, current_point * 2]:
        if v < 0 or v > 100000:
            continue
        if dist[v] != -1:
            continue
        deq.append(v)
        dist[v] = current_time + 1