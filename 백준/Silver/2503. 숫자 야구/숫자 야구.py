import sys

input = sys.stdin.readline
n = int(input())

lst = []
tmp = []
visited = [0] * 10


def re():
    if len(tmp) == 3:
        tmp2 = [el for el in tmp]
        lst.append(tmp2)
        return
    for i in range(1, 10):
        if visited[i]:
            continue
        tmp.append(i)
        visited[i] = 1
        re()
        tmp.pop()
        visited[i] = 0

re()

for _ in range(n):
    num, st, b = map(int, input().split())
    num = str(num)
    remove_count = 0
    for i in range(len(lst)):
        strike = 0
        ball = 0
        i -= remove_count
        for j in range(3):
            if num[j] == str(lst[i][j]):
                strike += 1
            elif str(lst[i][j]) in num:
                ball += 1
        if strike != st or ball != b:
            del lst[i]
            remove_count += 1

print(len(lst))