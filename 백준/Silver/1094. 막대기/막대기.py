import sys

n = int(sys.stdin.readline())
change_num = []

while n:
    change_num.append(n % 2)
    n //= 2

print(change_num.count(1))