import sys

n = int(sys.stdin.readline())
heights = [int(sys.stdin.readline()) for _ in range(n)]
answer = 0
stack = []

for i in range(n - 1, -1, -1):
    current_can_see = 0
    while stack:
        if stack[-1][1] < heights[i]:
            tmp = stack.pop()
            current_can_see += tmp[2] + 1
        else:
            break
    stack.append((i, heights[i], current_can_see))
    answer += current_can_see
print(answer)