import sys

n = int(sys.stdin.readline())
arr = [0] * (n + 1)
if n == 1:
    print(1)
    sys.exit(0)
arr[1] = 1
arr[2] = 1

for i in range(3, n + 1):
    arr[i] += 1
    tmp = i - 2
    while tmp:
        arr[i] += arr[tmp]
        tmp -= 1
print(arr[n])