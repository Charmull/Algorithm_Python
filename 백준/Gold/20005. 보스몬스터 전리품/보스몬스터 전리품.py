# 각 플레이어가 B에 닿는데 걸리는 시간 구하기 (bfs)
# 1_000_000 * 26
# 보스가 죽을때까지 타격 준 플레이어 구하기
# 26
import sys
from collections import defaultdict, deque

input = sys.stdin.readline
m, n, p = map(int, input().split())
board = [input().strip() for _ in range(m)]
dps = defaultdict(int)
for _ in range(p):
    who, num = input().split()
    dps[who] = int(num)
boss_ph = int(input())


def get_boss_idx():
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'B':
                return [i, j]


dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)
def bfs(start, who):
    deq = deque([start])
    dist = [[0] * n for _ in range(m)]
    dist[start[0]][start[1]] = 1

    while deq:
        y, x = deq.popleft()
        cur_d = dist[y][x]
        if y == boss_idx[0] and x == boss_idx[1]:
            time_player[cur_d].append(who)
            return
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= m or nx >= n:
                continue
            if board[ny][nx] == 'X' or dist[ny][nx]:
                continue

            if ny == boss_idx[0] and nx == boss_idx[1]:
                time_player[cur_d + 1].append(who)
                return
            dist[ny][nx] = cur_d + 1
            deq.append([ny, nx])

boss_idx = get_boss_idx()
time_player = defaultdict(list)

for i in range(m):
    for j in range(n):
        if board[i][j] not in ('.', 'X', 'B'):
            bfs([i, j], board[i][j])

arrive = list(time_player.items())
arrive.sort()
get_player = set()
cur_total_dps = 0
for i in range(len(arrive) - 1):
    if boss_ph <= 0:
        break
    for player in arrive[i][1]:
        get_player.add(player)
        cur_total_dps += dps[player]
    boss_ph -= (arrive[i + 1][0] - arrive[i][0]) * cur_total_dps

if boss_ph > 0:
    for player in arrive[-1][1]:
        get_player.add(player)

print(len(list(get_player)))