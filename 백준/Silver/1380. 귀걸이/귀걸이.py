import sys

input = sys.stdin.readline
t = 1
while True:
    n = int(input())
    if n == 0:
        break
        
    names = [input().strip() for _ in range(n)]
    isTake = [0] * (n)
    for _ in range(n * 2 - 1):
        num, alp = input().split()
        num = int(num)
        isTake[num - 1] = 1 if not isTake[num - 1] else 0
    for i in range(n):
        if isTake[i]:
            print(t, names[i])
            break
    t += 1