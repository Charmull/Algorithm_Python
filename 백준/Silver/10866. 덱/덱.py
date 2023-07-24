import sys
from collections import deque

n = int(sys.stdin.readline())
deq = deque()

for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push_front':
        deq.appendleft(command[1])
    elif command[0] == 'push_back':
        deq.append(command[1])
    elif command[0] == 'pop_front':
        print(-1 if len(deq) == 0 else deq.popleft())
    elif command[0] == 'pop_back':
        print(-1 if len(deq) == 0 else deq.pop())
    elif command[0] == 'size':
        print(len(deq))
    elif command[0] == 'empty':
        print(0 if deq else 1)
    elif command[0] == 'front':
        print(deq[0] if deq else -1)
    elif command[0] == 'back':
        print(deq[-1] if deq else -1)