# 백트래킹
# 1. 진실들은 사람 set, 거짓들은 사람 set 관리
# 2. 파티장마다, 오는 사람 중
#   2.1. 진실set O, 거짓set O -> 중지
#   2.2. 진실set O -> 진실 말하기
#   2.3. 진실set X -> 거짓 말하기, 진실 말하기

import sys
from collections import defaultdict

input = sys.stdin.readline
n, m = map(int, input().split())
true_set = set()
true_mem = list(map(int, input().split()))
for mem in true_mem[1:]:
    true_set.add(mem)
false_set = set()
party = [list(map(int, input().split())) for _ in range(m)]
result = [0]


def dfs(party_idx, true_set, false_set, cnt):
    if party_idx == m:
        result[0] = max(result[0], cnt)
        return

    party_num = party[party_idx][0]
    party_mem = party[party_idx][1:]

    is_true = 0
    is_false = 0
    is_other = 0
    for i in range(party_num):
        # break point
        if is_true and is_false:
            break

        if not is_true and party_mem[i] in true_set:
            is_true = 1
        if not is_false and party_mem[i] in false_set:
            is_false = 1
        if not is_other and party_mem[i] not in true_set and party_mem[i] not in false_set:
            is_other = 1

    talk_true = 0
    talk_false = 0
    if is_true and is_false:
        return
    if is_true and not is_false:
        # 진실 말하기
        talk_true = 1
    if not is_true and is_false:
        # 거짓 말하기
        talk_false = 1
    if not is_true and not is_false:
        # 거짓 말하기
        talk_false = 1
        # 진실 말하기
        talk_true = 1

    if talk_true:
        new_set = set(party_mem)
        new_set.update(true_set)
        dfs(party_idx + 1, new_set, false_set, cnt)
    if talk_false:
        new_set = set(party_mem)
        new_set.update(false_set)
        dfs(party_idx + 1, true_set, new_set, cnt + 1)


if true_mem[0] != n:
    dfs(0, true_set, false_set, 0)
print(result[0])