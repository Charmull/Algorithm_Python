# 투포인터
# 1. p1, 2n+1 까지 확인하는 p2 두기
#    - prev = true면 p2가 가리키는 값까지 갔을 때 cnt 올라간 거, false면 p1~p2는 확인할 필요 없음(p1 = p2로 바꾸기)

import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
S = input().strip()
p1 = 0
p2 = 0
cnt = 0
prev = False

while p1 < M and p2 < M:
    if not prev:
        while S[p1] != 'I' and p1 + 1 < M:
            p1 += 1
            p2 += 1

        if 2 * N + p2 >= M:
            break

        tmp = 0
        for i in range(N):
            p2 += 1
            if S[p2] == 'O' and S[p2 + 1] == 'I':
                p2 += 1
                tmp += 1
                continue
            break

        if tmp == N:
            cnt += 1
            prev = True
        else:
            p1 = p2
    else:
        for i in range(0, M - p2 - 1, 2):
            if p2 + 2 >= M:
                break
            p2 += 1
            if S[p2] == 'O' and S[p2 + 1] == 'I':
                cnt += 1
                p2 += 1
                continue
            break
        prev = False
        p1 = p2

print(cnt)