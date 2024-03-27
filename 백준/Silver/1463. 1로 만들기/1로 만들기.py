import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

def bfs(start):
    deq = deque([start])
    dist = [-1] * (1_000_001)
    dist[start] = 0
    
    while deq:
        x = deq.popleft()
        cur_time = dist[x]
        if x == n:
            return cur_time
        for nx in (x * 3, x * 2, x + 1):
            if nx > 1_000_000:
                continue
            if dist[nx] != -1:
                continue
            dist[nx] = cur_time + 1
            deq.append(nx)
            
print(bfs(1))