import sys
from bisect import bisect_left

input = sys.stdin.readline
n = int(input())
score = list(map(int, input().split()))
score.sort()

def count_target(i, j, num1):
    count = 0
    st = i
    en = j
    while st < en:
        total = score[st] + score[en] + num1
        if total < 0:
            st += 1
        elif total > 0:
            en -= 1
        else:
            if score[st] == score[en]:
                count += en - st
            else:
                k = bisect_left(score, score[en])
                count += en - k + 1
            st += 1
    return count


result = 0
for i in range(n - 2):
    result += count_target(i + 1, n - 1, score[i])

print(result)