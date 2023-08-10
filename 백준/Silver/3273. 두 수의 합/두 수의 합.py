import sys

input = sys.stdin.readline
n = int(input())
l = list(map(int, input().split()))
x = int(input())
visited = [0] * (x + 1)

count = 0
for num in l:
    if x - num <= 0: continue
    if visited[x - num]: count += 1
    visited[num] = 1
print(count)