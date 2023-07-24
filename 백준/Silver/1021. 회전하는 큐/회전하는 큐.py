import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
delete_list = list(map(int, sys.stdin.readline().split()))
deq = deque([i for i in range(1, n + 1)])
count = 0

while len(deq) > n - m:
    if deq[0] == delete_list[0]:
        deq.popleft()
        delete_list.pop(0)
    else:
        el_idx = deq.index(delete_list[0])
        if el_idx < len(deq) - el_idx:
            deq.rotate(-el_idx)
            count += el_idx
        else:
            deq.rotate(len(deq) - el_idx)
            count += len(deq) - el_idx
            
print(count)