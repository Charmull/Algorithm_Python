import sys

x = sys.stdin.readline().strip()
time = 0

while len(x) >= 2:
    rst = 0
    for i in range(len(x)):
        rst += int(x[i])
    x = str(rst)
    time += 1

print(time)
print('YES' if not int(x) % 3 else 'NO')