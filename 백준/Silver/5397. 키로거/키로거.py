n = int(input())
for _ in range(n):
    st1 = []
    st2 = []
    command = list(input())
    for c in command:
        if c == '-':
            if st1: st1.pop()
        elif c == '<':
            if st1: st2.append(st1.pop())
        elif c == '>':
            if st2: st1.append(st2.pop())
        else:
            st1.append(c)
    pw = st1 + list(reversed(st2))
    print(''.join(pw))