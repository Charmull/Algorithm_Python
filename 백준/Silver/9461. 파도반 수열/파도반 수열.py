import sys
input = sys.stdin.readline
t = int(input())
pn = [1] * 100
pn[3] = 2
pn[4] = 2
for i in range(5, 100):
    pn[i] = pn[i - 1] + pn[i - 5]

for _ in range(t):
    n = int(input())
    print(pn[n - 1])