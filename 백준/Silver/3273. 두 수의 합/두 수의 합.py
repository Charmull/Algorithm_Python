n = int(input())
nums = list(map(int, input().split()))
x = int(input())
nums.sort()
left, right = 0, n - 1

result = 0
while left < right:
    temp = nums[left] + nums[right]
    if temp == x:
        result += 1
    if temp < x:
        left += 1
        continue
    right -= 1
print(result)