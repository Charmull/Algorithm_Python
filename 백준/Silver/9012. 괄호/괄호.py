import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    st = input().rstrip()
    stack = []
    flag = True
    for el in st:
        if el == '(':
            stack.append(el)
        elif el == ')':
            if stack:
                stack.pop()
                continue
            flag = False
            break
    print('YES' if flag and not stack else 'NO')