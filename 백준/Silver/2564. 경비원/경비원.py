# 1. 같은 방향에 있으면 두번째 수 차이만 있으면 됨
# 2. 평행하게 있으면 (수평인 곳 전체 길이) + min(두 번째 수 둘 다 더한거, 전체 길이x2에 두 번째 수 둘 다 뺀거)
# 3. 수평이면
#    1북이면 -> 3서일 때 둘째자리 + 둘째자리 / 4동일 때 전체-둘째자리 + 둘째자리
#    2남이면 -> 3서일 때 둘째자리 + 전체-둘째자리 / 4동일 때 전체-둘째자리 + 전체-둘째자리
#    3서이면 -> 1북일 때 둘째자리 + 둘째자리 / 2남일 때 둘째자리 + 전체-둘째자리
#    4동이면 -> 1북일 때 전체-둘째자리 + 둘째자리 / 2남일 때 전체-둘째자리 + 전체-둘째자리

import sys

input = sys.stdin.readline
c, r = map(int, input().split())
num = int(input())
store = [list(map(int, input().split())) for _ in range(num)]
sq = list(map(int, input().split()))
total = 0

def check(st, sq, c, r):
    if st[0] == 1:
        if sq[0] == 3:
            return st[1] + sq[1]
        if sq[0] == 4:
            return c - st[1] + sq[1]
    elif st[0] == 2:
        if sq[0] == 3:
            return st[1] + r - sq[1]
        if sq[0] == 4:
            return c - st[1] + r - sq[1]
    elif st[0] == 3:
        if sq[0] == 1:
            return sq[1] + st[1]
        if sq[0] == 2:
            return sq[1] + r - st[1]
    elif st[0] == 4:
        if sq[0] == 1:
            return c - sq[1] + st[1]
        if sq[0] == 2:
            return c - sq[1] + r - st[1]

for st in store:
    if st[0] == sq[0]:
        total += abs(st[1] - sq[1])
        continue
    if st[0] in [1, 2] and sq[0] in [1, 2]:
        total += r + min(st[1] + sq[1], 2 * c - st[1] - sq[1])
        continue
    if st[0] in [3, 4] and sq[0] in [3, 4]:
        total += c + min(st[1] + sq[1], 2 * r - st[1] - sq[1])
        continue
    total += check(st, sq, c, r)
    
print(total)