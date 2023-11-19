from collections import deque

n = int(input())
kard = deque([i for i in range(1, n + 1)])
while kard:
    print(kard.popleft())
    if kard:
        kard.append(kard.popleft())