import sys

input = sys.stdin.readline
for _ in range(4):
    a_x1, a_y1, a_x2, a_y2, b_x1, b_y1, b_x2, b_y2 = map(int, input().split())
    if (a_x2 == b_x1 and a_y1 == b_y2) \
            or (a_x1 == b_x2 and a_y1 == b_y2) \
            or (a_x1 == b_x2 and a_y2 == b_y1) \
            or (a_x2 == b_x1 and a_y2 == b_y1):
        print('c')
    elif (a_x2 < b_x1) \
            or (b_x2 < a_x1) \
            or (a_y2 < b_y1) \
            or (b_y2 < a_y1):
        print('d')
    elif a_x2 == b_x1 or a_y1 == b_y2 or a_x1 == b_x2 or a_y2 == b_y1:
        print('b')
    else:
        print('a')