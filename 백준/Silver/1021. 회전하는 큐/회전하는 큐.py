# 풀이 1
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


# # 풀이 2
# import sys

# n, m = map(int, sys.stdin.readline().split())
# q = [*range(1, n + 1)]
# idx, cnt = 0, 0

# for i in list(map(int, sys.stdin.readline().split())):
#     el_idx = q.index(i)
#     cnt += min(abs(idx - el_idx), len(q) - abs(idx - el_idx))
#     idx = el_idx
#     del q[el_idx]

# print(cnt)