import sys

input = sys.stdin.readline
n = int(input())
nums = [int(input()) for _ in range(n)]
stack = []
add_num = 1
result = []

for num in nums:
    while add_num <= num:
        stack.append(add_num)
        add_num += 1
        result.append("+")
    if stack.pop(-1) != num:
        print("NO")
        sys.exit(0)
    result.append("-")

print('\n'.join(result))