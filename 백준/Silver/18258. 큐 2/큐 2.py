import sys

n = int(sys.stdin.readline())
dat = []
front = 0

for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        dat.append(command[1])
    elif command[0] == 'pop':
        if len(dat) - front == 0:
            print(-1)
        else:
            print(dat[front])
            front += 1
    elif command[0] == 'size':
        print(len(dat) - front)
    elif command[0] == 'empty':
        print(1 if len(dat) - front == 0 else 0)
    elif command[0] == 'front':
        print(dat[front] if len(dat) - front != 0 else -1)
    elif command[0] == 'back':
        print(dat[-1] if len(dat) - front != 0 else -1)