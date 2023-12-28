import sys

input = sys.stdin.readline
n = int(input())
last_time = 0   # 마지막 골 갱신 시간
a = [0, 0]  # 이기고 있던 시간, 점수
b = [0, 0]  # 이기고 있던 시간, 점수
for _ in range(n):
    team, time = input().split()
    time = int(time[0:2]) * 60 + int(time[-2:])

    if a[1] > b[1]:
        a[0] += time - last_time
    elif a[1] < b[1]:
        b[0] += time - last_time

    last_time = time
    if team == '1':
        a[1] += 1
    else:
        b[1] += 1

if a[1] > b[1]:
    a[0] += 48 * 60 - last_time
if a[1] < b[1]:
    b[0] += 48 * 60 - last_time

def formatting(s):
    if len(str(s)) < 2:
        return '0' + str(s)
    return str(s)

print(formatting(a[0] // 60), ':', formatting(a[0] % 60), sep='')
print(formatting(b[0] // 60), ':', formatting(b[0] % 60), sep='')