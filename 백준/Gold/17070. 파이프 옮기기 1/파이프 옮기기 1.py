import sys
import heapq

input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

q = []  # (총 이동 거리, 행, 열, 방향)
dist = [[[0] * 3 for _ in range(n)] for _ in range(n)]  # [행][열][방향]의 방문 횟수

# 가로:0, 세로:1, 대각선:2
nxt_d = {0: (0, 2), 1: (1, 2), 2: (0, 1, 2)}
heapq.heappush(q, (0, 0, 1, 0))
dist[0][1][0] = 1
while q:
    total_dist, y, x, d = heapq.heappop(q)
    cur_dist = dist[y][x][d]  # 현재 칸 방문 횟수

    # 가로로 갈 수 있다면
    if 0 in nxt_d[d] and x + 1 < n and not board[y][x + 1]:
        if not dist[y][x + 1][0]:  # 첫 방문이라면 heapq에 다음 칸 요소 추가 (중복 추가를 방지)
            heapq.heappush(q, (total_dist + 1, y, x + 1, 0))
        dist[y][x + 1][0] += dist[y][x][d]  # 다음 칸 dist에 '현재 칸에 도달한 횟수'를 더해주기

    # 세로로 갈 수 있다면
    if 1 in nxt_d[d] and y + 1 < n and not board[y + 1][x]:
        if not dist[y + 1][x][1]:
            heapq.heappush(q, (total_dist + 1, y + 1, x, 1))
        dist[y + 1][x][1] += dist[y][x][d]

    # 대각선으로 갈 수 있다면
    if 2 in nxt_d[d] and y + 1 < n and x + 1 < n and not (board[y + 1][x + 1] + board[y][x + 1] + board[y + 1][x]):
        if not dist[y + 1][x + 1][2]:
            heapq.heappush(q, (total_dist + 2, y + 1, x + 1, 2))  # 대각선은 '현재 총 이동 거리'에 2 추가해야 함
        dist[y + 1][x + 1][2] += dist[y][x][d]

print(sum(dist[-1][-1]))