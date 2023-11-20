import sys

input = sys.stdin.readline
switch_num = int(input())
switch = list(map(int, input().split()))
stu_num = int(input())

def upd_man(target):
    for i in range(target - 1, switch_num, target):
        switch[i] = 0 if switch[i] else 1

def upd_woman(target):
    switch[target] = 0 if switch[target] else 1

    l, r = target - 1, target + 1
    while l >= 0 and r < switch_num:
        if switch[l] == switch[r]:
            switch[l] = 0 if switch[l] else 1
            switch[r] = 0 if switch[r] else 1
            l -= 1
            r += 1
        else:
            break

for _ in range(stu_num):
    s, num = map(int, input().split())
    if s == 1:
        upd_man(num)
    else:
        upd_woman(num - 1)

for i in range(0, switch_num + 1, 20):
    if i + 20 >= switch_num:
        print(' '.join(map(str, switch[i:switch_num])))
        break
    print(' '.join(map(str, switch[i:i+20])))