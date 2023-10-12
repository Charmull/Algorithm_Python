import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    deq = deque(sys.stdin.readline()[1:-2].split(','))
    error_flag = False
    reverse_count = 0

    if list(deq) == [''] and 'D' in p:
        print('error')
        continue
    
    for func in p:
        if func == 'R':
            reverse_count += 1
        else:
            if deq:
                if reverse_count % 2 == 0:
                    deq.popleft()
                else:
                    deq.pop()
            else:
                error_flag = True
                break

    if error_flag:
        print('error')
    else:
        if reverse_count % 2 == 0:
            print('[' + ','.join(deq) + ']')
        else:
            deq.reverse()
            print('[' + ','.join(deq) + ']')