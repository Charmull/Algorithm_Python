import sys

input = sys.stdin.readline
n, k = map(int, input().split())
l = [[0, 0] for _ in range(6)]
for _ in range(n):
    s, y = map(int, input().split())
    l[y - 1][s] += 1
room = 0
for n1, n2 in l:
    room += n1 // k + 1 if n1 % 2 else n1 // k
    room += n2 // k + 1 if n2 % 2 else n2 // k
print(room)