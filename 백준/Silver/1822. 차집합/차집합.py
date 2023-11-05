import sys

input = sys.stdin.readline
nA, nB = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
result = list(a.difference(b))
result.sort()
print(len(result))
print(' '.join(map(str, result)))