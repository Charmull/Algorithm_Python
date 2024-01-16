# 모든 정점에서 다른 모든 정점까지 갈 수 있는지
import sys

input = sys.stdin.readline
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
board = [[int(1e9)] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        # if i == j or graph[i][j]:
        if graph[i][j]:
            board[i][j] = 1
        
for k in range(N):
    for i in range(N):
        for j in range(N):
            if board[i][j] > board[i][k] + board[k][j]:
                board[i][j] = board[i][k] + board[k][j]
                
for i in range(N):
    for j in range(N):
        print(1 if board[i][j] != int(1e9) else 0, end=" ")
    print()