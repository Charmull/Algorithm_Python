import sys

str = sys.stdin.readline().strip()

is_laser = True
current_bar = 0
total = 0
stack = []

for v in str:
    if v == '(':
        stack.append(v)
        current_bar += 1
        is_laser = True
    else:
        current_bar -= 1
        if is_laser:
            total += current_bar
            is_laser = False
        else:
            total += 1
print(total)