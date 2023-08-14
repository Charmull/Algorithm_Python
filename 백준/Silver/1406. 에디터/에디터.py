import sys

input = sys.stdin.readline
string = input().strip()
n = int(input())
left = list(string)
right = []

for _ in range(n):
    commands = input().split()
    if commands[0] == 'L' and left:
        right.append(left.pop())
    elif commands[0] == 'D' and right:
        left.append(right.pop())
    elif commands[0] == 'B' and left:
        left.pop()
    elif commands[0] == 'P':
        left.append(commands[1])

right.reverse()
print(''.join(left) + ''.join(right))