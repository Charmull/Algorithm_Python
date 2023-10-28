import sys

n = int(sys.stdin.readline())

if n == 1:
    print(0)
    print(1)
    sys.exit(0)
elif n < 3:
    print(1)
    print(2, 1)
    sys.exit(0)

d = [0] * (n + 1)
pre = [0] * (n + 1)
d[2] = 1
pre[2] = 1
d[3] = 1
pre[3] = 1

for i in range(4, n + 1):
    d[i] = d[i - 1] + 1
    pre[i] = i - 1
    if not i % 2 and d[i] > d[i // 2] + 1:
        d[i] = d[i // 2] + 1
        pre[i] = i // 2
    if not i % 3 and d[i] > d[i // 3] + 1:
        d[i] = d[i // 3] + 1
        pre[i] = i // 3
        
print(d[n])
curr = n
while curr:
    print(curr, end=' ')
    curr = pre[curr]