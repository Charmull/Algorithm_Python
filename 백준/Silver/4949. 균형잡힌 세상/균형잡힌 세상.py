import sys

input = sys.stdin.readline

while True:
    st = input().rstrip()
    if st == '.':
        break
        
    stack = []
    flag = True
    for el in st:
        if el in ('(', '['):
            stack.append(el)
            continue
        elif el == ')':
            if not stack or stack.pop() != '(':
                flag = False
                break
        elif el == ']':
            if not stack or stack.pop() != '[':
                flag = False
                break
    print('yes' if not stack and flag else 'no')