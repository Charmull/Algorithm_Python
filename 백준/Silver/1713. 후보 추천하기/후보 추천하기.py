import sys
from collections import deque

n = int(input())
time = int(input())
vote = list(map(int, input().split()))
candidate = deque()
num = [0] * 101

def remove_target():
    target = candidate[0]
    idx = 0
    for i, c in enumerate(candidate):
        if num[target] > num[c]:
            target = c
            idx = i
    del candidate[idx]
    num[target] = 0

for v in vote:
    if num[v]:
        num[v] += 1
        continue
    if len(candidate) < n:
        candidate.append(v)
        num[v] += 1
        continue
    remove_target()
    candidate.append(v)
    num[v] += 1

print(' '.join(map(str, sorted(candidate))))