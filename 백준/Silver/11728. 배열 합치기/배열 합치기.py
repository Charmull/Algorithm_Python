import sys

input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
arr = []
a_idx = 0
b_idx = 0
while a_idx < n and b_idx < m:
    if a[a_idx] < b[b_idx]:
        arr.append(a[a_idx])
        a_idx += 1
        continue
    arr.append(b[b_idx])
    b_idx += 1
    
if a_idx < n:
    arr += a[a_idx:]
elif b_idx < m:
    arr += b[b_idx:]
    
print(' '.join(map(str, arr)))