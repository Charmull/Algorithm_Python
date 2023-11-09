import sys
from collections import deque

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    score = deque(map(int, input().split()))
    max_deq = deque(sorted(score, reverse=True))

    count = 0
    while True:
        if score[0] == max_deq[0]:
            out = score.popleft()
            max_deq.popleft()
            count += 1
            if not m:
                print(count)
                break
            else:
                m -= 1
        else:
            score.append(score.popleft())
            if not m:
                m = len(score) - 1
            else:
                m -= 1