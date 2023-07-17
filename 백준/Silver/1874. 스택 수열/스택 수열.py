n = int(input())
lst = []
stack = []
for _ in range(n):
    lst.append(int(input()))

tmp = 1
result = []
while tmp <= n:
    if len(stack) != 0 and stack[len(stack) - 1] == lst[0]:
        stack.pop()
        result.append('-')
        del lst[0]
    else:
        stack.append(tmp)
        result.append('+')
        tmp += 1

if tmp > n and stack == list(reversed(lst)):
    result += ['-' for _ in stack]
    print('\n'.join(result))
else:
    print("NO")