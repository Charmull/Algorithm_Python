from collections import deque

T = int(input())

dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)


def bfs(board, n):
    deq = deque([[0, 0, board[0][0]]])
    visited = [[-1] * n for _ in range(n)]
    visited[0][0] = board[0][0]
    goal_candi = []

    while deq:
        y, x, cur_time = deq.popleft()
        if y == n - 1 and x == n - 1:
            goal_candi.append(cur_time)
        for i in range(4):
            for j in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or nx < 0 or ny >= n or nx >= n:
                    continue
                if visited[ny][nx] != -1 and visited[ny][nx] <= cur_time + board[ny][nx]:
                    continue
                deq.append([ny, nx, cur_time + board[ny][nx]])
                visited[ny][nx] = cur_time + board[ny][nx]

    return min(goal_candi)


for test_case in range(1, T + 1):
    n = int(input())
    board = [list(map(int, list(input().strip()))) for _ in range(n)]
    result = bfs(board, n)
    print(f'#{test_case} {result}')
