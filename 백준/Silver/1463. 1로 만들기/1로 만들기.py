import sys
from collections import deque

x = int(sys.stdin.readline())
dist = [0] * (x + 1)

def bfs(start):
    deq = deque([start])
    dist[start] = 1

    while deq:
        c = deq.popleft()
        current_cnt = dist[c]
        if c == x:
            return current_cnt - 1
        for nc in (c * 3, c * 2, c + 1):
            if nc < 1 or nc > x:
                continue
            if dist[nc]:
                continue
            deq.append(nc)
            dist[nc] = current_cnt + 1

print(bfs(1))