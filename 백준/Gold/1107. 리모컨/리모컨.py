# 1. 타겟 채널 번호 자릿수 > abs(현재 채널 번호 - 타겟 채널 번호) 면 후자 출력
# 2. 브루트포스
import sys

input = sys.stdin.readline
N = int(input())
rm_num = [0] * 10
rm_cnt = int(input())
if rm_cnt:
    tmp = list(map(int, input().split()))
    for el in tmp:
        rm_num[el] = 1


def isPass(num):
    str_num = str(num)
    for el in str_num:
        if rm_num[int(el)]:
            return True
    return False


result = abs(100 - N)
# 타겟 채널 번호 자릿수 > abs(현재 채널 번호 - 타겟 채널 번호) 면 후자 출력
if len(str(N)) > abs(100 - N):
    result = abs(100 - N)
# 고장난 번호키가 10개면
elif rm_cnt == 10:
    result = abs(100 - N)
else:
    for i in range(1000000):
        if isPass(i):
            continue
        if result > abs(N - i) + len(str(i)):
            result = abs(N - i) + len(str(i))

print(result)