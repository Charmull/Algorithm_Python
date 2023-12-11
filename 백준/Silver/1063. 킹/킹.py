import sys

input = sys.stdin.readline
k, d, n = input().split()
col = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
for i in range(8):
    if col[i] == k[0]:
        k = [8 - int(k[1]), i]
    if col[i] == d[0]:
        d = [8 - int(d[1]), i]

def check(move, k, d):
    if 0 <= k[0] + move[0] <= 7 and 0 <= k[1] + move[1] <= 7:
        if k[0] + move[0] == d[0] and k[1] + move[1] == d[1]:
            if 0 <= d[0] + move[0] <= 7 and 0 <= d[1] + move[1] <= 7:
                d[0] += move[0]
                d[1] += move[1]
            else:
                return
        k[0] += move[0]
        k[1] += move[1]

for _ in range(int(n)):
    cmd = input().strip()
    if cmd == 'R':
        check([0, 1], k, d)
    elif cmd == 'L':
        check([0, -1], k, d)
    elif cmd == 'B':
        check([1, 0], k, d)
    elif cmd == 'T':
        check([-1, 0], k, d)
    elif cmd == 'RT':
        check([-1, 1], k, d)
    elif cmd == 'LT':
        check([-1, -1], k, d)
    elif cmd == 'RB':
        check([1, 1], k, d)
    elif cmd == 'LB':
        check([1, -1], k, d)

for i in range(8):
    if i == k[1]:
        k = col[i] + str(8 - int(k[0]))
    if i == d[1]:
        d = col[i] + str(8 - int(d[0]))
print(k)
print(d)