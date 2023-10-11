import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
deq = deque()

for _ in range(n):
    commands = input().split()
    if commands[0] == 'push_front':
        deq.appendleft(commands[1])
    elif commands[0] == 'push_back':
        deq.append(commands[1])
    elif commands[0] == 'pop_front':
        print(-1 if not deq else deq.popleft())
    elif commands[0] == 'pop_back':
        print(-1 if not deq else deq.pop())
    elif commands[0] == 'size':
        print(len(deq))
    elif commands[0] == 'empty':
        print(0 if deq else 1)
    elif commands[0] == 'front':
        print(-1 if not deq else deq[0])
    elif commands[0] == 'back':
        print(-1 if not deq else deq[-1])