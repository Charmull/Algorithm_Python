import sys

input = sys.stdin.readline
score = [int(input()) for _ in range(8)]

temp = []
answer = 0
for i in range(5):
    answer += max(score)
    temp.append(score.index(max(score)) + 1)
    score[score.index(max(score))] = -1
temp.sort()

print(answer)
print(' '.join(map(str, temp)))