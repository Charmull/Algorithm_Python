import sys

while True:
    str = sys.stdin.readline().rstrip()
    if str == '.':
        break
    stack = []
    flag = True
    for v in str:
        if v == '(' or v == '[':
            stack.append(v)
        elif v == ')':
            if not stack:
                flag = False
                break
            elif stack.pop() != '(':
                flag = False
                break
        elif v == ']':
            if not stack:
                flag = False
                break
            elif stack.pop() != '[':
                flag = False
                break
        elif v == '.':
            continue
    print('yes' if not stack and flag else 'no')