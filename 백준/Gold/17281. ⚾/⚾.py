# 브루트포스 (백트래킹)
# 1. 타순 정하기
# 2. 결과 얻기
import sys
from itertools import permutations

input = sys.stdin.readline
n = [int(input())]
score = [list(map(int, input().split())) for _ in range(n[0])]
result = [0]

def game(od):
    now = 0
    sc = 0

    for i in range(n[0]):
        out = 0
        ru1 = ru2 = ru3 = 0
        while out < 3:
            cur = od[now]
            if score[i][cur] == 0:
                out += 1
            elif score[i][cur] == 1:
                sc += ru3
                ru1, ru2, ru3 = 1, ru1, ru2
            elif score[i][cur] == 2:
                sc += ru2 + ru3
                ru1, ru2, ru3 = 0, 1, ru1
            elif score[i][cur] == 3:
                sc += ru1 + ru2 + ru3
                ru1, ru2, ru3 = 0, 0, 1
            elif score[i][cur] == 4:
                sc += ru1 + ru2 + ru3 + 1
                ru1, ru2, ru3 = 0, 0, 0
            now = (now + 1) % 9

    return sc

def make_order():
    for order in permutations((range(1, 9)), 8):
        order = list(order[:3]) + [0] + list(order[3:])
        result[0] = max(result[0], game(order))

make_order()
print(result[0])