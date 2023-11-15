# 1. 미로큐브 만들기
#    큐브만드는 경우의 수: 4^5 * (5*4*3*2) => 1024 * 120 => 122,880 *52
# 2. 출구가 1인지 확인
# 3. 탈출 최단거리 구하기

import sys
from collections import deque, defaultdict
from copy import deepcopy

input = sys.stdin.readline
boards = [[list(map(int, input().split())) for _ in range(5)]
          for _ in range(5)]
rotate_comb = []
board_orders = []

# 판 회전 횟수 조합 만들기
def make_rotate_comb():
    for i in range(4 ** 5):
        tmp = deque([])
        for _ in range(5):
            tmp.appendleft(i % 4)
            i //= 4
        rotate_comb.append(tmp)

# 판 회전
def rotate(board):
    new_board = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            new_board[i][j] = board[5 - j - 1][i]
    for i in range(5):
        for j in range(5):
            board[i][j] = new_board[i][j]

# 순열(1~5) 만들기
def make_order(v, a):
    for i in range(5):
        if len(a) == 5:
            board_orders.append(a)
            break
        if v[i]:
            continue
        a += str(i)
        v[i] = 1
        make_order(v, a)
        a = a[:-1]
        v[i] = 0

# 최종 큐브만들기 위한 판 순서 배열 만들기
def make_cube_order():
    visited = [0] * 5
    arr = ''
    make_order(visited, arr)

di = (-1, 1, 0, 0, 0, 0)
dj = (0, 0, 1, 0, 0, -1)
dk = (0, 0, 0, 1, -1, 0)
# 최단거리 구하기
def bfs(start_point, end_point, cube):
    # 입구 막혀있을 경우
    if not cube[start_point[0]][start_point[1]][start_point[2]]:
        return -1
    # 탈출구 막혀있을 경우
    if not cube[end_point[0]][end_point[1]][end_point[2]]:
        return -1

    deq = deque([start_point])
    dist = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    dist[start_point[0]][start_point[1]][start_point[2]] = 1

    while deq:
        i, j, k = deq.popleft()
        cur_dist = dist[i][j][k]
        if i == end_point[0] and j == end_point[1] and k == end_point[2]:
            return cur_dist - 1
        for t in range(6):
            ni = i + di[t]
            nj = j + dj[t]
            nk = k + dk[t]
            if ni < 0 or nj < 0 or nk < 0 or ni >= 5 or nj >= 5 or nk >= 5:
                continue
            if not cube[ni][nj][nk] or dist[ni][nj][nk]:
                continue
            deq.append([ni, nj, nk])
            dist[ni][nj][nk] = cur_dist + 1
    return -1

make_rotate_comb()
make_cube_order()
result = 125
for r in rotate_comb:
    tmp_boards = deepcopy(boards)
    for i in range(5):
        el = r[i]
        while el:
            rotate(tmp_boards[i])
            el -= 1

    cube = []
    for order in board_orders:
        for el in order:
            cube.append(tmp_boards[int(el)])
        candi = bfs([0, 0, 0], [4, 4, 4], cube)
        if candi != -1:
            result = min(result, candi)
        if result == 12:
            break
        cube = []

print(result if result != 125 else -1)