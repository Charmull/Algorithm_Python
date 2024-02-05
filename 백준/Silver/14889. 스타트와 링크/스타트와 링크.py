# 1. 모든 가능한 팀 조합 (dfs) 184,756
# 2. 팀 조합에 따른 능력 계산
import sys

input = sys.stdin.readline
n = int(input())
ability = [list(map(int, input().split())) for _ in range(n)]
result = [int(1e9)]

def calc_ability(team, n):
    a_team = []
    b_team = []
    a_abl = 0
    b_abl = 0
    for i in range(n):
        if i in team:
            a_team.append(i)
        else:
            b_team.append(i)

    for i in range(n // 2):
        for j in range(n // 2):
            t1 = a_team[i]
            t2 = a_team[j]
            a_abl += ability[t1][t2]

            t1 = b_team[i]
            t2 = b_team[j]
            b_abl += ability[t1][t2]
    return abs(a_abl - b_abl)


visited = [0] * n
def dfs(team, idx, n):
    if len(team) == n // 2:
        tmp = calc_ability(team, n)
        result[0] = min(result[0], tmp)
        if result[0] == 0:
            print(0)
            sys.exit(0)
        return
    if idx == n:
        return

    for i in range(idx, n):
        if visited[i]:
            continue
        visited[i] = 1
        team.add(i)
        dfs(team, i + 1, n)
        visited[i] = 0
        team.remove(i)

dfs(set(), 0, n)
print(result[0])