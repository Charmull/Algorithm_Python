import sys

x = int(sys.stdin.readline())

line = 1
while x > line:
    x -= line
    line += 1
    
if not line % 2:
    print(x, '/', line - x + 1, sep='')
else:
    print(line - x + 1, '/', x, sep='')