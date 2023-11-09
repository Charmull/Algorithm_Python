import sys
from collections import defaultdict

input = sys.stdin.readline
k, l = map(int, input().split())
is_ready = defaultdict(int)
order = []
for i in range(l):
    num = input().strip()
    is_ready[num] = i
    order.append(num)

for i in range(l):
    if not k:
        break
    candi = order[i]
    if is_ready[candi] == i:
        print(candi)
        k -= 1