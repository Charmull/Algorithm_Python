# 풀이 1 / 해당 빌딩이 볼 수 있는 빌딩 수를 구하는 방법
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


# 풀이 2 / 해당 빌딩을 볼 수 있는 빌딩 수를 구하는 방법
import sys

n = int(sys.stdin.readline())
heights = [int(sys.stdin.readline()) for _ in range(n)]
answer = 0
stack = []

for i in range(n):
    x = heights[i]
    while stack and stack[-1] <= x:
        stack.pop()
    answer += len(stack)
    stack.append(x)
print(answer)