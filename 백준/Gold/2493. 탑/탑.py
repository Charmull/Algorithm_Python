import sys

n = int(sys.stdin.readline())
heights = list(map(int, sys.stdin.readline().split()))
stack = []
result = [0] * n

for i in range(n):
    while stack:
        if stack[-1][1] > heights[i]:
            result[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, heights[i]])

print(' '.join(map(str, result)))