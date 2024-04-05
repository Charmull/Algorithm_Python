import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
count = 0
visited = [0] * (n + 1)

for i in range(1, n + 1):
    if not visited[i]:
        st = [i]
        visited[i] = 1
        while st:
            target = st.pop()
            for el in graph[target]:
                if not visited[el]:
                    st.append(el)
                    visited[el] = 1
        count += 1
        
print(count)