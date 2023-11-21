import sys

input = sys.stdin.readline
k = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]
max_h = 0
max_h_idx = -1
max_w = 0
max_w_idx = -1
for i in range(6):
    dir, num = arr[i]
    if dir == 1 or dir == 2:
        if max_w < num:
            max_w = num
            max_w_idx = i
    elif dir == 3 or dir == 4:
        if max_h < num:
            max_h = num
            max_h_idx = i

sub_h = abs(arr[max_w_idx - 1][1] - arr[(max_w_idx + 1) % 6][1])
sub_w = abs(arr[max_h_idx - 1][1] - arr[(max_h_idx + 1) % 6][1])
print((max_h * max_w - sub_h * sub_w) * k)