import sys

n = int(sys.stdin.readline())
q = [i for i in range(1, n + 1)]
front = 0

if n == 1:
    print(1)
else:
    while len(q) - front > 2:
        q.append(q[front + 1])
        front += 2

    print(q[front + 1])
