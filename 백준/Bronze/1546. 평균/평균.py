import sys

n = int(input())
score = list(map(int, input().split()))
M = max(score)
result = sum([num / M * 100 for num in score]) / len(score)
print(result)