import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    string = input().strip()
    left = []
    right = []
    for v in string:
        if v == '-':
            if left: left.pop()
        elif v == '<':
            if left: right.append(left.pop())
        elif v == '>':
            if right: left.append(right.pop())
        else:
            left.append(v)
    right.reverse()
    print(''.join(left) + ''.join(right))