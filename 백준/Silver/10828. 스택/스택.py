import sys

n = int(sys.stdin.readline())
dat = []
pos = 0

for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'pop':
        if pos == 0:
            print(-1)
        else:
            print(dat.pop())
            pos -= 1
    elif command[0] == 'size':
        print(pos)
    elif command[0] == 'empty':
        print(1 if pos == 0 else 0)
    elif command[0] == 'top':
        print(-1 if pos == 0 else dat[pos - 1])
    else:
        dat.append(int(command[1]))
        pos += 1