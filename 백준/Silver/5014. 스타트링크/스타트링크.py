import sys
from collections import deque

input = sys.stdin.readline
f, s, g, u, d = map(int, input().split())
deq = deque([s])
dist = [-1] * (f + 1)
dist[s] = 0

while deq:
    current_floor = deq.popleft()
    current_dist = dist[current_floor]
    if current_floor == g:
        print(current_dist)
        sys.exit(0)
    for v in [current_floor + u, current_floor - d]:
        next_floor = v
        if next_floor <= 0 or next_floor > f:
            continue
        if dist[next_floor] != -1:
            continue
        deq.append(next_floor)
        dist[next_floor] = current_dist + 1
print("use the stairs")