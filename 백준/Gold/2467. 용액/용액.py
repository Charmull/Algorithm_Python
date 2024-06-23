import sys

input = sys.stdin.readline
cnt = int(input())
lst = list(map(int, input().split()))

result = [lst[0], lst[-1]]
diff = [abs((lst[0] + lst[-1]))]

def find(cnt, lst):
    left = 0
    right = cnt - 1
    while left < right:
        if lst[right] + lst[left] == 0:
            result[0] = lst[left]
            result[1] = lst[right]
            return
        elif lst[right] + lst[left] < 0:
            if abs(lst[right] + lst[left]) <= diff[0]:
                result[0] = lst[left]
                result[1] = lst[right]
                diff[0] = abs(lst[right] + lst[left])
            left += 1
        elif lst[right] + lst[left] > 0:
            if abs(lst[right] + lst[left]) <= diff[0]:
                result[0] = lst[left]
                result[1] = lst[right]
                diff[0] = abs(lst[right] + lst[left])
            right -= 1
            
find(cnt, lst)
print(result[0], result[1])