import sys
from collections import deque, defaultdict

a, b = map(int, sys.stdin.readline().split())
def bfs():
    deq = deque([a])
    dist = defaultdict(int)
    dist[a] = 1

    while deq:
        x = deq.popleft()
        cur_dist = dist[x]
        if x == b:
            return cur_dist

        for nx in (x * 2, x * 10 + 1):
            if nx <= b and not dist[nx]:
                deq.append(nx)
                dist[nx] = cur_dist + 1

    return -1

print(bfs())