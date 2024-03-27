import sys

input = sys.stdin.readline
n, m = map(int, input().split())
no_listen = set([input().strip() for _ in range(n)])
cnt = 0
result = []
for _ in range(m):
    name = input().strip()
    if name in no_listen:
        result.append(name)
        cnt += 1
        
result.sort()
print(cnt)
print('\n'.join(result))