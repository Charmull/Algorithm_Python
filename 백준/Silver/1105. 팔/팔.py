# l이나 r이 8 안들어간 숫자이면 -> 0
# 같은 자리수 아니면 -> 0
# 맨앞단위부터 같은 숫자 제외시키기. 제외시키면서 8 있으면 cnt += 1.

import sys
from collections import deque

input = sys.stdin.readline
l, r = input().split()
if '8' not in l or '8' not in r:
    result = 0
elif len(l) != len(r):
    result = 0
else:
    l = deque(list(l))
    r = deque(list(r))
    result = 0
    while len(l) > 0 and l[0] == r[0]:
        if l.popleft() == '8':
            result += 1
        r.popleft()

print(result)