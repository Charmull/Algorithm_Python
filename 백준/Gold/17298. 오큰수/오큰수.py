import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
stack = []    # 오큰수 후보
answer = [-1] * n

for i in range(n - 1, -1, -1):
    while stack and stack[-1] <= lst[i]:
        stack.pop()
    answer[i] = stack[-1] if stack else -1
    stack.append(lst[i])

print(' '.join(map(str, answer)))