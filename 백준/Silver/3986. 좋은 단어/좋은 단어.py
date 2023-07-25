import sys

n = int(sys.stdin.readline())
count = 0

for _ in range(n):
    word = sys.stdin.readline().strip()
    stack = []
    for v in word:
        if stack and v == stack[-1]:
            stack.pop()
        else:
            stack.append(v)
    if not stack:
        count += 1
        
print(count)