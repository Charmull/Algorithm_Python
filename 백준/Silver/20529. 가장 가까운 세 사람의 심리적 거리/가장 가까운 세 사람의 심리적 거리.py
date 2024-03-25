import sys
from collections import defaultdict

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    mbti = input().split()
    if n > 32:
        print(0)
        continue
    distance = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                tmp = 0
                for i2 in range(4):
                    tmp += 0 if mbti[i][i2] == mbti[j][i2] else 1
                    tmp += 0 if mbti[i][i2] == mbti[k][i2] else 1
                    tmp += 0 if mbti[j][i2] == mbti[k][i2] else 1
                distance = min(distance, tmp)

    print(distance)