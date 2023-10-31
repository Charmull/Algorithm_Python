import sys

input = sys.stdin.readline
n = int(input())
meet = [list(map(int, input().split())) for _ in range(n)]
meet.sort(key=lambda x:(x[1], x[0]))

result = 0
cursor = 0
for i in range(n):
    if cursor > meet[i][0]:
        continue
    result += 1
    cursor = meet[i][1]
            
print(result)