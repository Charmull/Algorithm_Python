import sys

input = sys.stdin.readline
arr = list(input())
result = 0
prev = '+'
is_minus = False
minus_stack = 0
for i in range(len(arr)):
    if arr[i] >= '0' and arr[i] <= '9':
        if prev != '-' and prev != '+':
            prev = prev * 10 + int(arr[i])
        else:
            prev = int(arr[i])
    elif arr[i] == '-':
        if is_minus:
            result -= (minus_stack + prev)
            minus_stack = 0
        if not is_minus:
            result += prev
            is_minus = True
        prev = '-'
    elif arr[i] == '+':
        if is_minus:
            minus_stack += prev
        if not is_minus:
            result += prev
        prev = '+'

if is_minus:
    result -= (minus_stack + prev)
else:
    result += prev
print(result)