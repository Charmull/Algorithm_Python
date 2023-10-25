import sys

input = sys.stdin.readline
n = int(input())
alps = set()
for _ in range(n):
    alps.add(input().strip())
    
print('\n'.join(sorted(list(alps), key=lambda x:(len(x), x))))