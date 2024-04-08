import sys
from collections import defaultdict, deque

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    parent_to_child = defaultdict(list)
    parent_cnt = [0] * (n + 1)
    for _ in range(k):
        x, y = map(int, input().split())
        parent_to_child[x].append(y)
        parent_cnt[y] += 1
    target = int(input())

    deq = deque([])
    total_cost = [0] * (n + 1)
    for i in range(1, n + 1):
        if not parent_cnt[i]:
            deq.append(i)

    while deq:
        build = deq.popleft()
        cur_cost = total_cost[build] + cost[build]
        if build == target:
            print(cur_cost)
            break
        for c in parent_to_child[build]:
            parent_cnt[c] -= 1
            total_cost[c] = max(total_cost[c], cur_cost)
            if not parent_cnt[c]:
                deq.append(c)