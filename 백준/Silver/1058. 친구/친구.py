import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N)]
for i in range(N):
    graph[i] = list(input().strip())
    
mn = 0
def count_friend(who):
    deq = deque([(0, who, 0)]) # (from, to, 몇촌)
    visited = [0] * (N + 1)
    cnt = 0
    
    while deq:
        cur, nxt, rel = deq.popleft()
        if visited[nxt]:
            continue
        visited[nxt] = 1
        cnt += 1
        for i in range(N):
            if graph[nxt][i] == 'Y' and not visited[i] and rel < 2:
                deq.append((nxt, i, rel + 1))
    return cnt - 1
          
for i in range(N):
    mn = max(mn, count_friend(i))
    
print(mn)