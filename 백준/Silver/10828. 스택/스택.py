import sys

input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    commands = input().split()
    if commands[0] == 'push':
        stack.append(commands[1])
    elif commands[0] == 'pop':
        if stack:
            print(stack.pop())
            continue
        print(-1)
    elif commands[0] == 'size':
        print(len(stack))
    elif commands[0] == 'empty':
        print(0 if stack else 1)
    elif commands[0] == 'top':
        if stack:
            print(stack[-1])
            continue
        print(-1)