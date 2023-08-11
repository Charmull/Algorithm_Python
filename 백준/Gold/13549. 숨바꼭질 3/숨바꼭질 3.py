import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())

visited = [0] * 100001
deq = deque([[n, 0]])
visited[n] = 1

while deq:
    point, time = deq.popleft()
    if point == k:
        print(time)
        break
    for i, p in enumerate([point * 2, point - 1, point + 1]):
        if p < 0 or p >= 100001:
            continue
        if visited[p]:
            continue
        next_time = time + 1 if i != 0 else time
        deq.append([p, next_time])
        visited[p] = 1