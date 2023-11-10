import sys

n = int(sys.stdin.readline())
arr = [0] * 9
while n:
    if n % 10 == 9:
        arr[6] += 1
    else:
        arr[n % 10] += 1
    n //= 10

count = 0
for i in range(9):
    num = arr[i]
    if i == 6:
        num = arr[i] // 2 if not arr[i] % 2 else arr[i] // 2 + 1
    count = max(count, num)

print(count)