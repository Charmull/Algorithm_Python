import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
matrix_org = [list(map(int, input().split())) for _ in range(n)]
matrix_upd = [list(row) for row in matrix_org]
cctv_dirs = []   # 모든 방향 조합을 담는 리스트
cctv_nums = 0
cctv_lst = []
for i in range(n):
    for j in range(m):
        if matrix_org[i][j] != 0 and matrix_org[i][j] != 6:
            cctv_nums += 1
            cctv_lst.append([i, j])

def get_dirs():
    # cctv는 4방향을 볼 수 있으니 나올 수 있는 cctv 방향 조합 수는 (4 ** k - 1)개
    for i in range(4 ** cctv_nums):
        # cctv 개수만큼의 자릿수가 나와야 함
        tmp = deque()
        for _ in range(cctv_nums):
            tmp.appendleft(i % 4)
            i //= 4
        cctv_dirs.append(tmp)

# cctv가 볼 수 있는 칸은 7로 마킹
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)
def upd(y, x, dir):
    while True:
        y += dy[dir]
        x += dx[dir]
        if y < 0 or x < 0 or y >= n or x >= m:
            return
        if matrix_upd[y][x] == 6:
            return
        if matrix_upd[y][x] != 0:
            continue
        matrix_upd[y][x] = 7


get_dirs()
result = n * m
for d in cctv_dirs:
    for i in range(cctv_nums):
        current_row = cctv_lst[i][0]
        current_col = cctv_lst[i][1]
        if matrix_upd[current_row][current_col] == 1:
            upd(cctv_lst[i][0], cctv_lst[i][1], d[i])
        if matrix_upd[current_row][current_col] == 2:
            upd(cctv_lst[i][0], cctv_lst[i][1], d[i] % 2)
            upd(cctv_lst[i][0], cctv_lst[i][1], d[i] % 2 + 2)
        if matrix_upd[current_row][current_col] == 3:
            set_d = d[i] + 1 if d[i] < 3 else 0
            upd(cctv_lst[i][0], cctv_lst[i][1], d[i])
            upd(cctv_lst[i][0], cctv_lst[i][1], set_d)
        if matrix_upd[current_row][current_col] == 4:
            tmp = {0, 1, 2, 3}
            tmp.remove(d[i])
            set_d = list(tmp)
            upd(cctv_lst[i][0], cctv_lst[i][1], set_d[0])
            upd(cctv_lst[i][0], cctv_lst[i][1], set_d[1])
            upd(cctv_lst[i][0], cctv_lst[i][1], set_d[2])
        if matrix_upd[current_row][current_col] == 5:
            upd(cctv_lst[i][0], cctv_lst[i][1], 0)
            upd(cctv_lst[i][0], cctv_lst[i][1], 1)
            upd(cctv_lst[i][0], cctv_lst[i][1], 2)
            upd(cctv_lst[i][0], cctv_lst[i][1], 3)

    # 빈 칸 수 세기
    count = 0
    for row in matrix_upd:
        for col in row:
            count += 1 if col == 0 else 0
    result = min(count, result)

    matrix_upd = [list(row) for row in matrix_org]

print(result)