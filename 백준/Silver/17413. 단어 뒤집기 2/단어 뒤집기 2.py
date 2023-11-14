import sys

input = sys.stdin.readline
st = input().strip()
word = ''
tag = ''

for i in range(len(st)):
    if st[i] == '<':
        if word:
            print(word[::-1], end='')
            word = ''
        tag = '<'
    elif st[i] == '>':
        print(tag, '>', sep='', end='')
        tag = ''
    elif st[i] == ' ':
        if tag:
            tag += ' '
        else:
            print(word[::-1], end=' ')
            word = ''
    else:
        if tag:
            tag += st[i]
        else:
            word += st[i]

if word:
    print(word[::-1])