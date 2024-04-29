import sys

input = sys.stdin.readline

str = input().strip()

for i in 'abcdefghijklmnopqrstuvwxyz':
    if i in str:
        print(str.index(i), end= ' ')
    else:
        print(-1, end =' ')