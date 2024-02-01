# 250,000 * 5*8 = 250,000 * 40 = 10,000,000
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
result = [0]

tet1 = [[(0, 0), (0, 1), (0, 2), (0, 3)], [(0, 0), (1, 0), (2, 0), (3, 0)]]
tet2 = [[(0, 0), (0, 1), (1, 0), (1, 1)]]
tet3 = [[(0, 0), (1, 0), (2, 0), (2, 1)], [(0, 0), (0, 1), (0, 2), (1, 0)],
        [(0, 0), (0, 1), (1, 1), (2, 1)], [(1, 0), (1, 1), (1, 2), (0, 2)],
        [(0, 1), (1, 1), (2, 1), (2, 0)], [(0, 0), (1, 0), (1, 1), (1, 2)],
        [(0, 0), (0, 1), (1, 0), (2, 0)], [(0, 0), (0, 1), (0, 2), (1, 2)]]
tet4 = [[(0, 0), (1, 0), (1, 1), (2, 1)], [(1, 0), (1, 1), (0, 1), (0, 2)],
        [(0, 1), (1, 1), (1, 0), (2, 0)], [(0, 0), (0, 1), (1, 1), (1, 2)]]
tet5 = [[(0, 0), (0, 1), (0, 2), (1, 1)], [(0, 1), (1, 1), (2, 1), (1, 0)],
        [(1, 0), (1, 1), (1, 2), (0, 1)], [(0, 0), (1, 0), (2, 0), (1, 1)]]
def tet(start_r, start_c):
    for pos in (tet1, tet2, tet3, tet4, tet5):
        for i in range(len(pos)):
            tmp = 0
            flag = True
            for r, c in pos[i]:
                nr = start_r + r
                nc = start_c + c
                if nr < 0 or nc < 0 or nr >= N or nc >= M:
                    flag = False
                    break
                tmp += board[nr][nc]
            if flag and result[0] < tmp:
                result[0] = tmp

for i in range(N):
    for j in range(M):
        tet(i, j)
print(result[0])