import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(0)
    sys.exit(0)

def bfs():
    deq = deque([[0, 0]])    # 현재 칸, 현재 점프 횟수
    dist = [-1] * n
    dist[0] = 0
    
    while deq:
        x, cur_jump_count = deq.popleft()
        if cur_jump_count > dist[x]:
            continue
        posi_jump = a[x] + 1
        for i in range(1, posi_jump):
            nx = x + i
            if n - 1 <= nx:
                return cur_jump_count + 1
            if dist[nx] != -1 and dist[nx] <= cur_jump_count + 1:
                continue
            deq.append([nx, cur_jump_count + 1])
            dist[nx] = cur_jump_count + 1
            
    return -1

result = bfs()
print(result)