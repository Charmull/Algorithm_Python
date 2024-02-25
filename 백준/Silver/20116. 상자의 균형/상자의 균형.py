import sys

input = sys.stdin.readline
n, l = map(float, input().split())
x_list = list(map(float, input().split()))
x_list.reverse()
sum_x = 0
result = True
for i in range(1, int(n)):
    width = [x_list[i] - l, x_list[i] + l]
    sum_x += x_list[i - 1]
    x = sum_x / i
    if x <= width[0] or x >= width[1]:
        result = False
        break

print('stable' if result else 'unstable')