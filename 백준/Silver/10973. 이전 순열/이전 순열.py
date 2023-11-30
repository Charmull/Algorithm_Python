import sys

input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))

# 1. 오름차순이 깨지는 부분을 뒤에서부터 찾기 (t)
# 2. 해당 수(t)보다 작은 수를 뒤에서부터 찾기 (t자리에 올 수 있는 t보다 작은 수 찾기)
# 3. t자리까지 픽스 후 그 뒤는 내림차순 정렬
for i in range(n - 1, 0, -1):
    if num[i] < num[i - 1]:
        for j in range(n - 1, i - 1, -1):
            if num[j] < num[i - 1]:
                num[j], num[i - 1] = num[i - 1], num[j]
                result = num[:i] + sorted(num[i:], reverse=True)
                print(' '.join(map(str, result)))
                sys.exit(0)

print(-1)