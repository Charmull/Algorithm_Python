import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline
n, r, q = map(int, input().split())
tree = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
    
q_list = [int(input()) for _ in range(q)]

dist = [1] * (n + 1)
def count(cur, parent):
    for nxt in tree[cur]:
        if nxt == parent:
            continue

        dist[cur] += count(nxt, cur)
    return dist[cur]

count(r, -1)

for target in q_list:
    print(dist[target])