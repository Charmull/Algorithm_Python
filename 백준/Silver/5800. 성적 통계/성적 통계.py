import sys

input = sys.stdin.readline
n = int(input())
for i in range(1, n + 1):
    score = list(map(int, input().split()))
    k = score[0]
    score = score[1:]
    score.sort()
    gap = [score[i + 1] - score[i] for i in range(k - 1)] + [0]
    gap.sort()
    print('Class', i)
    print(f'Max {score[-1]}, Min {score[0]}, Largest gap {gap[-1]}')