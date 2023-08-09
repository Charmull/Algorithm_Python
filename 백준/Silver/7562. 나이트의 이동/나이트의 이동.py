import sys
from collections import deque

dy = (1, 2, 2, 1, -1, -2, -2, -1)
dx = (-2, -1, 1, 2, 2, 1, -1, -2)
def bfs(l, start_row, start_col, dest_row, dest_col):
    deq = deque([[start_row, start_col]])
    dist = [[-1] * l for _ in range(l)]
    
    dist[start_row][start_col] = 0
    
    while deq:
        y, x = deq.popleft()
        current_count = dist[y][x]
        if y == dest_row and x == dest_col:
            print(current_count)
            break
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= l or nx >= l:
                continue
            if dist[ny][nx] != -1:
                continue
            deq.append([ny, nx])
            dist[ny][nx] = current_count + 1
            
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    l = int(input())
    start = list(map(int, input().split()))
    dest = list(map(int, input().split()))
    bfs(l, start[1], start[0], dest[1], dest[0])