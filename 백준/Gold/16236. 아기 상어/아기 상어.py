import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
time = [0]
size = 2
cnt = [0]

def find_yx():
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 9:
                return [i, j]

cur_yx = find_yx()
            

dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)
def bfs(start_row, start_col):
    deq = deque([[start_row, start_col]])
    dist = [[-1] * N for _ in range(N)]
    dist[start_row][start_col] = 0
    find_time = -1
    candidate = []
    
    while deq:
        y, x = deq.popleft()
        cur_time = dist[y][x]
        if find_time != -1 and find_time < cur_time + 1:
            candidate.sort()
            time[0] += find_time
            cnt[0] += 1
            return candidate[0][0], candidate[0][1]
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue
            if matrix[ny][nx] == 9:
                continue
            if dist[ny][nx] != -1 and dist[ny][nx] <= cur_time + 1:
                continue
            if matrix[ny][nx] > size:
                continue
            if matrix[ny][nx] != 0 and matrix[ny][nx] < size:
                find_time = cur_time + 1
                candidate.append([ny, nx])
            deq.append([ny, nx])
            dist[ny][nx] = cur_time + 1
            
    return -1

while True:
    temp = bfs(cur_yx[0], cur_yx[1])
    if (temp == -1):
        print(time[0])
        break
    if cnt[0] == size:
        size += 1
        cnt[0] = 0
    matrix[cur_yx[0]][cur_yx[1]] = 0
    matrix[temp[0]][temp[1]] = 9
    cur_yx = temp