import sys
from collections import deque

input = sys.stdin.readline
matrix = [list(input().strip()) for _ in range(12)]

dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)
def is_bomb(start_row, start_col, matrix, dist):
    deq = deque([[start_row, start_col]])
    color = matrix[start_row][start_col]
    
    dist[start_row][start_col] = 1
    count = 1
    
    while deq:
        y, x = deq.popleft()
        if count >= 4:
            return True
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= 12 or nx >= 6:
                continue
            if matrix[ny][nx] != color or dist[ny][nx]:
                continue
            deq.append([ny, nx])
            dist[ny][nx] = count + 1
            count += 1
    return False

def bomb_puyo(start_row, start_col, matrix):
    visited = [[0] * 6 for _ in range(12)]
    color = matrix[start_row][start_col]
    deq = deque([[start_row, start_col]])
    matrix[start_row][start_col] = '.'
    
    visited[start_row][start_col] = 1
    
    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= 12 or nx >= 6:
                continue
            if matrix[ny][nx] != color or visited[ny][nx]:
                continue
            deq.append([ny, nx])
            matrix[ny][nx] = '.'
            visited[ny][nx] = 1

def upd_matrix(matrix):
    for j in range(5, 0, -1):
        for i in range(11, 0, -1):
            if matrix[i][j] == '.':
                target = i - 1
                while target >= 0:
                    if matrix[target][j] != '.':
                        matrix[i][j] = matrix[target][j]
                        matrix[target][j] = '.'
                        break
                    target -= 1

def Gravity():
    for c in range(6):
        q = deque([])
        for r in range(11, -1, -1):
            if matrix[r][c] != '.':
                q.append(matrix[r][c])

        for r in range(len(q)):
            matrix[11-r][c] = q[r]
        for r in range(12-len(q)):
            matrix[r][c] = '.'
    return

count = 0
is_contn = True
while is_contn:
    dist = [[0] * 6 for _ in range(12)]
    is_contn = False
    this_turn_bomb = False
    
    for i in range(12):
        for j in range(6):
            if matrix[i][j] != '.' and not dist[i][j]:
                flag = is_bomb(i, j, matrix, dist)
                if flag:
                    bomb_puyo(i, j, matrix)
                    this_turn_bomb = True
                    is_contn = True
    
    if this_turn_bomb:
        count += 1
    Gravity()
    
print(count)