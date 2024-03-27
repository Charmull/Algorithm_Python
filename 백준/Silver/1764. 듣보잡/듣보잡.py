import sys

input = sys.stdin.readline
n, m = map(int, input().split())
no_listen = set([input().strip() for _ in range(n)])
no_see = set([input().strip() for _ in range(m)])
result = list(no_listen.intersection(no_see))
result.sort()
print(len(result))
print('\n'.join(result))