n = int(input())
nums = list(map(int, input().split()))
x = int(input())
occur = [0 for _ in range(x + 1)]

result = 0
for num in nums:
    if x - num <= 0: continue
    if occur[x - num] == 1: result += 1
    occur[num] = 1
print(result)