import sys
from collections import deque

n = int(sys.stdin.readline())
dist = [0] * (n + 1)
def bfs(start):
    deq = deque([[start]])
    dist[start] = 1
    
    while deq:
        route = deq.popleft()
        x = route[-1]
        curr_cnt = dist[x]
        if x == n:
            print(curr_cnt - 1)
            print(' '.join(map(str, route[::-1])))
        for nx in (x * 3, x * 2, x + 1):
            if nx < 1 or nx > n:
                continue
            if dist[nx]:
                continue
            deq.append(route + [nx])
            dist[nx] = curr_cnt + 1
            
bfs(1)