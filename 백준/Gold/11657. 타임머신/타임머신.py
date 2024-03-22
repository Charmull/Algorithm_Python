import sys

input = sys.stdin.readline
n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
    
dist = [float('inf')] * (n + 1)
def bellman(start):
    dist[start] = 0
    
    for i in range(n):
        for j in range(m):
            cur_node = edges[j][0]
            nxt_node = edges[j][1]
            cost = edges[j][2]
            if dist[cur_node] != float('inf') and dist[nxt_node] > dist[cur_node] + cost:
                dist[nxt_node] = dist[cur_node] + cost
                if i + 1 == n:
                    return True
    return False

is_infinite = bellman(1)
if is_infinite:
    print(-1)
else:
    for i in range(2, n + 1):
        print(dist[i] if dist[i] != float('inf') else -1)