import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
matrix = [list(map(int, list(input().strip()))) for _ in range(n)]

dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)
def bfs():
    deq = deque([[0, 0, True, 1]])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    
    while deq:
        y, x, can_break, current_dist = deq.popleft()
        if y == n - 1 and x == m - 1:
            print(current_dist)
            sys.exit(0)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            
            if not can_break:
                if visited[ny][nx]:
                    continue
                if matrix[ny][nx]:
                    continue
                deq.append([ny, nx, False, current_dist + 1])
                visited[ny][nx] = 2
            else:
                flag = True
                if visited[ny][nx] == 1:
                    continue
                if matrix[ny][nx]:
                    flag = False
                deq.append([ny, nx, flag, current_dist + 1])
                visited[ny][nx] = 1 if flag else 2
            
bfs()
print(-1)