# 1. 팀 나누기
# 2. 팀 점수 계산하기
import sys

input = sys.stdin.readline
n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
result = [int(1e9)]

team = [0] * n
def cal(team, n):
    team_a = []
    team_b = []
    a = 0
    b = 0
    for i in range(n):
        if team[i]:
            team_a.append(i)
        else:
            team_b.append(i)
    for i in range(n // 2):
        for j in range(i + 1, n // 2):
            target1 = team_a[i]
            target2 = team_a[j]
            a += table[target1][target2]
            a += table[target2][target1]

            target1 = team_b[i]
            target2 = team_b[j]
            b += table[target1][target2]
            b += table[target2][target1]
    return abs(a - b)

def make_team(idx, team, n, cnt):
    if cnt == n // 2:
        result[0] = min(result[0], cal(team, n))
        if result[0] == 0:
            print(0)
            sys.exit(0)
        return
    if cnt > n // 2:
        return

    for i in range(idx, n):
        if team[i]:
            continue
        team[i] = 1
        make_team(i + 1, team, n, cnt + 1)
        team[i] = 0

make_team(0, team, n, 0)
print(result[0])