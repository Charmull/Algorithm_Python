import sys
from collections import defaultdict, deque

input = sys.stdin.readline
n = int(input())
target1, target2 = map(int, input().split())
m = int(input())
graph = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
def bfs(start, target):
    deq = deque([start])
    dist = [-1] * (n + 1)
    dist[start] = 0
    
    while deq:
        cur = deq.popleft()
        cnt = dist[cur]
        if cur == target:
            return cnt
        for nxt in graph[cur]:
            if dist[nxt] != -1:
                continue
            deq.append(nxt)
            dist[nxt] = cnt + 1
    return -1
            
print(bfs(target1, target2))