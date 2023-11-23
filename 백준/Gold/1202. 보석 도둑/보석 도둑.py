import sys
import heapq

input = sys.stdin.readline
n, k = map(int, input().split())
jewel_data = [tuple(map(int, input().split())) for _ in range(n)]
bag_data = [int(input()) for _ in range(k)]

jewel_data.sort(reverse=True)
bag_data.sort()

h = []

result = 0
for c in bag_data:
    while jewel_data and jewel_data[-1][0] <= c:
        jewel = jewel_data.pop()
        heapq.heappush(h, -jewel[1])
    if h:
        result += -heapq.heappop(h)

print(result)