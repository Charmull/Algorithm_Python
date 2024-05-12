import sys

input = sys.stdin.readline
while True:
    num = input().strip()
    if num == '0':
        break
    result = 'yes'
    for i in range(len(num) // 2 + 1):
        if num[i] != num[len(num) - 1 - i]:
            result = 'no'
            break
    print(result)