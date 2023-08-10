import sys
from collections import deque

di = (1, -1, 0, 0, 0, 0)
dj = (0, 0, -1, 0, 0, 1)
dk = (0, 0, 0, -1, 1, 0)
def bfs(l, r, c, matrix, start_floor, start_row, start_col):
    deq = deque([[start_floor, start_row, start_col]])
    dist = [[[-1] * c for _ in range(r)] for _ in range(l)]
    dist[start_floor][start_row][start_col] = 0
    is_escape = False
    
    while deq:
        i, j, k = deq.popleft()
        current_dist = dist[i][j][k]
        if matrix[i][j][k] == "E":
            is_escape = True
            print(f'Escaped in {current_dist} minute(s).')
            break
        for v in range(6):
            ni = i + di[v]
            nj = j + dj[v]
            nk = k + dk[v]
            if ni < 0 or nj < 0 or nk < 0 or ni >= l or nj >= r or nk >= c:
                continue
            if matrix[ni][nj][nk] == "#" or dist[ni][nj][nk] != -1:
                continue
            deq.append([ni, nj, nk])
            dist[ni][nj][nk] = current_dist + 1
    return is_escape
    
input = sys.stdin.readline
while True:
    l, r, c = map(int, input().split())
    if l == r == c == 0: break
        
    matrix = []
    for i in range(l):
        temp = []
        for j in range(r):
            temp.append(list(input().strip()))
        input()
        matrix.append(temp)
    
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if matrix[i][j][k] == "S":
                    if not bfs(l, r, c, matrix, i, j, k): print("Trapped!")