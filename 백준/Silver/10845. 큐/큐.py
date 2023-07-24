import sys

n = int(sys.stdin.readline())
dat = []

for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        dat.append(command[1])
    elif command[0] == 'pop':
        print(-1 if len(dat) == 0 else dat.pop(0))
    elif command[0] == 'size':
        print(len(dat))
    elif command[0] == 'empty':
        print(1 if len(dat) == 0 else 0)
    elif command[0] == 'front':
        print(dat[0] if len(dat) != 0 else -1)
    elif command[0] == 'back':
        print(dat[len(dat) - 1] if len(dat) != 0 else -1)