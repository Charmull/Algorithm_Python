# 모든 정점에서 다른 모든 정점까지 갈 수 있는지
import sys

input = sys.stdin.readline
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
        
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1
                
for row in graph:
    print(' '.join(map(str, row)))