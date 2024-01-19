# 1. 2중 배열로 각 회원에 따른 점수 저장
# 2. 1번부터 N번까지 각각 큐에 연결된 사람을 추가하면서 확인
# or
# 플로이드 or 다익스트라
import sys
from collections import deque, defaultdict

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

score = [[int(1e9)] * (n + 1) for _ in range(n + 1)]


def check_score(who):
    d = deque([[0, who, 0]])  # (현재, 타겟, 점수)
    while d:
        cur, target, sc = d.popleft()
        if score[who][target] < sc:
            continue
        score[who][target] = sc
        for nxt_target in graph[target]:
            if score[who][nxt_target] < sc + 1:
                continue
            d.append([target, nxt_target, sc + 1])
    return max(score[who][1:])


cand_dic = defaultdict(list)
for i in range(1, n + 1):
    cand_dic[check_score(i)].append(i)

temp = list(cand_dic.items())
temp.sort()
print(temp[0][0], len(temp[0][1]))
print(' '.join(map(str, temp[0][1])))