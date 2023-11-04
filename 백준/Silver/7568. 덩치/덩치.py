import sys

input = sys.stdin.readline
n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]
result = [0] * n

for i in range(n):
    cnt = 1
    for j in range(n):
        if i == j:
            continue
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            cnt += 1
    result[i] = cnt
            
print(' '.join(map(str, result)))