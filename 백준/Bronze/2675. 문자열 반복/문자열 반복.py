import sys

input = sys.stdin.readline

st = int(input())
for i in range(st):
    b, c = input().split()
    for i in range(len(c)):
        print(int(b) * c[i], end='')
    print()