import sys
import heapq

input = sys.stdin.readline
n = int(input())
h = []
for _ in range(n):
    heapq.heappush(h, int(input()))
if n == 1:
    print(0)
    sys.exit(0)

result = 0
while len(h) >= 2:
    a, b = heapq.heappop(h), heapq.heappop(h)
    result += a + b
    heapq.heappush(h, a + b)
print(result)