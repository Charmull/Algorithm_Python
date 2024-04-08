import sys
from collections import defaultdict
sys.setrecursionlimit(1_000_000)

input = sys.stdin.readline
t = int(input())


def solve(target):
    total_cost[target] = cost[target]

    for p in child_to_parent[target]:
        if total_cost[p] == -1:
            solve(p)
        total_cost[target] = max(
            total_cost[target], total_cost[p] + cost[target])

    return total_cost[target]


for _ in range(t):
    n, k = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    child_to_parent = defaultdict(list)
    for _ in range(k):
        x, y = map(int, input().split())
        child_to_parent[y].append(x)
    target = int(input())

    total_cost = [-1] * (n + 1)
    print(solve(target))