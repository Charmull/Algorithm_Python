import sys
from collections import deque

input = sys.stdin.readline
T = int(input())


def com_D(num):
    return num * 2 % 10000


def com_S(num):
    return (num - 1) % 10000


def com_L(num):
    return (num % 1000) * 10 + (num // 1000)


def com_R(num):
    return (num // 10) + (num % 10) * 1000


def tracking(pre, num):
    if com_D(pre[num]) == num:
        return 'D'
    if com_S(pre[num]) == num:
        return 'S'
    if com_L(pre[num]) == num:
        return 'L'
    if com_R(pre[num]) == num:
        return 'R'


def append_deq(nxt_num, cur_num, pre, deq):
    if pre[nxt_num] == -1:
        deq.append(nxt_num)
        pre[nxt_num] = cur_num


for _ in range(T):
    A, B = map(int, input().split())
    pre = [-1 for _ in range(10000)]  # 이전 숫자
    deq = deque([A])
    pre[A] = A

    while deq:
        num = deq.popleft()
        if num == B:
            result = deque([])
            while pre[num] != num:
                result.appendleft(tracking(pre, num))
                num = pre[num]
            print(''.join(result))
            break

        append_deq(com_D(num), num, pre, deq)
        append_deq(com_S(num), num, pre, deq)
        append_deq(com_L(num), num, pre, deq)
        append_deq(com_R(num), num, pre, deq)