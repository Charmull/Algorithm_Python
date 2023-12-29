import sys

input = sys.stdin.readline
jeminis = list(map(int, input().split()))
gulibus = list(map(int, input().split()))
score = [0, 0]
for i in range(9):
    score[0] += jeminis[i]
    if score[0] > score[1]:
        print('Yes')
        sys.exit(0)
    score[1] += gulibus[i]

print('No')