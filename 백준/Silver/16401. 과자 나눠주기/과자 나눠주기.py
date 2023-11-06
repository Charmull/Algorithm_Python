import sys

input = sys.stdin.readline
m, n = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)

def count_snack_num(snack_len):
    num = 0
    for el in arr:
        if el >= snack_len:
            num += (el // snack_len)
    return num
    
result = 0
while (start < end):
    mid = (start + end + 1) // 2
    total = count_snack_num(mid)

    if total >= m:
        start = mid
    else:
        end = mid - 1

print(start)