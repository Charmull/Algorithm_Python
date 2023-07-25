import sys

t = int(sys.stdin.readline())

for _ in range(t):
    str = sys.stdin.readline().strip()
    stack = []
    flag = True
    for v in str:
        if v == '(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                flag = False
                break
    print('YES' if not stack and flag else 'NO')
                