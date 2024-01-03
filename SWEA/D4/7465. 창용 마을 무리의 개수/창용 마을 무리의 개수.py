from collections import defaultdict

T = int(input())


def dfs(who, relationship, visited):
    visited[who] = 1
    for to in relationship[who]:
        if not visited[to]:
            dfs(to, relationship, visited)


for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    relationship = defaultdict(list)
    for i in range(m):
        a, b = map(int, input().split())
        relationship[a].append(b)
        relationship[b].append(a)

    visited = [0] * (n + 1)
    result = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, relationship, visited)
            result += 1

    print(f'#{test_case} {result}')
