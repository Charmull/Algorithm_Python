# 1. 톱니바퀴 돌리기
# 2. 연쇄작용 확인 후 해당 톱니바퀴 돌리기

import sys
from collections import deque

input = sys.stdin.readline
a = deque(list(input().strip()))
b = deque(list(input().strip()))
c = deque(list(input().strip()))
d = deque(list(input().strip()))
k = int(input())
turn = []
for _ in range(k):
    who, dir = map(int, input().split())
    turn.append([who - 1, dir])

def change(who, dir):
    if who == 0:
        target = a
    elif who == 1:
        target = b
    elif who == 2:
        target = c
    else:
        target = d
        
    if dir == -1:
        target.append(target.popleft())
    else:
        target.appendleft(target.pop())
        
def rec(who, dir, cur):
    if who == 0:
        if cur[1][0]:
            change(1, -dir)
            cur[1][0] = False
            cur[0][1] = False
            rec(1, -dir, cur)
    if who == 3:
        if cur[2][1]:
            change(2, -dir)
            cur[2][1] = False
            cur[3][0] = False
            rec(2, -dir, cur)
    else:
        if cur[who - 1][1]:
            change(who - 1, -dir)
            cur[who - 1][1] = False
            cur[who][0] = False
            rec(who - 1, -dir, cur)
        if cur[who + 1][0]:
            change(who + 1, -dir)
            cur[who + 1][0] = False
            cur[who][1] = False
            rec(who + 1, -dir, cur)
            
    
for who, dir in turn:
    cur = [[False, a[2] != b[6]], [a[2] != b[6], b[2] != c[6]],
           [b[2] != c[6], c[2] != d[6]], [c[2] != d[6], False]]
    
    change(who, dir)
    rec(who, dir, cur)    
    
result = 0
if int(a[0]):
    result += 1
if int(b[0]):
    result += 2
if int(c[0]):
    result += 4
if int(d[0]):
    result += 8
    
print(result)