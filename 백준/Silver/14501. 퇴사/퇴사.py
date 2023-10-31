import sys

input = sys.stdin.readline
n = int(input())
T = [0] * n
P = [0] * n
for i in range(n):
    T[i], P[i] = map(int, input().split())
    
arr = [0] * n
for i in range(n):
    if i + T[i] > n:
        continue
    arr[i] = P[i]
    for j in range(i):
        if j + T[j] > n:
            continue
        if i >= j + T[j]:
            arr[i] = max(arr[i], arr[j] + P[i])
            
print(max(arr))