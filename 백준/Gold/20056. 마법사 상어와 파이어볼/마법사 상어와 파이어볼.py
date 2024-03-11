# 1. 모든 파이어볼 이동 -> 파이어볼이 있는 위치 기록해두기(origin, new)
# 2. 파이어볼 나누기

import sys
from collections import defaultdict

input = sys.stdin.readline
N, M, K = map(int, input().split())
origin_fireball = defaultdict(list)

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    origin_fireball[(r - 1, c - 1)].append((m, s, d))

nxt = {0: (-1, 0), 1: (-1, 1), 2: (0, 1), 3: (1, 1),
       4: (1, 0), 5: (1, -1), 6: (0, -1), 7: (-1, -1)}
def move(origin_fireball):
    new_fireball = defaultdict(list)
    for y, x in origin_fireball.keys():
        for m, s, d in origin_fireball[(y, x)]:
            ny = (y + nxt[d][0] * s) % N
            nx = (x + nxt[d][1] * s) % N
            new_fireball[(ny, nx)].append((m, s, d))

    return new_fireball


def upd(origin_fireball):
    new_fireball = defaultdict(list)
    for y, x in origin_fireball.keys():
        if len(origin_fireball[(y, x)]) < 2:
            new_fireball[(y, x)].append(origin_fireball[(y, x)][0])
            continue
        tm = 0
        ts = 0
        td = origin_fireball[(y, x)][0][2] % 2
        check_d = True
        cnt = 0
        for m, s, d in origin_fireball[(y, x)]:
            tm += m
            ts += s
            cnt += 1
            if check_d and d % 2 != td:
                check_d = False
        nm = tm // 5
        ns = ts // cnt
        nd = (0, 2, 4, 6) if check_d else (1, 3, 5, 7)
        if not nm:
            continue
        for el in nd:
            new_fireball[(y, x)].append((nm, ns, el))
    return new_fireball


def cnt_m(origin_fireball):
    tm = 0
    for y, x in origin_fireball.keys():
        for m, s, d in origin_fireball[(y, x)]:
            tm += m
    return tm


for i in range(K):
    origin_fireball = move(origin_fireball)
    origin_fireball = upd(origin_fireball)
print(cnt_m(origin_fireball))