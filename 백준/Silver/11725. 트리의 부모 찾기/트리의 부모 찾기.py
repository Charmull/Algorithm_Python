import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parent = [-1] * (n + 1)
def bfs(start):
    deq = deque([start])
    parent[start] = 0
    
    while deq:
        target = deq.popleft()
        for el in tree[target]:
            if el == parent[target]:
                continue
            deq.append(el)
            parent[el] = target

bfs(1)
for i in range(2, n + 1):
    print(parent[i])