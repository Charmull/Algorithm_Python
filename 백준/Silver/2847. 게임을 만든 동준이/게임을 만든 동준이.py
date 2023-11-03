import sys

input = sys.stdin.readline
n = int(input())
score = [int(input()) for _ in range(n)]
score = score[::-1]

result = 0
prev_score = score[0]
for i in range(1, n):
    if prev_score <= score[i]:
        result += (score[i] - prev_score + 1)
        score[i] = prev_score - 1
    prev_score = score[i]
    
print(result)